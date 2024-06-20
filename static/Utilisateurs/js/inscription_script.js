document.getElementById('nextBtn').addEventListener('click', function() {
    var email = document.getElementById('email').value;
    var pseudo = document.getElementById('pseudo').value;
    var password1 = document.getElementById('password1').value;
    var password2 = document.getElementById('password2').value;

    if (email && pseudo && password1 && password2) {
        if (password1 === password2) {
            // Validate latitude and longitude before proceeding
            var latitude = document.getElementById('id_latitude').value;
            var longitude = document.getElementById('id_longitude').value;

            if (latitude && longitude) {
                document.getElementById('initial-fields').classList.add('hidden');
                document.getElementById('additional-fields').classList.remove('hidden');
                // Scroll to the top of the additional fields
                document.querySelector('.form-container').scrollTop = 0;
            } else {
                alert('La géolocalisation est requise pour continuer.');
                document.getElementById('id_latitude').value = "0";  // Default latitude value
                document.getElementById('id_longitude').value = "0";  // Default longitude value
                document.getElementById('initial-fields').classList.add('hidden');
                document.getElementById('additional-fields').classList.remove('hidden');
                document.querySelector('.form-container').scrollTop = 0;
            }
        } else {
            alert('Les mots de passe ne correspondent pas.');
        }
    } else {
        alert('Veuillez remplir tous les champs de la première partie.');
    }
});

document.getElementById('backBtn').addEventListener('click', function() {
    document.getElementById('additional-fields').classList.add('hidden');
    document.getElementById('initial-fields').classList.remove('hidden');
    // Scroll to the top of the initial fields
    document.querySelector('.form-container').scrollTop = 0;
});