const callback =(json)=>{
    let element=document.getElementById('like'+json.id);
    element.textContent=json.like;
}

const like=(article_id)=>{
    fetch('/api/articles/'+article_id+'/like/')
    .then((response)=>response.json())
    .then(callback)
    .catch((error)=>console.error('Error:',error));
}