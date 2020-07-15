from tkinter import messagebox, simpledialog, Tk
window = Tk()
window.withdraw()

print('hello')
messagebox.showinfo(None, message = 'Hello from the message box.')
age = simpledialog.askstring(title='', prompt='')

age = int(age)

if(age == 20):
    messagebox.showinfo(None, message = 'Wow! You are pretty young!')
elif (age == 30):
    messagebox.showinfo(None, message = 'Wow! You are pretty old!')
        
        
window.mainloop()