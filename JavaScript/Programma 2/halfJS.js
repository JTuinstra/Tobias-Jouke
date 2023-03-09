document.addEventListener('keypress', function (event) {
    if (event.keyCode === 13) {
        check();
    }
});


function check() {
    let eindelijk = 0;
    let dom = ['kaas', 'pep', 'pepje', 'oma', 'plop', 'oma plop', 'pieter', 'post', 'pieter post', 'dom', 'geen zin', '', ' ', '   ', '    ', '     ']

    let check = document.getElementById("input").value.toLowerCase();

    if (dom.includes(check)) {
        alert("Wauw, je bent dom! :D\nIk had m kunnen verwachten...")
    } else if (check === 'ja') {
        if (eindelijk <= 2) {
            alert('Oke, je mag door')
            window.location.href = "quizMain.html";

        } else {
            alert('Man man man is het zo moeilijk om een serieus antwoord te geven?')
            eindelijk++;
        }

    } else if (check === 'nee') {
        alert('Oke, doei dan.')
        window.close();

    }
    else {
        alert("Ik heb geen idee wat voor bullshit je hebt ingevuld, maar het is niet goed.")
    }
}