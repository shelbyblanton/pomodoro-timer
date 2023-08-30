from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global TIMER, REPS
    window.after_cancel(TIMER)
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        title.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif REPS % 2 == 0:
        title.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title.config(text="Work")
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global REPS, TIMER

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 48), fg=GREEN, bg=YELLOW, highlightthickness=0)
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tom_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tom_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset)
reset.grid(column=2, row=2)

check = Label(font=(FONT_NAME, 24), fg=GREEN, bg=YELLOW, highlightthickness=0)
check.grid(column=1, row=3)

window.mainloop()