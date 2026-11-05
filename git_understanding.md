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