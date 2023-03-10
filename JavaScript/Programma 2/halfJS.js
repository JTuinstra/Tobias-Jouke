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

    } else if (check === 'ja' || check === 'jazeker' || check==='j') {
        if (eindelijk <= 2) {
            alert('Oke, je mag door')
            window.location.href = "quizMain.html";

        } else {
            alert('Man man man was het zo moeilijk om een serieus antwoord te geven?')

        }

    } else if (check === 'nee'|| check === 'n') {
        alert('Oke, doei dan.')
        window.location.href = "homePage.html";

    }
    else {
        alert("Ik heb geen idee wat voor bullshit je hebt ingevuld, maar het is niet goed.")
        eindelijk++;
    }
}