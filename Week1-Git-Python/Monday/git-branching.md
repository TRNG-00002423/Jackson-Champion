**Task 1: Initialize the Repository**

1: created a new directory and named it 'qa-project' using the local terminal using the      command '**mkdir qa-project**'. 

2: navigated into the new directory using '**cd qa-project**'

3: Initialized the directory as a git repo using '**git init**'

4: Created a README.md and added the desired message: '**echo "# QA Project" > README.md
echo "A quality assurance automation project." >> README.md**'

5: Staged and commited the changes using **git add README.md** and added the message         '**git commit -m "Initial commit: add README"**'

6: Verified the commit with '**git log --oneline**'. The log shows my one commit.


**Task 2: Create a Feature Branch**

1: Created and changed to new branch using '**git checkout -b feature/add-test-plan**'

2: created a test-plan using '**nano test-plan.md**' and added the necessary content

3: staged the changes and commited to the repo using  '**git add test-plan.md
git commit -m "Add test plan document"
git push origin feature/add-test-plan**'

4: Repeated steps 2 and 3 for another file named 'test-cases.md'. The changes are then staged and  committed with the message "**Add initial test cases**"

5: Verified the commit with '**git log --oneline**' and verified 3 commits on feature/add-test-plan, and only one on the main branch


**Task 3: Switch Back And Verify isolation**

1: Switch back to main using '**git checkout main**'

2: list the files in the directory using '**ls**'. Only the README.md file is shown

Q: **Where did test-plan.md and test-cases.md go?**.
A: The test-plan.md and test-cases.md file are not appearing because they were created inside the feature/add-test-plan branch. Changes from each branch are usually isolated from other branches until they are merged. Once a merge is made, main will have the two new files.


**Task 4: Make a Change on Main**

1: Made changes in README.md file in main in the terminal by adding a "Team" section using '**nano README.md**'.

2: Once changes are saved, staged the changes '**git add README.md**', commited '**git commit -m "Add team section to README", and pushed changes to main '**git push origin main**'.


**Task 5: Merge the Feature Branch**

1: Merged branch into main with '**git merge feature/add-test-plan**'

2: Verify test-plan.md and test-cases.md now exist in main with '**ls**'.

3: Run git log --oneline --graph to see the merge history.

4: delete feature/add-test-plan branch in terminal using '**git branch -d feature/add-test-plan**'. The test-case.md and test-plan.md file are present in main and feature/add-test-plan branch has been removed.


**Task 6: Simulate and Resolve a Merge Conflict**

1: Create the branch feature/update-test-plan with '**git checkout -b feature/update-test-plan**'.

2: on the new branch, edited test-plan.md with '**nano test-plan.md**', changing the "Scope" section.

3: commit changes '**git add test-plan.md git commit -m "Expand test plan scope on feature branch"**'

4: Switch back to main with '**git checkout main**'

5: opened test-plan.md file and edited in main '**nano test-plan.md**'. Changed the "Scope" section differently, with "- User profile management" and "-Admin Dashboard" added instead of "-Shopping cart" and "-Payment Processing".

6: commit changes '**git add test-plan.md git commit -m "Update test plan scope on main"**'

7: Attempted merge with '**git merge feature/update-test-plan**'

8: A merge conflict is found. Opening test-plan.md there are conflict markers showing the issue.

9: Issue resolves by deleting the conflict markers and combine both versions into one.

10: Staged and commit the resolved file with '**git add test-plan.md git commit -m "Resolve merge conflict: combine scope updates**"'

11: Run git log --oneline --graph to see the full merge history and push changes to main '**git push origin main**'.
