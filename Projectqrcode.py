# TO MAKE A QR CODE USING PYTHON
import qrcode as qr #using as alias(pet name)

#give url of the link
img = qr.make("https://www.linkedin.com/in/arjun-singh-3395691b1?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")  #give url of the link

#saves the image in png formate
img.save("Linkedin_ArjunSingh.png")


#SECONDARY CODE FOR CHANGING FUNCTIONALITIES OF QR CODE
'''
import qrcode
from PIL import Image    #used in formatting of image

#changing background colour
qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size= 10,border=10,)

#QRcode is a function in PIL module which is used for changing functionalaity of qrcode
qr.add_data("https://www.instagram.com/indiancricketteam?igsh=MjdqYmx5N3Fnb3h4") 
qr.make(fit=True)

img = qr.make_image(fill_color = "red",back_color = "blue")
img.save("InstaINDIANcricketTEAM.png")
'''