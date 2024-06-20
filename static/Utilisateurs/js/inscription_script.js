/*document.getElementById('nextBtn').addEventListener('click', function() {
    var email = document.getElementById('email').value;
    var pseudo = document.getElementById('pseudo').value;
    var password1 = document.getElementById('password1').value;
    var password2 = document.getElementById('password2').value;

    
    if (email && pseudo && password1 && password2) {
        document.getElementById('initial-fields').classList.add('hidden');
        document.getElementById('additional-fields').classList.remove('hidden');
    } else {
        alert('Veuillez remplir tous les champs de la première partie.');
    }
});

document.getElementById('backBtn').addEventListener('click', function() {
    document.getElementById('additional-fields').classList.add('hidden');
    document.getElementById('initial-fields').classList.remove('hidden');
});