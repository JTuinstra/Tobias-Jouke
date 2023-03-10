let score = 0;

function transition(number) {
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

        document.getElementById("antwoord1").disabled = false;
        document.getElementById("antwoord2").disabled = false;
        document.getElementById("antwoord3").disabled = false;
        document.getElementById("antwoord4").disabled = false;
    }, 4000);
}

function antwoord1(knop) {
    if (knop === 3) {
        document.getElementById("antwoord" + knop).innerHTML = "Correct!";
        document.getElementById("antwoord" + knop).style.backgroundColor = "green";
        score++;

        document.getElementById("antwoord1").disabled = true;
        document.getElementById("antwoord2").disabled = true;
        document.getElementById("antwoord3").disabled = true;
        document.getElementById("antwoord4").disabled = true;

        document.getElementById("score").innerHTML = "Score: " + score;

        setTimeout(transition, 5000);


    } else {
        document.getElementById("antwoord" + knop).innerHTML = "Fout!";
        document.getElementById("antwoord" + knop).style.backgroundColor = "red";

        document.getElementById("antwoord1").disabled = true;
        document.getElementById("antwoord2").disabled = true;
        document.getElementById("antwoord3").disabled = true;
        document.getElementById("antwoord4").disabled = true;

        if (score > 0) {
            score--;
        }

        transition(1)


    }

}

