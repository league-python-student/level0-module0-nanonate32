from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block 
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
   window = Tk()
    # Hide the window using the window's .withdraw() method
   window.withdraw()
    # Ask the user for their name and save it to a variable
      
   name = simpledialog.askstring(title='Greeter', prompt="What is your name?")
    
    # Show a message box with your message using the .showinfo() method
   messagebox.showinfo(None, 'You are my best bud, ' + name + '.')
   print('You are my best bud, ' + name + '.')
    # Print your message to the console using the print() function
        
    # Show an error message using messagebox.showerror()

   if(name == ""):
       messagebox.showerror(None, 'You did not type in your name. Please rerun the code and type in your name.')
       
       
    # Run the window's .mainloop() method
   window.mainloop()
