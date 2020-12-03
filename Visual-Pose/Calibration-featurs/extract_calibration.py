import cv2

# fichier path and type
cv_file = cv2.FileStorage("calib_images/test.yaml", cv2.FILE_STORAGE_READ)

camera_matrix = cv_file.getNode("camera_matrix").mat()
dist_matrix = cv_file.getNode("dist_coeff").mat()

print("camera_matrix : ", camera_matrix.tolist())
print("dist_matrix : ", dist_matrix.tolist())

cv_file.release()
