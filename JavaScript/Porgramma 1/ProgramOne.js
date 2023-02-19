let items = [];
let index = 0;
let total = 0;

function addItem() {
    let wat = document.getElementById("item").value;
    let hoeveel = document.getElementById("aantal").value;
    if (wat === "" || hoeveel === "") {
        alert("Vul alle velden in!");
    }
    if (hoeveel < 0) {
        alert("Voer een positief getal in!");
    }

    total = hoeveel;
    if (items.includes(wat + " x" + hoeveel)) {
        let x = items.indexOf(wat + " x" + hoeveel);
        let y = items[x].split("x");
        let z = parseInt(y[1]) + parseInt(hoeveel);
        items[x] = wat + " x" + z;
        let create = document.createElement("h4")
        let item = document.createTextNode(items[x]);
        index++;

        create.appendChild(item);

        document.body.appendChild(create);

    } else {

        items.push(wat + " x" + hoeveel);

        let create = document.createElement("h4")
        let item = document.createTextNode(items[index]);
        index++;

        create.appendChild(item);

        document.body.appendChild(create);

    }
}
