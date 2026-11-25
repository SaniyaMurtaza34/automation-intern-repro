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

# Clean Code: Small, Single-Purpose Functions

## 1. Introduction

Clean Code is about writing code that is easy to read, understand, test and maintain.

One important principle is to keep functions small and give each function a single responsibility. Instead of putting multiple operations into one large function, we can divide the code into smaller functions, where each function performs one specific task.

In this exercise, I explored how to refactor a complex order-processing function into smaller, reusable and easy-to-understand functions.

## 2. Best Practices for Writing Small Functions

The following are some important practices I learned:

- **Single Responsibility:** Each function should perform one specific task.
- **Meaningful Names:** Use descriptive names that explain what a function does.
- **Keep Functions Small:** Avoid putting too many operations inside one function.
- **Avoid Code Duplication:** Reuse existing functions instead of repeating the same logic.
- **Clear Parameters:** Pass only the information required by a function.
- **Easy Testing:** Smaller functions are easier to test independently.
- **Readability:** Write code that other developers can easily understand.

Following these practices makes code easier to maintain, debug and improve.

## 3. Example of a Long and Complex Function (Before Refactoring)

For this exercise, I created an example of an online shopping order process.

The original function handles several responsibilities:

- Validating customer information.
- Calculating the subtotal.
- Applying discount codes.
- Calculating the final order amount.
- Displaying the order summary.

### Before Refactoring

```javascript
function processOrder(user, products, discountCode) {
    // Validate user
    if (!user || !user.name || !user.email) {
        throw new Error("Invalid user information");
    }

    // Calculate subtotal
    let subtotal = 0;

    for (const product of products) {
        if (product.price <= 0 || product.quantity <= 0) {
            throw new Error("Invalid product information");
        }

        subtotal += product.price * product.quantity;
    }

    // Apply discount
    let discount = 0;

    if (discountCode === "SAVE10") {
        discount = subtotal * 0.10;
    } else if (discountCode === "SAVE20") {
        discount = subtotal * 0.20;
    }

    // Calculate final total
    const finalTotal = subtotal - discount;

    // Display order summary
    console.log("Order Summary");
    console.log("Customer: " + user.name);
    console.log("Subtotal: $" + subtotal);
    console.log("Discount: $" + discount);
    console.log("Final Total: $" + finalTotal);

    return finalTotal;
}
```

### Problems with the Original Function

The original `processOrder()` function performs multiple responsibilities in one place.

This creates some challenges:

- The function is harder to read because it contains several operations.
- Finding and fixing bugs can take more time.
- Testing individual operations is difficult.
- Updating one part of the logic can make the function more complicated.
- The code is less reusable because the logic is combined.

## 4. Refactoring into Small, Focused Functions (After Refactoring)

To improve the code structure, I divided the original function into five smaller functions.

Each function has one clear responsibility.

### Function 1: validateUser()

**Responsibility:** Checks whether the customer information is valid.

```javascript
function validateUser(user) {
    if (!user || !user.name || !user.email) {
        throw new Error("Invalid user information");
    }

    return true;
}
```

### Function 2: calculateSubtotal()

**Responsibility:** Calculates the total price of all products based on their prices and quantities.

```javascript
function calculateSubtotal(products) {
    let subtotal = 0;

    for (const product of products) {
        if (product.price <= 0 || product.quantity <= 0) {
            throw new Error("Invalid product information");
        }

        subtotal += product.price * product.quantity;
    }

    return subtotal;
}
```

### Function 3: applyDiscount()

**Responsibility:** Applies a discount based on the discount code.

```javascript
function applyDiscount(subtotal, discountCode) {
    if (discountCode === "SAVE10") {
        return subtotal * 0.10;
    }

    if (discountCode === "SAVE20") {
        return subtotal * 0.20;
    }

    return 0;
}
```

### Function 4: calculateFinalTotal()

**Responsibility:** Calculates the final order amount after subtracting the discount.

```javascript
function calculateFinalTotal(subtotal, discount) {
    return subtotal - discount;
}
```

### Function 5: displayOrderSummary()

**Responsibility:** Displays the customer information and order summary.

```javascript
function displayOrderSummary(user, subtotal, discount, finalTotal) {
    console.log("Order Summary");
    console.log("Customer: " + user.name);
    console.log("Subtotal: $" + subtotal);
    console.log("Discount: $" + discount);
    console.log("Final Total: $" + finalTotal);
}
```

### Main Function: processOrder()

After creating the smaller functions, the main function becomes much simpler.

It coordinates the individual functions instead of handling every operation itself.

```javascript
function processOrder(user, products, discountCode) {
    validateUser(user);

    const subtotal = calculateSubtotal(products);

    const discount = applyDiscount(subtotal, discountCode);

    const finalTotal = calculateFinalTotal(subtotal, discount);

    displayOrderSummary(user, subtotal, discount, finalTotal);

    return finalTotal;
}
```

