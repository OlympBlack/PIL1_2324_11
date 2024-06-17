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
const filterForm = document.querySelector(".filter .filter-form")

const openChat = document.querySelector("#openChat")
const closeChat = document.querySelector("#closeChat")
const chat = document.querySelector(".sidebar")

/**
 * Ouvrir ou fermer le chat
 */
openChat.addEventListener("click", () => {
    if(minScrenn()){
        closeChat.style.display = 'inline'
        openChat.style.display = 'none'
        chat.style.left = '0%'
    }else{
        closeChat.style.display = 'none'
        openChat.style.display = 'none'
        chat.style.left = '0%'
    }
})


closeChat.addEventListener("click", ()=>{
    if(minScrenn()){
        openChat.style.display = 'inline'
        closeChat.style.display = 'none'
        chat.style.left = "-100%"
    }else{
        closeChat.style.display = 'none'
        openChat.style.display = 'none'
        chat.style.left = '0%'
    }

})



openFilter.addEventListener('click', ()=> {
    if(filterHeader.classList.contains("positionRight")){
        console.log("Oui")
        filterHeader.classList.remove("positionRight")
    }else{
        console.log("non")
    }

    if(filterForm.style.display){
        filterForm.style.display = ''
    }else{
        filterForm.style.display = "none"

    }
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


filterup.addEventListener('click', toggleFilt)

function toggleFilt(){

    if(filterForm.style.display){
        if(filterForm.style.display == ''){

            if(filterForm.classList.contains("positionRight")) {
                filterForm.classList.remove("positionRight")
                filterup.classList.add("bi-caret-up-fill")
                filterup.classList.remove("bi-caret-down-fill")
            }else{
                filterForm.classList.add("positionRight")
                filterup.classList.remove("bi-caret-up-fill")
                filterup.classList.add("bi-caret-down-fill")
            }
        }else {
            if(filterForm.classList.contains("positionRight")) {
                filterForm.classList.remove("positionRight")
                filterup.classList.add("bi-caret-up-fill")
                filterup.classList.remove("bi-caret-down-fill")
            }else{
                filterForm.classList.add("positionRight")
                filterup.classList.remove("bi-caret-up-fill")
                filterup.classList.add("bi-caret-down-fill")
            }
            filterForm.style.display = ''
        }

    }else{
        if(filterForm.classList.contains("positionRight")) {
            filterForm.classList.remove("positionRight")
            filterup.classList.add("bi-caret-up-fill")
            filterup.classList.remove("bi-caret-down-fill")
        }else{
            filterForm.classList.add("positionRight")
            filterup.classList.remove("bi-caret-up-fill")
            filterup.classList.add("bi-caret-down-fill")
        }
        

    }



}

function minScrenn() {

    if(window.innerWidth <= 920){
        return true
    }else{
        return false
    }
}

