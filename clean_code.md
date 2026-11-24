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

## 1. Why is code formatting important?

Consistent code formatting makes code easier to read, understand, and maintain. When everyone follows the same coding style, it becomes easier to work with other developers, review changes, and identify potential issues. It also makes the codebase look more organised and professional.

## 2. What issues did the linter detect?

While reviewing and cleaning up the code, I focused on issues such as:

- **Unused variables:** Removed variables that were declared but never used.
- **Inconsistent formatting:** Fixed spacing, indentation, and quote inconsistencies to follow the project's coding standards.
- **Missing semicolons:** Added semicolons where required by the configured ESLint rules.

I also improved variable and function names. For example, I changed `calc` to `calculateProfit` to make the purpose of the function clearer.

## 3. Did formatting the code make it easier to read?

Yes, definitely. After applying consistent formatting, the code became cleaner and easier to follow. Meaningful variable and function names also helped me understand what each part of the code was doing without spending extra time figuring it out.

## 4. ESLint and Prettier – Completion

I finished configuring and running ESLint and Prettier on the project.

- Ran Prettier to format the code consistently.
- Ran ESLint to identify coding issues and potential problems.
- Fixed the reported issues and reviewed the updated files.
- Re-ran the checks to verify the changes.

The project now passes the configured ESLint and Prettier checks.

## 5. Final Reflection

This task helped me understand why maintaining consistent code quality is important. I learned that clean code is not just about making it look good; it is also about making it easier for other developers to understand, maintain, and improve in the future.

# Clean Code: Writing Small, Single-Purpose Functions

## 1. Research: Best Practices

While researching clean code principles, I learned that functions should be small, simple, and focused on doing one specific task.

Some important best practices include:

- **Single Responsibility:** Each function should have one clear responsibility.
- **Meaningful Names:** Use descriptive names that explain what the function does.
- **Avoid Long Functions:** Break complex logic into smaller, manageable functions.
- **Avoid Code Duplication:** Reuse existing functions instead of repeating the same logic.
- **Keep Functions Simple:** Make functions easy to understand, test, and maintain.
- **Use Clear Parameters:** Pass only the information a function actually needs.

## 2. Example of a Complex Function

I created an example of a function that handles multiple responsibilities, including validating user information, calculating the total price, applying discounts, and displaying the final result.

This makes the function difficult to understand, test, and maintain.

## 3. Refactoring into Smaller Functions

I refactored the original function by separating its responsibilities into smaller functions:

- `validateUser()` – Checks whether the user information is valid.
- `calculateSubtotal()` – Calculates the total price.
- `applyDiscount()` – Applies the appropriate discount.
- `calculateFinalTotal()` – Calculates the final amount.
- `displayOrderSummary()` – Displays the order information.

Each function now has a clear purpose, making the code easier to follow and maintain.

## 4. Reflection

### Why is breaking down functions beneficial?

Breaking down large functions makes the code easier to read, understand, and maintain. When a function handles too many responsibilities, it becomes difficult to identify problems and make changes without affecting other parts of the code.

By creating smaller functions, each task becomes easier to test and debug. It also makes the code more reusable because individual functions can be used in different parts of the application.

### How did refactoring improve the structure of the code?

Refactoring helped me organise the code into smaller functions, each responsible for a specific task. Instead of keeping all the logic in one large function, I separated the responsibilities into meaningful sections.

This improved readability, reduced complexity, and made the code easier to maintain and test. I also learned that writing clean code is not just about making the code work; it is about making it easier for other developers to understand and work with.

## 5. Conclusion

This task helped me understand the importance of writing small, single-purpose functions. I learned that good code structure makes a big difference in software development, especially when working on larger projects or collaborating with other developers.

Going forward, I will try to keep my functions simple, use meaningful names, and avoid putting too much logic into a single function.