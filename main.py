from tkinter import *
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    winsound.PlaySound("sounds/timer_start.wav",
                       winsound.SND_ASYNC | winsound.SND_ALIAS)
    countdown(5)


def reset_timer():
    winsound.PlaySound("sounds/reset_timer.wav",
                       winsound.SND_ASYNC | winsound.SND_ALIAS)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    if count > 0:
        canvas.itemconfig(timer_text, text=count)
        win.after(1000, countdown, count - 1)
    elif count == 0:
        canvas.itemconfig(timer_text, text=count)
        win.after(1000, countdown, count - 1)
        winsound.PlaySound("sounds/timer_complete.wav",
                           winsound.SND_ASYNC | winsound.SND_ALIAS)


# ---------------------------- UI SETUP ------------------------------- #

# Window setup
win = Tk()
win.title("Pomodoro App")
win.config(padx=50, pady=50, bg=YELLOW)
win.minsize(410, 334)

# Timer Title
timer_title = Label(text="Timer", font=(FONT_NAME, 60, "bold"), fg=GREEN, bg=YELLOW)
timer_title.grid(row=0, column=1)

# Image and Timer Text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(row=1, column=1)

# Start Button
start_button = Button(text="Start Session",
                      height=2, width=20,
                      font=(FONT_NAME, 10, "bold"),
                      highlightthickness=0,
                      command=start_timer)
start_button.grid(row=2, column=0)

# Reset Button
reset_button = Button(text="Reset Session",
                      height=2, width=20,
                      font=(FONT_NAME, 10, "bold"),
                      highlightthickness=0,
                      command=reset_timer)
reset_button.grid(row=2, column=2)

# Count of Sessions done
sessions = 0
session_count = Label(text=f"Sessions: {sessions}",
                      font=(FONT_NAME, 15, "bold"),
                      bg=YELLOW,
                      fg=GREEN)
session_count.grid(row=3, column=1, pady=35)

win.mainloop()
