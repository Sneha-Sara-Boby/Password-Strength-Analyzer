#  Password Strength Analyzer

A beginner-friendly Python project that checks the strength of a password using regular expressions (Regex).

##  Project Overview

The Password Strength Analyzer evaluates passwords based on common security requirements and assigns a strength rating.

It helps users understand password security and identify missing requirements.

##  Features

- Minimum 8-character length validation
- Uppercase letter detection
- Lowercase letter detection
- Number detection
- Special character detection
- Password strength scoring (0–5)
- Strength classification:
  - Weak
  - Medium
  - Strong
  - Very Strong
- Clear feedback on missing requirements
- Input validation
- Organized functions
- Follows Python PEP 8 coding standards

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Module:** `re` (Regular Expressions)

##  Project Structure

```text
password-strength-analyzer/
│
├── password_analyzer.py
└── README.md
```

##  How to Run

**Step 1:** Install Python 3 on your computer.

**Step 2:** Clone this repository.

```bash
git clone https://github.com/your-username/password-strength-analyzer.git
```

**Step 3:** Open the project folder.

```bash
cd password-strength-analyzer
```

**Step 4:** Run the Python program.

```bash
python password_analyzer.py
```

##  Example Output

```text
Password Strength Analyzer
------------------------------

Enter your password: Hello@123

========== Password Analysis ==========
Strength Score : 5/5
Password Rating: Very Strong

Excellent! Your password meets all security requirements.
=======================================
```

##  Password Scoring System

| Requirement | Score |
|---|---:|
| Minimum 8 characters | 1 |
| Uppercase letter | 1 |
| Lowercase letter | 1 |
| Number | 1 |
| Special character | 1 |
| **Maximum Score** | **5** |

### Password Ratings

| Score | Strength |
|---|---|
| 0–2 | Weak |
| 3 | Medium |
| 4 | Strong |
| 5 | Very Strong |

##  Learning Objectives

- Understand Python functions.
- Learn regular expressions.
- Practice conditional statements and loops.
- Understand password validation.
- Apply basic cybersecurity concepts.
- Improve Python programming skills.

##  Disclaimer

This project is intended for educational purposes. It checks basic password composition rules and does not guarantee that a password is secure against real-world attacks.

**Never enter or share your actual personal passwords in this program.**

##  Author

Created as a beginner-level Python and cybersecurity learning project.
