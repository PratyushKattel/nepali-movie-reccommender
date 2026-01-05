const form=document.querySelector('form')
const list=document.getElementById('result')

form.addEventListener('submit',async (e)=>{
    e.preventDefault();
    const formdata= new FormData(form)
    console.log(formdata)
    const response = await fetch("/submit",{
        method:'POST',
        body:formdata
    });


const data=await response.json()

document.getElementById('result').innerText=`The server says ${data.message}`
}
)