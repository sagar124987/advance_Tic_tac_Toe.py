import tkinter.messagebox
from tkinter import *
root = Tk()
root.geometry('1350x750+0+0')
root.title('Tic Tac Toe')
root.configure(background = 'Cadet Blue')

Tops = Frame(root, bg = 'Cadet Blue', pady = 2, width = 1350, height = 100, relief = RIDGE)
Tops.grid(row = 0, column = 0)

lblTitle = Label(Tops, font = ('arial', 50, 'bold'), text = 'Advance Tic Tac Toe Game', bd = 21, bg = 'Cadet Blue', fg = 'Cornsilk', justify = CENTER)
lblTitle.grid(row = 0, column = 0)

MainFrame = Frame(root, bg = 'Powder Blue', pady = 2, width = 1350, height = 600, relief = RIDGE)
MainFrame.grid(row = 1, column = 0)

LeftFrame = Frame(MainFrame, bd = 10, width = 560, height = 500, padx = 10, pady = 2, bg = 'Cadet Blue', relief = RIDGE)
LeftFrame.pack(side = LEFT)

RightFrame = Frame(MainFrame, bd = 10, width = 560, height = 500, padx = 10, pady = 2, bg = 'Cadet Blue', relief = RIDGE)
RightFrame.pack(side = RIGHT)

RightFrame1 = Frame(RightFrame, bd = 10, width = 560, height = 200, padx = 10, pady = 2, bg = 'Cadet Blue', relief = RIDGE)
RightFrame1.grid(row = 0, column = 0)

RightFrame2 = Frame(RightFrame, bd = 10, width = 560, height = 200, padx = 10, pady = 2, bg = 'Cadet Blue', relief = RIDGE)
RightFrame2.grid(row = 1, column = 0)

PlayerX = IntVar()
Player0 = IntVar()

PlayerX.set(0)
Player0.set(0)

buttons = StringVar()
click = True

def checker(buttons):
    global click
    if buttons['text'] == ' ' and click == True:
        buttons['text'] = 'x'
        click = False
        score()
    elif buttons['text'] == ' ' and click == False:
        buttons['text'] = '0'
        click = True
        score()
        
