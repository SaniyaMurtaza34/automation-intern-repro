# Clean Code Principles

## 1. Research and Summary

Clean code means writing code that is easy to read, understand, test and maintain. It helps developers work together and makes future changes easier.
Five important clean code principles

### 1. Simplicity

Keep the code as simple as possible. Avoid unnecessary logic, complicated conditions and duplicate code. Simple code is easier to understand and reduces the chances of introducing bugs.

### 2. Readability

Write code that other developers can easily understand. Use meaningful variable and function names, proper indentation and clear formatting.

### 3. Maintainability

Write code in a way that makes future updates and bug fixes easier. Break large functions into smaller, reusable functions and avoid repeating the same logic.

### 4. Consistency

Follow the same coding style throughout the project. Use consistent naming conventions, indentation, formatting and project guidelines so the code looks organised.

### 5. Efficiency

Write code that performs well without making it unnecessarily complicated. Avoid redundant operations and choose suitable solutions, but don't optimise code before there is a real need.

## 2. Example of Messy Code

Here is an example of poorly structured JavaScript code:
function calc(a, b, c) {
let x = a * b;
let y = x - c;
if (y > 0) {
console.log("Profit: " + y);
} else {
console.log("No profit");
}
}
calc(100, 5, 200);

Why is this code difficult to read?

- The function name calc does not explain what the function does.
- Variable names like a, b, c, x and y are unclear.
- There are no comments or explanations.
- The purpose of the calculation is not obvious.
- It would be harder to maintain if the calculation became more complicated.

### 3. Rewrite the Code Using Clean Code Principles

The same code can be improved by using meaningful names and making its purpose clearer.

Cleaned-up JavaScript code:
function calculateProfit(sellingPrice, quantity, totalCost) {
const totalRevenue = sellingPrice * quantity;
const profit = totalRevenue - totalCost;

    if (profit > 0) {
        console.log(`Profit: ${profit}`);
    } else {
        console.log("No profit");
    }

}

calculateProfit(100, 5, 200);

What has improved?
Clean Code Principle Improvement
Simplicity Removed unnecessary complexity.
Readability Used meaningful variable and function names.
Maintainability Made the calculation easier to update.
Consistency Used consistent camelCase naming and indentation.
Efficiency Used straightforward calculations without unnecessary operations.

The updated code produces the same result as the original code but is easier to understand and maintain.

### 4. Conclusion

Working on this task helped me understand that writing code is not just about making it work. It is also important to make sure other developers can understand and maintain it.

I learned that small improvements, such as meaningful variable names, proper formatting and breaking down complicated logic, can make a big difference in code quality.

# Clean Code – Reflection

### 1. Why is code formatting important?

Consistent code formatting makes code easier to read, understand and maintain. It also helps developers follow the same coding standards when working on a project. Good formatting makes it easier to identify errors, review changes and collaborate with other team members.

### 2. What issues did the linter detect?

While reviewing the codebase, I used ESLint to identify potential coding issues and inconsistencies. These included formatting problems, unused variables, inconsistent code style and other rule violations. I worked on fixing the reported issues to make the code cleaner and more consistent.

### 3. Did formatting the code make it easier to read?

Yes, formatting the code made it easier to read and understand. Prettier helped maintain consistent indentation, spacing and code structure, while ESLint helped identify potential issues. Overall, this task helped me understand the importance of maintaining clean, readable and maintainable code.

### 4. What did I learn?

I learned how ESLint and Prettier work together to improve code quality. I also reviewed the Airbnb JavaScript Style Guide and understood how following consistent coding standards can make collaboration and code maintenance easier.
