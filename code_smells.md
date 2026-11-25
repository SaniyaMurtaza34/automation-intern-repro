# Code Smells: Research, Examples and Refactoring

## 1. Introduction

Code smells are signs in source code that indicate potential problems with code quality. They do not necessarily mean that the code is broken, but they suggest that the code could be improved.

When code smells are not addressed, the codebase can become difficult to understand, test, debug, and maintain. Refactoring helps improve the internal structure of the code without changing its existing functionality.

In this task, I explored seven common code smells, understood their impact on code quality, and learned how to refactor them to make the code cleaner, more readable, and easier to maintain.

---

## 2. Common Code Smells and Their Examples

### 2.1 Magic Numbers and Strings

**What is it?**

Magic numbers and strings are hardcoded values used directly in the code without explaining what they represent.

This makes the code difficult to understand because other developers may not know why a particular number or string is being used.

**Example – Before Refactoring:**

```javascript
function calculateDiscount(price) {
    return price * 0.15;
}

if (userRole === "admin") {
    console.log("Access granted");
}
```

**Problem:**
- The number `0.15` does not clearly explain the discount percentage.
- The string `"admin"` is hardcoded.
- If these values change, we need to update them wherever they appear.

**After Refactoring:**

```javascript
const DISCOUNT_RATE = 0.15;
const ADMIN_ROLE = "admin";

function calculateDiscount(price) {
    return price * DISCOUNT_RATE;
}

if (userRole === ADMIN_ROLE) {
    console.log("Access granted");
}
```

**Improvement:**

Using meaningful constants makes the code easier to understand and update. It also reduces the risk of inconsistent values across the application.

### 2.2 Long Functions

**What is it?**

A long function performs too many operations or handles multiple responsibilities in one place.

This makes it harder to understand, test, and identify problems when something goes wrong.

**Example – Before Refactoring:**

```javascript
function registerUser(user) {
    if (!user.name || !user.email || !user.password) {
        console.log("Missing user information");
        return;
    }

    if (!user.email.includes("@")) {
        console.log("Invalid email");
        return;
    }

    const hashedPassword = "hashed_" + user.password;

    const newUser = {
        name: user.name,
        email: user.email,
        password: hashedPassword
    };

    console.log("Saving user:", newUser);
    console.log("Sending welcome email");
    console.log("Registration completed");
}
```

**Problem:**
- The function handles validation, password processing, user creation, and notifications.
- It is difficult to test each operation independently.
- Making changes to one operation can affect the entire function.

**After Refactoring:**

```javascript
function validateUser(user) {
    return user.name &&
        user.email &&
        user.password &&
        user.email.includes("@");
}

function hashPassword(password) {
    return "hashed_" + password;
}

function createUser(user) {
    return {
        name: user.name,
        email: user.email,
        password: hashPassword(user.password)
    };
}

function registerUser(user) {
    if (!validateUser(user)) {
        console.log("Invalid user information");
        return;
    }

    const newUser = createUser(user);

    console.log("Saving user:", newUser);
    console.log("Sending welcome email");
    console.log("Registration completed");
}
```

**Improvement:**

Breaking a long function into smaller functions gives each function a clear responsibility. It also makes individual operations easier to test, reuse, and maintain.

### 2.3 Duplicate Code

**What is it?**

Duplicate code happens when the same logic or functionality is repeated in multiple places instead of being reused.

This increases maintenance effort because the same changes may need to be made in several locations.

**Example – Before Refactoring:**

```javascript
function calculateEmployeeBonus(salary) {
    return salary * 0.10;
}

function calculateManagerBonus(salary) {
    return salary * 0.10;
}
```

**Problem:**
- Both functions contain exactly the same calculation.
- If the bonus percentage changes, both functions need updating.
- Repeated logic makes the code unnecessarily lengthy.

**After Refactoring:**

```javascript
const BONUS_RATE = 0.10;

function calculateBonus(salary) {
    return salary * BONUS_RATE;
}

function calculateEmployeeBonus(salary) {
    return calculateBonus(salary);
}

function calculateManagerBonus(salary) {
    return calculateBonus(salary);
}
```

**Improvement:**

Creating a reusable function eliminates repeated logic. If the calculation changes in the future, we only need to update it in one place.

### 2.4 Large Classes (God Objects)

**What is it?**

A large class, sometimes called a God Object, is a class that handles too many responsibilities.

Instead of focusing on one specific task, it manages several unrelated operations.

**Example – Before Refactoring:**

```javascript
class UserManager {
    createUser(user) {
        console.log("Creating user");
    }

    validateUser(user) {
        console.log("Validating user");
    }

    sendEmail(user) {
        console.log("Sending email");
    }

    generateReport() {
        console.log("Generating report");
    }

    saveToDatabase(user) {
        console.log("Saving user to database");
    }
}
```

**Problem:**
- The class handles user creation, validation, email notifications, reporting, and database operations.
- It becomes difficult to maintain as more features are added.
- Changes to one responsibility may affect unrelated functionality.

**After Refactoring:**

```javascript
class UserValidator {
    validateUser(user) {
        return user.name && user.email;
    }
}

class UserRepository {
    saveUser(user) {
        console.log("Saving user to database");
    }
}

class EmailService {
    sendEmail(user) {
        console.log("Sending email");
    }
}

class ReportService {
    generateReport() {
        console.log("Generating report");
    }
}

class UserManager {
    constructor() {
        this.validator = new UserValidator();
        this.repository = new UserRepository();
        this.emailService = new EmailService();
    }

    createUser(user) {
        if (!this.validator.validateUser(user)) {
            return;
        }

        this.repository.saveUser(user);
        this.emailService.sendEmail(user);
    }
}
```

