document.getElementById('nextBtn').addEventListener('click', function() {
    var email = document.getElementById('email').value;
    var pseudo = document.getElementById('pseudo').value;
    var password = document.getElementById('password').value;

    if (email && pseudo && password) {
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

// Animation au défilement
document.addEventListener('DOMContentLoaded', () => {
    const elements = document.querySelectorAll('.form-container');

    const options = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, options);

    elements.forEach(element => {
        observer.observe(element);
    });
});