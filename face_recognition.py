import ntpath
import os
import face_recognition
import cv2

def find_image(image) : 
    file_name = image
    lo = []
    for i in os.listdir(file_name) :
        try :
            a = ntpath.basename(r"{}".format(i))
            l = a.find('.')
            lo.append([a[0:l] , f"{file_name}\{a}"])
        except :
            print(None)
    return lo

def proceccing(image1) :
    name = 'Unknown'
    img1 = cv2.imread(image1)
    f1 = face_recognition.face_encodings(img1)[0]
    for i in find_image(r'< your location file >') :
        img2 = cv2.imread(i[1])
        f2 = face_recognition.face_encodings(img2)[0]
        an = face_recognition.compare_faces([f1] , f2)
        print(an)
        if an == [True] :
            print(i[0])
            name = i[0]
            for face_loc in face_recognition.face_locations(img1) :
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                print(y1, x2, y2, x1)
                cv2.putText(img1, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(img1, (x1, y1), (x2, y2), (0, 0, 200), 4)
                cv2.imshow('window 1' , img1)
            break

    cv2.waitKey(0)

proceccing(r'< your location file >')
            
    
