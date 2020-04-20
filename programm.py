#!/usr/bin/python

import re
import tkinter as tk

def count():
    textin= inputText.get("1.0","end-1c")

    #array of all words
    uneditedWords = textin.split()
    regex = re.compile(r"[^-a-zA-Z0-9]", re.IGNORECASE)

    editedWords = []
    #arrange strings
    for word in uneditedWords:
        w = regex.sub('', word)
        if(w== 'I\'m'):
            editedWords.append('I')
            editedWords.append('am')
        else:
            editedWords.append(w)
        #print(w)

    #print('\n\n\n')
    #counting strings
    
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

        root.update()
    






#Main
def main():
    global root
    global inputText
    global lb
    w = 700 # width for the Tk root
    h = 550 # height for the Tk root
    global frequency

    frequency = {}

    root = tk.Tk()

    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    
    root.title('WordCount')
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    #root.configure(bg='#9EA8B1')

    #titles
    inTitle = tk.Label(text="Input Text")
    inTitle.place(x=150, y=20)
    outTitle = tk.Label(text="Frequency of words")
    outTitle.place(x=475, y=20)

    #text area
    inputText = tk.Text(root, width=40, height=28)
    inputText.place(x=20, y=50)

    #button
    but = tk.Button(root, text="Count", command=count())
    but.pack()
    but.place(x=325, y=20)


    #adding frequencies of words
    frm = tk.Frame(root) 
    frm.place(x=400, y=50, width=150, height=300)

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    lb = tk.Listbox(root, yscrollcommand = scrollbar.set, height=50, width=50)

    if(frequency == {}):
        lb.insert(0, 'Please insert text!')
    else:
        #putting dict in a listbox
        i = 0
        for x in sorted(frequency.keys()):
            s = '%s: %s' % (x, frequency[x])
            lb.insert(i, s)
            i+=1

    lb.pack(side=tk.RIGHT, pady=50) 
    scrollbar.config(command = lb.yview)



    root.mainloop()

# Main
#    
if __name__ == "__main__":
    main()
