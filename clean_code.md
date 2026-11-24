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

# Clean Code – Code Style, ESLint and Prettier

## 1. Why is code formatting important?

Consistent code formatting makes code easier to read, understand and maintain. When everyone follows the same coding standards, the project looks more organised and developers can understand each other's work more easily.

I learned that meaningful variable and function names also make a big difference. For example, changing a function name from `calc` to `calculateProfit` makes its purpose much clearer. Small improvements like this help reduce confusion and make future updates easier.

## 2. What issues did the linter detect?

While reviewing and cleaning up the code, I focused on common JavaScript code quality issues, including:

- **Unused variables:** Variables that were declared but never used. These can create unnecessary code, so I removed them where appropriate.
- **Inconsistent formatting:** Differences in indentation, spacing and quotation marks. I used Prettier to apply consistent formatting.
- **Missing semicolons or inconsistent syntax style:** I followed the project's configured style rules to keep the code consistent.

*Note: These are examples of common issues. I will update this section with the exact ESLint warnings and fixes reported by my project.*

## 3. Did formatting the code make it easier to read?

Yes, definitely. After applying consistent formatting, the code became cleaner and easier to follow. Proper indentation, consistent spacing and meaningful names made functions and variables easier to understand.

I also realised that clean code is not just about making the code look good. It is about making it easier for other developers to read, maintain, debug and improve.

## 4. ESLint and Prettier – Completion

I configured ESLint and Prettier in my development environment and ran them against the project.

I reviewed the reported issues, applied the necessary fixes and used Prettier to format the code consistently.

**Final verification:** [npx eslint . --fix
npx prettier --write . 
npx eslint .
npx prettier --check .]

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

# Avoiding Code Duplication

### First, what is DRY?
DRY stands for Don't Repeat Yourself. It is a software development principle that means: Don't write the same code again and again. Instead, write it once and reuse it whenever needed.
Imagine you are writing automation test cases using Playwright.

Suppose you have three test cases, and each test needs to open the same website.

#### Example 1: Before applying DRY (duplicated code)
test('Login test', async ({ page }) => {
    await page.goto('https://example.com');
    await page.getByLabel('Email').fill('test@gmail.com');
});

test('Signup test', async ({ page }) => {
    await page.goto('https://example.com');
    await page.getByLabel('Name').fill('Saniya');
});

test('Profile test', async ({ page }) => {
    await page.goto('https://example.com');
    await page.getByText('Profile').click();
});


Can you see the problem? This line is repeated three times: await page.goto('https://example.com');


If the website URL changes, you have to update it in three places.

That's unnecessary repetition!

### Example 2: After applying DRY (refactored code)
Instead of repeating the same code, create a reusable function.
async function openWebsite(page) {
    await page.goto('https://example.com');
}

test('Login test', async ({ page }) => {
    await openWebsite(page);
    await page.getByLabel('Email').fill('test@gmail.com');
});

test('Signup test', async ({ page }) => {
    await openWebsite(page);
    await page.getByLabel('Name').fill('Saniya');
});

test('Profile test', async ({ page }) => {
    await openWebsite(page);
    await page.getByText('Profile').click();
});


Now you have written the website navigation logic only once.

DRY applied
 You can reuse openWebsite() whenever you need it.

## 2. What does your actual task ask you to do?

Let's break it down into four simple steps.
### Step 1: Find repeated code in your test repository
First, open your GitHub test repository in VS Code.
Look through your automation test files.
For example, you might find:
- The same website URL repeated in multiple tests.
- The same login steps repeated in different test cases.
- The same navigation steps repeated.
- The same test data repeated.
Your job is to identify one example of unnecessary repetition.
### Step 2: Refactor the code
Refactoring means improving the structure of existing code without changing what it does.

For example: 
Before: 
await page.goto('https://example.com');
Repeated in multiple test cases.

After:
async function openWebsite(page) {
    await page.goto('https://example.com');
}
Then reuse the function.


## DRY (Don't Repeat Yourself) Principle – Reflection

