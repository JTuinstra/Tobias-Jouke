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

function transition(vraagCount, scoreCount, vraagTekst, antwoord1, antwoord2, antwoord3, antwoord4) {
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

        document.getElementById("vraag").innerHTML = "Vraag " + vraagCount;
        document.getElementById("score").innerHTML = "Score: " + scoreCount;
        document.getElementById("vraagTekst").innerHTML = vraagTekst;

        document.getElementById("antwoord1").innerHTML = antwoord1;
        document.getElementById("antwoord2").innerHTML = antwoord2;
        document.getElementById("antwoord3").innerHTML = antwoord3;
        document.getElementById("antwoord4").innerHTML = antwoord4;

        enableButtons()
    }, 4000);
}

function foutAntwoord(knop, goed) {
    document.getElementById("antwoord" + knop).innerHTML = "Fout!";
    document.getElementById("antwoord" + knop).style.backgroundColor = "red";

    document.getElementById("antwoord" + goed).style.backgroundColor = "green";

    disableButtons()
    vraag++;

}

function goedAntwoord(knop) {
    document.getElementById("antwoord" + knop).innerHTML = "Correct!";
    document.getElementById("antwoord" + knop).style.backgroundColor = "green";
    score++;

    disableButtons()


    vraag++;
}


function antwoord(knop) {

    if (vraag === 1) {

        if (knop === 3) {
            goedAntwoord(knop)
            setTimeout(transition, 3000, 2, score, "Wat vind jij echt ons, ons ding?", "Walkie talkies", "CS:GO", "Muziek", "Creative Destruction")


        } else {
            foutAntwoord(knop, 3)
            setTimeout(transition, 3000, 2, score, "Wat vind jij echt ons, ons ding?", "Walkie talkies", "CS:GO", "Muziek", "Creative Destruction")


        }

    } else if (vraag === 2) {

        if (knop === 1 || knop === 2 || knop === 3 || knop === 4) {
            document.getElementById("antwoord1").innerHTML = "Correct!";
            document.getElementById("antwoord1").style.backgroundColor = "green";
            document.getElementById("antwoord2").innerHTML = "Correct!";
            document.getElementById("antwoord2").style.backgroundColor = "green";
            document.getElementById("antwoord3").innerHTML = "Correct!";
            document.getElementById("antwoord3").style.backgroundColor = "green";
            document.getElementById("antwoord4").innerHTML = "Correct!";
            document.getElementById("antwoord4").style.backgroundColor = "green";
            score++;
            vraag++;

            setTimeout(transition, 3000, 3, score, "Wie of wat is de echte sprayer?", 'De Russen', 'Ryan', 'Mark Rutte', 'RAM')
        }
    } else if (vraag === 3){
        if (knop === 4){
            goedAntwoord(knop)
            setTimeout(transition, 3000, 4, score, '')
        } else{
            foutAntwoord(knop)
            setTimeout(transition, 3000, )

        }
    }
}





