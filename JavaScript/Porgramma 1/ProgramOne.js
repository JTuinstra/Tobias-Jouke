function easy() {
    document.getElementById('diff').style.scale = 0;

    for (let i = 1; i < 12; i++) {
        let count = 0
        let container = document.createElement('div');
        let button = document.createElement('button');

        button.id = 'button' + i;
        button.innerHTML = '?';
        button.onclick = function () {
            button.innerHTML = i;
            alert(random_number)
        }

        if (count % 2 == 0) {
            button.innerHTML = Math.floor(Math.random * 100)
        }

        document.body.appendChild(container);
        container.appendChild(button);

    }
}