from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_num = 0
stop = True
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
# ---------------------------- TIMER MECHANISM ------------------------------- #
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global stop
    global check_num
    global timer

    min = count // 60
    sec = count % 60

    if count == 0:
        reps += 1
        if reps % 2 != 0:
            check_num += 1
            check_mark.config(text=CHECK_MARK * check_num)

            if reps == 7:
                timer_label.config(text="Break", fg=PINK)
                count = LONG_BREAK_MIN * 60
                reps = -1
            else:
                timer_label.config(text="Break", fg=RED)
                count = SHORT_BREAK_MIN * 60
        else:
            timer_label.config(text="Work", fg=GREEN)
            count = WORK_MIN * 60

    if sec < 10:
        canvas.itemconfig(current_time, text=f"{min}:0{sec}")

    else:
        canvas.itemconfig(current_time, text=f"{min}:{sec}")

    count -= 1

    timer = screen.after(1000, count_down, count)
# ---------------------------- UI SETUP ------------------------------- #


WIDTH = 600
HEIGHT = 600


def start():
    global stop
    if stop:
        timer_label.config(text="Work", fg=GREEN)
        count = WORK_MIN * 60
        count_down(count)
        stop = False


def reset():
    global stop
    global reps
    global check_num
    check_num = 0
    stop = True
    reps = 0
    check_mark.config(text="")
    timer_label.config(text="Timer", fg=GREEN)
    screen.after_cancel(timer)
    canvas.itemconfig(current_time, text=first_time)


screen = Tk()
screen.config(padx=100, pady=100, bg=YELLOW)
screen.title("Pomodoro")
first_time = "00:00"

# TIMER LABEL

timer_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 40), fg=GREEN)
timer_label.grid(row=0, column=1)
# CANVAS
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)

current_time = canvas.create_text(102, 135, text=first_time, font=(FONT_NAME, 20, ""), fill="white")
canvas.grid(row=1, column=1)

# BUTTONS
start_button = Button(text="Start", font=(FONT_NAME, 20, ""), command=start, highlightthickness=0)
start_button.grid(row=2, column=0)

start_button = Button(text="Reset", font=(FONT_NAME, 20, ""), command=reset, highlightthickness=0)
start_button.grid(row=2, column=2)

# CHECK_MARK
check_mark = Label(font=(FONT_NAME, 20, ""), bg=YELLOW, fg=GREEN)
check_mark.grid(row=3, column=1)

screen.mainloop()
