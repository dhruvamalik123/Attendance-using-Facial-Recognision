import cv2
import speech_recognition as sr
import pyttsx3
import numpy as np
result=""
answer="y"
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[1].id)
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)
while answer=="y" or answer=="Y":
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=1)
        engine.say("PLEASE SPEAK YOUR NAME , LOUD, AND , CLEARLY  ")
        engine.runAndWait()
        audio = r.listen(source, timeout=5)
    
    try:
        
        Name=r.recognize_google(audio);
        engine.say("Your Name is ,"+Name);
        engine.runAndWait();
        result="yes";
    except:
        engine.say("Sorry,we could not get your name  ");
        engine.runAndWait();
        pass;
    

    if result=="yes":
        engine.say("Your photo will  be clicked in 2 seconds,So postion yourself before the camera")
        engine.runAndWait()
        cap = cv2.VideoCapture(0)
        seconds = 2

        millis = seconds * 1000
        while (millis > 0):
           ret, frame = cap.read()
           millis = millis - 10
           cv2.imshow('video recording', frame)

           if cv2.waitKey(10) & 0xFF == ord('q'):               
               break


        img_name = "C:\\Users\\dhruva malik\\Documents\\Project\\Present\\"+Name+".jpg"
        cv2.imwrite(img_name, frame)
        cv2.destroyAllWindows()
        engine.say("Clicked")
        print("Photo clicked and saved successfully")
        engine.runAndWait()
        answer=input("Run Again (y/n ) : ")

