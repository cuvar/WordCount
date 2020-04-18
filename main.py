#!/usr/bin/python

#https://www.tutorialspoint.com/python/python_gui_programming.htm

import tkinter as tk


def initGui():
    w = 600 # width for the Tk root
    h = 500 # height for the Tk root

    root = tk.Tk()

    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    
    root.title('WordCount')
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(0, 0)
    #root.configure(bg='#9EA8B1')

    inTitle = tk.Label(text="Input Text")
    inTitle.place(x=100, y=20)

    outTitle = tk.Label(text="Quantity of words")
    outTitle.place(x=400, y=20)

    inputText = tk.Text(root, width=80, height=20)
    inputText.place(x=20, y=50)

    #input text
    #click button
    #output text

    root.mainloop()



#Main
def main():
    initGui()


# Main
#    
if __name__ == "__main__":
    main()