## 5. Understanding the Difference: Before vs After

| Before Refactoring | After Refactoring |
|---|---|
| One large function handles everything. | Multiple smaller functions handle individual tasks. |
| Difficult to understand the complete logic. | Each function has a clear purpose. |
| Harder to identify specific issues. | Easier to identify and debug issues. |
| Testing the entire function can be complicated. | Individual functions can be tested separately. |
| Logic is difficult to reuse. | Functions can be reused where needed. |
| Changes can make the main function more complicated. | Changes can be isolated to the relevant function. |

## 6. Reflection: Why Is Breaking Down Functions Beneficial?

Breaking down a large function into smaller functions makes the code easier to understand, test and maintain.

When all operations are written inside one function, developers need to understand the entire block of code to identify how a particular operation works.

By separating the responsibilities, developers can focus on one operation at a time.

For example, if there is an issue with discount calculation, I can directly investigate the `applyDiscount()` function instead of searching through the entire order-processing function.

I also learned that smaller functions improve reusability. A function such as `calculateSubtotal()` can potentially be used in different parts of an application without duplicating the same logic.

Overall, breaking down functions reduces complexity and makes development and maintenance easier.

## 7. Reflection: How Did Refactoring Improve the Structure of the Code?

Refactoring improved the overall code structure by separating different responsibilities into individual functions.

Before refactoring, the `processOrder()` function handled validation, calculations and displaying the order summary in one place.

After refactoring:

- Each function has a clear and meaningful name.
- The code is more organised and readable.
- The main function only coordinates the order-processing steps.
- Individual functions are easier to test and debug.
- Changes can be made to one function without unnecessarily affecting other operations.

I realised that refactoring does not always mean changing what the code does. It can also mean improving how the code is organised while maintaining the same expected behaviour.

## 8. QA Perspective: What Did I Learn?

As a Software Quality Assurance Engineer, I found this exercise particularly useful because clean code also makes testing easier.

For example:

- I can test `validateUser()` with valid and invalid customer information.
- I can test `calculateSubtotal()` with different product prices and quantities.
- I can test `applyDiscount()` with valid and invalid discount codes.
- I can test `calculateFinalTotal()` with different subtotal and discount values.
- I can verify that `displayOrderSummary()` displays the correct order information.

This makes it easier to identify which part of the application is causing an issue.

It also helps create focused test cases and improves overall testability.

## 9. Conclusion

Through this exercise, I learned the importance of writing small, single-purpose functions.

The main improvement was separating a large function into smaller functions with clear responsibilities.

This made the code easier to read, understand, test, debug and maintain.

Going forward, I will apply this principle when writing and reviewing code to make sure each function has a clear purpose and does not handle unnecessary responsibilities.


# Clean Code: Comments and Documentation

## 1. Introduction

Writing clean code is not only about making sure the application works. It is also about making the code easy to read, understand, maintain and update.

Comments and documentation help developers understand the purpose of the code, especially when someone else needs to work on it in the future.

However, adding too many comments is not always a good practice. Comments should provide useful information rather than simply repeat what the code is already doing.

## 2. Best Practices for Writing Comments and Documentation

After researching software development guidelines, I identified the following best practices:

### 2.1 Write clear and meaningful comments

- Use simple and understandable language.
- Explain why something is happening rather than repeating what the code does.
- Keep comments short and relevant.
- Avoid unnecessary comments that make the code harder to read.
- Make sure comments accurately describe the current implementation.

### 2.2 Use meaningful names

- Give variables, functions and classes descriptive names.
- Avoid unclear names such as `x`, `temp` or `data1`.
- Write code that explains its purpose without requiring additional comments.

### 2.3 Keep documentation updated

- Update documentation whenever the related functionality changes.
- Remove outdated or incorrect comments.
- Include important information about functions, parameters, expected results and limitations.
- Make documentation easy for other developers to understand.

### 2.4 Explain complex logic

- Add comments when working with complex algorithms or business rules.
- Explain unusual technical decisions.
- Document workarounds and important limitations.
- Use TODO comments to identify unfinished work that needs attention.

### 2.5 Follow consistent formatting

- Use proper spelling, grammar and punctuation.
- Follow the project's existing commenting conventions.
- Keep documentation organised with meaningful headings.
- Avoid writing long paragraphs when a short explanation is enough.

**Key takeaway:** Good comments should make the code easier to understand, not create more confusion.

## 3. Example of Poorly Commented Code

Consider the following JavaScript example.

### Before: Poor comments

```javascript
function calculateTotal(price, quantity) {
    // Multiply price by quantity
    let total = price * quantity;

    // Check if total is greater than 100
    if (total > 100) {
        // Apply discount
        total = total - (total * 0.10);
    }

    // Return total
    return total;
}
```

