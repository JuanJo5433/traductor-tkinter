# The tkinter library is imported
from tkinter import * 
from tkinter import ttk, messagebox

# The googletrans library is imported
import googletrans
from googletrans import Translator

# creates the window with the instance of the class
root = Tk()

# Title for the window
root.title("Google Translator")

# Size of window
root.geometry("1080x400")
root.resizable(False, False)

# Method that allows to change the label according to the combobox selection.
def label_change():
# The data is obtained from the combobox
	c1 = combo1.get()
	c2 = combo2.get()
	# The selected combobox element is loaded in the label.
	Label1.configure(text=c1)
	Label2.configure(text=c2)
	# Executes the label_change method after 1 second (Loads in the label the data after 1 second)
	root.after(1000, label_change)

def traslate_now():
	text_ = text1.get(1.0, END)
	t1 = Translator()
	# src is the language source where the text should be taken from 
	# dest is the language option to be translated into
	trans_text = t1.translate(text_,src=combo1.get(), dest=combo2.get())
	# The text is required
	trans_text = trans_text.text
	# The contents of the text box are deleted. 
	text2.delete(1.0, END)
	# The translated word is inserted
	text2.insert(END, trans_text)

# The window icon is added
image_icon = PhotoImage(file="icono.png")
root.iconphoto(False, image_icon)

# create the label with the image of the icon exchange
arrow_image = PhotoImage(file="intercambiar.png")
arrow_image = arrow_image.subsample(5)
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=460, y=50)

# The language instance is made with the languages that have the googletrans API.
language = googletrans.LANGUAGES
# The dictionary of language elements is saved
languagev = list(language.values())
# You can access the dictionary keys of the languages
lang1 = language.keys()

# First combo for the application
combo1 = ttk.Combobox(root, values=languagev, font="Roboto 14", state="r")
# Location of the combo
combo1.place(x=110, y=20)
# The default Spanish combo is displayed
combo1.set("Spanish") 

# create the label for the spanish languages
Label1 = Label(root, text="Spanish", font="segoe 30 bold", bg="white", width=18, bd=5, relief="groove")
Label1.place(x=10, y=50)

# create the box for the content of the text to be entered.
f = Frame(root, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)

# Create the option to allow text input in the frame
text1 = Text(f, font="Robote 20", bg="white", relief="groove", wrap=WORD)
text1.place(x=0, y=0, width=430	, height=200)

# Create a scroll for the first text to allow the writing inside the whole drawer.

scrollbar1 = Scrollbar(f)
# Vertical packaging
scrollbar1.pack(side="right", fill="y")
# yview is vertical orientation
scrollbar1.configure(command=text1.yview)
# yscrollcommand is vertical scroll
text1.configure(yscrollcommand=scrollbar1.set)


# Second combo for the application
combo2 = ttk.Combobox(root, values=languagev, font="Roboto 14", state="r")
# Location of the second combo
combo2.place(x=730, y=20)
# The default "Select Languages" combi is displayed
combo2.set("Select Languages")

# create the label for the second language
Label2 = Label(root, text="Spanish", font="segoe 30 bold", bg="white", width=18, bd=5, relief="groove")
Label2.place(x=620, y=50)

# create the drawer for the text content to be entered
f2 = Frame(root, bg="Black", bd=5)
f2.place(x=620, y=118, width=440, height=210)

# create the option to allow text input in the frame
text2 = Text(f2, font="Robote 20" ,bg="white", relief="groove", wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f2)
#vertical packaging
scrollbar2.pack(side="right", fill="y")
# yview is vertical orientation
scrollbar2.configure(command=text2.yview)
# yscrollcommand is vertical scroll
text2.configure(yscrollcommand=scrollbar2.set)

# The button is created and when clicked it changes the tone and invokes the traslate_now method.
traslate = Button(root, text="Traslate", font=("Roboto", 15), activebackground="white", cursor="hand2", bd=1, width=10, height=2, bg="black", fg="white", command=traslate_now).place(x=476, y=250)


 

# Invoke label_change method
label_change()


# Background color of the window
root.configure(bg="white")

#Infinite cycle for the window display
root.mainloop()

