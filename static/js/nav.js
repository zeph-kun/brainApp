const width  = window.innerWidth || document.documentElement.clientWidth || 
document.body.clientWidth;
const height = window.innerHeight|| document.documentElement.clientHeight|| 
document.body.clientHeight;
const buttons = document.getElementById("buttons");
const user = document.getElementById("user");
const menuusr = document.getElementById("menuusr");
const infosusr = document.getElementById("infosusr");
const menunotifs = document.getElementById("menunotifs");
const notif = document.getElementById("notif");
const panier = document.getElementById("panier");
const menupanier = document.getElementById("menupanier");
const messages = document.getElementById("messages");

infosusr.addEventListener("click", ()=>{
    if(menuusr.classList.contains("inactivemenu")){
        menuusr.classList.remove("inactivemenu");
    } else {
        menuusr.classList.add("inactivemenu");
    }
});

messages.addEventListener("click", ()=>{
    if(menunotifs.classList.contains("inactivemenu")){
        menunotifs.classList.remove("inactivemenu");
    } else {
        menunotifs.classList.add("inactivemenu");
    }
});

panier.addEventListener("click", ()=>{
    if(menupanier.classList.contains("inactivemenu")){
        menupanier.classList.remove("inactivemenu");
    } else {
        menupanier.classList.add("inactivemenu");
    }
});

notif.addEventListener("click", ()=>{
    if(menunotifs.classList.contains("inactivemenu")){
        menunotifs.classList.remove("inactivemenu");
    } else {
        menunotifs.classList.add("inactivemenu");
    }
});