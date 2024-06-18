const body  = document.body;
const openFilter = document.querySelector('#openFilter');
const closeSidebar = document.querySelector('#closeSidebar');
const toggleTheme = document.querySelector('.toggle-theme');
const sidebar = document.querySelector('.main-sidebar');
const light = toggleTheme.children[0]
const dark = toggleTheme.children[1]
const percentage = document.querySelector('.percentage p')


const filterHeader = document.querySelector(".filter .filter-header")
const filterup = filterHeader.children[1]
const filterForm = document.querySelector(".filter .fit")

const openChat = document.querySelector("#openChat")
const closeChat = document.querySelector("#closeChat")
const chat = document.querySelector(".sidebar")

/**
 * Ouvrir ou fermer le chat
 */
openChat.addEventListener("click", () => {
    chat.classList.add("left0")
    openChat.classList.add('di-none')
    closeChat.classList.add("di-inline")
})


closeChat.addEventListener("click", () => {
    chat.classList.remove("left0")
    openChat.classList.remove('di-none')
    closeChat.classList.remove('di-inline')
})



openFilter.addEventListener('click', ()=> {
    console.log("oui")
    filterForm.classList.toggle("filter-right")
})

closeSidebar.addEventListener('click', ()=> {
    sidebar.style.left = '-100%'
})

toggleTheme.addEventListener('click', changeTheme)

function changeTheme() {
    if(body.classList.contains('dark-mode')) {
        lightMode()
    }else if (!body.classList.contains('dark-mode')) {
        darkMode()
    }

    if(window.matchMedia('(prefers-color-sheme: dark)').matches) {
        darkMode()
    }

    function lightMode () {
        body.classList.remove('dark-mode')
        light.classList.add('active')
        dark.classList.remove('active')
    }

    function darkMode() {
        body.classList.add('dark-mode')
        light.classList.remove('active')
        dark.classList.add('active')
    }

    /**
     * Pour les fitres
     */

}

function minScrenn() {

    if(window.innerWidth <= 920){
        return true
    }else{
        return false
    }
}

//TRAITEMENT DE L'ENVOIE DES MESSAGES

const chatForm = document.querySelector("#chat-form");
const sendButton = document.querySelector("#chatSubmit");

sendButton.addEventListener("click", async (event) => {
    event.preventDefault();

    const message = chatForm.querySelector("#message").value;
    const disc = chatForm.querySelector("#disc").value
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value
    console.log(disc)


    try {
        dataTosend = {
            disc : disc,
            message : message
        }
        const response = await fetch(`/send/${disc}`, {
            method: "POST",
            body: JSON.stringify(dataTosend),
            headers: {
                "Content-Type": "application/json",
                'X-CSRFToken': csrfToken,
            },
        });

        if (response.ok) {
            // Le message a été envoyé avec succès
            console.log("Message envoyé !");
        } else {
            // Gestion des erreurs (par exemple, afficher un message d'erreur)
            console.error("Erreur lors de l'envoi du message :", response.status);
        }
    } catch (error) {
        console.error("Erreur lors de l'envoi des données :", error);
    }
});



