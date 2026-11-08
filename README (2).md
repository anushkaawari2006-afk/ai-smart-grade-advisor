# Smart Grade Advisor (AI-Powered)

**Module 05: AI Tools & Mini Project (Day 17 – Day 20)**

This project is an upgrade of my Module 02 *Student Grade Calculator*. Instead of only reporting marks, it uses a simple **machine learning model (linear regression)** to find each subject's trend, predict the next exam score and give personalised study advice.

## What it does
- Takes a student's marks history for each subject (oldest to latest exam)
- Fits a trend line to the marks with `numpy.polyfit` (linear regression)
- Labels each subject as **Improving**, **Stable** or **Declining**
- Predicts the score and grade for the next exam
- Gives subject-wise advice and a suggested weekly study plan (weaker subjects get more hours)
- Saves a progress chart (`progress_chart.png`) showing past marks and the predicted next exam

## How the AI part works
For each subject, the exam number (1, 2, 3, ...) is the input and the marks are the output. Linear regression finds the straight line that best fits the marks, and extending that line one exam ahead gives the prediction. The slope of the line is the average change in marks per exam, which decides the trend label.

> Predictions are estimates from a simple trend line, not guarantees. Small amounts of data give rough results.

## AI Tools Used
An AI assistant (Claude) helped plan, write and test this project. I reviewed and ran the code myself. See [AI_TOOLS_NOTES.md](AI_TOOLS_NOTES.md) for my notes on AI tools and responsible use.

## How to Run

Requires Python 3.

```bash
pip install -r requirements.txt

python smart_grade_advisor.py          # enter your own marks
python smart_grade_advisor.py --demo   # run with sample data
```

When asked, type marks separated by commas, for example `55, 62, 70, 78`. At least 2 exam marks are needed for each subject.

## Sample Output (demo mode)

```
=== Smart Grade Advisor (AI-powered) ===
Running in demo mode with sample data...

==============================================================
SMART GRADE ADVISOR: Demo Student
==============================================================
Subject      Latest       Trend  Predicted  Grade
--------------------------------------------------------------
Maths            78   Improving       85.5      A
Science          66   Declining       61.5      C
English          65      Stable       65.5      C
History          38   Declining       34.5      F
--------------------------------------------------------------
Current average: 61.8%
Predicted next average: 61.7% (Grade C)

PERSONAL ADVICE
- Maths: Great improvement! Keep the same routine.
- Science: Marks are falling. Revise recent topics and practise past papers.
- English: Steady performance. Small daily practice can push your marks higher.
- History: High risk of failing the next exam. Ask your teacher for help and revise the basics daily.

SUGGESTED WEEKLY STUDY PLAN (10 hours)
- History     3.9 hrs
- Science     2.5 hrs
- English     2.3 hrs
- Maths       1.3 hrs
```

## Project Files

| File | Description |
|------|-------------|
| `smart_grade_advisor.py` | Main program |
| `requirements.txt` | Python packages needed |
| `AI_TOOLS_NOTES.md` | Notes on AI tools and how they were used |
| `progress_chart.png` | Example chart created by the demo |

## Python Concepts Used
Functions, loops, lists and dictionaries, input validation with `try / except`, NumPy, Matplotlib, linear regression and command-line arguments.

## Possible Improvements
- Save student data to a CSV file
- Use more exams and a stronger model (for example, scikit-learn)
- Add a simple web interface

## Author
Your Name Here
