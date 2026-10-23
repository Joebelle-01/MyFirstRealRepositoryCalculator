# Git Reflection Essay

**Author:** Joebelle Dumapias  
**Section:** IT3R10  
**Word Count:** 182 words  

---

During the development of this project, I encountered a git merge conflict when attempting to merge my feature branch back into the main branch. I had modified the function definitions in calculator.py on the feature branch while simultaneously adjusting the documentation and function call signatures directly on the main branch. When executing git merge, Git halted the automated process and flagged conflict markers inside the script.

At first, seeing conflict indicators inside my code was intimidating because I was concerned about accidentally losing changes. To solve the issue, I ran git status to identify the conflicting files. I then opened calculator.py in my code editor, carefully compared the contrasting lines, and decided which logic to retain. After manually removing the conflict markers and keeping both the exponentiation logic and the updated comments, I ran syntax checks to ensure the script executed without errors. Finally, I staged the resolved file using git add calculator.py and finalized the merge with git commit. This experience taught me how Git tracks line-by-line changes and gave me confidence in resolving branch divergence.