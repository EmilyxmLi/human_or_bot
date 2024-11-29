
#meow
print('Bot or Human? Lets figure it out!')
#ask user for the activity of bot or human
# to know when they're active
activity = float(input('When did you recieve\
 a response? (between 0-24)'))

#function to tell user they're talking to a bot
def	talking_with_bot():
    print('You were talking with a bot!')
    
 #function to tell user theyre talking to a human
def talking_with_human():
    print('You were talking with a human!')

if 2<= activity <=5:
    talking_with_bot()
    
else:
    response=float(input('How long did it \
take for you to recieve a response? (in seconds)'))
   
    if response< 9:
       talking_with_bot()
    
    else:
        words=float(input('How many words did you\
 recieve in their response?'))
        WPM = words/response
        if WPM <= 66:
            talking_with_human()
        else:
            typos=float(input('how many typos were in\
 the program?'))
            if typos>= 1:
                talking_with_human()
            else:
                print('Please ask the bot/human to perfrom \
the "eeooeotetto" test')
                test=float(input('How many t\'s were in \
their response?'))
                if test==3:
                    talking_with_human()
                else:
                    talking_with_bot()
        
            
    
        

    