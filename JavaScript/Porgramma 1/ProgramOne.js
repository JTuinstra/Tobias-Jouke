let cards = ['Sugar', 'Salt', 'Pepper', 'Mint', 'Cinnamon', 'Cumin', 'Sugar', 'Salt', 'Pepper', 'Mint', 'Cinnamon', 'Cumin'];
let openedCards = [];
let won = [];

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
        card.id = i;
        card.className = "card";
        card.value = i;
        card.onclick = cardClicked;
        container.appendChild(card);

    }


}

function cardClicked() {
    let card = document.getElementById(this.id);
    openedCards.push(card);
    card.value = cards[this.id - 1];
    if (openedCards.length === 2) {
        let allCards = document.getElementsByClassName('card');

        if (openedCards[0].value === openedCards[1].value) {
            openedCards[0].disabled = true
            openedCards[1].disabled = true;
            openedCards[0].style.backgroundColor = "white";
            openedCards[1].style.backgroundColor = "white";



            openedCards = [];



            let score = document.getElementById('score');
            score.innerHTML = "Score: " + (parseInt(score.innerHTML.split(" ")[1]) + 1);

        } else {
            for (let i = 0; i < allCards.length; i++) {
            if (!openedCards.includes(allCards[i])) {
                allCards[i].disabled = true;
            }
        }
            setTimeout(function () {
                openedCards[0].value = openedCards[0].id;
                openedCards[1].value = openedCards[1].id;
                openedCards = [];

                for (let i = 0; i < allCards.length; i++) {
                    allCards[i].disabled = false;
                }
            }, 1000);
        }
    }
}
