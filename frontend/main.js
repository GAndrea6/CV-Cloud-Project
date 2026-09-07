window.addEventListener('DOMContentLoaded', () => {
    getVisitCount();
});

// Indirizzo dell'API (verrà sostituito dall'URL definitivo dell'Azure Function)
const functionApiUrl = ' https://func-resumegara.azurewebsites.net/api/getresumecounter'; 

function getVisitCount() {
    // Per ora simuliamo un valore di test finché non creiamo il backend
    fetch('https://func-resumegara.azurewebsites.net/api/GetResumeCounter')
        .then(response => response.json())
        .then(data => {
            document.getElementById('counter').innerText = data.count;
        })
        .catch(error => {
            console.error('Errore contatore:', error);
            document.getElementById('counter').innerText = "1 (Modalità Demo)";
        });
}