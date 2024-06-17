document.getElementById('nextBtn').addEventListener('click', function() {
    var email = document.getElementById('email').value;
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    
    if (email && username && password) {
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