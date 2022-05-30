// Make a keyless car! This car will only let you drive if you are over 18. Make it do the following:

// If the user's age is below 18, respond with: "Sorry, you are too young to drive this car. Powering off."
// If the user's age is above 18, respond with: "Powering on. Enjoy the ride!"
// If the user's age is exactly 18, respond with: "Congratulations on your first year of driving. Enjoy the ride!"

// Make the code have a function called checkDriverAge(). Whenever you call this function, you will get prompted 
// for age. Use Function Declaration to create this function.

function checkDriverAge() {
	var age = prompt("What is your age?");

	if (Number(age) < 18) {
		alert("Sorry, you are too young to drive this car. Powering off.");
	} else if (Number(age) > 18) {
		alert("Powering On. Enjoy the ride!");
	} else if (Number(age) === 18) {
		alert("Congratulations on your first year of driving. Enjoy the ride!");
	}
}

// Create another function that does the same thing, called checkDriverAge2() using Function Expression.

const checkDriverAge2 = function(){
	var age = prompt("What is your age?");

	if (Number(age) < 18) {
		alert("Sorry, you are too young to drive this car. Powering off.");
	} else if (Number(age) > 18) {
		alert("Powering On. Enjoy the ride!");
	} else if (Number(age) === 18) {
		alert("Congratulations on your first year of driving. Enjoy the ride!");
	}	
}