import React from 'react'
import { useState } from 'react'

const App = ()=>{
  const [Image , setImage] = useState(null)
  const form = new FormData()
  form.append('image',Image)
  const HandlePrediction = ()=>{
      fetch('http://192.168.1.54:8000/prediction/',{
        method:'POST',
        body:form,
      })
      .then(res=>res.json())
      .then(res=>{
        if(res.status){
          console.log(res.result)
          const p = document.createElement('p')
          p.textContent = `the integer in the given image is : ${res.result}`
          const result = document.getElementById('result')
          result.appendChild(p)
        }
      })
  }

  return(
    <div id='body' className='App'>
       <label>Image : </label><input id='image' type='file'onChange={(e)=>{
         const file = e.target.files[0]
         setImage(file)
        const formData = new FormData();
        formData.append('file', file);
        const result = document.getElementById('result')
        result.innerHTML = ""
        const reader = new FileReader();
        reader.onload = function(e) {
            const uploadedImage = document.createElement('img');
            uploadedImage.src = e.target.result;
            uploadedImage.style.display = 'block';
            uploadedImage.height= 90
            uploadedImage.width = 90
            result.appendChild(uploadedImage)
        };
        reader.readAsDataURL(file);
       }} /> 
       <button onClick={HandlePrediction} >predict</button>
       <div id='result'></div>
    </div>
  )

}



export default App