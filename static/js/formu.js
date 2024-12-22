document.getElementById('formu').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const ruta = '/static/img/exito/Correcto.svg';
    
    fetch('http://127.0.0.1:8000/api/Datos/',{
        method: 'POST',
        body: formData,
        })
        .then(response => {
            if (!response.ok){
                throw new Error('Error en la peticion')
            }
            return response.json();
        })
        .then(data => {document.getElementById('messageSuccess').innerHTML += `<div class="row justify-content-center">
                                    <div class="col-3">
                                        <img src="${ruta}" height=100 width= 100 class="fit-image mt-4">
                                    </div>
                                </div>
                                <br><br>
                                <div class="row justify-content-center mt-4">
                                    <div class="col-7 text-center">
                                        <h5 class="purple-text text-center">Se han registrado los datos correctamente <a href="http://127.0.0.1:8000/pdf/">Extraer PDF</a></h5>
                                    </div>
                                </div>`})
        .catch(error => {console.error('Error',error);
        });
    });
    