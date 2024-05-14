const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('navlist')[0]
const closeMsg = document.getElementsByClassName('close');

toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active');
});
