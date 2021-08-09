import sqlite3
import time
import datetime
import requests
import threading
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
import matplotlib.animation as animation

conn = sqlite3.connect('AA_db.sqlite',check_same_thread=False)
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS experiments (ndate INTEGER, nval INTEGER)')
conn.commit()

#########store data
def one():
    while True:
        value = ()
        col  = ()
        time.sleep(1)
        URL = "https://allsafe.in/"
        try:
            page = requests.get(URL)
            value = page.status_code
        except:
            value = 500
        time_stamp = datetime.datetime.now()
        time_stamp = time_stamp.strftime(" %H:%M:%S")
        col = time_stamp
        value = str(value)
        cur.execute("INSERT INTO experiments VALUES (:nval,:ndate )",
			{    
				
				'nval':col,
                                'ndate':value

					
			})
			
        conn.commit()  
        #print(value)
        #print(col)
        


###################graph show
def three():
    style.use('fivethirtyeight')
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)

    def animate(i):
        con = sqlite3.connect("AA_db.sqlite")
        live_df = pd.read_sql_query("SELECT * from experiments", con)
        #print(live_df)
        df = live_df
        ys = df.iloc[0: , 1].values
        xs = list(range(1, len(ys)+1))
        ax1.clear()
        ax1.plot(xs,ys)
        ax1.set_title('down or up', fontsize=12)


    plt.ani = animation.FuncAnimation(fig,animate,interval = 1000 )
    plt.tight_layout()
    plt.show()

############################## 

t1 = threading.Thread(target=one)  
t2 = threading.Thread(target=three)  
t2.start()
time.sleep(3)
t1.start()





