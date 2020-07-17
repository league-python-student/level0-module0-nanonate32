from tkinter import messagebox, simpledialog, Tk
import random
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    
    
    hiddenNumber = random.randint(1,100)
    numberGuesses = 10
    guess = 0
    while numberGuesses > 0 and guess != hiddenNumber:
         
        guess = simpledialog.askinteger(title = None, prompt = "Guess a number from 1 to 100.")
        if(guess > hiddenNumber):
            messagebox.showinfo(title = None, message = "Too high!")
        if(guess < hiddenNumber):
            messagebox.showinfo(title = None, message = "Too low!")
        if(guess == hiddenNumber):
            messagebox.showinfo(title = None, message = "You are correct!")
            break
        if(numberGuesses == 0):
            messagebox.showinfo(title = None, message = "Sorry! You ran out of guesses! Better luck next time!")
            break
    window.mainloop()