**Improvement:**

Separating responsibilities into smaller classes makes the application easier to understand, test, and extend. Each class now has a more clearly defined purpose.

### 2.5 Deeply Nested Conditionals

**What is it?**

Deeply nested conditionals occur when multiple `if`, `else if`, and `else` statements are placed inside one another.

This makes the logic difficult to follow and increases the chances of introducing errors.

**Example – Before Refactoring:**

```javascript
function checkAccess(user) {
    if (user) {
        if (user.isActive) {
            if (user.role === "admin") {
                console.log("Access granted");
            } else {
                console.log("Admin access required");
            }
        } else {
            console.log("Account is inactive");
        }
    } else {
        console.log("User not found");
    }
}
```

**Problem:**
- Multiple nested conditions make the code difficult to read.
- It takes more time to understand the different execution paths.
- Adding more conditions can make the function even more complicated.

**After Refactoring:**

```javascript
function checkAccess(user) {
    if (!user) {
        console.log("User not found");
        return;
    }

    if (!user.isActive) {
        console.log("Account is inactive");
        return;
    }

    if (user.role !== "admin") {
        console.log("Admin access required");
        return;
    }

    console.log("Access granted");
}
```

**Improvement:**

Using early returns reduces unnecessary nesting and makes the conditions easier to understand. Each validation is handled separately, making the function easier to debug and maintain.

### 2.6 Commented-Out Code

**What is it?**

Commented-out code refers to old or unused code that has been left in the source files instead of being removed.

Developers sometimes keep old code in comments because they think they might need it later.

**Example – Before Refactoring:**

```javascript
function calculateTotal(price, quantity) {

    // const total = price + quantity;

    // function calculateOldDiscount() {
    //     return price * 0.05;
    // }

    const total = price * quantity;

    return total;
}
```

**Problem:**
- Unused code creates unnecessary clutter.
- It makes it difficult to identify which implementation is currently being used.
- Developers may waste time trying to understand outdated logic.

**After Refactoring:**

```javascript
function calculateTotal(price, quantity) {
    const total = price * quantity;

    return total;
}
```

**Improvement:**

Removing unused code keeps the source files clean and makes the actual implementation easier to understand. If old implementations are needed, version control tools such as Git can be used to retrieve them.

### 2.7 Inconsistent Naming

**What is it?**

Inconsistent naming happens when variables, functions, or classes have unclear names or follow different naming conventions.

Good naming is important because it helps developers understand the purpose of the code without needing additional explanations.

**Example – Before Refactoring:**

```javascript
function getData(x, y) {
    let a = x * y;
    let temp = a + 10;

    return temp;
}
```

**Problem:**
- Names such as `x`, `y`, `a`, and `temp` do not explain their purpose.
- Other developers may find it difficult to understand the calculation.
- Unclear naming makes debugging and maintenance harder.

**After Refactoring:**

```javascript
function calculateOrderTotal(unitPrice, quantity) {
    const subtotal = unitPrice * quantity;
    const serviceFee = subtotal + 10;

    return serviceFee;
}
```

**Improvement:**

Using descriptive variable and function names makes the code self-explanatory. Consistent naming conventions also make it easier for developers to work together.

---

## 3. How Code Smells Impact Code Quality

Code smells can negatively affect software quality in several ways:

1. **Readability:** Unclear names, long functions, and deeply nested conditions make the code difficult to understand.

2. **Maintainability:** Duplicate code and large classes make changes more complicated because multiple parts of the application may need updating.

3. **Testability:** Functions and classes with too many responsibilities are harder to test independently.

4. **Debugging:** Complex logic and repeated code make it more difficult to identify the root cause of a defect.

5. **Scalability:** Poorly structured code becomes harder to extend when new features are introduced.

6. **Team Collaboration:** Clean and consistent code helps developers understand each other's work and reduces confusion during code reviews.

---

## 4. Reflection

### What code smells did I find in my code?

During this exercise, I explored seven common code smells: magic numbers and strings, long functions, duplicate code, large classes, deeply nested conditionals, commented-out code, and inconsistent naming.

I learned that even when code works correctly, its structure may not be ideal. For example, using hardcoded values, repeating the same logic, or putting too many responsibilities into one function can make future changes more difficult.

This exercise helped me understand how to recognise these issues and how to improve code quality through refactoring.

### How did refactoring improve the readability and maintainability of the code?

Refactoring helped me organise the code into smaller and more meaningful sections.

By replacing hardcoded values with constants, using descriptive names, removing duplicate logic, and separating responsibilities, the code became easier to understand.

I also learned that using early returns instead of deeply nested conditions makes the logic simpler to follow.

Overall, refactoring improved the structure of the code without changing its intended functionality.

### How can avoiding code smells make future debugging easier?

Avoiding code smells can make debugging much easier because clean code helps developers understand how different parts of an application work.

When functions have clear responsibilities and variables have meaningful names, it becomes easier to identify where an issue might be occurring.

Removing duplicate code also reduces the chances of fixing one part of the application while accidentally leaving the same problem in another location.

As a QA professional, I believe clean code is important because it makes software easier to test, maintain, and improve. It also helps developers identify defects earlier and reduces the time required to investigate and resolve issues.

---

## 5. Conclusion

This exercise helped me understand that writing code is not only about making an application work. It is also about making sure the code is understandable, reusable, and maintainable.

I learned how to identify common code smells, understand their impact, and apply basic refactoring techniques to improve code quality.

Going forward, I will pay more attention to clean coding practices, meaningful naming, reusable functions, and separation of responsibilities when writing or reviewing code.

**My key takeaway:** Good code should not only work today; it should also be easy for another developer to understand, test, and maintain in the future.