# Research: Integrating E2E Tests into CI/CD Using Pywinauto

## 1. Introduction

In this task, I researched how End-to-End (E2E) automated tests can be integrated into a CI/CD pipeline and how Pywinauto tests can be executed automatically. I also explored how test failures affect software deployment, the challenges of running Windows GUI automation in CI/CD, and how tests can be executed locally to simulate a CI environment. The main goal is to understand how automated testing helps maintain application quality and stability during software development.

---

## 2. What is CI/CD?

CI/CD stands for Continuous Integration and Continuous Delivery or Continuous Deployment. It is a process that helps developers build, test and release software more efficiently.

### Continuous Integration (CI)

Continuous Integration means automatically checking code whenever developers make changes and push them to a shared repository such as GitHub.

For example:

1. A developer makes changes to the Focus Bear application.
2. The developer pushes the changes to GitHub.
3. The CI pipeline automatically starts.
4. The pipeline installs the required dependencies.
5. Automated tests are executed.
6. The results show whether the tests passed or failed.

This helps identify bugs early instead of waiting until the end of development.

### Continuous Delivery (CD)

Continuous Delivery means that after the application passes the required tests, it is prepared for deployment. A person may still need to approve the release before it goes live.

### Continuous Deployment

Continuous Deployment takes automation one step further. When all required checks pass, the application can be deployed automatically without manual approval.

### Why is CI/CD important?

CI/CD helps the development team:

- Find bugs earlier.
- Reduce repetitive manual testing.
- Receive faster feedback.
- Improve collaboration between developers and QA engineers.
- Reduce deployment risks.
- Maintain application stability.
- Deliver updates more frequently.

---

## 3. What is End-to-End (E2E) Testing?

End-to-End testing is a type of software testing that checks whether an entire application works correctly from the user's perspective. Instead of testing only one button or function, E2E testing checks a complete user journey.

### Example: Focus Bear application

Imagine a user wants to start a focus session and create a task. An E2E test could perform the following steps:

1. Open the Focus Bear application.
2. Log in to the application.
3. Navigate to the Focusing tab.
4. Start a focus session.
5. Open the Add Task option.
6. Create a new task.
7. Enter the task details.
8. Save the task.
9. Verify that the task appears successfully.

If the task is created successfully, the test passes. If the application does not create the task or displays an unexpected result, the test fails.

### Why do we use E2E testing?

E2E testing helps verify that different parts of an application work together correctly.

It is useful for:
- Testing complete user workflows.
- Finding issues between different application components.
- Checking important functionality after updates.
- Reducing manual regression testing.
- Improving confidence before releasing new versions.

---

## 4. How are E2E tests integrated into CI/CD workflows?

E2E tests can be included as one of the automated testing stages in a CI/CD pipeline. For example, when a developer pushes new code to GitHub, the pipeline can automatically build the application and execute automated tests.

### Example CI/CD workflow

1. **Code changes:** A developer updates the application.
2. **Code push:** The developer pushes the changes to GitHub.
3. **Pipeline trigger:** GitHub Actions or another CI/CD tool detects the changes.
4. **Build:** The application is built.
5. **Dependency installation:** Required libraries and tools are installed.
6. **Automated testing:** Unit, integration and E2E tests are executed.
7. **Test reporting:** Test results are generated.
8. **Deployment decision:** The pipeline checks whether the required tests passed.
9. **Release:** If all required checks pass, the application can proceed to deployment.

If an important test fails, the pipeline can stop the deployment process.

### Example

Suppose a developer changes the task creation functionality in Focus Bear.

The existing E2E tests can automatically check whether:

- The Focusing tab opens correctly.
- A focus session starts.
- The Add Task window opens.
- A new task can be created.
- The created task is displayed correctly.

This helps identify whether the new code has affected existing functionality.

---

## 5. What is Pywinauto?

Pywinauto is a Python library used to automate Windows desktop applications. It allows QA engineers to interact with application windows and controls without manually performing every action.

Using Pywinauto, we can:

- Open desktop applications.
- Click buttons.
- Enter text into input fields.
- Select menu options.
- Interact with application windows.
- Read text from controls.
- Verify application behaviour.

### Example of Pywinauto

```python
from pywinauto.application import Application

# Start the Windows application
app = Application(backend="uia").start(
    r"C:\Path\To\FocusBear.exe"
)

# Connect to the application window
window = app.window(title_re=".*Focus Bear.*")

# Wait until the window becomes visible
window.wait("visible", timeout=30)

# Print the window title
print(window.window_text())
```

### Explanation of the code

- `Application`: Used to start or connect to a Windows application.
- `backend="uia"`: Uses Microsoft's UI Automation technology to interact with application controls.
- `start()`: Launches the application.
- `window()`: Finds the application window.
- `wait()`: Waits until the window becomes visible.
- `window_text()`: Retrieves the window title.

