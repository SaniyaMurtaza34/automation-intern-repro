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


# Clean Code: Meaningful Variable and Function Names

I researched clean code naming practices and learned that variable and function names should be clear, meaningful, and easy to understand. A good name should explain the purpose of the variable or function without requiring someone to read the entire code to understand it.

I reviewed the existing code and identified some unclear variable and function names. I refactored the code by replacing short or confusing names with meaningful ones that better describe their purpose.

## 1. What makes a good variable or function name?

A good name should:
- Clearly describe its purpose.
- Be simple, meaningful, and easy to understand.
- Use consistent naming conventions.
- Use verbs for function names to describe actions.
- Avoid unnecessary abbreviations and single-letter names.

## 2. What issues can arise from poorly named variables?

Poorly named variables and functions can make code difficult to understand and maintain. They can also cause confusion when debugging, increase the time needed to identify issues, and make collaboration more challenging for other developers.

## 3. How did refactoring improve code readability?

Refactoring helped make the code cleaner, more organised, and easier to understand. By replacing unclear names with meaningful ones, it became easier to identify what each variable and function does. It also improved maintainability and made future updates easier.

## My Reflection

This task helped me understand that writing clean code is not just about making the code work; it is also about making it understandable for other developers. As a QA professional, I believe readable code makes debugging, reviewing changes, and identifying potential issues easier. I will apply these naming practices in my future testing and automation projects.


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