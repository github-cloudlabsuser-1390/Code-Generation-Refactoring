import Calculator from './calculator.js';

const calculator = new Calculator();

document.addEventListener('DOMContentLoaded', () => {
    const resultDisplay = document.getElementById('result');
    const form = document.getElementById('calculator-form');

    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const a = parseFloat(document.getElementById('input-a').value);
        const b = parseFloat(document.getElementById('input-b').value);
        const operation = document.querySelector('input[name="operation"]:checked').value;

        let result;

        try {
            switch (operation) {
                case 'add':
                    result = calculator.add(a, b);
                    break;
                case 'subtract':
                    result = calculator.subtract(a, b);
                    break;
                case 'multiply':
                    result = calculator.multiply(a, b);
                    break;
                case 'divide':
                    result = calculator.divide(a, b);
                    break;
                default:
                    throw new Error('Invalid operation');
            }
            resultDisplay.textContent = `Result: ${result}`;
        } catch (error) {
            resultDisplay.textContent = `Error: ${error.message}`;
        }
    });
});