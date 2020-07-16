from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
        
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER
    Q1 = simpledialog.askstring(title = 'Question 1', prompt = "What is the capital of Virginia?")
    if(Q1 == "richmond" or Q1 == "Richmond"):
       score += 1
    elif(Q1 != "richmond"or Q1 != "Richmond" and score != 0):
        score -= 1
    Q2 = simpledialog.askstring(title = 'Question 1', prompt = "Who is the fourth president of the United States?")
    if(Q2 == "james madison" or Q2 == "James Madison"):
       score += 1
    elif(Q2 != "James Madison" or Q2 != "james madison" and score != 0):
        score -= 1
    Q3 = simpledialog.askstring(title = 'Question 1', prompt = "What is the capital of New York?")
    if(Q3 == "albany" or Q3 == "Albany" ):
       score += 1
    elif(Q3 != "albany" or Q3 != "Albany" and score != 0):
        score -= 1
    score = str(score)
    messagebox.showinfo(title = "Results", message = "Your score is " + score)               
    #      // 2.  Ask the user a question 
    
    #      // 3.  Use an if statement to check if their answer is correct

    #      // 4.  if the user's answer was correct, add one to their score 
 
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
    