**Task 1: Initialize the Repository**

1: I created a new directory and named it 'qa-project' using the local terminal using the      command '**mkdir qa-project**'. 

2: I navigated into the new directory using '**cd qa-project**'

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

4: Repeated steps 2 and 3 for another file named 'test-cases.md', staged and committed the changes with the message "**Add initial test cases**"

5: Verified the commit with '**git log --oneline**' and verified 3 commits on feature/add-test-plan, and only one on the main branch
