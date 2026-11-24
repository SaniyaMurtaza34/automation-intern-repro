// Before applying DRY: Repeated code

// Display welcome message for Saniya
console.log("Welcome, Saniya!");

// Display welcome message for Ali
console.log("Welcome, Ali!");

// Display welcome message for Ahmed
console.log("Welcome, Maaz!");

console.log("After applying DRY: Using a resusable function")
// After applying DRY: Using a reusable function

// Create a reusable function to welcome different users
function welcomeUser(name) {

    // Display a welcome message using the provided name
    console.log("Welcome, " + name + "!");
}

// Call the same function for different users
welcomeUser("Saniya");
welcomeUser("Ali");
welcomeUser("Maaz");