The application path and window title must match the actual Focus Bear installation. This is a basic example. Actual test scripts need appropriate application controls and assertions.

---

## 6. How can Pywinauto tests run in a CI/CD pipeline?

Pywinauto tests can be integrated into CI/CD by using a Windows machine configured to execute automated GUI tests. Unlike browser automation, Pywinauto interacts directly with the Windows desktop. Therefore, it normally requires an interactive desktop session.

### Step 1: Organise test files

Keep automated test scripts organised in the project repository.

Example folder structure:

```text
FocusBear/
│
├── tests/
│   ├── test_login.py
│   ├── test_focus_session.py
│   ├── test_task_creation.py
│   ├── test_morning_routine.py
│   └── test_evening_routine.py
│
├── requirements.txt
│
└── README.md
```

### Step 2: Install dependencies

The Windows testing machine needs Python and the required libraries.

Commands:

```bash
pip install pywinauto
pip install pytest
```

If the project already has a requirements.txt file:

```bash
pip install -r requirements.txt
```

### Step 3: Prepare the Windows testing machine

The machine should have:

- Windows operating system.
- Python installed.
- Pywinauto installed.
- Pytest installed.
- Focus Bear application installed.
- Required test data and configuration.
- An active interactive desktop session.

### Step 4: Configure a CI/CD agent

A self-hosted Windows agent can be configured using a CI/CD platform such as:

- GitHub Actions.
- Azure Pipelines.
- Jenkins.

The agent receives jobs from the CI/CD system and executes the required commands on the Windows machine. For Pywinauto, the agent must be configured so that GUI tests can access an interactive desktop session.

### Step 5: Execute automated tests

The pipeline can execute tests using:

```bash
pytest tests/ -v
```

This command runs the test files inside the tests folder.

### Step 6: Generate test reports

We can generate a JUnit XML report:

```bash
pytest tests/ -v --junitxml=test-results.xml
```

The report contains test execution results and can be uploaded as a CI/CD artifact.

### Step 7: Save screenshots and logs

When tests fail, screenshots and application logs can help QA engineers understand what happened This makes debugging easier and helps developers investigate the issue.

---

## 7. What is Headless Mode?

Headless mode means executing automated tests without displaying the normal graphical interface. For example, browser automation tools such as Playwright and Selenium can run supported browsers in headless mode. The browser performs automated actions without displaying a normal browser window.

### Headless versus normal execution

**Normal execution:**

- The browser or application window is visible.
- We can observe the automation.
- Useful for debugging and learning.

**Headless execution:**

- The browser runs without displaying its normal window.
- Tests execute without requiring a visible browser interface.
- Commonly used in CI/CD environments.

### Can Pywinauto run in headless mode?

Pywinauto is different from Playwright and Selenium. Pywinauto interacts directly with Windows desktop controls, such as buttons, windows and input fields. Therefore, it generally requires an active interactive Windows desktop session. It does not provide native GUI headless execution in the same way as browser automation tools. A Python test process can run unattended, but the Windows desktop session must still be available for GUI interaction.

### How can I simulate CI execution locally?

I can practise the test execution process on my local Windows machine.

**Step 1: Open VS Code.**

Open the project folder and select:

Terminal → New Terminal.

**Step 2: Activate the virtual environment.**

```powershell
.venv\Scripts\activate
```

This step is only needed if the project uses a virtual environment named `.venv`.

**Step 3: Install the dependencies.**

```bash
pip install pywinauto pytest
```

**Step 4: Execute the tests.**

```bash
pytest tests/ -v
```

**Step 5: Generate a test report.**

```bash
pytest tests/ -v --junitxml=test-results.xml
```

**Step 6: Review the results.**

Example output:

```text
================ test session starts ================

tests/test_login.py PASSED
tests/test_focus_session.py PASSED
tests/test_task_creation.py FAILED

================ test results ========================

2 passed, 1 failed
```

This is an example of test output, not an actual result from Focus Bear. It shows how Pytest reports successful and failed test cases. This process simulates the test execution part of a CI/CD pipeline locally.

---

## 8. How do test failures impact the deployment process?

Automated test failures can affect whether an application is allowed to proceed to deployment. For example, suppose a developer makes changes to the Focus Bear task creation functionality. The automated test tries to create a new task but the application does not respond. The test fails. The CI/CD pipeline can be configured to stop deployment until the issue is investigated.

### What happens when a test fails?

1. A developer pushes new code.
2. The CI/CD pipeline starts.
3. Automated tests execute.
4. One or more tests fail.
5. The pipeline reports the failure.
6. Developers and QA engineers investigate the issue.
7. The developer fixes the problem.
8. Tests are executed again.
9. If the required checks pass, deployment can continue.

### Why is this important?

