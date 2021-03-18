import cv2

img= cv2.imread("galaxy.jpg", 0)

#Imprime el tipo que es img
print(type(img))
#imprime el valor de img
print(img)
#imprime el tañano de la forva px x px
print(img.shape)
#imprime el numero de dimensiones de img
print(img.ndim)

#Para mostrar la imagen en una ventana
cv2.imshow("Galaxy", img) #Dos parametros, el nombre para mostrar en la ventana, la imagen a mostrar
#indica cuando cerrar la ventana
cv2.waitKey(0) #ya sea presionando una tecla o indicando el tiempo de espera ej. 2000
cv2.destroyAllWindows()

#Redimensionando la imagen
resized_image= cv2.resize(img, (500,1000))
#Redimensionando conservando relacion respecto imagen
resized_image2=cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Red", resized_image)
cv2.imshow("relacion", resized_image2)
cv2.imwrite("Galaxy_resized.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
