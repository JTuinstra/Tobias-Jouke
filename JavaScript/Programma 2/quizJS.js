    let score = 0;
let vraag = 1;

let antwoorden = [];

function antwoordenOpslaan(knop, correctAntwoord) {
    let vraag = document.getElementById("vraagTekst").innerHTML;
    let antwoord = document.getElementById("antwoord" + knop).innerHTML;
    antwoorden.push(vraag + " : " + 'Jouw antwoord: ' + antwoord + ' : ' + 'Goed antwoord: ' + correctAntwoord);


    return antwoorden;
}


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

function transition(vraagCount, scoreCount, vraagTekst, antwoord1, antwoord2, antwoord3, antwoord4, hoeveelButtons, end) {
    document.getElementById("vraag").style.opacity = "0";
    document.getElementById("antwoord1").style.opacity = "0";
    document.getElementById("antwoord2").style.opacity = "0";
    document.getElementById("antwoord3").style.opacity = "0";
    document.getElementById("antwoord4").style.opacity = "0";
    document.getElementById("score").style.opacity = "0";
    document.getElementById('vraagTekst').style.opacity = "0";
    document.getElementById("vraag").style.transition = "opacity 0.5s";
    document.getElementById("score").style.transition = "opacity 0.5s";
    document.getElementById('vraagTekst').style.transition = "opacity 0.5s";

    setTimeout(function () {
        document.getElementById("vraag").style.opacity = "1";
        document.getElementById("antwoord1").style.opacity = "1";
        document.getElementById("antwoord2").style.opacity = "1";
        document.getElementById("antwoord3").style.opacity = "1";
        document.getElementById("antwoord4").style.opacity = "1";
        document.getElementById("score").style.opacity = "1";
        document.getElementById('vraagTekst').style.opacity = "1";
        document.getElementById("vraag").style.transition = "opacity 0.5s";
        document.getElementById("score").style.transition = "opacity 0.5s";
        document.getElementById('vraagTekst').style.transition = "opacity 0.5s";

        if (hoeveelButtons === true) {
            document.getElementById("antwoord3").style.display = "none";
            document.getElementById("antwoord4").style.display = "none";

        } else {
            document.getElementById("antwoord3").style.display = "block";
            document.getElementById("antwoord4").style.display = "block";
        }

        document.getElementById("antwoord1").style.backgroundColor = "darkorange";
        document.getElementById("antwoord2").style.backgroundColor = "darkorange";
        document.getElementById("antwoord3").style.backgroundColor = "darkorange";
        document.getElementById("antwoord4").style.backgroundColor = "darkorange";

        if (end === 'end') {
            document.getElementById("vraag").innerHTML = 'Einde';
            document.getElementById("score").innerHTML = "Je score is: " + scoreCount + "/?";

        } else {
            document.getElementById("vraag").innerHTML = "Vraag " + vraagCount;
            document.getElementById("score").innerHTML = "Score: " + scoreCount;
        }
        document.getElementById("vraagTekst").innerHTML = vraagTekst;

        document.getElementById("antwoord1").innerHTML = antwoord1;
        document.getElementById("antwoord2").innerHTML = antwoord2;
        document.getElementById("antwoord3").innerHTML = antwoord3;
        document.getElementById("antwoord4").innerHTML = antwoord4
    }, 4000);

    if (end !== 'end') {
        setTimeout(enableButtons, 5500)
    } else {
    }
}


function goedAntwoord(knop) {
    document.getElementById("antwoord" + knop).innerHTML = "Correct!";
    document.getElementById("antwoord" + knop).style.backgroundColor = "green";
    score++;

    disableButtons()


    vraag++;
}

function foutAntwoord(knop, goed) {
    document.getElementById("antwoord" + knop).innerHTML = "Fout!";
    document.getElementById("antwoord" + knop).style.backgroundColor = "red";

    document.getElementById("antwoord" + goed).style.backgroundColor = "green";

    disableButtons()
    vraag++;

}

function allesGoed() {
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

    disableButtons()
}


