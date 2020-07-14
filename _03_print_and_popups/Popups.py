from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()
print('hello from the print method')
messagebox.showinfo('Message Box', "Hello from the message box")
food = simpledialog.askstring(None, prompt =  'What is your favorite food')
messagebox.showerror(None, "Wow! I also love " + food + '.')
window.mainloop()
