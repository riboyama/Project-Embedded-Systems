from UnoNetworking import UnoNetworkController
from random import randint
import time

controller = UnoNetworkController();

controller.connect()
#controller.rollOut(0)

print(controller.getTempThreshold());
while(1):
    msg = controller.waitForMessage();
    if(msg != None):
        print(msg)
       #     print(msg[1])
       # elif "light_is" in msg:
        #    print(msg[1])


