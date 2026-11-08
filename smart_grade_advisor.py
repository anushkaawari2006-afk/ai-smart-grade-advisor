"""
smart_grade_advisor.py - AI-powered Study Advisor
Module 05: AI Tools & Mini Project

An upgrade of my Module 02 Student Grade Calculator.
Instead of only reporting marks, it now uses a simple machine learning model
(linear regression) to:
  - find the trend in each subject (improving, stable or declining)
  - predict the score in the next exam
  - give personalised advice for every subject
  - suggest how to split weekly study time
  - save a progress chart (if matplotlib is installed)

Run normally:   python smart_grade_advisor.py
Run with demo:  python smart_grade_advisor.py --demo
"""

import sys

import numpy as np

MAX_MARKS = 100
PASS_MARKS = 35
WEEKLY_STUDY_HOURS = 10

DEMO_DATA = {
    "Maths": [55, 62, 70, 78],
    "Science": [80, 76, 71, 66],
    "English": [65, 64, 66, 65],
    "History": [48, 45, 41, 38],
}


# ------------------------------------------------------------------ input
def get_text(prompt):
    """Keep asking until the user types something."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("  This field cannot be empty.")


def get_int(prompt, minimum, maximum):
    """Keep asking until the user enters a whole number in the given range."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"  Please enter a number between {minimum} and {maximum}.")


def get_marks_list(prompt):
    """Read marks separated by commas, e.g. '55, 62, 70'."""
    while True:
        parts = [p.strip() for p in input(prompt).split(",") if p.strip()]
        try:
            marks = [int(p) for p in parts]
        except ValueError:
            print("  Use whole numbers separated by commas, e.g. 55, 62, 70")
            continue
        if len(marks) < 2:
            print("  Enter at least 2 exam marks so a trend can be found.")
        elif any(m < 0 or m > MAX_MARKS for m in marks):
            print(f"  Every mark must be between 0 and {MAX_MARKS}.")
        else:
            return marks


def read_student_data():
    """Ask the user for a name and the marks history of each subject."""
    name = get_text("\nStudent name: ")
    count = get_int("Number of subjects (1-8): ", 1, 8)
    data = {}
    for i in range(1, count + 1):
        subject = get_text(f"\nSubject {i} name: ")
        data[subject] = get_marks_list(
            f"Marks in {subject} from oldest to latest exam (e.g. 55, 62, 70): "
        )
    return name, data


# --------------------------------------------------------------- the "AI"
def calculate_grade(percentage):
    """Return a letter grade for a percentage."""
    for limit, grade in ((90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D"), (40, "E")):
        if percentage >= limit:
            return grade
    return "F"


def predict_next(marks):
    """
    Fit a straight line through the marks (linear regression) and use it
    to predict the next exam. Returns (predicted_marks, slope).
    The slope is the average change in marks per exam.
    """
    exams = np.arange(len(marks))
    slope, intercept = np.polyfit(exams, marks, 1)
    predicted = slope * len(marks) + intercept
    predicted = float(np.clip(predicted, 0, MAX_MARKS))
    return predicted, float(slope)


def trend_label(slope):
    if slope >= 2:
        return "Improving"
    if slope <= -2:
        return "Declining"
    return "Stable"


def get_advice(latest, predicted, slope):
    """Rule-based personal advice for one subject."""
    if predicted < PASS_MARKS:
        return "High risk of failing the next exam. Ask your teacher for help and revise the basics daily."
    if slope <= -2:
        return "Marks are falling. Revise recent topics and practise past papers."
    if latest < 50:
        return "Weak area. Study a little every day and solve easy questions first."
    if slope >= 2:
        return "Great improvement! Keep the same routine."
    if latest >= 85:
        return "Excellent. Try harder problems or help classmates to stay sharp."
    return "Steady performance. Small daily practice can push your marks higher."


def analyse(data):
    """Run the prediction and advice for every subject."""
    results = []
    for subject, marks in data.items():
        predicted, slope = predict_next(marks)
        results.append({
            "subject": subject,
            "marks": marks,
            "latest": marks[-1],
            "predicted": predicted,
            "slope": slope,
            "trend": trend_label(slope),
            "grade": calculate_grade(predicted),
            "advice": get_advice(marks[-1], predicted, slope),
        })

    # Weaker predicted subjects get more of the weekly study time
    weights = [100 - r["predicted"] + 10 for r in results]
    total = sum(weights)
    for r, w in zip(results, weights):
        r["hours"] = round(w / total * WEEKLY_STUDY_HOURS, 1)
    return results


# ----------------------------------------------------------------- output
def print_report(name, results):
    line = "=" * 62
    print(f"\n{line}\nSMART GRADE ADVISOR: {name}\n{line}")
    print(f"{'Subject':<12}{'Latest':>7}{'Trend':>12}{'Predicted':>11}{'Grade':>7}")
    print("-" * 62)
    for r in results:
        print(f"{r['subject']:<12}{r['latest']:>7}{r['trend']:>12}{r['predicted']:>11.1f}{r['grade']:>7}")
    print("-" * 62)

    current_avg = sum(r["latest"] for r in results) / len(results)
    predicted_avg = sum(r["predicted"] for r in results) / len(results)
    print(f"Current average: {current_avg:.1f}%")
    print(f"Predicted next average: {predicted_avg:.1f}% (Grade {calculate_grade(predicted_avg)})")

    print("\nPERSONAL ADVICE")
    for r in results:
        print(f"- {r['subject']}: {r['advice']}")

    print(f"\nSUGGESTED WEEKLY STUDY PLAN ({WEEKLY_STUDY_HOURS} hours)")
    for r in sorted(results, key=lambda r: r["hours"], reverse=True):
        print(f"- {r['subject']:<12}{r['hours']} hrs")

    print("\nNote: predictions are estimates from a simple trend line, not guarantees.")


def save_chart(name, results, filename="progress_chart.png"):
    """Save marks history and the predicted next exam as a chart (optional)."""
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("(Install matplotlib to also get a progress chart: pip install matplotlib)")
        return

    plt.figure(figsize=(9, 5))
    longest = 0
    for r in results:
        exams = list(range(1, len(r["marks"]) + 1))
        longest = max(longest, len(exams) + 1)
        (line,) = plt.plot(exams, r["marks"], marker="o", label=r["subject"])
        plt.plot(
            [exams[-1], exams[-1] + 1],
            [r["marks"][-1], r["predicted"]],
            linestyle="--",
            marker="*",
            markersize=11,
            color=line.get_color(),
        )
    plt.title(f"{name}: marks history and predicted next exam (dashed line, star)")
    plt.xlabel("Exam number")
    plt.ylabel("Marks")
    plt.ylim(0, 100)
    plt.xticks(range(1, longest + 1))
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=120)
    plt.close()
    print(f"Progress chart saved as {filename}")


def main():
    print("=== Smart Grade Advisor (AI-powered) ===")
    if "--demo" in sys.argv:
        name, data = "Demo Student", DEMO_DATA
        print("Running in demo mode with sample data...")
    else:
        name, data = read_student_data()

    results = analyse(data)
    print_report(name, results)
    save_chart(name, results)


if __name__ == "__main__":
    main()
