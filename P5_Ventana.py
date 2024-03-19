# -*- coding: utf-8 -*-
"""
Este script procesa una imagen para realizar tres tareas.
1. Convertir la imagen a binario, pasandola por un clasificador. 
2. Etiquetar objetos en la imagen etiquetando la imagen del clasificador. 
3. Localizacion de ventanas en los objetos etiquetados similares en las regiones. 

Vision artificial Marzo 2024 
Primer parcial Practica V

@author: Dea Angel
"""


import cv2
import numpy as np

#______________________CLASIFICADOR_________________________________
imagen = cv2.imread("mariposa.jpg")
m, n, c = imagen.shape
imagenb = np.zeros((m, n))
cv2.imwrite("imagenz.jpg", imagenb)
for x in range(m):
    for y in range(n):
        if (28 < imagen[x, y, 0] < 244) and (9 < imagen[x, y, 1] < 234) and (31 < imagen[x, y, 2] < 252):
            imagenb[x, y] = 255
                

imagen_clasificada = cv2.resize(imagenb, (400,350))

#__________________________________________LABELING
def labeling(imagen):
    m, n = imagen.shape
    etiquetas = np.zeros_like(imagen, dtype=int)
    etiqueta_actual = 1
    colores = {}
    rectangulos = {}
    for i in range(m):
        for j in range(n):
            if imagen[i, j] == 255 and etiquetas[i, j] == 0:
                etiquetas, x1, y1, x2, y2 = etiquetar_region(imagen, etiquetas, i, j, etiqueta_actual)
                color = np.random.randint(0, 256, 3)
                colores[etiqueta_actual] = color
                rectangulos[etiqueta_actual] = (x1, y1, x2, y2)
                etiqueta_actual += 1
                
    return etiquetas, colores, rectangulos

def etiquetar_region(imagen, etiquetas, i, j, etiqueta_actual):
    m, n = imagen.shape
    etiquetas[i, j] = etiqueta_actual
    x1, y1, x2, y2 = j, i, j, i
    
    direcciones = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1),           (0, 1),
                   (1, -1),  (1, 0),  (1, 1)]
    
    for dx, dy in direcciones:
        ni, nj = i + dx, j + dy
       
        if 0 <= ni < m and 0 <= nj < n and imagen[ni, nj] == 255 and etiquetas[ni, nj] == 0:
            etiquetas, rx1, ry1, rx2, ry2 = etiquetar_region(imagen, etiquetas, ni, nj, etiqueta_actual)
            x1 = min(x1, rx1)
            y1 = min(y1, ry1)
            x2 = max(x2, rx2)
            y2 = max(y2, ry2)
            
    return etiquetas, x1, y1, x2, y2

etiquetas, colores, rectangulos = labeling(imagen_clasificada)

etiquetas_rgb = np.zeros((etiquetas.shape[0], etiquetas.shape[1], 3), dtype=np.uint8)
for etiqueta, color in colores.items():
    etiquetas_rgb[etiquetas == etiqueta] = color

imagen_con_rectangulos = np.copy(etiquetas_rgb)
for etiqueta, rectangulo in rectangulos.items():
    x1, y1, x2, y2 = rectangulo
    cv2.rectangle(imagen_con_rectangulos, (x1, y1), (x2, y2), (255, 255, 255), 1)


imagen_etiquetada = np.copy(etiquetas_rgb)
for etiqueta, color in colores.items():
    region_indices = np.where(etiquetas == etiqueta)
    x_center = int(np.mean(region_indices[1]))
    y_center = int(np.mean(region_indices[0]))
   
    x_center += 20  
    y_center += 20 
    etiqueta_texto = str(etiqueta)
    cv2.putText(imagen_etiquetada, etiqueta_texto, (x_center, y_center), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    
cv2.imshow('Clasificada', imagen_clasificada)
cv2.imwrite("clasificada.jpg",  imagen_clasificada)
    
original = cv2.resize(imagen, (400,350))
cv2.imshow('Original', original)
cv2.imshow('Etiquetaje', imagen_etiquetada)
cv2.imwrite("Etiquetaje.jpg", imagen_etiquetada)
cv2.imshow('Localizacion', imagen_con_rectangulos)
cv2.imwrite("Localizacion.jpg", imagen_con_rectangulos)

cv2.waitKey(0)
cv2.destroyAllWindows()
