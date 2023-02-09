import tkinter as tk
import winsound
import os
# from pygame import mixer
from tkinter import messagebox
import pyttsx3


def sound():
    f = 3800
    d = 145
    winsound.Beep(f, d)


sc = tk.Tk()
l = 800
b = 590
i = 0
flag = 0
FONT="green"
sc.minsize(l, b)
sc.configure(bg="black")

user_texts = []  # collects the users chats records
alice_texts = [] # collects the bots chats records


t = tk.StringVar()
t.set("  ")





scroll = 0 # used for scroll button
dialogs = [] # stores the dialog in queue form
scroll_dialog = []


    
for i in range(20):
    scroll_dialog.append(" ")


def scroll_down():
    sound()
    global scroll
    if scroll < len(dialogs)-20 and scroll>=0:
        for i in range(20):
            scroll_dialog[i]=dialogs[i+scroll+1]
            block[i].set(scroll_dialog[i])
        scroll += 1
    else:
        scroll = len(dialogs)-20 - 2
        messagebox.showinfo("info", "chat end")
    print(scroll)


def scroll_up():
    sound()
    global scroll
    if scroll < len(dialogs)-20 and scroll >=-1:
        for i in range(20):
            scroll_dialog[i]=dialogs[i+scroll+1]
            block[i].set(scroll_dialog[i])
        scroll -= 1
    else:
        scroll = 0+1
        messagebox.showinfo("info", "chat end")
    print(scroll)



def speak(txt):
    eng = pyttsx3.init()
    voice = eng.getProperty('voices')
    eng.setProperty('voice', voice[1].id)
    eng.say(txt)
    eng.runAndWait()
    eng.stop()
    pass


def alice(txt):
    t = txt.lower()
    if 'hello' in t:
        return "hi!  i am alice, what can i do for you?"
    elif 'your creator' in t:
        return "I am created by Shreya Chaturvedi"
    elif 'are you a human' in t:
        return "No! I am a chatbot helping you"
    elif 'what is your hobby' in t:
        return "Chatting with humans"
    elif 'your mood' in t:
        return "I am always happy & joyful"
    elif ('joke' in t) and ('another' not in t):
        return "What..did..the.... buffalo say when his son left for college? Bison.!"
    elif ('joke' in t) and ('another' in t):
        return "sorry...i have! only one joke, i will tell you later"
    elif "okay, can i collect the list of songs?" in alice_texts and t == 'yes':
        speak("here are the list of songs")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        for root, dirs, files in os.walk(dir_path):
	        for file in files:
                    i = 1
                    if file.endswith('.mp3'):
                        songs= (str(i)+file)
                        i+=1
                  
    elif 'music' in t or 'play' in t or 'song' in t:
        return "okay, can i collect the list of songs?"
    else:
        return  "sorry! i didn't understand that " 
        pass
    

def display(txt):
    # global reply
    # step -> 4 for displaying user's message on screen
    # step -> 8 for displaying alice's message on screen 
    if len(dialogs)<1:   # initiall insertion of dialog string
        dialogs.append(txt)
    else:   # stores the dialogs in the string in queue form
        j = 0
        s = len(dialogs)-1
        size = s
        dialogs.append(dialogs[s])
        while j<size: # this loop swaps the dialog form lower position to higher position
            dialogs[s]=dialogs[s-1]
            s = s-1
            j = j+1
        dialogs[0]=txt  # stores last dialog in 0 position of list
    for d in range(len(dialogs)):
        if d > 19:
            break
        else:
            block[d].set(dialogs[d])



# def alice(txt):     #  step -> 6 this is original alice which accept the user txt
#     user = txt.lower()
#     # step 7
#     if user == "hello" or user == "hii" or user == "hey":
#         reply = "hey i am ALICE what i can do for you?"
#     elif user == "play music" or user == "play song":
#         reply = "okay playing one song for you"
#     display(reply) # step 8
    
    
                