If failed tests are ignored, broken functionality might reach users. Stopping deployment after critical test failures helps reduce the risk of releasing defective software. However, not every failed test indicates an application bug.

A test can also fail because of:

- Incorrect test data.
- Application loading delays.
- Unavailable network connections.
- Windows desktop session problems.
- Incorrect element locators.
- Automation script issues.

QA engineers should investigate the failure and identify its root cause before deciding what action to take.

---

## 9. What are Flaky Tests?

Flaky tests are automated tests that sometimes pass and sometimes fail even though the application code has not changed.

### Example

Imagine running a Focus Bear login test:

- First execution: Passed.
- Second execution: Failed.
- Third execution: Passed.

This is an example of a flaky test.

### Common reasons for flaky tests

1. **Timing issues:** The application takes longer to load than expected.
2. **Unstable elements:** Application controls change their properties or identifiers.
3. **Network problems:** The application cannot load data correctly.
4. **Environment problems:** The Windows machine is slow or the desktop session is locked.
5. **Test data problems:** Previous test executions affect the next test.

### How can flaky tests be handled?

**1. Use explicit waits**

Wait until an application window or control is ready instead of using fixed delays.

Example:

```python
window.wait("visible", timeout=30)
```

**2. Use stable element identifiers**

Use reliable properties such as automation IDs and control names.

**3. Implement limited retries**

Retry a failed test when appropriate, but investigate why the original execution failed.

**4. Maintain test isolation**

Make sure tests can run independently without depending on previous test results.

**5. Capture screenshots and logs**

Save evidence when a test fails to help identify the root cause.

**6. Maintain a consistent environment**

Use the same application configuration, dependencies and test data.

**7. Review flaky tests regularly**

Fix unreliable scripts instead of allowing them to create repeated failures in the CI/CD pipeline.

The main goal is to identify the actual reason behind a test failure rather than simply rerunning the test.

---

## 10. What are the next steps to fully integrate Focus Bear's automated tests into its deployment pipeline?

Based on my research, I would suggest the following steps:

### Step 1: Organise automated tests

Store Pywinauto test scripts in the GitHub repository and organise them according to application functionality.

Examples:

- Login.
- Focus sessions.
- Task creation.
- Morning routines.
- Evening routines.
- Scheduling and timezone functionality.

### Step 2: Prepare a Windows test environment

Install Python, Pywinauto, Pytest and the Focus Bear application on a dedicated Windows machine. Make sure the machine has an active interactive desktop session.

### Step 3: Configure a CI/CD agent

Set up a self-hosted Windows agent using GitHub Actions, Azure Pipelines or Jenkins.

### Step 4: Automate test execution

Configure the pipeline to execute automated tests when:

- Developers push code.
- Pull requests are created.
- Changes are merged into the main branch.
- A new release is prepared.

### Step 5: Generate test reports

Save test execution results, screenshots, logs and error messages.

### Step 6: Configure deployment rules

Configure the pipeline to stop deployment when important automated tests fail. The development team should investigate and resolve critical failures before continuing with the release.

### Step 7: Maintain automated tests

Regularly review existing scripts, add test cases for new features and fix flaky tests. This will help maintain test coverage as the application develops.

---

## 11. Practical Commands Reference

These are the main commands I can use when practising locally.

### Install Pywinauto

```bash
pip install pywinauto
```

### Install Pytest

```bash
pip install pytest
```

### Install project dependencies

```bash
pip install -r requirements.txt
```

### Run all automated tests

```bash
pytest tests/ -v
```

### Run one specific test file

```bash
pytest tests/test_login.py -v
```

### Generate a JUnit XML report

```bash
pytest tests/ -v --junitxml=test-results.xml
```

### Stop execution after the first failure

```bash
pytest tests/ -v -x
```

### Show more detailed test output

```bash
pytest tests/ -vv
```

---

## 12. Reflection and What I Learned

Through this task, I learned how E2E testing can be integrated into CI/CD workflows to automatically verify application functionality whenever developers make changes. I understood that CI/CD helps identify bugs early, reduces repetitive manual testing and provides faster feedback to developers. I also learned how Pywinauto can automate Windows desktop applications by interacting with buttons, windows, input fields and other application controls. One important thing I discovered is that Pywinauto is different from browser automation tools because it normally requires an active Windows desktop session. It cannot run native desktop GUI tests in headless mode in the same way as Playwright or Selenium. I also learned how failed automated tests can stop the deployment process and why QA engineers need to investigate failures before allowing an application to proceed to release.
Another important concept I learned is flaky testing. I understood why explicit waits, stable locators, test isolation and proper test environments are important for reliable automation. My next step is to practise running Pywinauto tests locally, generate test reports and explore how GitHub Actions can execute automated tests. Overall, this research helped me understand how QA automation works together with CI/CD to improve software quality, application stability and release confidence.

---

