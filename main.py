#!/usr/bin/python

#https://www.tutorialspoint.com/python/python_gui_programming.htm

import tkinter as tk

def count():
    
    frequency_words = "Text"
    
    textin= inputText.get("1.0","end-1c")
    print(textin)


    #show in window
    msg = tk.Message(root, text = frequency_words, width=250)
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
