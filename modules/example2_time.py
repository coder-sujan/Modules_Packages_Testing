#using time module

import time 


print("Please just wait for  3 secs....")
time.sleep(3) #pause program for 3 secs
print('Ok Done, ok your account has been created!!')


#Example: current time!
#show current time in seconds 
print('Whats the time now:', time.time())


#time for humans
current_time_now = time.ctime()
print("Time:", current_time_now)
