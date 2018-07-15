from datetime import datetime
import time
import random

odds =[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]

right_in_time = datetime.today().minute
i=0
for i in range(5):
    if right_in_time in odds:
       # print(datetime.today())
        print("this is odd time" , right_in_time)
    else:
        print("even time" , right_in_time)
    wait_time=random.randint(1,10)
    i=i+1
    if (i!=5):
        time.sleep(wait_time)
        print("this is wait time-----", wait_time)



