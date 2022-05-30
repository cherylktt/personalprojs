// Make a Calculator! using prompt(), and variables, make a program that does the following:
// 1. Prompts the user for first number.
// 2. Stores that first number
// 3. Prompts the user for the second number.
// 4. stores that number and responds with the SUM by using an alert.  
// BONUS: Make a program that can subtract, multiply, and also divide!

var firstNumber = prompt("What is the first number?");
var secondNumber = prompt("What is the second number?");
var operation = prompt("What is the opreation? (+, -, *, /)");
if (operation === "+"){
	var sum = Number(firstNumber) + Number(secondNumber);
	alert("The sum of is: " + sum);
} else if (operation === "-"){
	var difference = Number(firstNumber) - Number(secondNumber);
	alert("The difference is: " + difference);
} else if (operation === "*"){
	var product = Number(firstNumber) * Number(secondNumber);
	alert("The product is: " + product);
} else if (operation === "/"){
	var quotient = Number(firstNumber) / Number(secondNumber);
	alert("The quotient is: " + quotient);
} else {
	alert("Not a valid operation.")
}