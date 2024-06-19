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