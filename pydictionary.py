import requests
from tkinter import *
from tkinter import messagebox

root = Tk()

#modify root window
root.title("pyDictionary")
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
    print(textEntry.get())
    userWord = textEntry.get().lower()
    checkWord(userWord)

#checks word validity and prints the index, max of 3 definitions
def checkWord(recievedWord):
    textOutput.delete('1.0', END)

    payload = {'sp' : recievedWord, 'md' : 'd'}
    r = requests.get('https://api.datamuse.com/words', params=payload)
    apiReturn = r.json()[0]['word']

    if recievedWord == apiReturn:
        print("Word exists within the API.")
        indexSize = len(r.json()[0]['defs'])
        print(indexSize)
        i = 0;
        while indexSize >= 0:
            textOutput.insert('1.0', r.json()[0]['defs'][i] + '\n')
            if indexSize == 0:
                break
            elif indexSize == 1:
                break
            elif i == 2:
                break
            i += 1

    #Error message in case of word not being recognized or being unable to connect to server
    else:
        print('Error')
        messagebox.showinfo('Error', 'Please check your connection or ' + recievedWord + ' is a valid word.')


button = Button(app, text = "Lookup", command = retrieveUserInput)
button.grid()

#initialize the event loop
root.mainloop()