import numpy as np
import cv2
import cv2.aruco as aruco
import glob

cap = cv2.VideoCapture(0)

#-------------------Extraction of the the camera parameters---------------------#

cv_file = cv2.FileStorage("calib_images/test.yaml", cv2.FILE_STORAGE_READ)
mtx = cv_file.getNode("camera_matrix").mat()
dist= cv_file.getNode("dist_coeff").mat()

###------------------ ARUCO TRACKER ---------------------------##
while (True):                                                   #
    ret, frame = cap.read()                                     #
    # on frame operation                                        #
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)              #
                                                                #
    #  dictionaire aruco (selon le marcker)                     #
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)       #
                                                                #
    parameters = aruco.DetectorParameters_create()              #
    parameters.adaptiveThreshConstant = 10                      #
                                                                #
    # lists des ids et les coins apartenant a chaque ids        # 
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, 
                             aruco_dict, parameters=parameters) #
                                                                #
    # panel pour affichier le txt                               #
    font = cv2.FONT_HERSHEY_SIMPLEX                             #
                                                                #
   #si la list des ids est vide                                 #
    if np.all(ids != None):                                     #
                                                                #        
 # estimer la position de chaque marcker et renvoyer la valeur  #
 # rvec, tvec de la calibration de la camera                    #
        rvec, tvec ,_ = aruco.estimatePoseSingleMarkers(corners,
                                                0.05, mtx, dist)
########################################################################
                                                                       #
        for i in range(0, ids.size):                                   #
            # tracé les axes du marcker aruco                          #
            aruco.drawAxis(frame, mtx, dist, rvec[i], tvec[i], 0.1)    #
                                                                       #
        # tracé a caré autour du marcker                               #
        aruco.drawDetectedMarkers(frame, corners)                      #
                                                                       #
        # coordone en pixel centre du marqueur                         #
                                                                       #
        x = (corners[i-1][0][0][0] + corners[i-1][0][1][0] +  
             corners[i-1][0][2][0] + corners[i-1][0][3][0]) /4
             
        y = (corners[i-1][0][0][1] + corners[i-1][0][1][1] + 
             corners[i-1][0][2][1] + corners[i-1][0][3][1]) /4

        cv2.putText(frame,direction[0] +" and  "+ direction[1] ,
                         (0,100), font, 1, (0,255,0),2,cv2.LINE_AA)
        cv2.circle(frame, centre, radius, (255,0,0), 2)
    else :                                                      ########
        # no ids si aucun marcker trouvé                               #
        cv2.putText(frame, "No Ids", (0,64), font, 1, (0,255,0),2,cv2.LINE_AA)
                                                                       #
    ##################################################################
    
    # afficher la frame
    cv2.imshow('frame',frame)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



    
