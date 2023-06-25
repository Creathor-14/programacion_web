function validarNombres(tipo) {
    let elemento = document.getElementById(tipo);
    let valor = elemento.value.trim();

    let errorMin = document.getElementById(`error_${tipo}_min`);
    let errorMax = document.getElementById(`error_${tipo}_max`);
    
    let letrasRegex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/;

    if (valor.length === 0) {
        errorMin.style.display = "inline";
        errorMax.style.display = "none";
        elemento.classList.add("is-invalid");
    } else if (valor.length > 15) {
        errorMin.style.display = "none";
        errorMax.style.display = "inline";
        elemento.classList.add("is-invalid");
    } else if (!letrasRegex.test(valor)) {
        errorMin.style.display = "inline";
        errorMax.style.display = "none";
        elemento.classList.add("is-invalid");
    } else {
        errorMin.style.display = "none";
        errorMax.style.display = "none";
        elemento.classList.remove("is-invalid");
        elemento.classList.add("is-valid");
    }
}
function validarRut() {
    let rutInput = document.getElementById("rut");
    let rut = rutInput.value.trim();
  
    if (rut.length === 0) {
      document.getElementById("error_rut_valido").style.display = "none";
      document.getElementById("error_rut").style.display = "inline";
      rutInput.classList.add("is-invalid");
      return false;
    }
  
    rut = rut.replace(/[^\dkK]+/g, '');
    if (rut.length < 2) {
      document.getElementById("error_rut").style.display = "none";
      document.getElementById("error_rut_valido").style.display = "inline";
      rutInput.classList.add("is-invalid");
      return false;
    }
  
    var dv = rut.slice(-1).toUpperCase();
    var rutNumerico = parseInt(rut.slice(0, -1), 10);
    if (isNaN(rutNumerico)) {
      document.getElementById("error_rut_valido").style.display = "inline";
      rutInput.classList.add("is-invalid");
      return false;
    }
  
    var suma = 0;
    var factor = 2;
    while (rutNumerico > 0) {
      suma += (rutNumerico % 10) * factor;
      rutNumerico = Math.floor(rutNumerico / 10);
      factor = factor === 7 ? 2 : factor + 1;
    }
  
    var dvCalculado = 11 - (suma % 11);
    dvCalculado = dvCalculado === 11 ? '0' : dvCalculado === 10 ? 'K' : dvCalculado.toString();
    if (dv !== dvCalculado) {
      document.getElementById("error_rut_valido").style.display = "inline";
      rutInput.classList.add("is-invalid");
      return false;
    }
  
    document.getElementById("error_rut_valido").style.display = "none";
    rutInput.classList.remove("is-invalid");
    rutInput.classList.add("is-valid");
    return true;
}
function validarEmail(){
    let email = document.getElementById("email").value;
    let rgEmail = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
    if (rgEmail.test(email) == false){  
        document.getElementById("error_email").style.display = "inline";
        document.getElementById("email").classList.add("is-invalid");
    }
    else{
        document.getElementById("error_email").style.display = "none";
        document.getElementById("email").classList.remove("is-invalid");
        document.getElementById("email").classList.add("is-valid");

    }
}
function validarComentario() {
    let comentarios = document.getElementById("comentarios");
    let errorComentarios = document.getElementById("error_comentarios");

    if (comentarios.value.trim().length === 0) {
        errorComentarios.style.display = "inline";
        comentarios.classList.add("is-invalid");
    } else if (comentarios.value.length > 500) {
        errorComentarios.style.display = "inline";
        comentarios.classList.add("is-invalid");
    } else {
        errorComentarios.style.display = "none";
        comentarios.classList.remove("is-invalid");
        comentarios.classList.add("is-valid");
    }

    let contador = document.getElementById("contador_caracteres");
    contador.textContent = comentarios.value.length + "/500";
}

document.getElementById("mostrar_datos").addEventListener("click", function(event) {
    //event.preventDefault();*/
    var nombre = document.getElementById("nombre").value;
    var apellidoPaterno = document.getElementById("paterno").value;
    var email = document.getElementById("email").value;
    var seleccion = document.getElementById("seleccione").value;
    var comentarios = document.getElementById("comentarios").value;

    if (
      nombre === "" ||
      apellidoPaterno === "" ||
      comentarios === "" ||
      email === "" ||
      seleccion === ""
    ) {
      alert("Por favor, complete todos los campos obligatorios del formulario.");
      return;
    }
  
    var mensaje = "Nombre: " + nombre + "\n" +
      "Apellido Paterno: " + apellidoPaterno + "\n" +
      "Email: " + email + "\n" +
      "Tipo de selección: " + seleccion + "\n" +
      "Comentarios: " + comentarios;
  
    alert(mensaje);
});

document.getElementById("comentarios").addEventListener("input", function() {
    this.style.height = "auto";
    this.style.height = (this.scrollHeight + 2) + "px";
});