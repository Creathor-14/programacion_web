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
function validarDireccion(){
    let direccion = document.getElementById("direccion");
    
    if (direccion.value.trim().length == 0){
        document.getElementById("error_direccion_min").style.display = "inline";
        document.getElementById("error_direccion_max").style.display = "none";
        document.getElementById("direccion").classList.add("is-invalid");
    }
    else if(direccion.value.trim().length > 20){
        document.getElementById("error_direccion_max").style.display = "inline";
        document.getElementById("error_direccion_min").style.display = "none";
        document.getElementById("direccion").classList.add("is-invalid");
    }
    else{
        document.getElementById("error_direccion_min").style.display = "none";
        document.getElementById("error_direccion_max").style.display = "none";
        document.getElementById("direccion").classList.remove("is-invalid");
        document.getElementById("direccion").classList.add("is-valid");
    }
}
function validarTelefono() {
    let telefono = document.getElementById("telefono");
    let telefonoValue = telefono.value.trim();

    if (telefonoValue.length !== 9 || isNaN(telefonoValue)) {
        document.getElementById("error_telefono").style.display = "inline";
        telefono.classList.add("is-invalid");
    } else {
        document.getElementById("error_telefono").style.display = "none";
        telefono.classList.remove("is-invalid");
        telefono.classList.add("is-valid");
    }
}
function validarContraseña(){ 
    let password = document.getElementById("password").value;
    let rgPass = /^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{6,10}$/;
    if(rgPass.test(password) == false){
        document.getElementById("error_password").style.display = "inline";
        document.getElementById("password").classList.add("is-invalid");
    }
    else{
        document.getElementById("error_password").style.display = "none";
        document.getElementById("password").classList.remove("is-invalid");
        document.getElementById("password").classList.add("is-valid");
    }
}



document.getElementById("mostrar_datos").addEventListener("click", function() {
    event.preventDefault();
    var nombre = document.getElementById("nombre").value;
    var apellidoPaterno = document.getElementById("paterno").value;
    var apellidoMaterno = document.getElementById("materno").value;
    var rut = document.getElementById("rut").value;
    var email = document.getElementById("email").value;
    var direccion = document.getElementById("direccion").value;
    var telefono = document.getElementById("telefono").value;
    var comentarios = document.getElementById("Comentarios").value;
    var fechaNacimiento = document.getElementById("fecha_nac").value;
    var password = document.getElementById("password").value;
  
    // Verificar si se han completado todos los campos
    if (
      nombre === "" ||
      apellidoPaterno === "" ||
      apellidoMaterno === "" ||
      rut === "" ||
      email === "" ||
      direccion === "" ||
      telefono === "" ||
      password === ""
    ) {
      alert("Por favor, complete todos los campos obligatorios del formulario.");
      return;
    }
  
    // Mostrar la información en una alerta
    var mensaje = "Nombre: " + nombre + "\n" +
      "Apellido Paterno: " + apellidoPaterno + "\n" +
      "Apellido Materno: " + apellidoMaterno + "\n" +
      "RUT: " + rut + "\n" +
      "Email: " + email + "\n" +
      "Dirección: " + direccion + "\n" +
      "Teléfono: " + telefono + "\n" +
      "Comentarios: " + comentarios + "\n" +
      "Fecha de Nacimiento: " + fechaNacimiento + "\n" +
      "Contraseña: " + password;
  
    alert(mensaje);
});