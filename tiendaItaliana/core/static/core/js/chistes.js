const btnJoke = document.getElementById("btn-joke");
const jokeContainer = document.getElementById("joke-container");

btnJoke.addEventListener("click", () => {
    // Generar valores aleatorios para la traslación en los ejes X e Y
    const translateX = getRandomValue(-100, 100);
    const translateY = getRandomValue(-100, 100);

    // Aplicar la traslación al estilo del botón
    btnJoke.style.transform = `translate(${translateX}px, ${translateY}px)`;

    const apiUrl = "https://v2.jokeapi.dev/joke/Any?lang=es";

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            let jokeText;

            if (data.type === "single") {
                jokeText = data.joke;
            } else {
                jokeText = `${data.setup} ${data.delivery}`;
            }

            jokeContainer.innerHTML = jokeText;

            // Reiniciar la posición del botón después de 2 segundos (ajustar el tiempo según sea necesario)
            setTimeout(() => {
                btnJoke.style.transform = "translate(0, 0)";
            }, 2000);
        })
        .catch(error => console.error(error));
});

// Función para generar un valor aleatorio en un rango dado
function getRandomValue(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}