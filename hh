<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Anarchy Chat</title>
    <style>
        .anarchy-chat {
            width: 500px;
            height: 600px;
            border: 1px solid #000;
            padding: 10px;
            overflow: auto;
        }
    </style>
</head>
<body>
    <h1>Anarchy Chat</h1>
    <div class="anarchy-chat" id="anarchy-chat"></div>
    <input type="text" id="anarchy-chat-input" placeholder="Type your message here...">
    <button onclick="sendChatMessage()">Send</button>
    <script>
        // Fetch chat content from the remote API
        function fetchChatContent() {
            var chatUrl = "https://gptcall.net/chat?data=%7B%22contact%22%3A%7B%22id%22%3A%227ppofiEl1zkx0Ouu-0nra%22%2C%22flow%22%3Atrue%7D%7D#chatID=%222024-06-19T05%3A59%3A17.995Z%22";
            fetch(chatUrl)
                .then(function(response) {
                    return response.text();
                })
                .then(function(chatContent) {
                    document.querySelector('#anarchy-chat').innerText = chatContent;
                });
        }

        // Send a chat message to the remote API
        function sendChatMessage() {
            var chatInput = document.querySelector('#anarchy-chat-input');
            var chatMessage = chatInput.value;
            if (chatMessage) {
                var chatUrl = "https://gptcall.net/chat?data=%7B%22contact%22%3A%7B%22id%22%3A%227ppofiEl1zkx0Ouu-0nra%22%2C%22flow%22%3Afalse%2C%22message%22%3A%22" + encodeURIComponent(chatMessage) + "%22%7D%7D#chatID=%222024-06-19T05%3A59%3A17.995Z%22";
                fetch(chatUrl)
                    .then(function(response) {
                        return response.text();
                    })
                    .then(function(chatContent) {
                        document.querySelector('#anarchy-chat').innerText = chatContent;
                        chatInput.value = "";
                    });
            }
        }

        // Periodically fetch chat content from the remote API
        setInterval(fetchChatContent, 1000);
    </script>
</body>
</html>