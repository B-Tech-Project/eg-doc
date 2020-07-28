const contain = document.querySelector('div.loader');
const loader = document.createElement('div');
loader.className = 'progress';
const loadingBar = document.createElement('div');
loadingBar.className = 'indeterminate';
loader.appendChild(loadingBar);
contain.appendChild(loader);
window.addEventListener('load', (event) => {
    contain.style.display = 'none';
    contain.classList.add('hidden');
});




