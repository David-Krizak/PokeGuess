let finalScore = 0;
let modal;

window.onload = async () => {
    modal = new bootstrap.Modal(
        document.getElementById("gameOverModal")
    );
    await loadPokemon();
};

async function submitGuess() {
    const guess = document.getElementById("guess").value;

    const res = await fetch("/guess", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({guess})
    });

    const data = await res.json();

    if (data.result === "correct") {
        document.getElementById("score").innerText = "⭐ " + data.score;
        document.getElementById("guess").value = "";
        loadPokemon();
    }
    else if (data.result === "wrong") {
        document.getElementById("lives").innerText = "❤️ " + data.lives;
        shake();
    }
    else {
        endGame(data.answer, data.score);
    }
}

async function getHint() {
    const res = await fetch("/hint");
    const data = await res.json();
    document.getElementById("hint").innerText = data.hint;
}

async function giveUp() {
    const res = await fetch("/giveup", {method: "POST"});
    const data = await res.json();
    endGame(data.answer, data.score);
}

function endGame(answer, score) {
    finalScore = score;
    document.getElementById("pokemon-img").classList.remove("silhouette");
    document.getElementById("final-score").innerText =
        `Score: ${score} | Bio je: ${answer}`;
    modal.show();
}

async function saveScore() {
    const player = document.getElementById("player-name").value || "Anon";

    await fetch("/save-score", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({player, score: finalScore})
    });

    modal.hide();
    loadScores();
}

async function loadPokemon() {
    const res = await fetch("/pokemon");
    const data = await res.json();
    const img = document.getElementById("pokemon-img");
    img.src = data.image;
    img.classList.add("silhouette");
}

async function loadScores() {
    const res = await fetch("/scores");
    const data = await res.json();
    const board = document.getElementById("scoreboard");
    const list = document.getElementById("scores");
    list.innerHTML = "";
    data.forEach(s => {
        list.innerHTML += `<li>${s.player} – ${s.score}</li>`;
    });
    board.classList.remove("d-none");
}
function shake() {
    const card = document.querySelector(".game-card");
    card.classList.add("shake");
    setTimeout(() => card.classList.remove("shake"), 300);
}
function newGame() {
    window.location.reload();
}
