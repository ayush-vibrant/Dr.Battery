import notify2 
import battery as b
  
# path to notification icon 
ICON_PATH = '/home/ayush/Desktop/Dr.Battery/battery2.jpg'

notify2.uninit()

# initialise the d-bus connection 
notify2.init("Dr.Battery!!") 
  
# create Notification object 
n = notify2.Notification(None, icon = ICON_PATH) 

# set urgency level 
n.set_urgency(notify2.URGENCY_CRITICAL) 
  
# set timeout for a notification 
n.set_timeout(1000) 

n.update(b.message)
n.show()
n.close()

 
