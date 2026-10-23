# Command-Line Calculator

## Student Information
- **Name:** Joebelle Dumapias
- **Section:** IT3R10

---

## Description
This repository contains an interactive Command-Line Interface (CLI) calculator built in Python. It supports standard arithmetic operations including addition, subtraction, multiplication, and division, as well as exponentiation and modulo, equipped with zero-division error handling and input validation.

---

## How to Run the Program

### Prerequisites
- Python 3.x installed on your computer.

### Steps
1. Clone this repository or download the source files:
   `ash
   git clone <YOUR_REPOSITORY_URL>
   cd calculator-project
   `

2. Run the program using Python:
   `ash
   python calculator.py
   `

3. Follow the on-screen prompts to select an arithmetic operation and input your numbers.

---

## Git Reflection (150–200 words)

During the development of this project, I encountered a git merge conflict when attempting to merge my feature branch back into the main branch. I had modified the function definitions in calculator.py on the feature branch while simultaneously adjusting the documentation and function call signatures directly on the main branch. When executing git merge, Git halted the automated process and flagged conflict markers inside the script.

At first, seeing conflict indicators inside my code was intimidating because I was concerned about accidentally losing changes. To solve the issue, I ran git status to identify the conflicting files. I then opened calculator.py in my code editor, carefully compared the contrasting lines, and decided which logic to retain. After manually removing the conflict markers and keeping both the exponentiation logic and the updated comments, I ran syntax checks to ensure the script executed without errors. Finally, I staged the resolved file using git add calculator.py and finalized the merge with git commit. This experience taught me how Git tracks line-by-line changes and gave me confidence in resolving branch divergence.