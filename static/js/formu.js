document.getElementById('formu').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const ruta = '/static/img/exito/Correcto.svg';
    
    fetch('https://formulariomedico-production.up.railway.app/api/Datos/',{
        method: 'POST',
        body: formData,
        })
        .then(response => {
            if (!response.ok){
                throw new Error('Error en la peticion')
            }
            return response.json();
        })
        .then(data => 
            {   document.getElementById('messageError').innerHTML = '';
                document.getElementById('messageSuccess').innerHTML = '';
                document.getElementById('messageSuccess').innerHTML += `<div class="row justify-content-center">
                                    <div class="col-3">
                                        <img src="${ruta}" height=100 width= 100 class="fit-image mt-4">
                                    </div>
                                </div>
                                <br><br>
                                <div class="row justify-content-center mt-4">
                                    <div class="col-7 text-center">
                                        <h5 class="purple-text text-center">Se han registrado los datos correctamente <a href="https://formulariomedico-production.up.railway.app/pdf/">Extraer PDF</a></h5>
                                    </div>
                                </div>`})
        .catch(error => {
        console.error('Error', error);
        document.getElementById('messageError').innerHTML = `
        <div class="row justify-content-center mt-4">
            <div class="col-7 text-center">
                <h5 style= "color: red; " class="red-text text-center">Ocurrió un error al registrar los datos: ${error.message}</h5>
            </div>
        </div>`;
});
    });
    