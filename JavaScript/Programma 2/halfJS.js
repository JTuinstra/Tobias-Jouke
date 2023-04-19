document.addEventListener('keypress', function (event) {
    if (event.keyCode === 13) {
        check(true)
        document.getElementById("button").click();
    }
});


function check(bool) {

    if (bool === 'ja') {
        alert('Oke, je mag door')
        window.location.href = "quizMain.html";
    } else if (bool === 'nee') {
        alert('Oke, doei dan.')
        window.location.href = "homePage.html";
    } else {

        let eindelijk = 0;
        let dom = ['kaas', 'pep', 'pepje', 'oma', 'oma p', 'poep', 'peop', 'plop', 'oma plop', 'pieter', 'post', 'pieter post', 'dom', 'geen zin', '', ' ', '   ', '    ', '     ']

        let check = document.getElementById("input").value.toLowerCase();

        if (dom.includes(check)) {
            if (bool === true) {
            } else {
                alert("Wauw, je bent dom! :D\nIk had m kunnen verwachten...")
                eindelijk++;
            }

        } else if (check === 'ja' || check === 'jazeker' || check === 'j') {
            if (eindelijk <= 2) {
                if (bool === true) {
                    window.location.href = "quizMain.html";
                } else {
                    alert('Oke, je mag door')
                    window.location.href = "quizMain.html";
                }

            } else {
                alert('Man man man was het zo moeilijk om een serieus antwoord te geven?')

            }

        } else if (check === 'nee' || check === 'n') {
            if (bool === true) {
                window.location.href = "homePage.html";
            } else {
                alert('Oke, doei dan.')
                window.location.href = "homePage.html";
            }


        } else {
            if (bool === true) {
            } else {
                alert("Ik heb geen idee wat voor bullshit je hebt ingevuld, maar het is niet goed.")
                eindelijk++;
            }
        }
    }
}