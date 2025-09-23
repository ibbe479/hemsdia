// Denna fil hanterar live-förhandsvisningen av jobbannonser

// Hämta formulärfälten och förhandsvisningselementen
const titelInput = document.querySelector('input[name="titel"]');
const beskrivningInput = document.querySelector('input[name="beskrivning"]');
const lonInput = document.querySelector('input[name="lon"]'); // Ändrad från "lön" till "lon"
const platsInput = document.querySelector('input[name="plats"]');

const previewTitel = document.getElementById('preview-titel');
const previewBeskrivning = document.getElementById('preview-beskrivning');
const previewLon = document.getElementById('preview-lon');
const previewPlats = document.getElementById('preview-plats');

// Funktion för att uppdatera förhandsvisningen
function updatePreview() {
    previewTitel.textContent = titelInput.value;
    previewBeskrivning.textContent = beskrivningInput.value;
    previewLon.textContent = lonInput.value;
    previewPlats.textContent = platsInput.value;
}

// Lägg till händelselyssnare på varje formulärfält
titelInput.addEventListener('input', updatePreview);
beskrivningInput.addEventListener('input', updatePreview);
lonInput.addEventListener('input', updatePreview);
platsInput.addEventListener('input', updatePreview);