import csv
import time
import datetime
import requests
import threading
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#########store data
def one():    
    while True:
        value = []
        time.sleep(1)
        URL = "https://allsafe.in/"
        try:
            page = requests.get(URL)
            filename = "real-time.csv"
            value.append(page.status_code)
        except:
            value.append(500)
            
        time_stamp = datetime.datetime.now()
        time_stamp = time_stamp.strftime(" %H:%M:%S")
        col = [time_stamp]
        col.extend(value)
        df = pd.DataFrame(col)
        df = df.T
        df.to_csv('real time value.csv',mode='a',header = False)
        print(col)
        
            


##################plot show
def two():
    style.use('fivethirtyeight')
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)

    def animate(i):
        df = pd.read_csv('real time value.csv')
        ys = df.iloc[1: , 2].values
        xs = list(range(1, len(ys)+1))
        ax1.clear()
        ax1.plot(xs,ys)
        ax1.set_title('down or up', fontsize=12)


    plt.ani = animation.FuncAnimation(fig,animate,interval = 1000 )
    plt.tight_layout()
    plt.show()

#########################runing plot 

t1 = threading.Thread(target=one)  
t2 = threading.Thread(target=two)  

t1.start()
time.sleep(3)
t2.start()