### What is wrong with these comments?

1. Most comments simply repeat what the code already explains.
2. They do not provide any additional information.
3. The reason for applying a 10% discount is not explained.
4. The code could be easier to understand with more meaningful variable names.

### After: Improved comments and cleaner code

```javascript
function calculateOrderTotal(unitPrice, quantity) {
    const subtotal = unitPrice * quantity;

    // Orders above $100 qualify for a 10% discount.
    const discountRate = 0.10;

    if (subtotal > 100) {
        return subtotal * (1 - discountRate);
    }

    return subtotal;
}
```

### Why is the improved version better?

- The function name clearly explains its purpose.
- Variable names such as `unitPrice` and `subtotal` make the code easier to understand.
- Unnecessary comments have been removed.
- The remaining comment explains the business rule behind the discount.
- The code is cleaner and easier to maintain.

The main lesson is that comments should explain information that cannot be easily understood from the code itself.

## 4. When Should You Add Comments?

I believe comments are useful when the purpose or reasoning behind a particular piece of code is not immediately clear.

I would add comments in the following situations:

1. **Complex business logic:** When a function contains complicated conditions or business rules that need additional explanation.

2. **Technical decisions:** When a particular approach has been chosen for a specific reason that might not be obvious to another developer.

3. **Workarounds:** When a temporary solution or workaround is necessary because of a technical limitation.

4. **Important limitations:** When there are restrictions or special conditions that other developers should know before modifying the code.

5. **Public functions and APIs:** When documenting how a function works, what parameters it accepts, what it returns and how other developers should use it.

6. **TODO comments:** When there is unfinished work or an improvement that needs to be addressed later.

## 5. When Should You Avoid Comments and Improve the Code Instead?

Comments are not always the best solution. Sometimes, the code itself needs improvement.

I would avoid adding comments in these situations:

1. **When the code is already clear:** If the function or variable name explains its purpose, an additional comment is unnecessary.

2. **When comments repeat the code:** Avoid explaining obvious operations such as adding two numbers or returning a variable.

3. **When variable names are unclear:** Instead of explaining what a variable represents in a comment, give it a meaningful name.

4. **When functions are too complicated:** If a function performs too many operations, consider breaking it into smaller functions.

5. **When comments are outdated:** Remove or update comments that no longer match the actual implementation.

6. **When code can be simplified:** Improve the code structure and readability instead of adding multiple comments to explain complicated logic.

I learned that writing clean code is better than relying on comments to explain code that could have been written more clearly.

## 6. My Personal Reflections

While researching comments and documentation, I learned that writing code is not just about completing a task or making an application work. It is also about making sure other developers can understand and maintain that code.

As someone working in Software Quality Assurance, I understand the importance of clarity and consistency. When reviewing code, unclear logic and outdated comments can make it difficult to understand the expected behaviour and identify potential issues.

I also realised that adding more comments does not necessarily make code better. Sometimes, improving variable names, simplifying conditions and breaking complicated functions into smaller parts can make a much bigger difference.

Going forward, I will focus on writing meaningful comments that explain the reason behind complex logic rather than describing every line of code. I will also make sure documentation stays updated whenever functionality changes.

This will help me improve my coding practices, collaborate more effectively with developers and contribute to better software quality.

## Best Practices for Writing Comments and Documentation

Good comments and documentation help other developers understand code, maintain it, and make changes confidently. Comments should be clear, concise, accurate, and useful.

Best practices include:

- **Explain why, not just what:** Comments should explain the reason behind a decision rather than repeat what the code already does.
- **Use meaningful names:** Choose descriptive names for variables and functions so the code is easy to understand.
- **Keep comments simple and clear:** Use straightforward language and avoid unnecessary technical details.
- **Keep comments updated:** When the code changes, update or remove comments that are no longer accurate.
- **Document important behaviour:** Explain business rules, assumptions, limitations, and edge cases that may not be obvious.
- **Avoid unnecessary comments:** Too many comments can make code harder to read instead of improving clarity.

## Example of Poorly Commented Code

### Before: Unclear code and unnecessary comments

```javascript
// Calculate something
function calc(a, b, c) {
    // Multiply a and b
    let x = a * b;

    // Subtract c
    let y = x - c;

    // Return the result
    return y;
}
```

The function name `calc` and parameter names `a`, `b`, and `c` do not clearly explain the purpose of the function. The comments only repeat what the code is doing and do not provide any meaningful information.

### After: Improved code with meaningful names

```javascript
function calculateProfit(sellingPrice, quantity, totalCost) {
    const totalRevenue = sellingPrice * quantity;
    const profit = totalRevenue - totalCost;

    return profit;
}
```

