import face_recognition 

def Simple_Faces_Compare(target,biometric):#SFC
            target= face_recognition .load_image_file(target)
            lookup= face_recognition .load_image_file(biometric)
            target_encoding= face_recognition .face_encodings(target)
            lookup_encoding=  face_recognition .face_encodings(lookup)
            if(len(target_encoding)>0):target_encoding=target_encoding[0] 
            else:return 'No Face Found in image 1'
            if(len(lookup_encoding)>0):lookup_encoding=lookup_encoding[0]
            else:return 'No Face Found in image 2'
            return True if True in face_recognition.compare_faces([target_encoding],lookup_encoding) else False
       
def Foreced_Faces_Compare(biometrics,target):#FFC
        lookups=  face_recognition.load_image_file(biometrics)
        target= face_recognition.load_image_file(target)
        lookups_encoding=   face_recognition.face_encodings(lookups)
        target_encoding=  face_recognition.face_encodings(target)
        if(len(lookups_encoding)>0):pass
        else:return 'no Faces Found in image 1'
        if(len(target_encoding)>0):target_encoding=target_encoding[0]
        else:return 'no Face Found in image 2'
        return True if True in  face_recognition.compare_faces(lookups_encoding,target_encoding) else False
   

