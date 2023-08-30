# Pomodoro Application

## **[100 Days of Code: The Complete Python Pro Bootcamp for 2023](https://www.udemy.com/course/100-days-of-code/)**

By Dr. Angela Yu

*Day 31 of 100:* Tkinter, Dynamic Typing and the Pomodoro GUI Application

## Project Specs

Using TkInter and the Math libraries, develop a **[pomodoro technique](https://en.wikipedia.org/wiki/Pomodoro_Technique)** time management application to help people be more productive.

From Wikipedia: *"Each interval is known as a pomodoro, from the Italian word for tomato, after the tomato-shaped kitchen timer Cirillo used as a university student."*

This application is written with Python 3.11.

![Pomodoro Timer Application](https://github-readme.s3.us-west-1.amazonaws.com/PomodoroTimer.png)

### Main Features
The app uses a counting-down timer to break work into 25 minute-long intervals, separated by short, 5-minute breaks. Each work and short break interval is called a pomodoro.

Each interval type (work or rest) shows as a header in green above the tomato graphic. The timer itself counts down in white integers within the tomato graphic. 

After completing 4 pomodoros, the timer then sets to a 20 minute "long" break.

## Usage & Requirements

This project uses two libraries:
- TkInter
- Math

### Workflow
First we create the Graphic User Interface (GUI) using Tkinter, using variable variable constants to set the interface colors, font name, and background image.  

```
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

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
```

We then add two buttons to the interface which will start and reset our pomodoro timer:
- Start - tied to the `start_timer()` function 
- Reset - tied to the `reset()` function

```angular2html
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset)
reset.grid(column=2, row=2)

check = Label(font=(FONT_NAME, 24), fg=GREEN, bg=YELLOW, highlightthickness=0)
check.grid(column=1, row=3)
```

The `start_timer()` function counts how many cycles of work and short breaks have been completed, and starts our timer with the appropriate amount of time:

```angular2html
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
```

Once the `start_timer()` function knows the amount of time to count, it then calls to the `count_down()` function which animates the timer at the top of the interface, informing the user how much time is left in each interval:

```angular2html
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
```

![Pomorodo Timer Showing a Work Interval and counting down from 25 minutes](https://github-readme.s3.us-west-1.amazonaws.com/PomodoroTimer-Work.png)

Lastly, to reset the timer and start the intervals from the beginning, we add the `reset()` function:

```angular2html
def reset():
    global TIMER, REPS
    window.after_cancel(TIMER)
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text="")
    REPS = 0
```

# Getting Started

All of the commands below should be typed into the Python terminal of your IDE (I use PyCharm for my Python Development).

First, clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:shelbyblanton/pomodoro-timer.git
    
Then open the project in PyCharm.

**Setup is complete!** 

Click Run in PyCharm to see the app in action.


# Author & Credits

Programmed by **[M. Shelby Blanton](https://www.linkedin.com/in/shelbyblanton/)** under the instructional guidance of **[Dr. Angela Yu](https://www.udemy.com/user/4b4368a3-b5c8-4529-aa65-2056ec31f37e/)** via **[Udemy.com](udemy.com)**.
