// Variables with initial values
let name = 'javohir';
let age = 20;
let lastname = 'rashidov';

console.log(age, lastname, name);

function findName() {
    var name = 'javohir'; 
    return name.toUpperCase() ;
}

console.log('myname is', findName());


// Job hiring criteria based on skills
let html = false;
let css = false;
let js = false;
let message = ''; // Corrected spelling from `massage` to `message`

if (html && css && js) {
    message = "You can come to our interview";
} else if (html || css || js) {
    message = 'Sorry we cannot hire you for now. You do not have enough skills. Please learn them and try again.';
} else {
    message = 'Please don\'t waste your time by searching for a job.';
}
console.log(message);


// Function to check CV based on skills
function checkCV(html, css, js) { 
    let message = ''; 
    if (html && css && js) {
        message = "You can come to our interview";
    } else if (html || css || js) {
        message = 'Sorry we cannot hire you for now. You do not have enough skills. Please learn them and try again.';
    } else {
        message = 'Please don\'t waste your time by searching for a job.';
    }
    return message;
}

console.log(checkCV(true, false, true));


// Function expressions and arrow functions

const myaFunction = function(a, b) {
    return a * b;
}

console.log(myaFunction(3, 5)); 

const mybFunction = (a, b) => {
    return a * b;
}

console.log(mybFunction(2, 4)); 

const mycFunction = (a, b) => a * b;

console.log(mycFunction(3, 6)); 


// Function to check if a number is even or odd
function mydfunction(number) {
    if (number % 2 === 0) {
        console.log(`${number} is even`);
    } else {
        console.log(`${number} is odd`);
    }
}

mydfunction(4); 


// Function expressions to check if a number is even or odd

const myfFunction = function(number) {
    if (number % 2 === 0) {
        console.log(`${number} is even`);
    } else {
        console.log(`${number} is odd`);
    }
}

myfFunction(5); 

const mygFunction = number => {
    if (number % 2 === 0) {
        console.log(`${number} is even`);
    } else {
        console.log(`${number} is odd`);
    }
}

mygFunction(6); 


// Function to reverse the digits of a number
const reverse = number => {
    const numberStr = String(number); 
    const reversed = numberStr.split('').reverse().join(''); 
    return reversed; 
}

console.log(reverse(51)); 
