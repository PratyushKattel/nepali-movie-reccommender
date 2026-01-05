from fastapi import FastAPI, Request,Form
from fastapi.responses import HTMLResponse,FileResponse
# from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app=FastAPI()
# templates=Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory='static'),name="static")

@app.get("/favicon.ico",include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")
@app.get("/")
async def read_index():
    return FileResponse('static/index.html')
   
@app.post("/submit")
async def handle_form(movie_name:str=Form(...)):
    print(f"Recieved movie is :{movie_name}")
    return {"message":f"server receives the message {movie_name}"}

