# CI/CD Research, Implementation and Reflection

## 1. Introduction to CI/CD

CI/CD stands for **Continuous Integration and Continuous Delivery/Deployment**. It is a software development practice that helps developers automate the process of checking, testing, building, and delivering code changes.

CI/CD makes software development more efficient by identifying problems early and reducing the amount of manual work required before code can be merged or released.

### What is Continuous Integration (CI)?

Continuous Integration is the practice of regularly merging code changes into a shared repository. Whenever a developer pushes new code or creates a Pull Request (PR), automated checks can run to verify that the changes meet the project's requirements.

For example, CI can automatically:
- Check Markdown files for formatting issues.
- Identify spelling mistakes.
- Run automated tests.
- Check code quality.
- Identify errors before changes are merged.

The main purpose of CI is to detect issues early and make sure that new changes do not negatively affect the existing project.

### What is Continuous Delivery (CD)?

Continuous Delivery is the process of automatically preparing code changes so they are ready to be released. The application is built, tested, and prepared for deployment, but the final production release may still require manual approval.

### What is Continuous Deployment?

Continuous Deployment takes automation one step further. Whenever code successfully passes all required checks and tests, it can automatically be deployed to the production environment without requiring manual approval.

### Difference Between CI, Continuous Delivery and Continuous Deployment

| Practice | Purpose |
|---|---|
| Continuous Integration | Automatically checks and tests code changes. |
| Continuous Delivery | Automatically prepares code for release, with deployment approval when required. |
| Continuous Deployment | Automatically releases successful changes to production. |

## 2. Why Is CI/CD Used in Software Development?

CI/CD is used to improve software quality, save development time, and make the development process more reliable.

Some important benefits include:

1. **Early error detection:** Automated checks identify issues before code is merged into the main branch.

2. **Improved code quality:** Linting, spell checking, and automated tests help maintain consistent project standards.

3. **Reduced manual effort:** Developers do not need to manually check every file for common formatting and spelling issues.

4. **Faster development:** Automated workflows allow developers to receive feedback quickly.

5. **Better team collaboration:** Everyone follows the same quality standards when contributing to a shared repository.

6. **Reliable releases:** Automated testing helps reduce the possibility of introducing errors into the application.

From a QA perspective, CI/CD is useful because it supports continuous quality checks throughout the development lifecycle rather than waiting until the end of development.

## 3. Setting Up a CI Workflow for Markdown Linting and Spell Checking

For this task, I used GitHub Actions to create an automated CI workflow.

The objective is to make sure Markdown files follow consistent formatting rules and do not contain common spelling mistakes.

### Tools Used

- **GitHub Actions:** Automates the CI workflow when code is pushed or a Pull Request is created.
- **markdownlint-cli2:** Checks Markdown files for formatting and style issues.
- **cspell:** Identifies potential spelling mistakes in Markdown files.
- **Git:** Manages version control and code changes.
- **Husky:** Runs Git hooks to enforce checks before commits.

### Step 1: Prepare the Repository

First, clone your GitHub repository to your local machine.

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

Navigate to the project directory:

```bash
cd REPOSITORY
```

If your project does not already have a `package.json` file, initialize npm:

```bash
npm init -y
```

### Step 2: Install Markdown Linting and Spell-Checking Tools

Install the required development dependencies:

```bash
npm install --save-dev markdownlint-cli2 cspell
```

These tools will help identify Markdown formatting problems and spelling mistakes.

### Step 3: Configure Markdown Linting

Create a file named:

`.markdownlint-cli2.jsonc`

Add the following configuration:

```json
{
  "config": {
    "default": true,
    "MD013": false
  },
  "ignores": [
    "node_modules/**"
  ]
}
```

This configuration enables the default Markdown linting rules.

The `MD013` rule is disabled because long lines, such as URLs and paragraphs, can sometimes be intentional.

### Step 4: Configure Spell Checking

Create a file named:

`cspell.json`

Add the following configuration:

```json
{
  "version": "0.2",
  "language": "en",
  "files": [
    "**/*.md"
  ],
  "ignorePaths": [
    "node_modules/**"
  ],
  "allowCompoundWords": true
}
```

This configuration tells cspell to check Markdown files using English spelling rules.

If the project contains technical words, tool names, or project-specific terminology, they can be added to the configuration's `words` list to avoid unnecessary spelling warnings.

### Step 5: Add Scripts to package.json

Open `package.json` and add the following scripts inside the existing `scripts` section:

```json
{
  "scripts": {
    "lint:md": "markdownlint-cli2 \"**/*.md\"",
    "spellcheck": "cspell \"**/*.md\"",
    "prepare": "husky"
  }
}
```

If your project already has scripts, keep them and add these entries rather than replacing the entire section.

These commands allow the checks to run locally:

```bash
npm run lint:md
```

This checks Markdown formatting.

```bash
npm run spellcheck
```

This checks spelling mistakes in Markdown files.