def send():
    sound() # produce sound
    user_texts.append(t.get().lower())
    # step -> 3
    display(t.get())   #display the reply of use...
    # step -> 5
    r = alice(t.get())
    alice_texts.append(r)
    speak(r) # voice of alice text after diplay
    display("Bot :-> "+r)
    # display(reply) # step 8
    # if 'play songs' in user_texts or 'play music' in user_texts:
        # if t.get().lower() == 'yes' or t.get().lower() == 'yea' or t.get().lower() == 'hmm':
        #     speak("here are the list of songs")
        #     dir_path = os.path.dirname(os.path.realpath(__file__))
        #     for root, dirs, files in os.walk(dir_path):
	    #         for file in files:
        #              i = 1
        #              if file.endswith('.mp3'):
        #                 display(str(i)+file)
    t.set("  ")
    








block=[]
for i in range(20):  # generate a space in list to store the messages in the form of queue to display it on screen
    block.append(" ")
    block[i]=tk.StringVar()
    block[i].set(" ")




block[0].set("hi there i am alice!")
t=tk.StringVar()
b19=tk.Label(sc,textvariable=block[19], bg="black", fg=FONT, font="comicsms 14 bold").grid(row=0, column=0)
b = tk.Button(sc, text="up  ", bg="blue", fg="white", font="comicsms 16 bold", command = scroll_up).grid(row=0, column=1)
b18=tk.Label(sc,textvariable=block[18], bg="black", fg="blue", font="comicsms 14 bold").grid(row=1, column=0)
b17=tk.Label(sc,textvariable=block[17], bg="black", fg=FONT, font="comicsms 14 bold").grid(row=2, column=0)
b16=tk.Label(sc,textvariable=block[16], bg="black", fg="blue", font="comicsms 14 bold").grid(row=3, column=0)
b15=tk.Label(sc,textvariable=block[15], bg="black", fg=FONT, font="comicsms 14 bold").grid(row=4, column=0)
b14=tk.Label(sc,textvariable=block[14], bg="black", fg="blue", font="comicsms 14 bold").grid(row=5, column=0)
b13=tk.Label(sc,textvariable=block[13], bg="black", fg=FONT, font="comicsms 14 bold").grid(row=6, column=0)
b12=tk.Label(sc,textvariable=block[12], bg="black", fg="blue", font="comicsms 14 bold").grid(row=7, column=0)
b11=tk.Label(sc,textvariable=block[11], bg="black", fg=FONT, font="comicsms 14 bold").grid(row=8, column=0)
b10=tk.Label(sc,textvariable=block[10], bg="black", fg="blue", font="comicsms 14 bold").grid(row=9, column=0)
b9=tk.Label(sc,textvariable=block[9], bg="black", fg=FONT, font="comicsms 14 bold").grid(row=10, column=0)
b8=tk.Label(sc,textvariable=block[8], bg="black", fg="blue", font="comicsms 14 bold").grid(row=11, column=0)
b7=tk.Label(sc,textvariable=block[7], bg="black", fg=FONT, font="comicsms 14 bold").grid(row=12, column=0)
b6=tk.Label(sc,textvariable=block[6], bg="black", fg="blue", font="comicsms 14 bold").grid(row=13, column=0)
b5=tk.Label(sc,textvariable=block[5], bg="black", fg=FONT, font="comicsms 14 bold").grid(row=14, column=0)
b4=tk.Label(sc,textvariable=block[4], bg="black", fg="blue", font="comicsms 14 bold").grid(row=15, column=0)
b3=tk.Label(sc,textvariable=block[3], bg="black", fg=FONT, font="comicsms 14 bold").grid(row=16, column=0)
b2=tk.Label(sc,textvariable=block[2], bg="black", fg="blue", font="comicsms 14 bold").grid(row=17, column=0)
b1=tk.Label(sc,textvariable=block[1], bg="black", fg=FONT, font="comicsms 14 bold").grid(row=18, column=0)
b0=tk.Label(sc,textvariable=block[0], bg="black", fg="blue", font="comicsms 14 bold").grid(row=19, column=0)

# text area for user
# step -> 1
e = tk.Entry(sc, textvariable=t, bg="white", fg="black", borderwidth=5,width=51,
            font="comicsms 19 bold").grid(row = 20, column = 0)


# send button
# step -> 2
send_buton = tk.Button(sc, text="send",  bg="green", fg="pink", 
                        font="comicsms 19 bold",command=send).grid(row=20, column=1)
  


b1 = tk.Button(sc, text="down", bg="blue", fg="white", 
                font="comicsms 16 bold", command=scroll_down).grid(row=18, column=1)




sc.mainloop()













