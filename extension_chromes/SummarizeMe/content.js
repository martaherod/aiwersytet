function insertTextIntoPage(text) {
    const backgroundContainer = document.createElement('div');
    backgroundContainer.className = "dokodu_summary_popup_background";

    const popupContainer = document.createElement('div');
    popupContainer.className = 'dokodu_summary_popup_container';

    // Stwórz element dla treści popupa
    const popupContent = document.createElement('div');
    popupContent.className = 'dokodu_summary_popup';
    popupContent.textContent = text; // Ustaw treść popupa

    // Dodaj treść do kontenera
    popupContainer.appendChild(popupContent);
    backgroundContainer.appendChild(popupContainer);

    // Dodaj kontener popupa do body strony
    document.body.appendChild(backgroundContainer);

    backgroundContainer.addEventListener('click', () => {
        backgroundContainer.remove();
    })
}


chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
        if (request.type === 'INSERT_SUMMARY') {
            insertTextIntoPage(request.text);
        }
    }
);