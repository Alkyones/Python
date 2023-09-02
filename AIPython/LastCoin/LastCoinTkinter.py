from tkinter import *
from tkinter import ttk




root = Tk()
root.geometry('900x900')
root.title('Last Coin')
root.configure(bg="DarkGreen")

def gameEnd():
    if int(coins_label["text"]) <= 0:
        print("game Ended") 

def TakeCoin():
    if coin_selected["values"] == "1":
        coins_label["text"] = eval(coins_label["text"] - 1)

    if coin_selected["values"] == "2":
        coins_label["text"] -= 2
    if coin_selected["values"] == "3":
        coins_label["text"] -= 3
def gameStart():
    if user_button["text"] == "Start":
        action_label["text"] = "Game started there is 25 coins on the table..."
        user_button.pack_forget()
        user_play_button.pack()
        coin_selected.pack(side=TOP, pady=40)

    


coins_label = Label(root,font=("Arial",56),bg='DarkGreen',fg='white',text="25")
coins_label.pack(side=TOP,pady=20)

coins_name_label = Label(root,font=("Arial",36),bg='DarkGreen',fg='white',text="Coins Left")
coins_name_label.pack(side=TOP)

action_frame= Frame(root,bg='DarkGreen')
action_frame.pack(side=BOTTOM,pady=120)

action_label = Label(action_frame,font=("Arial",18),bg='DarkGreen',fg='white',text="Click start button to start the game")
action_label.pack(side=TOP)

coin_select_frame = Frame(action_frame,bg='DarkGreen')
coin_select_frame.pack(side=TOP)

n = StringVar()
coin_selected = ttk.Combobox(coin_select_frame, width = 400,font=("Arial",28), textvariable = n)
coin_selected['values'] = ("1","2","3")
coin_selected.current(1)

user_button = Button(action_frame,background="white",height=3,width=900, fg="DarkGreen",font=("Arial",20), text='Start', command=gameStart)
user_play_button = Button(action_frame,background="white",height=3,width=900, fg="DarkGreen",font=("Arial",20), text='Take Coin', command=TakeCoin)

user_button.pack(side=BOTTOM)

root.mainloop()