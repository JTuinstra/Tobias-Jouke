let score = 0;

function transition() {

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


    }

}

