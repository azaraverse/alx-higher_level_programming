#!/usr/bin/node

function add(a, b) {
    const result = parseInt(a) + parseInt(b);
    console.log(result);
}

const num1 = process.argv[2];
const num2 = process.argv[3];

add(num1, num2);
