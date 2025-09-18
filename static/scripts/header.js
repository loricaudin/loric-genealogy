let nav = document.querySelector("header nav");
let menuCompte = document.querySelector("header .menu-compte");
let boutonNav = document.querySelector("header #bouton-menu-nav")
let boutonCompte = document.querySelector("header .icone-compte");

let header = document.querySelector("header");

function ouvrirFermerMenuNav() {
    boutonNav.classList.toggle("ouvert");
    let resultat = nav.classList.toggle("nav-ouvert");
    if(resultat){
        header.classList.add("header-ouvert");
        header.classList.remove("header-ferme");
    }
    else{
        header.classList.add("header-ferme");
        header.classList.remove("header-ouvert");
    }
}

function ouvrirFermerMenuCompte() {
    menuCompte.classList.toggle("nav-ouvert");
}

if(boutonNav) {
    boutonNav.addEventListener("click", ouvrirFermerMenuNav);
}

if(boutonCompte) {
    boutonCompte.addEventListener("click", ouvrirFermerMenuCompte);
}

document.addEventListener('click', function() {
    if (!header.contains(event.target) && nav.classList.contains("nav-ouvert")) {
        ouvrirFermerMenuNav();
    }
    if (!header.contains(event.target) && menuCompte.classList.contains("nav-ouvert")) {
        ouvrirFermerMenuCompte();
    }
});