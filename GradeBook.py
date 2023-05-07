from tkinter import *
import tkinter.messagebox

# CONSTANTS
TITLE = 'Grade Calculator'
LABEL_TEXT = ['Discussions (5%)', 'Quizzes (20%)', 'Revel Labs (10%)', 'Programs/ Project (15%)',
              'Mid-Term Exam (25%)', 'Final Exam (25%)']
BUTTON_TEXT = ['Calculate', 'Clear', 'Quit']
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# MAIN CLASS
class Grade_Calculator:
    def __init__(self):

        self.myWindow = Tk()
        self.myWindow.title(TITLE)
        self.topFrame = Frame(self.myWindow)
        self.midFrame = Frame(self.myWindow)
        self.midCalcFrame = Frame(self.myWindow)
        self.botFrame = Frame(self.myWindow)

        self.topFrame.pack()
        self.midFrame.pack()
        self.midCalcFrame.pack()
        self.botFrame.pack()

        self.labelTop = Label(self.topFrame, text='Enter your raw scores for the following assignments/exams: ')
        self.labelTop.pack()
        # CREATE LISTS TO STORE LABELS AND ENTRIES.
        self.labels = []
        self.entries = []

        # ITERATE THROUGH THE RANGE OF THE NUMBER OF LABELS AND ENTRIES YOU WANT TO CREATE.
        for i in range(6):
            # Create a label and an entry for each iteration
            label = Label(self.midFrame, text=LABEL_TEXT[i])
            entry = Entry(self.midFrame, width=15)

            # ADD THE LABEL AND ENTRY TO THEIR RESPECTIVE LISTS.
            self.labels.append(label)
            self.entries.append(entry)

            # GRID THE LABEL AND ENTRY IN THE SPECIFIED ROW AND COLUMN.
            self.labels[i].grid(row=i + 1, padx=10, pady=10)
            self.entries[i].grid(row=i + 1, column=2, padx=10, pady=10)

        self.calculateButton = Button(self.midCalcFrame, text="Calculate", command=self.calculate)
        self.calculateButton.pack(side='left')
        self.avgResultLabel = Label(self.midCalcFrame, width=8, borderwidth=1, relief="solid")
        self.avgResultLabel.pack(side='left')

        # BOTTOM FRAME --------------------------------------------------------------------------------------------------------------------------

        self.clear = Button(self.botFrame, text="Clear", command=self.clearEntries)
        self.clear.grid(row=0, column=1, padx=10, pady=10)
        self.quitButton = Button(self.botFrame, text="Quit", command=self.quitProgram)
        self.quitButton.grid(row=0, column=2, padx=10, pady=10)

        tkinter.mainloop()

    # CALCULATE METHODE USING TRY AND EXCEPT: FIRST SCORES VARAIBLE STORS THE NUMBERS, THEN GRADE VARIABLE USES SUM FUNCTION TO CALCULATE AND ZIPS IT
    def calculate(self):
        try:
            scores = [float(entry.get()) for entry in self.entries]
            weights = [0.05, 0.2, 0.1, 0.15, 0.25, 0.25]
            grade = sum(score * weight for score, weight in zip(scores, weights))
            letter = self.findLetterGrade(grade)
            self.avgResultLabel.config(text=f"{grade:.2f}%, {letter}")
        except ValueError:
            tkinter.messagebox.showerror("Invalid input", "Please enter valid numbers")

    # USES THE CALCULATION TO DETERMINE THE LETTER GRADE, IT PASSES THE GRADE PARAMATER WHICH IS FROM THE CALCULATE METHODE
    def findLetterGrade(self, grade):
        if grade >= 90:
            return "A"
        elif 80 <= grade < 90:
            return "B"
        elif 70 <= grade < 80:
            return "C"
        elif 60 <= grade < 70:
            return "D"
        else:
            return "F"

    # METHODE FOR CLEARING THE ENTRIES
    def clearEntries(self):
        for entry in self.entries:
            entry.delete(0, END)
        self.avgResultLabel.config(text="")

    # METHODE FOR QUITING THE PROGRAM
    def quitProgram(self):
        self.myWindow.destroy()

# MAIN
def main():
    grade_calculator = Grade_Calculator()


main()
