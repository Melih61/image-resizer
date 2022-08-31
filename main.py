import PIL.Image
import PIL.ImageTk
from tkinter import *
from tkinter import filedialog, messagebox

BACKGROUND_COLOR = 'grey'
FOREGROUND_COLOR = 'white'

def open_file():
    file_name = filedialog.askopenfilename(filetypes=[('Image file', '*.png *.jpg *.jpeg'), ('All files', '*.*')])
    image_directory.delete(0, END)
    x_entry.delete(0, END)
    y_entry.delete(0, END)
    image_directory.insert(0, file_name)
    try:
        image = PIL.Image.open(file_name)
        x_entry.insert(0, image.width)
        y_entry.insert(0, image.height)
    except:
        messagebox.showerror(title='Error', message='File is not a image')
        image_directory.delete(0, END)

def resize_image():
    try:
        image_path = image_directory.get()
        x = int(x_entry.get())
        y = int(y_entry.get())
        image = PIL.Image.open(image_path)
        new_image = image.resize((x, y))
        filename = filedialog.asksaveasfilename(filetypes=[('PNG', '*.png'), ('JPG', '*.jpg'), ('JPEG', '*.jpeg'), ('All files', '*.*')], defaultextension=[('PNG', '*.png'), ('JPG', '*.jpg'), ('JPEG', '*.jpeg', ('All files', '*.*'))])
        if(len(filename) == 0):
            pass
        else:
            if filename:
                new_image.save(filename)
            messagebox.showinfo(title='Completed', message='Successfully resized image')
    except:
        messagebox.showerror(title='Error', message='There was an error\nMaybe the image path is wrong')


window = Tk()
window.title('Image resizer')
window.geometry('655x270')
window.resizable(False, False)
window.configure(background=BACKGROUND_COLOR)

for number in range(0,5):
    Label(master=window, text='\t').grid(row=number, column=0)
Label(master=window, text='\tImage resizer', font=('Consolas',25), padx=20, pady=20).grid(row=0, column=0, columnspan=3)
Label(master=window, text='Image:', font=('Consolas', 12)).grid(row=1, column=1, sticky='W')
image_directory = Entry(master=window, font=('Consolas', 12), width=40)
image_directory.grid(row=1, column=2, padx=10)
Button(master=window, text='Open image', font=('Consolas',12), command=open_file, relief='ridge').grid(row=1, column=3)
Label(master=window, text='Width:', font=('Consolas',12)).grid(row=3, column=1, sticky='W')
x_entry = Entry(master=window, font=('Consolas',12), width=6)
x_entry.grid(row=3, column=2, sticky='W', padx=10)
Label(master=window, text='Height:', font=('Consolas',12)).grid(row=4, column=1, sticky='W')
y_entry = Entry(master=window, font=('Consolas',12), width=6)
y_entry.grid(row=4, column=2, sticky='W', padx=10)
Button(master=window, text='Resize image', font=('Consolas',15), relief='ridge', command=resize_image, width=20).grid(row=5, column=1, columnspan=3, pady=20)

for i in window.winfo_children():
    try:
        i.config(background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR, activeforeground=FOREGROUND_COLOR, activebackground=BACKGROUND_COLOR)
    except:
        i.config(background=BACKGROUND_COLOR, foreground=FOREGROUND_COLOR)

window.mainloop()
