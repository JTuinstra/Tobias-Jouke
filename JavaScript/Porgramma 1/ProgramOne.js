let cards = ['Sugar', 'Salt', 'Pepper', 'Mint', 'Cinnamon', 'Cumin', 'Sugar', 'Salt', 'Pepper', 'Mint', 'Cinnamon', 'Cumin'];
let openedCards = [];

function MemoryEasy() {

    cards.sort(() => Math.random() - 0.5);

    document.getElementById('diff').style.scale = "0";

    let container = document.createElement("div");
    container.id = "container";
    document.body.appendChild(container);
    let score = document.createElement("h2");
    score.id = "score";
    score.innerHTML = "Score: 0";
    container.appendChild(score);

    for (let i = 1; i <= 12; i++) {
        let card = document.createElement("input");
        card.type = "button";
        card.id = cards[i];
        card.className = "card";
        card.value = i;
        card.addEventListener("click", cardClicked);
        container.appendChild(card);

    }


}

function cardClicked() {
    let card = document.getElementById(this.id);

    if (openedCards.length < 2) {
        card.style.backgroundColor = "gray";
        openedCards.push(card);

        if (openedCards[0] == openedCards[1]) {
            openedCards[0].style.backgroundColor = "white";
            openedCards[1].style.backgroundColor = "white";
            openedCards = [];
        }
    } else {
        openedCards[0].style.backgroundColor = "green";
        openedCards[1].style.backgroundColor = "green";
        openedCards = [];
    }


}