from fastapi import FastAPI, Request,Form,Depends
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
import pandas as pd
import numpy as np
from database import init_db,get_db,SearchHistory
from sqlalchemy.orm import Session
import json
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from sqlalchemy import func

@asynccontextmanager
async def lifespan(app: FastAPI):
    # my startup_code , run once
    print("Loading the similarity matrix ......")
    matrix=np.load("project/similarity_matrix.pkl",allow_pickle=True)
    init_db()
    yield {'similarity_matrix':matrix}

    print("shutting down....")

app=FastAPI(lifespan=lifespan)
app.mount("/static",StaticFiles(directory='static'),name="static")

@app.get("/favicon.ico",include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")

@app.get("/")
async def read_index():
    return FileResponse('static/index.html')
   
@app.post("/submit")
async def handle_form(request:Request,movie_name:str=Form(...),db:Session=Depends(get_db)):
    df=pd.read_parquet("api_serve/movies_list.parquet")
    similarity=request.state.similarity_matrix   
    try:
        index=df[df['movie_name'] == movie_name].index[0]

    except IndexError:
        raise HTTPException(status_code=404, detail="Movie not found")  
      
    distances = similarity[index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [df.iloc[i[0]]['movie_name'] for i in movie_indices]  # Fixed column name
#    storing the value before returning response
    search_record=SearchHistory(
        movie_searched=movie_name,
        reccomendations=json.dumps(recommended_movies)
    )
    db.add(search_record)
    db.commit()
    return {'message':f"server receives the message {movie_name}",
            'recommended_movies':recommended_movies}



    # return {"message":f"server receives the message {movie_name}"}

@app.get("/search-movies/")
async def search_movies(q: str):
    df=pd.read_parquet("api_serve/movies_list.parquet")
    if not q:
        return{"suggestions":[]}
    matches=df[df['movie_name'].str.contains(q,case=False,na=False)]
    suggestions=matches['movie_name'].tolist()[:10]
    return{"suggestions":suggestions}

# displaying the hisotry
@app.get("/history")
async def get_history(db:Session=Depends(get_db)):
    searches=db.query(SearchHistory).all()
    return{
        "total_searches":len(searches),
        'searches':[
            {
                'id':s.id,
                'movie_name':s.movie_searched,
                'reccomendations':json.loads(s.reccomendations),
                'timestamp':str(s.timestamp)
            }
            for s in searches
        ]
    }

@app.get('/analytics')
async def get_analytics(db:Session=Depends(get_db)):
    total_movies=db.query(SearchHistory).count()

    popular=db.query(
        SearchHistory.movie_searched,
        func.count(SearchHistory.movie_searched).label('count')
    ).group_by(SearchHistory.movie_searched)\
    .order_by(func.count(SearchHistory.movie_searched).desc())\
    .limit(10)\
    .all()

    return{
        "total_searches":total_movies,
        "popular_movies":[
            {'movie':p[0],'searches':p[1]} for p in popular
        ]
    }

    