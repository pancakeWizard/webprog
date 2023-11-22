document.addEventListener("DOMContentLoaded", (event) => {
    let modal = document.querySelector('.modal');
    let openModalBtn = document.querySelector('.openModal')

    openModalBtn.addEventListener("OnClick", (event) =>{
        modal.style.display = "block";
    })

})