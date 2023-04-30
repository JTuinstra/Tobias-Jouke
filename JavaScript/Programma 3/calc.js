let sum = '';
let sumInput = document.getElementById('sum');


function calculate() {
    let result = eval(sum);
    result = Math.round(result * 100) / 100;
    sumInput.value = result;
    sum = result;

}

function add(id) {
    let possible = [1, 2, 3, 4, 5, 6, 7, 8, 9, '+', '-', '*', '/']

    if (!possible.includes(sum)) {
        alert('Please use numbers and operators only.');
        return;
    }

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
