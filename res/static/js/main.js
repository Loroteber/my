fakMaxBusy = false;

function fakMax(e) {
    if (!fakMaxBusy) {
        fakMaxBusy = true;
       
        const sound = new Audio('/static/sound/gaster.mp3');
       
        sound.addEventListener('ended', () => { e.remove(); });
       
        e.classList.add('disappearing');

        sound.play();    
    }

}

async function updateMusic() {
    console.log("[music] updating...")
    
    const response = await fetch("/service/music");
    if (!response.ok) return console.log("[music] fuck");

    const musicBody = document.querySelector("#music");
    const newBody = await response.text();

    const temp = document.createElement("div");
    temp.innerHTML = newBody;

    if (musicBody.innerHTML !== temp.innerHTML) {
        musicBody.innerHTML = temp.innerHTML;
        console.log("[music] updated!");
    } else {
        console.log("[music] no need to update");
    } 
}

setInterval(updateMusic, 15000);