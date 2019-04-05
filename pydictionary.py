import requests
from tkinter import *
from tkinter import messagebox

root = Tk()

#modify root window
root.title("Simple Dictionary")
root.geometry("330x200")

app = Frame(root)
app.grid()

label = Label(app, text = "Lookup: ")
label.grid()

textEntry = Entry(app)
textEntry.grid()

textOutput = Text(app, height=8, width=40)
textOutput.grid()


def retrieveUserInput():
#    textOutput.delete('1.0')
 #   textOutput.update()
    print(textEntry.get())
    userWord = textEntry.get().lower()
    checkWord(userWord)

def checkWord(recievedWord):
    payload = {'sp' : recievedWord, 'md' : 'd'}
    r = requests.get('https://api.datamuse.com/words', params=payload)
    apiReturn = r.json()[0]['word']

    if recievedWord == apiReturn:
        print("Good")
        definiton = r.json()[0]['defs'][0]
        textOutput.insert('1.0', definiton)
        
    else:
        print('Error')
        messagebox.showinfo('Error', 'Please check your connection or ' + recievedWord + ' is a valid word.')


button = Button(app, text = "Lookup", command = retrieveUserInput)
button.grid()

#initialize the event loop
root.mainloop()

#todo
#fix error handeling
#fix ui layout