document.querySelector("#message-destroy")?.addEventListener("click", () => {
  document.querySelector("#message-destroy").parentElement.remove()
  console.log("Hello");
});


const reactions = document.querySelectorAll(".reaction")
console.log(reactions);
async function getPostsReactions(){
try{
  const response= await fetch('http://localhost:8000/api/reactions/3')
const json=await response.json()
console.log(json);
}catch(error){
console.error(error)
}
} 

getPostsReactions()