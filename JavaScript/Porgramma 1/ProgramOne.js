function easy() {
    document.getElementById('diff').style.scale = 0;

    for (let i = 1; i < 12; i++) {
        let container = document.createElement('div');

        let button = document.createElement('button');
        button.id = 'button' + i;
        button.innerHTML = '?';
        button.onclick = function () {
            button.innerHTML = i;
        }

        document.body.appendChild(container);
        container.appendChild(button);

    }
}