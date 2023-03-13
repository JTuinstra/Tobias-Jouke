let score = 0;
let vraag = 1;


function disableButtons() {
    document.getElementById("antwoord1").disabled = true;
    document.getElementById("antwoord2").disabled = true;
    document.getElementById("antwoord3").disabled = true;
    document.getElementById("antwoord4").disabled = true;
}

function enableButtons() {
    document.getElementById("antwoord1").disabled = false;
    document.getElementById("antwoord2").disabled = false;
    document.getElementById("antwoord3").disabled = false;
    document.getElementById("antwoord4").disabled = false;
}

function transition() {
    document.getElementById("vraag").style.opacity = "0";
    document.getElementById("antwoord1").style.opacity = "0";
    document.getElementById("antwoord2").style.opacity = "0";
    document.getElementById("antwoord3").style.opacity = "0";
    document.getElementById("antwoord4").style.opacity = "0";
    document.getElementById("score").style.opacity = "0";
    document.getElementById('vraagTekst').style.opacity = "0";
    document.getElementById("vraag").style.transition = "opacity 2s";
    document.getElementById("score").style.transition = "opacity 2s";
    document.getElementById('vraagTekst').style.transition = "opacity 2s";

    setTimeout(function () {
        document.getElementById("vraag").style.opacity = "1";
        document.getElementById("antwoord1").style.opacity = "1";
        document.getElementById("antwoord2").style.opacity = "1";
        document.getElementById("antwoord3").style.opacity = "1";
        document.getElementById("antwoord4").style.opacity = "1";
        document.getElementById("score").style.opacity = "1";
        document.getElementById('vraagTekst').style.opacity = "1";
        document.getElementById("vraag").style.transition = "opacity 2s";
        document.getElementById("score").style.transition = "opacity 2s";
        document.getElementById('vraagTekst').style.transition = "opacity 2s";

        document.getElementById("antwoord1").style.backgroundColor = "darkorange";
        document.getElementById("antwoord2").style.backgroundColor = "darkorange";
        document.getElementById("antwoord3").style.backgroundColor = "darkorange";
        document.getElementById("antwoord4").style.backgroundColor = "darkorange";

        enableButtons()
    }, 4000);
}

function foutAntwoord(knop, goed) {
    document.getElementById("antwoord" + knop).innerHTML = "Fout!";
    document.getElementById("antwoord" + knop).style.backgroundColor = "red";

    document.getElementById("antwoord" + goed).style.backgroundColor = "green";

    disableButtons()
    vraag++;

    if (score > 0) {
        score--;
    }

}

function goedAntwoord(knop) {
    document.getElementById("antwoord" + knop).innerHTML = "Correct!";
    document.getElementById("antwoord" + knop).style.backgroundColor = "green";
    score++;

    disableButtons()

    document.getElementById("score").innerHTML = "Score: " + score;
    vraag++;
}

function nieuweVraag(vraagCount, scoreCount, vraagTekst, antwoord1, antwoord2, antwoord3, antwoord4) {
    document.getElementById("vraag").innerHTML = "Vraag " + vraagCount;
    document.getElementById("score").innerHTML = "Score: " + scoreCount;
    document.getElementById("vraagTekst").innerHTML = vraagTekst;

    document.getElementById("antwoord1").innerHTML = antwoord1;
    document.getElementById("antwoord2").innerHTML = antwoord2;
    document.getElementById("antwoord3").innerHTML = antwoord3;
    document.getElementById("antwoord4").innerHTML = antwoord4;


}

function antwoord(knop) {

    if (vraag === 1) {

        if (knop === 3) {
            goedAntwoord(knop)
            setTimeout(transition, 3000)
            setTimeout(nieuweVraag(2, score, "Wat vind jij echt ons, ons ding?", "Walkie talkies", "CSGO", "Muziek", "Creative Destruction"), 3000)

        } else {
            foutAntwoord(knop, 3)
            setTimeout(transition, 3000)
            setTimeout(nieuweVraag(2, score, "Wat vind jij echt ons, ons ding?", "Walkie talkies", "CSGO", "Muziek", "Creative Destruction"), 3000)

        }

    } else if (vraag === 2) {
        nieuweVraag(2, score, "Wat vind jij echt ons, ons ding?", "Walkie talkies", "CSGO", "Muziek", "Creative Destruction");

        if (knop === 1 || knop === 2 || knop === 3 || knop === 4) {
            goedAntwoord(knop)
        }
    }
}

