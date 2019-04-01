
import random
#import datetime
#import webbrowser
import pyttsx3
#import wikipedia
#import speech_recognition as sr

################## set up bot speech with pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate -5)
#######################################################
############# predefined conversation patterns ########
greetings=['hello','hi','hey','hey!']
greetings_responses=['Was sup','yo!','Long time no see','Ahh! Its you again']
greeting_questions=['how are you doing?','how are you']
greeting_questions_responses=['I\'m Okay','Fine I guess','Not half bad','Ehh. can\'t complain']
joke_request=['tell me a joke','say something funny']
jokes=['Did you hear about the monkeys who shared an Amazon account? They were Primate mates','What do you call 8 hobbits? A hobbyte',
'Did you hear about the database admins who walked into a NoSql bar.Yah I didnt think so, since they left after not being able to find a table',
'Normally i like to tell computer jokes but heres a good one that not computer related. Why did the man put his money in the freezer? Because he wanted cold hard cash',
'why did the computer go to the doctor? Because it had a virus!']
farewell=['bye','good bye','goodbye','farewell','see yah','see you later']
farewell_response=['hasta la vista baby','ciao','sayonara','guten tag','see yah','bye']
other_Responses=['I didnt get that, so here is an 8 ball response. ']
eightball_response=['it is certain','without a doubt','most likely','Ask again later','Cannout predit now','Concentrate and ask again','Dont count on it','No','Outlook not so good']
########################################################
################get user text input and respond############
stop_listening = 0
user_input = input('Hi, enter anything to get started')
while True:
    # Note in computing capital letters are differnt from lower case letters
    # charchter a binary value is 0110 0001
    # charchter A binary value is 0100 0001
    # as you can imagine Hi will not result in same as HI or hi
    # therefore its perfered method to lower case input and what its being compared with
    # or uppercase both
    user_input = user_input.lower()
    if user_input in greetings:
        random_response = random.choice(greetings_responses)
    elif user_input in greeting_questions:
        random_response = random.choice(greeting_questions_responses)
    elif user_input in joke_request:
        random_response = random.choice(jokes)
    elif user_input  in farewell:
        random_response = random.choice(farewall)
        stop_listening = 1
    else:
        random_response = random.choice(other_Responses)
        random_response += random.choice(eightball_response)
    if stop_listening:
        break
    print(random_response)
    engine.say(random_response)
    engine.runAndWait()
    user_input = input('')
################################################################
# The implementation above is not intelligent by any means and is essentially a switch case handling diffrent possibilites
# assuming infinite storage capacity and ultra-fast processing speeds you could potentially hard code every possible case for discussion purposes
# that is if languages didnt evolve over time and you derive every possible pattern for every possible message
# simple to do, but lacks efficency, and the bigger the range of entries-responses created the slower it will become
#################################################################
# fun fact for those unfamilair the while true loop is common for speech/text system basically instructing the system to run forever or until its ordered to stop from within
# Just for visual sake imagine alexa and hey google : ignoring the specific instructions/algorthims designed to make the system more efficent, and/or faster
# on the outer level itll follow this schema
# while True:
#   speech = listen_microphone()
#   text = convert(speech) // filter out noise and collect known sounds to build language as text
#   if text == 'alexa' or ' hey google':
#       listen(speech)
#       text = convert(speech)
#       handle_Text_Request(text)
# where listen, conver, and handle_Text_Request are functions they created for procssin and handling user requests
################################################################################################################################
# scary possibility for systems of this dynamic that are always listening, is that while it might be set to only respond to you on set phrases as listed above if enabled
# to do so by a programmer,information on anything you say could be collected and processed
# For this reason its imperative that people exercise caution with systems of this dynamic especially if they are not from established(well-known) companies
