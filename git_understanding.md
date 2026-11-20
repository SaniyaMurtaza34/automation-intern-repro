# Understanding Git Merge Conflicts

## 1. What caused the conflict?

I created a new branch called 'feature/git-merge-conflict' and updated the welcome message in the 'README.md' file.

After that, I switched back to the 'main' branch and changed the same line, but used different wording.

When I tried to merge my feature branch into 'main', Git detected that both branches had changed the same line. Since the changes were different, Git couldn't automatically decide which version to keep, so it reported a merge conflict.

## 2. How did I resolve it?

I used GitHub Desktop to identify the conflict in 'README.md'. It showed me that one file needed attention before the merge could be completed.

I opened the file in Visual Studio Code and compared the changes from both branches. Instead of keeping only one version, I combined the wording to create a final welcome message:

"Welcome to my Software Quality Assurance and Automation Testing Portfolio."

I removed the conflict markers, saved the file and returned to GitHub Desktop. After confirming that the conflict was resolved, I clicked **Continue merge** to complete the process.

## 3. What did I learn?

This exercise gave me a better understanding of how Git handles changes when working with multiple branches.

A few things I learned from this experience:

- Two branches can cause a merge conflict when they modify the same line in different ways.
- Working with separate branches allows developers to make changes independently without directly affecting the main branch.
- Git cannot always decide which changes are correct, so reviewing and resolving conflicts manually is important.
- GitHub Desktop makes it easier to identify conflicts and manage the merging process.
- Visual Studio Code helps compare different versions of a file and combine changes when needed.
- It's important to review the final file after resolving a conflict to make sure nothing useful has been lost.

Overall, I found this exercise helpful because I was able to create and resolve a merge conflict myself rather than just reading about how it works. It also reminded me that, as a QA Engineer, reviewing changes carefully is important to maintain software quality and avoid introducing unexpected issues.


# Understanding Git Staging and Committing

## 1. What is the difference between staging and committing?

While learning Git, I understood that staging and committing are two different steps in managing changes in a project.

**Staging** means selecting the changes I want to include in my next commit. It allows me to prepare specific files or changes before saving them to the repository's history. I can use `git add <file>` to stage a file.

**Committing** means saving the staged changes as a snapshot in Git's history. I can use `git commit -m "commit message"` to record those changes.

In simple terms, staging is preparing my changes, while committing is saving those selected changes in the project's history.

## 2. Why does Git separate these two steps?

Git separates staging and committing to give developers more control over their work.

It allows me to review my changes before committing them and decide exactly which files or updates should be included. It also helps keep commits organised by grouping related changes together instead of committing everything at once.

This makes the project history easier to understand and maintain.

## 3. When would I want to stage changes without committing?

I might want to stage changes without committing when I am not ready to save them in the repository's history.

For example:
- When I want to review my changes before committing.
- When I have modified multiple files but only want to commit one specific file.
- When I want to separate different tasks into individual commits.
- When I have finished one part of a feature but am still working on other changes.

Staging gives me the flexibility to prepare and organise my work before creating a commit.

## 4. Practical Staging and Committing Experiment

To understand how staging and committing work in practice, I used the terminal and experimented with the Git commands.

Here are the steps I followed:

**1. Modified a file**

I made changes to my existing `git_understanding.md` file and saved it.

**2. Staged the file**

I used the following command: `git add git_understanding.md`
This added my modified file to the staging area.

**3. Checked the Git status**

I ran: `git status`
Git showed `git_understanding.md` under **Changes to be committed**, confirming that the file was successfully staged.

**4. Unstaged the file**

Next, I used: `git reset HEAD git_understanding.md `
After checking `git status` again, the file appeared under **Changes not staged for commit**. This helped me understand that unstaging removes a file from the staging area without deleting my actual changes.

**5. Staged and committed the file**

I added the file again and committed it: `git add git_understanding.md`, `git commit -m "Update Git staging and committing notes" `
After committing, Git confirmed that the commit was created successfully. When I ran `git status` again, it showed that my working tree was clean.

**What I observed:**

Through this experiment, I understood the difference between modified, staged and committed changes. I also learned that I can move changes out of the staging area without losing my work. Once committed, the changes become part of Git's commit history.

## 5. What I Learned

Through this exercise, I learned how staging and committing work together in Git. I also understood that staging does not permanently save changes in the commit history. It simply prepares them for the next commit. This practical experience helped me understand how to manage changes more carefully, review my work and maintain a clean Git history.


# Git Commands – Learning and Practical Reflection

## 1. What Does Each Command Do?

### `git checkout main -- <file>`
This command allows me to restore a specific file from the `main` branch without affecting other files or changes in my current branch. I learned that it is useful when I accidentally modify a file and want to bring back its original version.

### `git cherry-pick <commit>`
This command allows me to take a specific commit from another branch and apply it to my current branch. It is useful when I need a particular fix or feature without merging all the changes from that branch.

### `git log`
This command displays the commit history of a repository. It helps me understand what changes were made, when they were made, and who made them. I can also use it to find a specific commit when working on an issue.

### `git blame <file>`
This command shows who last modified each line of a file and the corresponding commit information. It helps me understand the history of a particular section of code and makes it easier to investigate issues.

