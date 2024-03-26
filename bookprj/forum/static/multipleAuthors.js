document.addEventListener("DOMContentLoaded", function(){
    let multipleAuthorsTrigger = document.querySelector("#moreAuthorsTrigger")
    console.log(multipleAuthorsTrigger)
    let authors = 1
    multipleAuthorsTrigger.addEventListener("click", function(){
        authors++;
        console.log("event")
        const node = document.querySelector("#mainAuthorSelect");
        const clone = node.cloneNode(true);
        document.querySelector("#authors").appendChild(clone);
        let cloneSelect = clone.childNodes[3];
        cloneSelect.setAttribute("name", `bookAuthor_${authors}`)
        document.querySelector("#authorHelper").setAttribute("value", `${authors}`)
    })
})