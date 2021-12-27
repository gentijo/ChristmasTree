
import time
from XmasTree import XmasTree

#
# Wait 5 seconds, while printing a message to com port
# Makes it easier to send a soft reset to break out of main loop
#

for i in range(1,5):
    print ("Waiting...")
    time.sleep(1)

#Oh
XmasTree()