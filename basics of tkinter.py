
# coding: utf-8

# In[55]:


from tkinter import *
import random
import time


# In[56]:


tk = Tk()
WIDTH = 800
HEIGHT = 900
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.configure(background='black')


# In[57]:


ball = canvas.create_oval(10,10,60,60, fill="yellow")
x = 1
y = 3
while True:
    canvas.move(ball, x,y)
    pos = canvas.coords(ball)
    if pos[3] >= HEIGHT or pos[1] <= 0:
        y = -y
        
    
    if pos[2] >= WIDTH or pos[0] <=0:
        x = -x
        
    tk.update()
    time.sleep(0.01)
tk.mainloop()

