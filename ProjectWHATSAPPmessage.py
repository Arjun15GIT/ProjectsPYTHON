# PROJECT TO SEND AUTOMATE MESSAGES ON WHATSAPP USING "Pywhatkit"

# message will be sent and delivered automatically by python script

'''
install module Pywhatkit using
"pip install pywhatkit"
'''


''' 
pywhatkit module provides a function 
which helps us to send messages 
function as 4 parameters
('number to which we want to send message(with country code)','message to be sent',hours,minutes)
'''

import pywhatkit as pyw
pyw.sendwhatmsg('+91XXXXXXXXXX','message to be delievered',22,35)
