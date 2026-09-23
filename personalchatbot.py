import datetime
import time
presenthour=datetime.datetime.now().hour
name=input("please enter your name:")
if 5<=presenthour<=11:
    print("good morning", name)
elif 11<=presenthour<=15:
    print("good afternoon", name)
elif 15<=presenthour<=20:
    print("good evening",name)
else:
    print("good night",name)

# create chatbot memory to responses
response={
    "hello":"hii, wlc to smart personal ai chat bot",
    "thanks":"how can i help you ",
    "how are you ":" i am good thanks for your concer , how are you doing",
    "good":"glad to hear that",
    "motivate me":"padhle bcz motivation is temp. but dicipline is permanent"
}

def responseofbot(userinput):
    userinput=userinput.lower()
    for eachkey in response:
        if eachkey in userinput:
            return response[eachkey]
    return("i am still learnig")

while True:
    userinput=input("please enter your question:")
    reply=responseofbot(userinput)
    print(reply)

    if "bye" in userinput.lower():
        print("bye")
        break