from tkinter import *
import random
questions = ["Is Libya part of the Arabic World?" ,"Is Argentina bigger than Brazil?" , "Is Croatia a part of the Balcan Peninsula?" , "Is Cambodia in Central Asia?" , "Is Hawaii in the Caribbean sea?" , "Is Hong Kong a sovereign state?" , "Is Nicaragua in South America?" , "Is Belarus in Europe?" , "Is Aruba a part of the ABC islands?" , "Is Iraq bigger than Iran?" , "Is Instabul the capital of Turkey?" , "Is Denmark a Scandinavian country?" , "Is Niger in Sub-Saharan Africa?" , "Is Jordan in Northern Africa?", "Is Saint Kitts and Nevis in the Pacific Ocean?" , "Is Albania a mostly christian county?" , "Is Romania a Slavic country?", "Is Uzbekistan in South East Asia?", "Is Portugal in the Iberian Peninsula?" , "Is Urugay landlocked?"]
done=[]
answers = [True , False , True , False , False , False , False ,True , True , False , False ,True , True , False ,False , False , False , False , True , True]
i=0
score=0
state=False
pick=0      
def run(x):
       global state, i , score , done , pick
       if (x=="START") and i==0:
              state=True
              pick = random.randrange(20)
              text.set(questions[pick])
              done.append(pick)
       if (state==True and x!="START"):
              if x==answers[pick]:
                     score=score+10
              if i<9:
                     pick = random.randrange(20)
                     while pick in done:
                            pick = random.randrange(20)
                     done.append(pick)
                     i=i+1
                     text.set(questions[pick])
              elif i==9:
                            score=str(score)
                            y= "Your score is " + score + "/100"
                            text.set(y)
                            state=False
                            
      
       
def clear():
       global state, i , score , pick
       global done
       pick=0
       done =[]
       state=False
       score=0
       i=0
       text.set("Start the quiz? (PRESS START)")
       

              
if __name__=="__main__":
       gui=Tk()
       gui.configure(background="purple")
       gui.geometry("1000x1000")
       gui.title("Quiz")
       text=StringVar()
       text.set("This is simple geography quiz with randomized questions. Press START to proceed.")
       box=Entry(gui, textvariable=text, font=(30))
       box.grid(columnspan=20, ipadx=750, ipady=100)
       yes=Button(gui, text="YES", fg="purple", bg="yellow", height=10, width=20, command=lambda: run(True))
       yes.grid(column=0, row=3)
       no=Button(gui, text="NO", fg="purple", bg="yellow", height=10, width=20, command=lambda: run(False))
       no.grid(column=1, row=3)
       reset=Button(gui, text="RESET", fg="purple", bg="yellow", height=10, width=20, command=lambda: clear() )
       reset.grid(column=2, row=3)
       start=Button(gui, text="START", fg="purple", bg="yellow", height=10, width=20, command=lambda: run("START") )
       start.grid(column=3, row=3) 

gui.mainloop()
