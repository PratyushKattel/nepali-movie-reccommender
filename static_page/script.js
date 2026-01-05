const form=document.querySelector(form);

form.addEventListener('submit',(e)=>{
    e.preventDefault()
    const text_val=document.getElementById('movie').ariaValueMax

    const response=await fetch('/submit')
})