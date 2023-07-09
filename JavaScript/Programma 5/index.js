//Colors:
let blauw = document.getElementById("blauw");

//Events:
blauw.addEventListener("click", function () {
    chooseColor("blue");
})

function chooseColor(color) {
    document.body.style.background = color;
}
