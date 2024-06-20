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
        const dataTosend = {
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
        console.error("Erreur lors de l'envoi des données :", error)
    }
    document.getElementById('message').value = ""
    let small_talk = document.querySelector("#smallTalk")
    small_talk.scrollTop = small_talk.scrollHeight;
});

let urlDisc = 0
    function getDatas(none=0){
            const lien = window.location.href
            const disc = lien.charAt(lien.length - 1)
        
            const url = `/getMessages/${disc}-${none}`;
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    if(!(data["deja"])){
                        let sender = data["sender"]
                        let messages = data["messages"]
                        let lastMessage = messages[messages.length -1]
                        let day = lastMessage["id"]
                        urlDisc = day
                        let receiver_img = data["receiver_img"]
                        let sender_img = data["sender_img"]
                        donnees = messageOrderByDate(messages)
                        
                        addedDateAndCreateMessage(donnees, sender, sender_img, receiver_img)
                    }
                })
                .catch(error => {
                    console.error('Erreur lors de la récupération des données :', error)
                })
   
    }
/*     setInterval(() => {
        console.log(urlDisc)
        getDatas(urlDisc); // Appel de getDatas avec urlDisc comme argument
    }, 500) */




function FormatDate(dateISO) {
    // Créer un objet Date à partir de la chaîne ISO 8601
    let date = new Date(dateISO)

    // Obtenir l'heure et les minutes
    let heures = date.getHours()
    let minutes = date.getMinutes()

    // Formater les heures et les minutes avec deux chiffres (ajouter un zéro devant si nécessaire)
    let heuresFormatees = heures < 10 ? '0' + heures : heures;
    let minutesFormatees = minutes < 10 ? '0' + minutes : minutes;

    // Retourner la chaîne au format "HH:mm"
    return heuresFormatees + ':' + minutesFormatees;
}

function messageOrderByDate(messages){
    let date = {}
    for(let message of messages) {
        const day = getChurtDate(message["created_at"])
        ajouterMessage(day, message, date)
    }
    return date
}

function addedDateAndCreateMessage(data, sender, sender_img, receiver_img, scroll=1) {
    let chatDate = document.querySelectorAll(".chat-date")
    
    if(chatDate.length >0){
        lastDate = chatDate[(chatDate.length) -1]
        for(key in data){
            if(lastDate.dataset.date == key) {
                messageRender(data[key], sender, sender_img, receiver_img, scroll)
            }else{
                createChatDate(key)
                messageRender(data[key], sender, sender_img, receiver_img, scroll)
            }
        }
    }else{
        for(key in data){
            createChatDate(key)
            messageRender(data[key], sender, sender_img, receiver_img, scroll)
        }   

    }
}

function createChatDate(key){
    let small_talk = document.querySelector("#smallTalk")
    let chat_date = document.createElement("div")
    let small = document.createElement("small")
    small.textContent = key
    chat_date.classList.add("chat-date")
    chat_date.appendChild(small)
    chat_date.dataset.date = key
    small_talk.appendChild(chat_date)
    }

function messageRender(messages, sender, sender_img, receiver_img, scroll = 1) {
    for(let message of messages){
        let small_talk = document.querySelector("#smallTalk")
        let talk = document.createElement("div")
        let talk_mess_hor = document.createElement("div")
        let talk_img = document.createElement("div")
        let img = document.createElement("img")
        let p = document.createElement('p')
        let small = document.createElement('small')
        talk_img.classList.add("talk_img")
        talk.classList.add("talk")

        talk_mess_hor.classList.add("chat-mes-hor")


        if(message["user_id"] === sender){
            talk.classList.add("right")
            img.src = sender_img
        }else{
            talk.classList.add("left")
            img.src = receiver_img
        }
        talk_img.appendChild(img)
        p.textContent = message["content"]
        talk_mess_hor.appendChild(p)
        small.textContent = FormatDate(message["created_at"])
        talk_mess_hor.appendChild(small)
        talk.appendChild(talk_img)
        talk.appendChild(talk_mess_hor)
        if (scroll == 1) {
            small_talk.appendChild(talk)
            scrollToBottom("#smallTalk")
            
        }else{
            small_talk.appendChild(talk)
            
        }
    }
}



function ajouterMessage(jour, message, date) {
    // Vérifier si la journée existe déjà dans l'objet date
    if (!date[jour]) {
        date[jour] = []; // Si non, créer un tableau vide pour cette journée
    }
    // Ajouter le message au tableau correspondant à la journée
    date[jour].push(message);
}




function getChurtDate(date) {
    return (new Date(date)).toLocaleString(undefined, {dateStyle: 'medium'})
}

function in_array(data, element) {
    return data.includes(element);
}


function getTimeStamp(timestamp){
    const date = new Date(timestamp)
    return date.getTime()
}

document.addEventListener('DOMContentLoaded', function() {
    let small_talk = document.querySelector('#smallTalk');
    if (small_talk !== null) {
        small_talk.scrollTop = small_talk.scrollHeight;
    }
});

window.onload = function() {
    let small_talk = document.querySelector('#smallTalk');
    if (small_talk !== null) {
        small_talk.scrollTop = small_talk.scrollHeight;
    }
};

function scrollToBottom(elementId) {
    let element = document.querySelector(elementId);
    if (element) {
        element.scrollTop = element.scrollHeight;
    }
}


/* GESTION DE LIKE */



async function senderLike(element1, element2){
    try {
        const dataTosend = {
            liker : element1,
            liked : element2
        }
        const response = await fetch(`/like/${element1}/${element2}`, {
            method: "POST",
            body: JSON.stringify(dataTosend),
            headers: {
                "Content-Type": "application/json"
            }
        });
    
        if (response.ok) {
            // Le message a été envoyé avec succès
            console.log("Message envoyé !");
        } else {
            // Gestion des erreurs (par exemple, afficher un message d'erreur)
            console.error("Erreur lors de l'envoi du message :", response.status);
        }
    } catch (error) {
        console.error("Erreur lors de l'envoi des données :", error)
    }
}




function  generatedSuggest() {

}


function matchingUser (element) {
    let liker = element.dataset.user
    let liked = element.dataset.like
    let url = "lo"
    fetch(url)
}

const likeButtons = document.querySelectorAll('.like');

// Parcourir chaque bouton 'like' et ajouter un écouteur de clic
likeButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Code à exécuter lorsque l'élément 'like' est cliqué
        console.log('Bouton like cliqué !');
        // Ajoutez ici le code que vous souhaitez exécuter lors du clic sur un bouton 'like'
    });
});



/* document.getElementById('message').value = ""
let small_talk = document.querySelector("#smallTalk")
small_talk.scrollTop = small_talk.scrollHeight;                 'X-CSRFToken': csrfToken,*/