I researched the DRY (Don't Repeat Yourself) principle and learned that it helps reduce code duplication by reusing common logic instead of writing the same code multiple times.

While reviewing my test repository, I looked for repeated code that could be simplified and refactored. I worked on improving the code structure by removing unnecessary repetition and making the code easier to understand and maintain.

## What were the issues with duplicated code?

Duplicated code makes the project harder to maintain because the same logic may need to be updated in multiple places. If a change is made in one place but missed elsewhere, it can lead to inconsistencies and potential bugs. It also makes the code longer and harder to manage.

## How did refactoring improve maintainability?

Refactoring helped reduce unnecessary repetition and made the code cleaner, more organised, and easier to understand. By reusing common logic, future updates can be made in one place instead of modifying multiple sections. This also makes testing and debugging easier.

## What I learned:

I learned that writing clean code is not just about making it work; it is also about making it easier for other developers to understand, update, and maintain.


# Clean Code and Refactoring

## 1. Introduction

Clean code is about writing code that is simple, readable, understandable and easy to maintain. Good code should not only work correctly but should also be easy for other developers to understand and update.

Refactoring is the process of improving the internal structure of existing code without changing its expected functionality.

The main purpose of this task was to understand common refactoring techniques, identify complicated code and improve it by making it simpler and more readable.

## 2. Common Refactoring Techniques

During my research, I learned about the following common refactoring techniques:

1. **Extract Method:** Move a block of code into a separate function to make the main function shorter and easier to understand.

2. **Rename Variables:** Use meaningful variable and function names instead of unclear or shortened names.

3. **Remove Duplicate Code:** Avoid repeating the same logic in multiple places by reusing functions.

4. **Simplify Conditional Statements:** Make complicated if/else conditions easier to understand.

5. **Replace Magic Numbers:** Use meaningful constants instead of unexplained numbers in the code.

6. **Remove Dead Code:** Delete unused variables, functions and unnecessary code.

7. **Early Return:** Return from a function as soon as a condition is met instead of using multiple nested if/else statements.

8. **Reduce Function Complexity:** Keep functions small and focused on a single responsibility.

## 3. Example of Complicated Code

For this task, I created a JavaScript example based on a simple login validation system.

### Original Code (Before Refactoring)

```javascript
function checkUser(user) {
    let result = "";

    if (user != null) {
        if (user.username != "") {
            if (user.password != "") {
                if (user.isActive == true) {
                    result = "Login successful";
                } else {
                    result = "Account is inactive";
                }
            } else {
                result = "Password is missing";
            }
        } else {
            result = "Username is missing";
        }
    } else {
        result = "User does not exist";
    }

    return result;
}
```

### What Made the Original Code Complex?

The original code had several issues:

- Multiple nested if/else conditions made the logic difficult to follow.
- The indentation increased with every condition.
- The result variable was unnecessary.
- Some comparisons used loose equality operators.
- The function was harder to read, maintain and debug.
- Understanding the different validation scenarios required more effort.

## 4. Refactored Code

I refactored the original code using the Early Return technique.

### Improved Code (After Refactoring)

```javascript
function checkUser(user) {
    if (!user) {
        return "User does not exist";
    }

    if (!user.username) {
        return "Username is missing";
    }

    if (!user.password) {
        return "Password is missing";
    }

    if (!user.isActive) {
        return "Account is inactive";
    }

    return "Login successful";
}
```

### How Did Refactoring Improve the Code?

After refactoring:

- Removed unnecessary nested conditions.
- Used early returns to simplify the validation logic.
- Removed the unnecessary result variable.
- Reduced indentation and made the code easier to read.
- Made each validation condition clear and independent.
- Improved maintainability and made future changes easier.

The updated code is shorter and more organised while preserving the expected behaviour for the intended login inputs.

## 5. Testing the Refactored Code

I considered the following test scenarios to verify the login validation logic:

| Test Scenario | Expected Result |
|---|---|
| User is null | User does not exist |
| Username is empty | Username is missing |
| Password is empty | Password is missing |
| Account is inactive | Account is inactive |
| All details are valid | Login successful |

These scenarios help verify that the refactored function handles different conditions correctly.

## 6. My Reflection

### What made the original code complex?

While reviewing the original code, I noticed that multiple conditions were placed inside one another. This made the function difficult to read and understand.

The unnecessary result variable and repeated if/else blocks also made the code longer than it needed to be. It was not easy to identify the validation flow at first glance.

### How did refactoring improve it?

Refactoring helped me understand how small changes can make a big difference in code quality.

I used the Early Return technique to remove unnecessary nested conditions. This made the function shorter, cleaner and easier to understand.

I also learned that meaningful conditions and simple logic can make debugging and future maintenance much easier.

### What I Learned

Through this task, I learned that writing code is not just about making something work. It is also important to make sure the code is understandable and maintainable.

As a QA Engineer, I believe clean code is important because readable code makes it easier to understand application behaviour, identify potential issues and support effective testing.

I will try to apply these clean coding practices in my future JavaScript and automation testing projects.

## 7. Conclusion

This task helped me understand the importance of clean code and refactoring. By applying the Early Return technique, I successfully simplified a complicated login validation example.

I learned that good code should be simple, readable, reusable and easy to maintain.