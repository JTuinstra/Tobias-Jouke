function easy() {
    document.getElementById('diff').style.scale = 0;

    for (let i = 1; i < 12; i++) {
        let count = 0
        let container = document.createElement('div');
        let button = document.createElement('button');
        count += 1

        if (count % 2 == 0) {
            random_num = Math.floor(Math.random * 100)
            button.innerHTML = random_num
            alert(random_num)
        }

        button.id = 'button' + i;
        button.onclick = function () {
        }

        document.body.appendChild(container);
        container.appendChild(button);

    }
}