The improved version uses descriptive function and variable names, making the purpose of the code easier to understand. The unnecessary comments have been removed because the code now explains itself.

## When Should You Add Comments?

I should add comments when the reason behind the code is not obvious from the implementation. Comments are useful for explaining why a particular approach was chosen, documenting important business rules, or describing unusual edge cases. For example, I might explain why a specific validation is required or why a function handles a particular situation differently.

## When Should You Avoid Comments and Improve the Code Instead?

I should avoid comments that simply repeat what the code is doing. Instead, I should use clear variable and function names, break large functions into smaller ones, and simplify complicated logic. If I need several comments to explain a simple function, I should consider improving the code so that it is easier to understand without extra explanation.

## Conclusion

Good comments and documentation are important parts of clean code. They help developers understand complex logic, technical decisions and the expected behaviour of an application. My main takeaway is: Write code that explains itself, and add comments only when additional context is needed.

## Reflection

This task helped me understand that comments are not a replacement for clean code. I learned that meaningful names and simple logic can make code easier to maintain, while useful comments should provide additional context that the code cannot explain on its own. In future projects, I will focus on writing readable code first and adding comments only when they provide value to other developers.


# Clean Code: Error Handling and Edge Cases

## 1. Research: Strategies for Handling Errors and Edge Cases

While working on this task, I learned that proper error handling is an important part of writing clean, reliable, and maintainable code. A function should not only work with valid inputs but should also handle unexpected situations safely.

Some strategies I learned include:

### Guard Clauses

Guard Clauses are used to check invalid inputs or unexpected conditions at the beginning of a function. If a condition is not valid, the function returns early or throws an appropriate error.

This helps avoid unnecessary nested `if` statements and makes the code easier to read.

For example:

```javascript
function calculateTotal(price, quantity) {
  if (price < 0) {
    throw new Error("Price cannot be negative");
  }

  if (quantity <= 0) {
    throw new Error("Quantity must be greater than zero");
  }

  return price * quantity;
}
```

### Input Validation

Before processing data, I should check whether the input is valid and in the expected format. For example, checking whether a value is missing, whether a number is negative, or whether a string is empty.

### Handling Errors Properly

Errors should be handled in a meaningful way instead of being ignored. Depending on the situation, I can use `try...catch`, return an appropriate error message, or throw an error that can be handled by the calling function.

### Handling Edge Cases

Edge cases are situations that may not happen frequently but can cause unexpected behaviour. Examples include:

- Empty or missing input
- Null or undefined values
- Negative numbers
- Unexpected data types
- Very large or very small values
- Empty arrays or strings

Considering these cases helps prevent unexpected crashes and incorrect results.

## 2. Find an Existing Function with Improper Error Handling

I reviewed the existing code and identified a function that did not properly validate its inputs or handle unexpected situations.

The original function could produce incorrect results or fail when it received invalid or unexpected data. It did not clearly explain what went wrong, which made the function difficult to debug and maintain.

I selected this function for refactoring to improve its input validation and error handling.

## 3. Refactor the Function

I refactored the function by adding appropriate validation and error handling.

The main improvements included:

- Adding Guard Clauses to handle invalid inputs early.
- Checking for missing or unexpected values.
- Preventing the function from continuing when the input is invalid.
- Providing clear and meaningful error messages.
- Simplifying the function's logic to make it easier to understand.
- Ensuring that valid inputs continue to produce the expected results.

After refactoring, the function became easier to read and more reliable when handling unexpected situations.

## 4. Reflection: What Was the Issue with the Original Code?

The main issue with the original code was that it did not properly handle invalid inputs and unexpected conditions. It assumed that the input would always be correct, which could lead to incorrect results or unexpected errors.

The function also lacked clear validation and meaningful error messages. This made it harder to identify the cause of a problem when something went wrong.

By refactoring the function, I learned that clean code should not only handle the expected scenario but should also consider what could go wrong.

## 5. Reflection: How Does Error Handling Improve Reliability?

Proper error handling improves reliability by allowing the application to respond safely when something unexpected happens.

It helps prevent invalid data from being processed, reduces unexpected failures, and makes debugging easier by providing clear information about the problem.

Using Guard Clauses also makes the code more readable because invalid conditions are handled at the beginning of the function instead of being mixed with the main logic.

This task helped me understand that writing reliable code means thinking about both successful scenarios and possible failures. As a QA professional, I also understand how important it is to test invalid inputs and edge cases to make sure the application behaves as expected.

## Conclusion

This task helped me improve my understanding of clean code practices, especially error handling, input validation, and Guard Clauses. I learned that handling errors properly makes code more readable, maintainable, and reliable. It also helps prevent unexpected behaviour and makes it easier for developers and QA engineers to identify and resolve issues.