

# Procesamiento de Imágenes para Detección de Objetos

Este script procesa una imagen para realizar tres tareas:

1. **Conversión de la imagen a binario:** La imagen se pasa por un clasificador para convertirla en una imagen binaria, donde se marcan las regiones de interés.

2. **Etiquetado de objetos:** Se etiquetan los objetos en la imagen identificada por el clasificador. Cada objeto se etiqueta con un número único.

3. **Localización de ventanas:** Se localizan las ventanas en los objetos etiquetados, identificando regiones similares.

## Ejecución del Script

Para ejecutar el script, se debe proporcionar una imagen como entrada. El script realizará las tres tareas mencionadas anteriormente y mostrará los resultados.


## Requisitos

El script fue desarrollado utilizando las siguientes tecnologías y bibliotecas:

- Python 3.x
- OpenCV
- NumPy

## Resultados

El script generará varias imágenes como salida:

- **Imagen Clasificada:**
![Imagen clasificada]
- **Imagen Etiquetada:** Muestra la imagen etiquetada con números para cada objeto identificado.
- **Localización:** Muestra la imagen con rectángulos que delimitan las ventanas identificadas en los objetos.

## Contribuciones

Las contribuciones son bienvenidas. Si desea realizar alguna mejora o corregir algún error, no dude en enviar una solicitud de extracción.

¡Gracias por utilizar este script!



