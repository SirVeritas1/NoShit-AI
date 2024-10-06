document.getElementById('sendButton').addEventListener('click', async () => {
    const userInput = document.getElementById('userInput').value;
    if (userInput.trim() === '') return;

    // Display user input
    appendMessage(`You: ${userInput}`, 'user');

    // Clear the input field
    document.getElementById('userInput').value = '';

    // Fetch response from your NoShit AI API (this is a placeholder URL)
    const response = await fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.json();

    // Display AI response
    appendMessage(`NoShit: ${data.reply}`, 'ai');
});

function appendMessage(message, type) {
    const chatOutput = document.getElementById('chatOutput');
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    messageDiv.className = type === 'user' ? 'user-message' : 'ai-message';
    chatOutput.appendChild(messageDiv);
}
