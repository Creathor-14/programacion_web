const toggle = document.getElementById('modoOscuro');
const html = document.querySelector('html');
const format = document.querySelector("body");


toggle.addEventListener('click',function(){
    
    this.classList.toggle('bi-moon');
    this.classList.toggle('bi-brightness-high-fill');
    if(html.getAttribute("new-data-bs-theme")=="dark"){
        html.setAttribute("new-data-bs-theme","light")
        format.setAttribute("formato","light");
        /*
        var contenedor = primaryColor;
        primaryColor= secondaryColor;
        secondaryColor= contenedor;*/
    }else{       
        html.setAttribute("new-data-bs-theme","dark")
        format.setAttribute("formato","dark");
        /*
        var contenedor = primaryColor;
        primaryColor= secondaryColor;
        secondaryColor= contenedor;*/
    }  
})

toggle.onmouseenter = function(e){
    
    this.classList.toggle('bi-moon');
    toggle.style.transition="1s";
    this.classList.toggle('bi-brightness-high-fill');
}
toggle.onmouseleave = function(e){
    
    
    this.classList.toggle('bi-moon');
    toggle.style.transition="1s";
    this.classList.toggle('bi-brightness-high-fill');
}