def score():
    if (button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x'):
        button1.configure(background = 'powder blue')
        button2.configure(background = 'powder blue')
        button3.configure(background = 'powder blue')
        
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X Wins")
        
            
    if (button4['text'] == 'x' and button5['text'] == 'x' and button6['text'] == 'x'):
        button4.configure(background = 'Red')
        button5.configure(background = 'Red')
        button6.configure(background = 'Red')
        
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X Wins")
        
    if (button7['text'] == 'x' and button8['text'] == 'x' and button9['text'] == 'x'):
        button1.configure(background = 'powder blue')
        button2.configure(background = 'powder blue')
        button3.configure(background = 'powder blue')
        
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X Wins")
        
            
    if (button1['text'] == 'x' and button4['text'] == 'x' and button7['text'] == 'x'):
        button1.configure(background = 'Red')
        button4.configure(background = 'Red')
        button7.configure(background = 'Red')
        
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X Wins")
    if (button2['text'] == 'x' and button5['text'] == 'x' and button7['text'] == 'x'):
        button2.configure(background = 'powder blue')
        button5.configure(background = 'powder blue')
        button7.configure(background = 'powder blue')
        
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X Wins")
        
            
    if (button3['text'] == 'x' and button6['text'] == 'x' and button9['text'] == 'x'):
        button3.configure(background = 'Red')
        button6.configure(background = 'Red')
        button9.configure(background = 'Red')
        
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X Wins")    
    if (button1['text'] == 'x' and button5['text'] == 'x' and button9['text'] == 'x'):
        button1.configure(background = 'powder blue')
        button5.configure(background = 'powder blue')
        button9.configure(background = 'powder blue')
        
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X Wins")
        
            
    if (button3['text'] == 'x' and button5['text'] == 'x' and button7['text'] == 'x'):
        button3.configure(background = 'Red')
        button5.configure(background = 'Red')
        button7.configure(background = 'Red')
        
        n = int(PlayerX.get())
        score = n+1
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X Wins")
        
    if (button1['text'] == '0' and button2['text'] == '0' and button3['text'] == '0'):
        button1.configure(background = 'Orange')
        button2.configure(background = 'Orange')
        button3.configure(background = 'Orange')
        
        n = int(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0","Player 0 Wins")
        
            
    if (button4['text'] == '0' and button5['text'] == '0' and button6['text'] == '0'):
        button4.configure(background = 'blue')
        button5.configure(background = 'blue')
        button6.configure(background = 'blue')
        
        n = int(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0","Player 0 Wins")
        
    if (button7['text'] == '0' and button8['text'] == '0' and button9['text'] == '0'):
        button1.configure(background = 'Green')
        button2.configure(background = 'Green')
        button3.configure(background = 'Green')
        
        n = int(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0","Player 0 Wins")
        
            
    if (button1['text'] == '0' and button4['text'] == '0' and button7['text'] == '0'):
        button1.configure(background = 'cadet blue')
        button4.configure(background = 'cadet blue')
        button7.configure(background = 'cadet blue')
        
        n = int(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0","Player 0 Wins")
    if (button2['text'] == '0' and button5['text'] == '0' and button7['text'] == '0'):
        button2.configure(background = 'blue')
        button5.configure(background = 'blue')
        button7.configure(background = 'blue')
        
        n = int(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0","Player 0 Wins")
        
            
    if (button3['text'] == '0' and button6['text'] == '0' and button9['text'] == '0'):
        button3.configure(background = 'Red')
        button6.configure(background = 'Red')
        button9.configure(background = 'Red')
        
        n = int(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0","Player 0 Wins")    
    if (button1['text'] == '0' and button5['text'] == '0' and button9['text'] == '0'):
        button1.configure(background = 'powder blue')
        button5.configure(background = 'powder blue')
        button9.configure(background = 'powder blue')
        
        n = int(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner 0","Player 0 Wins")
        
            
    if (button3['text'] == '0' and button5['text'] == '0' and button7['text'] == '0'):
        button3.configure(background = 'Red')
        button5.configure(background = 'Red')
        button7.configure(background = 'Red')
        
        n = int(Player0.get())
        score = n+1
        Player0.set(score)
        tkinter.messagebox.showinfo("Winner X","Player X Wins")
def reset():
    button1['text'] = ' '
    button2['text'] = ' '
    button3['text'] = ' '
    button4['text'] = ' '
    button5['text'] = ' '
    button6['text'] = ' '
    button7['text'] = ' '
    button8['text'] = ' '
    button9['text'] = ' '
    
    button1.configure(background = 'gainsboro')
    button2.configure(background = 'gainsboro')
    button3.configure(background = 'gainsboro')
    button4.configure(background = 'gainsboro')
    button5.configure(background = 'gainsboro')
    button6.configure(background = 'gainsboro')
    button7.configure(background = 'gainsboro')
    button8.configure(background = 'gainsboro')
    button9.configure(background = 'gainsboro')
    
def NewGame():
    reset()
    PlayerX.set(0)
    Player0.set(0)

lblPlayerX = Label(RightFrame1, font = ('arial', 40, 'bold'), text = 'Player X :', padx = 2, pady = 2, bg = 'Cadet Blue')
lblPlayerX.grid(row = 0, column = 0, sticky = W)
txtPlayerX = Entry(RightFrame, font = ('arial', 40, 'bold'), bd = 2, fg = 'black', textvariable = PlayerX, width = 14, justify = LEFT).grid(row = 0, column = 1)

lblPlayer0 = Label(RightFrame1, font = ('arial', 40, 'bold'), text = 'Player 0 :', padx = 2, pady = 2, bg = 'Cadet Blue')
lblPlayer0.grid(row = 1, column = 0, sticky = W)
txtPlayer0 = Entry(RightFrame, font = ('arial', 40, 'bold'), bd = 2, fg = 'black', textvariable = Player0, width = 14, justify = LEFT).grid(row = 1, column = 1)

btnReset = Button(RightFrame2, text = 'Reset', font = ('Times 26 bold'), height = 3, width = 20, bg = 'gainsboro', command = reset)
btnReset.grid(row = 0, column = 0)

btnNewGame = Button(RightFrame2, text = 'New Game', font = ('Times 26 bold'), height = 3, width = 20, bg = 'gainsboro', command = NewGame)
btnNewGame.grid(row = 1, column = 0)



button1 = Button(LeftFrame, text = ' ', font = ('Times 26 bold'), height = 3, width = 8, bg = 'gainsboro', command = lambda:checker(button1))
button1.grid(row = 1, column = 0, sticky = S+N+E+W)

button2 = Button(LeftFrame, text = ' ', font = ('Times 26 bold'), height = 3, width = 8, bg = 'gainsboro', command = lambda:checker(button2))
button2.grid(row = 1, column = 1, sticky = S+N+E+W)

button3 = Button(LeftFrame, text = ' ', font = ('Times 26 bold'), height = 3, width = 8, bg = 'gainsboro', command = lambda:checker(button3))
button3.grid(row = 1, column = 2, sticky = S+N+E+W)

button4 = Button(LeftFrame, text = ' ', font = ('Times 26 bold'), height = 3, width = 8, bg = 'gainsboro', command = lambda:checker(button4))
button4.grid(row = 2, column = 0, sticky = S+N+E+W)

button5 = Button(LeftFrame, text = ' ', font = ('Times 26 bold'), height = 3, width = 8, bg = 'gainsboro', command = lambda:checker(button5))
button5.grid(row = 2, column = 1, sticky = S+N+E+W)

button6 = Button(LeftFrame, text = ' ', font = ('Times 26 bold'), height = 3, width = 8, bg = 'gainsboro', command = lambda:checker(button6))
button6.grid(row = 2, column = 2, sticky = S+N+E+W)

button7 = Button(LeftFrame, text = ' ', font = ('Times 26 bold'), height = 3, width = 8, bg = 'gainsboro', command = lambda:checker(button7))
button7.grid(row = 3, column = 0, sticky = S+N+E+W)

button8 = Button(LeftFrame, text = ' ', font = ('Times 26 bold'), height = 3, width = 8, bg = 'gainsboro', command = lambda:checker(button8))
button8.grid(row = 3, column = 1, sticky = S+N+E+W)

button9 = Button(LeftFrame, text = ' ', font = ('Times 26 bold'), height = 3, width = 8, bg = 'gainsboro', command = lambda:checker(button9))
button9.grid(row = 3, column = 2, sticky = S+N+E+W)

root.mainloop()
