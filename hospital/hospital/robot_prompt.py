import time

def countdown(t): 
    # status = "deactivated"
    # if status == "activated" 
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')
    # status = "deactivated"
  
  
# input time in seconds
t = 15 # 15*60 seconds

#countdown(int(t))
'''
def hello():
    countdown(int(15*60))

hello()
'''
