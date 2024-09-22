//Criação das variaveis 
const bpm = document.getElementById('bpm');
const h5 = document.querySelector('h5')
const play = document.getElementById('play')
const audio = document.querySelector('audio')
const increaseBpmButton = document.getElementById('increaseBpm')
const decreaseBpmButton = document.getElementById('decreaseBpm')
const bpmValue = document.getElementById('bpmValue');


let currentBpm = 40
let isPlaying = false
let timer = null

function tick(){
    audio.currentTime = 0
    audio.play()
}

// aumenta os bpms quando clicar no botao +
increaseBpmButton.addEventListener('click', function() {
    const currentBpm = parseInt(bpmValue.textContent);
    bpmValue.textContent = currentBpm + 1 + ' bpm';
});

// diminui os bpms quando clicar no botao -
decreaseBpmButton.addEventListener('click', function() {
    const currentBpm = parseInt(bpmValue.textContent);
    if (currentBpm > 1) {
        bpmValue.textContent = currentBpm - 1 + ' bpm';
    }
});






//Sempre que arrastamos a linha o texto muda consoante a velocidade
bpm.addEventListener('change', function(){
    h5.innerHTML = this.value + 'bpm'
    currentBpm = parseInt(this.value)
    if(isPlaying){
        clearInterval(timer)
        tick()
        timer = setInterval(tick, (60 * 1000) / currentBpm) // Set the interval time correctly
    }
})

// Alterna entre Play e Stop no botão play e inicia/para o metrônomo
play.addEventListener('click',  function(){
    if(isPlaying){
        play.innerHTML = 'Play '
        clearInterval(timer)
    }else{
        play.innerHTML = 'Stop '
        tick()
        timer = setInterval(tick, (60 * 1000) / currentBpm) // Set the interval time correctly
    }
    isPlaying = !isPlaying
})