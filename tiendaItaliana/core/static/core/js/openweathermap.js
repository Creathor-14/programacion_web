function obtenerCordenadas(){
    if (navigator.geolocation) { 
        position = navigator.geolocation.getCurrentPosition(function(position){
            latitud = position.coords.latitude;
            longitud = position.coords.longitude;
            obtenerNombreRegion(latitud,longitud);
        });   
    }
}

function obtenerNombreRegion(latitud, longitud) {
    var r ="";
    const url = `https://nominatim.openstreetmap.org/reverse?lat=${latitud}&lon=${longitud}&format=jsonv2`;
    fetch(url)
      .then(response => response.json())
      .then(data => {
        if (data && data.address) {
          var region = data.address.state || data.address.province || data.address.region;
          desplegarDatosClima(region);
        } else {
            console.log(`No se encontró una región para las coordenadas dadas (${latitud}, ${longitud}).`);
        }
      })
      .catch(error => {
        console.log('Error:', error);
      });
    return "none";
}

function desplegarDatosClima(region){
    let ciudad_buscada = region;
    let units = 'metric';
    let lang = 'es';
    let apiid = 'c6a7fe5bc4025f2fdfd88dfa3756ce76';
    let urlClima = `https://api.openweathermap.org/data/2.5/weather?q=${ciudad_buscada}&lang=${lang}&units=${units}&appid=${apiid}`;

    $.getJSON(urlClima, function (dataClima) {
        let urlPais = `https://restcountries.com/v3.1/alpha/${dataClima.sys.country}`;
        $.getJSON(urlPais, function (dataPais) {
            let html =
                `<p>${dataClima.name} (${dataPais[0].translations.spa.common})<br>
                Temperatura: ${dataClima.main.temp}°C</p>`;

            $('#info-clima-comprimido').html(html);
            
            let img = `<img src="https://openweathermap.org/img/wn/${dataClima.weather[0].icon}@2x.png" />`;

            $('#img-clima-comprimido').html(img);
        });
    })
    .fail(function () {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'La ciudad ingresada no existe en el mundo mundial!',
            confirmButtonText: 'Ok'
        })
    });
}


obtenerCordenadas();