### Step 6: Create the GitHub Actions CI Workflow

Inside your repository, create the following directory structure:

`.github/workflows/ci.yml`

Add this configuration:

```yaml
name: Markdown Quality Checks

on:
  pull_request:
  push:
    branches:
      - main

jobs:
  markdown-checks:
    name: Markdown Lint and Spell Check
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm

      - name: Install dependencies
        run: npm ci

      - name: Run Markdown linting
        run: npm run lint:md

      - name: Run spell checking
        run: npm run spellcheck
```

### How This Workflow Works

1. **Trigger:** The workflow starts whenever a Pull Request is opened or code is pushed to the main branch.

2. **Checkout repository:** GitHub Actions downloads the repository code so the workflow can access the files.

3. **Set up Node.js:** The workflow prepares the Node.js environment.

4. **Install dependencies:** The `npm ci` command installs the dependencies listed in the package-lock.json file.

5. **Markdown linting:** markdownlint checks Markdown files for formatting and style problems.

6. **Spell checking:** cspell scans Markdown files and identifies possible spelling mistakes.

7. **Results:** GitHub Actions displays whether each automated check passed or failed.

**Important:** Commit both `package.json` and `package-lock.json` so that `npm ci` can install the required dependencies.

## 4. Experimenting with Git Hooks Using Husky

Git Hooks are scripts that run automatically when specific Git events occur.

For example, a pre-commit hook runs before a developer creates a commit.

Husky is a tool that makes it easier to configure and manage Git Hooks in a project.

### Why Use Husky?

Husky helps prevent common issues from entering the repository by running checks before code is committed.

For this task, I used Husky to run Markdown linting and spell checking before every commit.

### Step 1: Install Husky

Run:

```bash
npm install --save-dev husky
```

### Step 2: Initialize Husky

Run:

```bash
npx husky init
```

This creates the `.husky` directory and configures the prepare script.

### Step 3: Configure the Pre-Commit Hook

Open the following file:

`.husky/pre-commit`

Add:

```bash
npm run lint:md && npm run spellcheck
```

### How It Works

Whenever I try to commit changes, Husky automatically runs:

1. Markdown linting.
2. Spell checking.

If both checks pass, Git allows the commit to continue.

If either check fails, the commit is stopped until the issue is corrected.

This helps identify basic quality issues before code is pushed to GitHub.

**Note:** This example checks all Markdown files in the repository before every commit. In a larger project, the checks can be optimized to run only on changed files.

## 5. Creating and Testing a Pull Request

After configuring GitHub Actions and Husky, the next step is to test whether the automated checks work correctly.

### Step 1: Create a New Branch

Create a separate branch for testing:

```bash
git checkout -b test/markdown-ci
```

### Step 2: Make a Small Change

Create or update a Markdown file, for example:

`ci_cd_test.md`

Add some sample content:

```markdown
# CI/CD Testing

This file is created to test automated Markdown linting and spell checking.

The purpose is to verify that the GitHub Actions workflow runs correctly.
```

### Step 3: Test the Checks Locally

Run:

```bash
npm run lint:md
```

Then:

```bash
npm run spellcheck
```

Check the output and fix any reported issues.

### Step 4: Test Husky

Add the changes:

```bash
git add .
```

Try to commit:

```bash
git commit -m "test: verify markdown quality checks"
```

Husky should automatically execute the configured checks before allowing the commit.

### Step 5: Push the Branch

```bash
git push -u origin test/markdown-ci
```

### Step 6: Open a Pull Request

1. Open your repository on GitHub.
2. Navigate to the Pull Requests section.
3. Select New Pull Request.
4. Select `test/markdown-ci` as the source branch.
5. Select `main` as the target branch.
6. Add a title and description.
7. Create the Pull Request.

### Step 7: Review Automated Checks

After opening the Pull Request:

1. Navigate to the Pull Request page.
2. Find the Checks section.
3. Open the Markdown Quality Checks workflow.
4. Review the Markdown linting result.
5. Review the spell-checking result.
6. Confirm whether both checks have passed.

If a check fails, review the error message, correct the issue, commit the changes, and push again.

GitHub Actions will automatically run the workflow again.

### Expected Results

| Check | Expected Result |
|---|---|
| Markdown linting | Passed |
| Spell checking | Passed |
| Husky pre-commit | Passed |
| GitHub Actions workflow | Successful |
| Pull Request checks | All required checks passed |

These are the expected results. Actual results should be recorded after running the workflow in the repository.

## 6. Pushing CI/CD Configuration to GitHub

After completing the configuration and testing, push all the required files to the repository.

The important files include:

- `.github/workflows/ci.yml`
- `.husky/pre-commit`
- `.markdownlint-cli2.jsonc`
- `cspell.json`
- `package.json`
- `package-lock.json`
- `ci_cd_reflection.md`

Use the following commands:

```bash
git add .
```

