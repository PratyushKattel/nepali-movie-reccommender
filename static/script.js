const form=document.querySelector('form')
const result=document.getElementById('result')

form.addEventListener('submit',async (e)=>{
    e.preventDefault();
    const formdata= new FormData(form)
    // console.log(formdata)
    try{
    const response = await fetch("/submit",{
        method:'POST',
        body:formdata
    });


const data=await response.json()
console.log(data)
if (!response.ok){
    result.innerText=`Error ${data.detail}`
    result.style.color='red'
}else{
    result.style.color='green'
    const usercontainer=result.querySelector('#rec-movies')
    const recommended_movies=data.recommended_movies
    recommended_movies.forEach(movie => {
    const li=document.createElement('li')
    const textNode = document.createTextNode(movie);
    li.appendChild(textNode);
    document.querySelector('ul').appendChild(li);
    });
    // console.log(typeof data.recommended_movies)
}


}catch(error){
    console.log(error)
    result.innerText+="Check the connection , Sever is not responding"

}


}
)