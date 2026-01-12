const form=document.querySelector('form')
const result=document.getElementById('result')
const ul=document.createElement('ul')
const ul_id=document.querySelector("#rec-movies")

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
    // document.querySelector('.container').append(ul)
    const recommended_movies=data.recommended_movies
    recommended_movies.forEach(movie => {
    const li=document.createElement('li')
    const textNode = document.createTextNode(movie);
    li.appendChild(textNode);
    ul_id.appendChild(li);
    });
    // console.log(typeof data.recommended_movies)
}


}catch(error){
    console.log(error)
    result.style.color="orange"
    result.innerText="Check the connection , Sever is not responding"

}


}
)

function debounce(func,wait){
    let timeout;
    console.log("Deboucne funtion created");
    
    return function(...args){
// console.log("Wrapper called with args ",...args)
        // console.log("Clearing the previous timeout",timeout)

        clearTimeout(timeout)
        timeout=setTimeout(()=>{
            func(...args)
        },wait)
        // console.log("the new timeout is set :",timeout)
    }
}

async function fetchsuggestion(query){
    try{
        let response= await fetch(`/search-movies?q=${(query)}`)
        const data= await response.json()
        currentsuggestion=data.suggestions
        console.log(currentsuggestion)
    }
catch(error){
    console.error("Error in fetching suggestions :",error)
}}

function displaysuggetions(suggestions){
    suggestions.forEach((item)=>{
        document.querySelector('.suggestions').appendChild(item)
    })   
}
const debouncedfetch=debounce(fetchsuggestion,300)
document.querySelector('input').addEventListener('input',(e)=>{
    
    debouncedfetch(e.target.value)

})
