# import module
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pyttsx3
import pymysql
from PIL import ImageTk,Image,ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from connection import *
from tkinter import messagebox

def face_recognitions_main():
    # messagebox.showinfo("showinfo","Please Wait Until We Setup Every Thing")

    # Function used for fetching all photos from database
    def get_all_photos():
        path = 'images'
        images = []
        classNames = []
        myList = os.listdir(path)

        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])

        cur=connection()
        cur.execute("Select * from student_details")
        rows = cur.fetchall()
        # print(len(rows))

        for i in range(0,len(rows)):
            if str(rows[i][0]) not in classNames:
                rec_data=rows[i][7]
                with open(f'images/{rows[i][0]}.jpg','wb') as f:
                    f.write(rec_data)

        # messagebox.showinfo("showinfo","Wait we are encoding the images !")

    get_all_photos()
    # print("all done")
    path = 'images'
    images = []
    classNames = []
    myList = os.listdir(path)

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    
    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markAttendance(name):
        now = datetime.now()

        con = pymysql.connect(host="localhost", user="root",password="", database="stm")
        cur = con.cursor()
        cur.execute("select registration_number from attendance_details where date=%s",(now.date()))
        rows = cur.fetchall() 
        lst=[]
        for row in rows:
            lst.append(row[0])
        
        if name not in lst:
            cur.execute(("insert attendance_details set  registration_number=%s, attandance=%s , date=%s "),(name,'Present',now.date()))
            con.commit()
            talk('Hello '+name+' your attendance is noted')

    # Updating students attendance in database
    def markAbsentAttendence():
        now = datetime.now()
        con = pymysql.connect(host="localhost", user="root",password="", database="stm")
        cur = con.cursor()
        cur.execute("select registration_number from attendance_details where date=%s",(now.date()))
        presentRegNos = cur.fetchall() 
        cur.execute("select registration_number from student_details")
        allRegNos = cur.fetchall() 
        lst=[]
        for no in presentRegNos:
            lst.append(no[0])

        for regNo in allRegNos:
            if str(regNo[0]) not in lst:
                cur.execute(("insert attendance_details set  registration_number=%s, attandance=%s , date=%s "),(regNo[0],'Absent',now.date()))
                con.commit()

    def talk(text):
        engine.say(text)
        engine.runAndWait()   
    
        get_all_photos()
  
  
    encodeListKnown = findEncodings(images)
    print(len(encodeListKnown))
    print('Encoding Complete')

    # messagebox.showinfo("showinfo","All Set To use !")
    
    cap = cv2.VideoCapture(0)
    
    while True:
        success, img = cap.read()
        # imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
    
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            #print(faceDis)
            matchIndex = np.argmin(faceDis)
    
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                #print(name)
                y1,x2,y2,x1 = faceLoc
                # y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                markAttendance(name)
                
        cv2.imshow('Attendence Camera',img)
        cv2.waitKey(1)
        if cv2.getWindowProperty('Attendence Camera', cv2.WND_PROP_VISIBLE) <1:
            break

    cv2.destroyAllWindows()
    cap.release()
    markAbsentAttendence()

# face_recognitions_main()