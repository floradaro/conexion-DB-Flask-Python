document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('form').addEventListener('submit', function (e) {
        e.preventDefault();  // Evita el envío del formulario hasta validar

        const formElements = {
            fullname: document.getElementById('fullname'),
            phone: document.getElementById('phone'),
            email: document.getElementById('email')
        };

        const errorElements = document.querySelectorAll('.error');
        errorElements.forEach(element => {
            element.style.display = 'none';  
            element.textContent = "";  
        });

        let isValid = true;

        // Validación del nombre completo
        if (formElements.fullname && formElements.fullname.value.trim() === "") {
            isValid = false;
            const error = document.getElementById('fullname-error');
            error.style.display = 'block';
            error.textContent = "El nombre completo es obligatorio.";
        } else if (formElements.fullname.value.split(' ').length < 2) {
            // Verifica que haya al menos dos palabras separadas por espacio
            isValid = false;
            const error = document.getElementById('fullname-error');
            error.style.display = 'block';
            error.textContent = "Debe ingresar al menos un nombre y un apellido.";
        }

        // Validación del teléfono
        if (formElements.phone.value.trim() === "") {
            isValid = false;
            const error = document.getElementById('phone-error');
            error.style.display = 'block';
            error.textContent = "El teléfono es obligatorio.";
        }

        // Validación del email
        if (formElements.email.value.trim() === "") {
            isValid = false;
            const error = document.getElementById('email-error');
            error.style.display = 'block';
            error.textContent = "El correo electrónico es obligatorio.";
        } else if (!/\S+@\S+\.\S+/.test(formElements.email.value)) {
            isValid = false;
            const error = document.getElementById('email-error');
            error.style.display = 'block';
            error.textContent = "Por favor ingresa un correo electrónico válido.";
        }

        if (isValid) {
            this.submit(); 
        }
    });
});
