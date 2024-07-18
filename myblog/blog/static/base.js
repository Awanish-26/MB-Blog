const toggleButton = document.getElementsByClassName('toggle-button')[0]
const navbarLinks = document.getElementsByClassName('navlist')[0]
const closeMsg = document.getElementsByClassName('close');
const toogleTheme = document.getElementById('dark-mode-toggle');
const htmlElement = document.documentElement;

toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active');
});


toogleTheme.addEventListener('click', () => {
  htmlElement.classList.toggle('dark-mode');
  if (toogleTheme.innerHTML.includes('<i class="bi bi-sun"></i>')){
    toogleTheme.innerHTML = "<i class='bi bi-moon'></i>";
  }
  else{
    toogleTheme.innerHTML = '<i class="bi bi-sun"></i>'
  }
});