function antwoord(knop) {

    if (vraag === 1) {

        if (knop === 3) {
            antwoordenOpslaan(knop, 'Amsterdam')
            goedAntwoord(knop)
            setTimeout(transition, 1000, 2, score, "Wat vind jij echt ons, ons ding?", "Walkie talkies", "CS:GO", "Muziek", "Creative Destruction", false, 'none')

        } else {
            antwoordenOpslaan(knop, 'Amsterdam')
            foutAntwoord(knop, 3)
            setTimeout(transition, 1000, 2, score, "Wat vind jij echt ons, ons ding?", "Walkie talkies", "CS:GO", "Muziek", "Creative Destruction", false, 'none')


        }

    } else if (vraag === 2) {

        if (knop === 1 || knop === 2 || knop === 3 || knop === 4) {
            antwoordenOpslaan(knop, 'Alles')
            allesGoed()
            setTimeout(transition, 1000, 3, score, "Wie of wat is de echte sprayer?", 'De Russen', 'Ryan', 'Mark Rutte', 'RAM', false, 'none')

        }

    } else if (vraag === 3) {

        if (knop === 4) {
            antwoordenOpslaan(knop, 'RAM')
            goedAntwoord(knop)
            setTimeout(transition, 1000, 4, score, "Wat is de beste game?", "CS:GO", "Minecraft", "Creative Destruction", "Fortnite", false, 'none')

        } else {
            antwoordenOpslaan(knop, 'RAM')
            foutAntwoord(knop, 4)
            setTimeout(transition, 1000, 4, score, "Wat is de beste game?", "CS:GO", "Minecraft", "Creative Destruction", "Fortnite", false, 'none')

        }
    } else if (vraag === 4) {

        if (knop === 1 || knop === 2 || knop === 3 || knop === 4) {
            antwoordenOpslaan(knop, 'Alles')
            allesGoed()
            setTimeout(transition, 1000, 5, score, 'Ben je het eens met de volgende stelling: Oma Plop is de beste rapper?', 'Ja', 'Nee', 'Misschien', 'Ik weet het niet', false, 'none')

        }
    } else if (vraag === 5) {

        if (knop === 1 || knop === 2 || knop === 3 || knop === 4) {
            antwoordenOpslaan(knop, 'Alles')
            allesGoed()
            setTimeout(transition, 1000, 6, score, 'Kies een van de volgende dingen:', 'Muziek', 'Gamen', 'Programmeren', 'Koekjes', false, 'none')

        }
    } else if (vraag === 6) {

        if (knop === 1 || knop === 2 || knop === 3 || knop === 4) {
            antwoordenOpslaan(knop, 'Alles')
            allesGoed()
            setTimeout(transition, 1000, 7, score, 'Welke muziek vind je het leukst?', 'Lofi', 'Lofi rap', 'Playlist van Jouke', 'Andere playlist van Jouke', false, 'none')
        }

    } else if (vraag === 7) {

        if (knop === 1 || knop === 2 || knop === 3 || knop === 4) {
            antwoordenOpslaan(knop, 'Alles')
            allesGoed()
            setTimeout(transition, 1000, 8, score, 'Gefeliciteerd nog', 'Ja', 'Hou je bek', 'Nee', 'Dankjewel', false, 'none')
        }
    } else if (vraag === 8) {
        if (knop === 1 || knop === 2 || knop === 3 || knop === 4) {
            antwoordenOpslaan(knop, 'Alles')
            allesGoed()
            setTimeout(transition, 1000, '9', score, 'Dakota?', 'Dakota', 'Ja', 'Dakota', 'Nee', false, 'none')
            setTimeout(einde, 1000, score)
        }
    }
}

function einde(eindscore) {

    function fallIn(create) {
        create.style.scale = "1";
    }

    let vraag = document.getElementById("vraag");
    let score = document.getElementById("score");
    let vraagTekst = document.getElementById("vraagTekst");
    let antwoord1 = document.getElementById("antwoord1");
    let antwoord2 = document.getElementById("antwoord2");
    let antwoord3 = document.getElementById("antwoord3");
    let antwoord4 = document.getElementById("antwoord4");

    vraagTekst.style.scale = "0";
    antwoord1.style.scale = "0";
    antwoord2.style.scale = "0";
    antwoord3.style.scale = "0";
    antwoord4.style.scale = "0";

    vraag.innerHTML = "Einde";
    score.innerHTML = "Je score is: " + eindscore + "/7";


    setTimeout(function () {
        document.getElementById("vraag").innerHTML = "Einde";

        disableButtons()

        let newDIV = document.createElement("div");
        newDIV.id = "eind";
        document.body.appendChild(newDIV);

        console.log(antwoorden)
        for (let i = 0; i < antwoorden.length; i++) {
            let create = document.createElement("p");
            create.style.scale = "0";

            setTimeout(fallIn, 1000, create)
            if (i === 0) {
                create.style.marginTop = "-170px";
            }

            create.innerHTML = antwoorden[i];
            newDIV.appendChild(create);

        }
    }, 5000)


}






