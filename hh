<style>
body {
background-color: #000;
color: #fff;
font-family: 'Montserrat', sans-serif;
margin: 0;
padding: 0;
overflow-x: hidden;
}
.header {
position: fixed;
top: 0;
left: 0;
width: 100%;
height: 100px;
background-color: #000;
display: flex;
justify-content: center;
align-items: center;
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
.logo {
width: 150px;
height: auto;
margin-right: 20px;
}
.title {
font-size: 48px;
margin: 0;
}
.content {
padding: 100px 20px;
}
.quote {
position: relative;
font-size: 32px;
margin-bottom: 20px;
}
.quote:before {
content: '';
position: absolute;
top: 0;
left: -50px;
width: 50px;
height: 100%;
background-color: #f00;
transform: skewX(-45deg);
}
.quote:after {
content: '';
position: absolute;
top: 0;
right: -50px;
width: 50px;
height: 100%;
background-color: #f00;
transform: skewX(45deg);
}
.quote span {
display: block;
font-size: 24px;
margin-top: 20px;
}
.trivia {
margin-top: 50px;
}
.trivia h3 {
font-size: 32px;
margin-bottom: 20px;
}
.trivia input[type="radio"] {
margin-right: 10px;
}
.trivia button {
margin-top: 20px;
}
.music-player {
position: fixed;
bottom: 0;
left: 0;
width: 100%;
height: 80px;
background-color: #000;
display: flex;
justify-content: center;
align-items: center;
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
.music-player audio {
width: 80%;
}
.music-visualizer {
position: absolute;
bottom: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(255, 0, 0, 0.1);
}
.music-visualizer canvas {
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
}
.chat {
position: fixed;
bottom: 0;
right: 0;
width: 300px;
height: 400px;
background-color: #000;
color: #fff;
display: flex;
flex-direction: column;
justify-content: space-between;
padding: 20px;
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
.chat input[type="text"] {
width: 100%;
height: 50px;
padding: 10px;
margin-bottom: 20px;
}
.chat button {
width: 100%;
height: 50px;
background-color: #f00;
color: #fff;
border: none;
padding: 10px;
cursor: pointer;
}
</style>
<div class="header">
<img class="logo" src="https://i.imgur.com/gLZbBmj.jpg" alt="Anarchy Symbol">
<h1 class="title">Anarchy🖤</h1>
</div>
<div class="content">
<div class="quote">
<q>Anarchy is the only slight glimmer of hope.</q>
<br>
<span>- Slavoj Žižek</span>
</div>
<div class="trivia">
<h3>Test your Anarchy🖤 knowledge</h3>
<p>What is the political philosophy that advocates for the abolition of all government and the establishment of a society based on voluntary cooperation and mutual aid?</p>
<label><input type="radio" name="trivia1" value="Anarchy">Anarchy</label>
<br>
 more_vert <label><input type="radio" name="trivia1" value="Monarchy">Monarchy</label>
<br>
<label><input type="radio" name="trivia1" value="Democracy">Democracy</label>
<br>
<button onclick="checkTrivia()">Submit</button>
<p id="trivia-result"></p>
</div>
<div class="music-player">
<audio id="music-player" src="https://www.bensound.com/bensound-music/bensound-anarchist.mp3" preload="auto" loop></audio>
<div class="music-visualizer">
<canvas id="visualizer"></canvas>
</div>
</div>
</div>
<div class="chat">
<input type="text" id="chat-input" placeholder="Type your message here...">
<button onclick="sendChat()">Send</button>
<div id="chat-output"></div>
</div>
<script>
const triviaForm = document.querySelector('.trivia form');
const triviaAnswer = document.querySelector('.trivia input[value="Anarchy"]');
const triviaResult = document.getElementById('trivia-result');
const chatInput = document.getElementById('chat-input');
const chatOutput = document.getElementById('chat-output');
const musicPlayer = document.getElementById('music-player');
const visualizer = document.getElementById('visualizer');
triviaForm.addEventListener('submit', (e) => {
e.preventDefault();
if (triviaAnswer.checked) {
triviaResult.textContent = 'Correct!';
triviaResult.style.color = '#0f0';
} else {
triviaResult.textContent = 'Incorrect. The correct answer is Anarchy.';
triviaResult.style.color = '#f00';
}
});
function checkTrivia() {
triviaForm.dispatchEvent(new Event('submit'));
}
function sendChat() {
const message = chatInput.value;
const p = document.createElement('p');
p.textContent = message;
chatOutput.appendChild(p);
chatInput.value = '';
}
musicPlayer.volume = 0.2;
const analyser = musicPlayer.getContext('webkitAudioContext').createAnalyser();
analyser.fftSize = 512;
const dataArray = new Uint8Array(analyser.frequencyBinCount);
musicPlayer.addEventListener('play', () => {
musicPlayer.setSinkId('default');
analyser.getByteTimeDomainData(dataArray);
visualizer.width = visualizer.parentElement.offsetWidth;
visualizer.height = visualizer.parentElement.offsetHeight;
visualizer.style.backgroundColor = '#000';
visualizer.style.mixBlendMode = 'multiply';
visualizer.getContext('2d').lineWidth = 2;
visualizer.getContext('2d').strokeStyle = '#f00';
visualizer.getContext('2d').beginPath();
visualizer.getContext('2d').moveTo(0, visualizer.height / 2);
const draw = () => {
requestAnimationFrame(draw);
analyser.getByteTimeDomainData(dataArray);
visualizer.getContext('2d').lineTo(visualizer.width, dataArray[Math.floor(dataArray.length * (musicPlayer.currentTime % dataArray.length) / musicPlayer.duration)] / 255 * visualizer.height);
visualizer.getContext('2d').stroke();
};
draw();
});
</script>
