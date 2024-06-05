import tkinter as tk
from tkinter import messagebox


def start_quiz():
    if messagebox.askyesno("Welcome to my computer quiz!", "Do you want to play?"):
        next_question()
    else:
        root.quit()


def check_answer():
    global score
    questions = {
        "What does CPU stand for?": "central processing unit",
        "What does GPU stand for?": "graphics processing unit",
        "What does RAM stand for?": "random access memory",
        "What does PSU stand for?": "power supply unit",
    }

    current_question = question_label.cget("text")
    user_answer = answer_entry.get().lower().strip()

    if user_answer == questions[current_question]:
        score += 1
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", "Incorrect")

    next_question()


def next_question():
    global question_index, questions_list

    question_index += 1
    if question_index < len(questions_list):
        question_label.config(text=questions_list[question_index])
        answer_entry.delete(0, tk.END)
    else:
        result = f"You got {score} question(s) correct!\nYou got {(score / len(questions_list)) * 100:.2f}%."
        messagebox.showinfo("Quiz Completed", result)
        root.quit()


# Initialize the GUI application
root = tk.Tk()
root.title("Computer Quiz")
root.geometry("500x300")

score = 0
question_index = -1

questions_list = [
    "What does CPU stand for?",
    "What does GPU stand for?",
    "What does RAM stand for?",
    "What does PSU stand for?",
]

# Set up GUI elements
question_label = tk.Label(root, text="", font=('Arial', 14))
question_label.pack(pady=20)

answer_entry = tk.Entry(root, font=('Arial', 14))
answer_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=check_answer, font=('Arial', 14))
submit_button.pack(pady=20)

# Start the quiz
root.after(100, start_quiz)

# Run the application
root.mainloop()