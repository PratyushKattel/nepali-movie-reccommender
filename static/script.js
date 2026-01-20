const form=document.querySelector('form')
const result=document.getElementById('result')
const ul=document.createElement('ul')
const ul_id=document.querySelector("#rec-movies")
const suggestion_div=document.querySelector(".suggestions")
let currentsuggestions=[]
const movie_input=document.querySelector('input')
let selected_item=-1;

window.onload=getstat()
// submiting into the /submit endpoint fo the api
async function getstat(){
    const response= await fetch("/analytics")
    const data= await response.json()

    document.getElementById('statscontent').innerHTML=`<p> The total searches made were ${data.total_searches}</p> 
    <p>The most popular movies are :</p>
     <ul>
            ${data.popular_movies.slice(0, 5).map(m => 
                `<li>${m.movie} (${m.searches} times)</li>`
            ).join('')}
        </ul>
`
}
form.addEventListener('submit',async (e)=>{
    e.preventDefault();
    if (ul_id.children.length>0){
        ul_id.innerHTML=""
    }
    const formdata= new FormData(form)
    try{
    const response = await fetch("/submit",{
        method:'POST',
        body:formdata
    });


const data=await response.json()

if (!response.ok){
    result.innerText=`Error ${data.detail}`
    result.style.color='red'

}else{
    result.style.color='green'
    result.innerText="Response was recived "
    const recommended_movies=data.recommended_movies
    recommended_movies.forEach(movie => {
    const li=document.createElement('li')
    const textNode = document.createTextNode(movie);
    li.appendChild(textNode);
    ul_id.appendChild(li);
    });
}


}catch(error){
    console.log(error)
    result.style.color="orange"
    result.innerText="Check the connection , Sever is not responding"

}

}
)
// ---submission of form data ends 

// -------Fetching and displaying suggestions as the user types the movie name------

function debounce(func,wait){
    let timeout;
    return function(...args){   //a wrapper function debounce takes my function and a wait time and transform  it to a function that waits for wait time to be called again

        clearTimeout(timeout)
        timeout=setTimeout(()=>{
            func(...args)
        },wait)
    }
}

async function fetchsuggestion(query){
    try{
        if (!query || query.length<2){
            currentsuggestions=[]
            displaysuggestions([])
            return;
        }
        //fetching suggestions from the /search-movie endpoint
        const response= await fetch(`/search-movies?q=${(query)}`)
        const data= await response.json()
        currentsuggestions=data.suggestions
        console.log(currentsuggestions)
        displaysuggestions(currentsuggestions)
    }
catch(error){
    console.error("Error in fetching suggestions :",error)
    currentsuggestions=[]
    displaysuggestions([])
}}


function displaysuggestionds(suggestions){
    if( suggestions.length==0){
        suggestion_div.classList.remove('active')
        suggestion_div.innerHTML=''
        return
    }
    suggestion_div.innerHTML=suggestions.map((movie,index)=>
        `<div class="suggested-item" data_index="${index}">${movie}</div>`
).join('')

    suggestion_div.classList.add('active')
    suggestionclickhander()

    }


const debouncedfetch=debounce(fetchsuggestion,300)
movie_input.addEventListener('input', async (e)=>{
    debouncedfetch(e.target.value)   

})

function suggestionclickhander(){
    document.querySelectorAll('.suggested-item').forEach((item)=>{
        item.addEventListener('click',(e)=>{
             movie_input.value=e.target.textContent;
            // console.log(e.target.textContent)
            hidesuggestions();
        })
    })
}

function hidesuggestions(){
    suggestion_div.classList.remove('active')
    suggestion_div.innerHTML=''
    currentsuggestions=[]
    selecteditem=-1
}


