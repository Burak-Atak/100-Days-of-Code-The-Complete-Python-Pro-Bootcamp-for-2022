from tkinter import *
from question import Question

THEME_COLOR = "#375362"
CANVAS_HEIGHT = 400
CANVAS_WIDTH = 600


class QuizUi:
    def __init__(self, url):
        # Define window
        self.window = Tk()
        self.window.title("Trivia")
        self.window.config(bg=THEME_COLOR, padx=50, pady=50)

        # Define question class
        self.question_class = Question(url)

        # Define parameters
        self.score = 0
        self.question = ""
        self.correct_answer = ""

        # Define canvas
        self.canvas = Canvas(height=CANVAS_HEIGHT,
                             width=CANVAS_WIDTH,
                             highlightthickness=0)

        self.question_text = self.canvas.create_text(CANVAS_WIDTH / 2,
                                                     CANVAS_HEIGHT / 2,
                                                     text=self.question,
                                                     font=("Times", "30", "bold"),
                                                     width=CANVAS_WIDTH - 100)

        self.score_text = self.canvas.create_text(CANVAS_WIDTH - 120,
                                                  CANVAS_HEIGHT - 350,
                                                  text=f"Score:{self.score}",
                                                  font=("Times", "20", "bold"))

        self.canvas.grid(row=0, column=0, columnspan=2, padx=50, pady=50)

        # Define button photos and buttons
        self.true_image = PhotoImage(file="true.png")
        self.false_image = PhotoImage(file="false.png")

        self.true_button = Button(image=self.true_image,
                                  highlightthickness=0,
                                  borderwidth=0,
                                  command=self.true_button_func)
        self.false_button = Button(image=self.false_image,
                                   highlightthickness=0,
                                   borderwidth=0,
                                   command=self.false_button_func)
        self.true_button.grid(row=1, column=1)
        self.false_button.grid(row=1, column=0)

        # Run question func one time
        self.after_func = self.window.after(0, self.question_func)

        self.window.mainloop()

    # Define what will happen when pushed  the "True Button"
    def true_button_func(self):
        self.window.after_cancel(self.after_func)
        if self.correct_answer == "True":
            self.score += 1
            self.update_score()
            self.change_canvas_bg("g")
        else:
            self.change_canvas_bg("r")

        self.after_func = self.window.after(1000, self.question_func)

    # Define what will happen when pushed  the "False Button"
    def false_button_func(self):
        self.window.after_cancel(self.after_func)
        if self.correct_answer == "False":
            self.score += 1
            self.update_score()
            self.change_canvas_bg("g")
        else:
            self.change_canvas_bg("r")

        self.after_func = self.window.after(1000, self.question_func)

    # Question choosing func
    def question_func(self):
        self.question, self.correct_answer = self.question_class.chose_question()
        self.canvas.itemconfig(self.question_text, text=f"{self.question}")
        self.change_canvas_bg("w")

    # Score updating func
    def update_score(self):
        self.canvas.itemconfig(self.score_text, text=f"Score:{self.score}")

    # Canvas's background changing func
    def change_canvas_bg(self, colour):
        if colour == "g":
            self.canvas.config(background="#29b677")
        elif colour == "w":
            self.canvas.config(background="white")
        else:
            self.canvas.config(background="#ee665d")
