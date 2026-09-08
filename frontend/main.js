window.addEventListener('DOMContentLoaded', () => {
    getVisitCount();
});


const functionApiUrl = 'https://func-resumegara.azurewebsites.net/api/getresumecounter'; 

function getVisitCount() {
    
    fetch('https://func-resumegara.azurewebsites.net/api/getresumecounter')
        .then(response => response.json())
        .then(data => {
            document.getElementById('counter').innerText = data.count;
        })
        .catch(error => {
            console.error('Errore contatore:', error);
            document.getElementById('counter').innerText = "1 (Modalità Demo)";
        });
}