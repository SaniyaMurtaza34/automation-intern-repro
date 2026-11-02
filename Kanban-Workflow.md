# Agile Workflows & Kanban

## Research & Learn

### 1. How does a Kanban board work, and how does it help manage workflow?

A Kanban board is a visual tool that helps a team organise tasks and track their progress. It allows everyone to see what needs to be done, what is currently being worked on, and what has been completed.

As a QA Engineer, I can use a Kanban board to manage testing tasks, track bugs, monitor automation work, and make sure important tasks are completed on time. It also helps me understand my priorities and identify any tasks that are delayed.

### 2. What do the different columns on a Kanban board represent?

Each column represents a different stage of the workflow. For example:

- **Backlog / Not Started:** Tasks that need to be completed but haven't been started yet.
- **In Progress:** Tasks that I am currently working on, such as writing test cases or executing tests.
- **Blocked:** Tasks that cannot move forward because something is missing or needs to be resolved.
- **Ready for Review:** Tasks that are completed and waiting for someone to review them.
- **Approved by Bot:** Tasks that have passed the required automated checks, if this stage is part of the workflow.
- **Done:** Tasks that have met the completion criteria and require no further action.

These columns make it easier to understand the current status of each task.

### 3. How do tasks move through the board, and who is responsible for updating them?

Tasks move from one column to another as work progresses. For example, when I start testing a new feature, I move the task from "Not Started" to "In Progress." Once testing is complete, I move it to "Ready for Review." After the review and any required checks are completed, it can move to "Done."

The person responsible for the task should keep its status updated. As a QA Engineer, I am responsible for updating my testing tasks, reporting blockers, and adding relevant comments so the team understands the progress.

### 4. What are the benefits of limiting work in progress (WIP)?

Limiting work in progress means focusing on a manageable number of tasks instead of trying to do everything at once.

I believe this is helpful because working on too many tasks at the same time can lead to mistakes, delays, and confusion. By focusing on fewer tasks, I can complete my testing more carefully, identify issues earlier, and deliver better-quality results.

It also helps the team identify bottlenecks and finish existing work before taking on too many new tasks.

## Reflection

### 1. How does Kanban help manage priorities and avoid overload?

Kanban helps me understand which tasks are most important and what needs my attention first. By looking at the board, I can see my current workload, upcoming tasks, and anything that is blocked.

For example, if I have a critical bug to retest and a new automation script to write, I can discuss the priorities with my team and focus on the most urgent task first.

It also reminds me not to take on too many tasks at once. This helps me stay organised, avoid unnecessary stress, and give each task the attention it needs.

### 2. How can you improve your workflow using Kanban principles?

I can improve my workflow by breaking larger testing tasks into smaller, manageable tasks and updating their status regularly. I can also set clear priorities, communicate blockers early, and focus on completing tasks before starting new ones.

As I continue learning test automation, I can use Kanban to track my progress from writing automation scripts to executing tests and reviewing the results.

This approach will help me stay organised, manage my time better, and make my work more transparent to the team.

## Task

### 1. Create a Kanban board for your repository

I would create a Kanban board for my repository with the following columns:

| Column | Purpose |
|---|---|
| Not Started | Tasks that are waiting to be started. |
| In Progress | Tasks that I am currently working on. |
| Blocked | Tasks that cannot continue because of an issue or dependency. |
| Ready for Review | Tasks that are completed and waiting for review. |
| Approved by Bot | Tasks that have passed the required automated checks. |
| Done | Tasks that have been completed and meet the acceptance criteria. |

### 2. Move at least one task through the Kanban process

For example, I can create a task called **"Write and execute a Playwright test for the login page."**

I would move the task through the following stages as I complete each step:

**Not Started → In Progress → Ready for Review → Approved by Bot → Done**

If I encounter an issue, such as a failing test caused by an application bug, I would update the task or create a related bug and mark the work as blocked if it cannot proceed.

I would only move the task to the next stage when it meets the requirements for that stage. I would also update the board with comments or relevant details so the team can follow my progress.

*Note: This is an example workflow. I would update the actual repository board as I complete the task.*

### 3. Identify one way to improve task tracking in my role

One way I can improve task tracking is by keeping task statuses and comments updated regularly. I would include clear acceptance criteria, testing progress, blockers, and the next steps for each task.

For example, instead of writing "Testing in progress," I could provide a more useful update such as "Login functionality tested on Chrome. One validation issue identified and reported. Retesting is pending after the fix."

This would help my team understand exactly what has been completed, what still needs attention, and whether any support is required.