THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_barin:QuizBrain):
        self.quiz = quiz_barin
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)
        self.canvas = Canvas(bg="white", height=250,width=300)
        self.canvas.grid(column=0, row =1,columnspan =2,pady=50)
        # Width of text will be less than canvas width so question will fit on the canvas perfectly.
        self.quest_text = self.canvas.create_text(150,125,text="question",
                                                  font=("Arial",10,"italic"),
                                                  fill = THEME_COLOR,width=280)

        # Text
        self.score_text = Label(text="Score : 0",bg=THEME_COLOR,foreground="white",font=("Arial",20,"bold"))
        self.score_text.grid(row=0, column=1)

        # Buttons
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(column=0, row=2)


        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img,highlightthickness=0,command=self.false_passed)
        self.false_button.grid(column=1,row =2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_text.config(text =f"Score: {self.quiz.score} / {self.quiz.question_number}")
            que_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quest_text,text= que_text)
        else:
            self.canvas.itemconfig(self.quest_text,text="You have reached to the end of the quiz !!",font = 30)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_passed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
           self.canvas.config(bg="green")
        else:
           self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)
