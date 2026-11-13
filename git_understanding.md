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