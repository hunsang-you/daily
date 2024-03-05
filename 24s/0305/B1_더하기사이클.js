/**
 26

 55

 1

 0

 71
 */
// 수학, 구현

let input = Number(require('fs').readFileSync('/dev/stdin').toString());
let number = input;

let sum_number;
let i = 0;
while (True) {
    i++;

    sum_number = Math.floor(num / 10) + num % 10;
    number = (num % 10) * 10 + sum_number % 10;

    if (input == number) {
        break;
    }
}