#!/usr/bin/python

import re
import tkinter as tk

def count():
    
    textin= inputText.get("1.0","end-1c")

    #array of all words
    uneditedWords = textin.split()
    regex = re.compile(r'[^-a-zA-Z0-9]', re.IGNORECASE)
    
    editedWords = []
    #arrange strings
    for word in uneditedWords:
        w = regex.sub('', word)
        editedWords.append(w)
        print(w)

    print('\n\n\n')
    #counting strings
    frequency = {}
    
    for w in editedWords:
        i = 1
        match = False

        for key in frequency:
            if w.casefold() == key:
                match = True
        if(match):
            frequency[w.casefold()] += 1
        else:
            frequency.update({w.casefold() : i})

    #sorting list
    for x in sorted(frequency.keys()):
        print('%s: %s' % (x, frequency[x]))
    
    #putting dict in a string for msg
    s = ''
    for x in sorted(frequency.keys()):
        s += '%s: %s\n' % (x, frequency[x])

    #show in window

    entry = tk.Entry(root, textvariable=s, state='readonly')
    myscroll = tk.Scrollbar(root, orient='vertical', command=entry.xview)
    entry.config(xscrollcommand=myscroll.set)
    msg = tk.Message(root, text = s, width=250)
    msg.pack()
    msg.place(x=400, y=50)


def initGui():
    w = 700 # width for the Tk root
    h = 550 # height for the Tk root

    global root
    root = tk.Tk()

    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    
    root.title('WordCount')
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    #root.configure(bg='#9EA8B1')

    #in title
    inTitle = tk.Label(text="Input Text")
    inTitle.place(x=150, y=20)
    
    #text area
    global inputText
    inputText = tk.Text(root, width=40, height=30)
    inputText.place(x=20, y=50)

    #button
    but = tk.Button(root, text="Count", command=count)
    but.pack()
    but.place(x=325, y=20)

    #out title
    outTitle = tk.Label(text="Frequency of words")
    outTitle.place(x=475, y=20)

    

    root.mainloop()



#Main
def main():
    initGui()

# Main
#    
if __name__ == "__main__":

    main()
