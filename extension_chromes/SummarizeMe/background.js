chrome.runtime.onInstalled.addListener(function(){
    chrome.contextMenus.create({
        id: "SummarizeMeMenu",
        title: "Stwórz streszczenie",
        contexts: ["selection"]
    });
});

chrome.contextMenus.onClicked.addListener(function(info, tab){
    if (info.menuItemId == "SummarizeMeMenu") {
        const selectedText = info.selectionText;
        const url = "http://127.0.0.1:5000/summarize";

        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({text: selectedText}),
            mode: 'cors',
        }

        fetch(url, options)
            .then(response => response.json())
            .then(data => chrome.tabs.sendMessage(tab.id, {type: "INSERT_SUMMARY", text: data.text}))
            .catch(error => console.error('Error', error))
    }
})
