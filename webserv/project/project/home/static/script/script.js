function sleep(millis) {
    var t = (new Date()).getTime();
    var i = 0;
    while (((new Date()).getTime() - t) < millis) {
        i++;
    }
}

document.addEventListener("DOMContentLoaded", (event) => {
    let mainMenuBtn = document.querySelector('.navigation')
    
    let calcMenuBtn = document.querySelector('.calc_link')
    let formMenuBtn = document.querySelector('.form_link')
    mainMenuBtn.addEventListener("mouseover", () =>
    {
        // mainMenuBtn.style.bottom = '-85px'
        // calcMenuBtn.style.display = 'block'
        calcMenuBtn.style.opacity = '100'
        calcMenuBtn.style.bottom = '90px'
        calcMenuBtn.style.left = '80px'
        formMenuBtn.style.opacity = '100'
        formMenuBtn.style.bottom = '150px'
        formMenuBtn.style.left = '0px'
        // formMenuBtn.style.display = 'block'
        
    })
    mainMenuBtn.addEventListener("mouseleave", () => {
        sleep(500)
        calcMenuBtn.style.opacity = '0'
        calcMenuBtn.style.bottom = '30px'
        calcMenuBtn.style.left = '15px'
        formMenuBtn.style.opacity = '0'
        formMenuBtn.style.bottom = '1px'
        formMenuBtn.style.left = '1px'
    });
  });