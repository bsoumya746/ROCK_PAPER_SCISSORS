from tkinter import *
from PIL import Image,ImageTk
from random import *


#main window
root=Tk()
root.title("ROCK_PAPER_SCISSOR")
root.configure(background="Black")

#picture
rock_img=ImageTk.PhotoImage(Image.open("user_stone.png"))
paper_img=ImageTk.PhotoImage(Image.open("user_paper.png"))
scissor_img=ImageTk.PhotoImage(Image.open("user_scissor.png"))
rock_img_com=ImageTk.PhotoImage(Image.open("com_stone.png"))
paper_img_com=ImageTk.PhotoImage(Image.open("com_paper.png"))
scissor_img_com=ImageTk.PhotoImage(Image.open("com_scissor.png"))

#insert picture
com_label=Label(root,image=scissor_img,bg="Black")
user_label=Label(root,image=scissor_img_com,bg="Black")
com_label.grid(row=1,column=4)
user_label.grid(row=1,column=0)

#scores
playerscore=Label(root,text=0,font="100",bg="Black",fg="White")
computerscore=Label(root,text=0,font="100",bg="Black",fg="White")
playerscore.grid(row=1,column=1)
computerscore.grid(row=1,column=3)

#indicator
user_indicator=Label(root,font="50",text="USER",bg="Black",fg="White")
com_indicator=Label(root,font="50",text="COMPUTER",bg="Black",fg="White")
user_indicator.grid(row=0,column=1)
com_indicator.grid(row=0,column=3)

#messages
msg=Label(root, font="100", bg="Black",fg="White")
msg.grid(row=3,column=2)


#update message
def upd_message(x):
    msg['text']=x

#update user score
def upd_us_scr():
    score=int(playerscore["text"])
    score=score+1
    playerscore["text"]=str(score)

#update computer score
def upd_com_scr():
    score=int(computerscore["text"])
    score=score+1
    computerscore["text"]=str(score)

#update choices
com_choices=["rock","paper","scissor"]
def choice(x):
    #for computer
    compchoice=com_choices[randint(0,2)]
    if compchoice == "rock":
        com_label.configure(image=rock_img_com)
    elif compchoice == "paper":
        com_label.configure(image=paper_img_com)
    elif compchoice == "scissor":
        com_label.configure(image=scissor_img_com)
    #for user   
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    elif x=="scissor":
        user_label.configure(image=scissor_img)
    
    chk_win(x,compchoice)

#check_Winner
def chk_win(player,computer):
    if player == computer:
        upd_message("Its a tie!!!!")
    elif player == "rock":
        if computer == "paper":
            upd_message("You loose!!!!")
            upd_com_scr()
        elif computer == "scissor":
            upd_message("You win!!!!")
            upd_us_scr()
    elif player == "paper":
        if computer == "rock":
            upd_message("You win!!!!")
            upd_us_scr()
        elif computer == "scissor":
            upd_message("You loose!!!!")
            upd_com_scr()
    elif player == "scissor":
        if computer == "rock":
            upd_message("You loose!!!!")
            upd_com_scr()
        elif computer == "paper":
            upd_message("You win!!!!")
            upd_us_scr()  
  

#buttons
rock=Button(root,width=20,height=2,text="ROCK",bg="Magenta",fg="White",command=lambda:choice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="Green",fg="White",command=lambda:choice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="Orange",fg="White",command=lambda:choice("scissor")).grid(row=2,column=3)


root.mainloop()