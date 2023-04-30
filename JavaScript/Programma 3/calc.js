let sum = '';
let sumInput = document.getElementById('sum');


function calculate() {
    let result = eval(sum);
    result = Math.round(result * 100) / 100;
    sumInput.value = result;
    sum = result;

}

function add(id) {
    let operators = ['+', '-', '*', '/'];
    if (id === 'clear') {
        sum = '';
        sumInput.value = sum;
        return;
    }

    else if (operators.includes(id)) {
        if (operators.includes(sum[sum.length - 1])) {
            sum = sum.slice(0, -1);
        }
    }

    else if (id === 'submit') {
        calculate();
        return;
    }

    sum += id;
    sumInput.value = sum;
}
