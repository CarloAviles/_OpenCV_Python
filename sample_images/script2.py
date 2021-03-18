#Programa que lee un directorio con archivos de imagen, transforma su tamaño y lo guarda en nuevo archivo
import cv2
import glob

imagenes =  glob.glob("*.jpg")

for imagen in imagenes:
    img = cv2.imread(imagen,0)
    resized_imagen= cv2.resize(img, (100,100))
    cv2.imshow("Try", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("./sample_images/resized_" + imagen, resized_imagen)
    
    
    
    
  