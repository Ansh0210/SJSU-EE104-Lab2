from twilio.rest import Client

account_sid = 'Your account sid'  #this is your account SID
auth_token = 'your auth token'     #this is your own auth_token
client = Client(account_sid, auth_token)

message = """Subject: Second COVID-19 Vaccination Reminder

Hello {First} {Last} your second COVID 19 vaccination is coming up on 09/17/2022."""

FirstName = 'Shivansh'
LastName = 'Shukla'



message = client.messages.create(
                    body=message.format(
                        First=FirstName, Last=LastName
                        ),
                    from_="+18444050186", #this is your own Twilio number
                    to='+16692546847'  #this is your own phone number to receive the text msg
                    )

print(message.sid)