document.addEventListener('DOMContentLoaded', function() {
    const checkBtn = document.getElementById('checkBtn');
    const resultDisplay = document.getElementById('result');

    checkBtn.addEventListener('click', async () => {
        // Get the current tab's URL
        let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        
        resultDisplay.innerText = "Checking...";

        try {
            // Send it to our Python server
            const response = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ url: tab.url })
            });
            
            const data = await response.json();
            resultDisplay.innerText = "Result: " + data.status;
            resultDisplay.style.color = data.status === "Safe" ? "green" : "red";
        } catch (error) {
            resultDisplay.innerText = "Error: Server not running!";
            resultDisplay.style.color = "orange";
        }
    });
});