## 2. When Would I Use These Commands in a Real Project?

In a real project, especially when multiple developers are working on the same codebase, these commands can make development and collaboration easier.

- **Git checkout:** I would use it when I accidentally change a file and need to restore its original version from the main branch.
- **Git cherry-pick:** I would use it when a specific bug fix needs to be applied to another branch without merging unrelated changes.
- **Git log:** I would use it to review previous commits, track changes and understand the development history of a feature.
- **Git blame:** I would use it when investigating a bug or trying to understand why a particular line of code was added or modified.

## 3. What Surprised Me While Testing These Commands?

While experimenting with these commands, I realised that Git provides more control over individual changes than I initially expected.

What surprised me most was that `git cherry-pick` allows me to select just one commit from another branch instead of merging the entire branch. I also found `git blame` useful because it helps trace individual lines of code back to their previous changes.

Another thing I learned is that `git checkout main -- <file>` can restore a specific file without affecting other files in my working directory. This is particularly helpful when working on multiple changes at the same time.

Overall, this exercise helped me understand how Git can be used to manage changes, investigate issues and collaborate more confidently with other developers in a long-running project.



# Git Understanding – Git Bisect

## 1. What does `git bisect` do?

Git Bisect is a useful debugging tool that helps identify the exact commit that introduced a bug into a project. It works using a binary search approach, comparing good and bad commits to narrow down the issue.

Instead of manually checking every commit, Git selects commits in between and helps locate the problematic change much faster.

## 2. When would you use it in a real-world debugging situation?

I would use Git Bisect when an application was working correctly before, but after several updates or releases, I noticed unexpected behaviour or a new bug.

For example, if a feature was working in an earlier version but stopped working after multiple commits, I could use Git Bisect to identify which commit introduced the issue.

This would help me investigate the root cause, understand what changed, and work with the development team to resolve the problem.

## 3. How does it compare to manually reviewing commits?

Before learning about Git Bisect, I would normally consider reviewing commits one by one to identify where something went wrong. However, this can take a lot of time, especially in projects with many changes.

Git Bisect makes this process more efficient by using binary search to narrow down the possible commits. It reduces unnecessary investigation and helps identify the problematic change faster.

## 4. My Learning Reflection

During this exercise, I learned how Git Bisect can be used as part of a debugging process. I created multiple commits in a test repository, intentionally introduced a bug, and experimented with identifying the commit responsible for it.

As a QA engineer, I found this particularly useful because identifying when a defect was introduced can help with root cause analysis and make communication with developers more effective.

Overall, this exercise helped me understand that Git is not only useful for version control but also provides practical tools for investigating and resolving software defects.


# Understanding Git Commit Messages

## 1. What makes a good commit message?

After exploring Git commit histories and learning about commit message best practices, I realised that a good commit message should be clear, meaningful and easy to understand.

It should briefly explain what has been changed and why the change was necessary. Using action words such as Add, Fix, Update and Remove makes messages easier to understand.

I also learned that commit messages should not be too vague or unnecessarily long. A short but meaningful message helps other developers understand the purpose of a change without having to review the entire code.

## 2. How does a clear commit message help in team collaboration?

Clear commit messages make communication between team members easier. When multiple developers work on the same project, everyone needs to understand what changes have been made.

For example, if a developer commits a bug fix with a message like `fix: correct login validation`, another team member can quickly understand the purpose of that commit.

It also makes code reviews, debugging and tracking changes easier. Good commit messages help the whole team stay organised and reduce confusion.

## 3. How can poor commit messages cause issues later?

Poor commit messages can create confusion, especially when developers need to investigate an old bug or understand why a particular change was introduced.

For example, a message like `fixed stuff` does not provide enough information about what was fixed. Developers may need to open multiple files or compare changes just to understand the purpose of that commit.

Overly detailed messages can also make the commit history difficult to read because important information gets lost in unnecessary explanations.

## 4. What I learned from this exercise

During this exercise, I practised writing three different types of commit messages: vague, overly detailed and well-structured.

I noticed that the quality of a commit message makes a big difference when reviewing project history. The well-structured message was much easier to understand because it explained the change clearly without adding unnecessary information.

Going forward, I will try to write meaningful commit messages that describe the actual changes I make. I understand that good commit messages are not just a Git convention; they are also an important part of professional development and effective teamwork.

# My Understanding of Git Pull Requests

### 1. Why are PRs important in a team workflow?

As a beginner, I learned that Pull Requests help developers work together without directly changing the main branch. They give team members an opportunity to review changes, identify possible bugs and provide feedback before the changes are merged. This helps maintain software quality and makes teamwork easier.

### 2. What makes a well-structured PR?

A good PR should have a clear title and description explaining what was changed and why. It should contain only relevant changes, include related issue links when applicable, and provide screenshots or testing results if needed. This makes it easier for other developers to understand and review the changes.

### 3. What did I learn from reviewing an open-source PR?

By reviewing an open-source PR, I learned how developers communicate through comments, share suggestions and request changes. I understood that code reviews are an important part of software development because they help identify problems and improve code quality before merging changes.