```bash
git commit -m "feat: add markdown CI checks and Husky hooks"
```

```bash
git push origin test/markdown-ci
```

After pushing, create or update the Pull Request and verify that the workflow runs successfully.

Once the Pull Request has been reviewed and all required checks have passed, it can be merged into the main branch according to the repository's contribution process.

## 7. Reflection Questions

### Q1. What is the purpose of CI/CD?

The main purpose of CI/CD is to automate the process of integrating, testing, and delivering software changes.

It helps developers identify problems early instead of waiting until the end of development. By running automated checks whenever code is pushed or a Pull Request is created, teams can maintain better software quality and reduce manual effort.

From my QA perspective, CI/CD is especially useful because it allows quality checks to happen continuously throughout the development process. It also helps developers and QA engineers identify issues earlier, which can reduce the time required for debugging and fixing defects.

### Q2. How does automating style checks improve project quality?

Automating style checks improves project quality by making sure that everyone follows consistent coding and documentation standards.

For example, Markdown linting identifies formatting problems, while spell checking detects potential spelling mistakes in documentation.

Without automation, developers need to manually review files, which can take additional time and may allow small mistakes to go unnoticed.

Automated checks provide quick and consistent feedback. They also make documentation easier to read, understand, and maintain.

I learned that even small checks, such as formatting and spelling, can make a difference in maintaining a professional and well-organized project.

### Q3. What are some challenges with enforcing checks in CI/CD?

Although CI/CD provides many benefits, there can also be some challenges.

**1. Initial configuration:** Setting up workflows, dependencies, and configuration files can take time, especially when working with CI/CD tools for the first time.

**2. False positives:** Sometimes automated tools identify technical terms, project names, or intentional formatting as errors.

**3. Maintenance:** Dependencies, workflow configurations, and linting rules need to be maintained and updated.

**4. Pipeline failures:** A small configuration issue or missing dependency can cause the entire workflow to fail.

**5. Execution time:** Running too many automated checks can increase pipeline execution time, especially in large repositories.

**6. Team adoption:** Developers need to understand the rules and follow the same standards. Strict checks can sometimes become frustrating if they are not configured properly.

I also learned that automated checks should be practical and relevant to the project. The goal is to improve quality, not create unnecessary obstacles for developers.

### Q4. How do CI/CD pipelines differ between small projects and large teams?

CI/CD pipelines can vary depending on the size, complexity, and requirements of a project.

**Small Projects:**

Small projects usually have simpler CI/CD pipelines because they contain fewer files, dependencies, and contributors.

For example:
- Basic Markdown linting.
- Spell checking.
- Simple automated tests.
- GitHub Actions workflows.
- Basic pre-commit hooks using Husky.
- Manual approval before merging changes.

These checks are usually sufficient to maintain quality in a small project.

**Large Projects and Development Teams:**

Large projects generally require more advanced CI/CD pipelines because multiple developers may work on different features simultaneously.

For example:
- Automated unit, integration, and end-to-end testing.
- Code quality and security scanning.
- Build and deployment automation.
- Multiple development and testing environments.
- Branch protection rules and mandatory Pull Request reviews.
- Deployment approvals and rollback strategies.
- Monitoring and reporting.

Large teams also need to manage pipeline performance, permissions, test environments, and integration between different services.

**My Understanding:**

The main difference is the level of automation and complexity.

A small project may only need basic linting and spell-checking workflows, while a large project may require multiple stages of testing, security validation, building, and deployment.

However, the overall goal remains the same: deliver reliable software while maintaining quality throughout the development lifecycle.

## 8. What I Learned from This Task

Through this task, I developed a better understanding of how CI/CD supports software development and quality assurance.

Some of the key things I learned include:

- Understanding the difference between Continuous Integration, Continuous Delivery, and Continuous Deployment.
- Learning how GitHub Actions automates quality checks.
- Understanding how Markdown linting helps maintain consistent documentation.
- Learning how cspell identifies potential spelling mistakes.
- Experimenting with Husky and Git Hooks to enforce checks before commits.
- Understanding how automated checks run when a Pull Request is created.
- Learning how CI/CD helps teams identify problems earlier in the development process.

As a QA engineer, I found this task useful because it helped me understand how quality assurance can be integrated into the development workflow rather than being performed only after development is complete.I also realized that automation is not limited to functional testing. Even documentation checks, code quality checks, and pre-commit validations can contribute to a more reliable development process.

## 9. Conclusion

CI/CD is an important part of modern software development because it helps teams automate repetitive tasks, identify issues early, and maintain consistent quality. By implementing GitHub Actions for Markdown linting and spell checking and experimenting with Husky pre-commit hooks, I gained practical experience with automated quality checks. This task also helped me understand how developers and QA engineers can work together to prevent issues before changes are merged into the main branch. Overall, I learned that quality should be maintained throughout the development lifecycle, and CI/CD makes this process more efficient, consistent, and reliable.