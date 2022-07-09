from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 0.5
LONG_BREAK_MIN = 1
reps = 0
timing = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timing, reps
    #to stop timer
    window.after_cancel(timing)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer.config(text = "Timer")
    check_marks.config(text = "")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60


    if reps % 2 ==0 :
        count(short_break_seconds)
        timer.config(text = "Short break!!", fg = PINK )
    elif reps ==8:
        count(long_break_seconds)
        timer.config(text="Long break", fg=RED)
    else:
        count(work_seconds)
        timer.config(text="Work!!", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count(n):
    global reps, timing

    count_minutes = math.floor(n/60)
    count_seconds = int(n % 60)
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text = f"{count_minutes} : {count_seconds}")

    if n > 0:
        timing = window.after(1000, count, n - 1)
        print(n)

    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "Done"
        check_marks.config(text = marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = RED )


timer = Label(text = "Timer", fg= GREEN, bg = RED, font = (FONT_NAME, 28, "bold"))
timer.grid(column = 1, row = 0)


# create a canvass

canvas = Canvas(width = 220, height = 224, bg = RED, highlightthickness=0 )
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 142, text = "00:00", fill = "blue", font = (FONT_NAME, 28, ))
canvas.grid(column = 1, row = 1)



start_button = Button(text = "Start",command = start_timer )
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "Reset", command = reset_timer)
reset_button.grid(column = 2, row = 2)

check_marks = Label(fg = GREEN, bg= RED)
check_marks.grid(column = 1, row = 3)



window.mainloop()