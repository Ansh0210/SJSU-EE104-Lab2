#Make sure you pip install yagmail
import yagmail

from_address = 'ee104lab2py@gmail.com' #this is your own gmail account
app_password = 'ifstoktgoljeaedj' # a token for gmail, this is the app password from Gmail Security
to_address = 'ee104Lab2py@gmail.com'   #send test to another email or the same email is OK

subject = 'Test sending email using yagmail'  #modify the subject line anyway you like
content = ['Hello EE104ers, this is a test message','cat.jpg','test.png', 'Ironman.jpeg']  #you can have different email and attachment

with yagmail.SMTP(from_address, app_password) as yag:
    yag.send(to_address, subject, content)
    print('Email is Successfully sent')  #you can have different success message
    