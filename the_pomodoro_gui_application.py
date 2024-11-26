from tkinter import *
import os
os.system('clear')

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
TIMER = ''


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(TIMER)
    top_label.config(text='Timer')
    global REPS
    REPS = 0
    canvas.itemconfig(timer_time, text='00:00')
    checks_label.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        top_label.config(text='Break', fg=RED)
        count_down(long_break_seconds)
    elif REPS % 2 == 0:
        top_label.config(text='Break', fg=PINK)
        count_down(short_break_seconds)
    else:
        top_label.config(text='Work')
        count_down(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_time, text=(f'{minutes}:0{seconds}' if seconds < 10 else f'{minutes}:{seconds}'))
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checks = ''
        for _ in range(REPS // 2):
            checks += '✔'
        checks_label.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(99, 112, image=tomato_image)
timer_time = canvas.create_text(99, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)

top_label = Label(text='Timer', font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
top_label.grid(column=2, row=1)

start_button = Button(text='Start', bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text='Reset', bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=3, row=3)

checks_label = Label(bg=YELLOW, fg=GREEN)
checks_label.grid(column=2, row=4)

window.mainloop()
