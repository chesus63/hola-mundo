02 from microbit import *                                                           # Importa todas las funciones y clases del módulo microbit
03 display.scroll('Hola Mundo', delay=1500)                              # Muestra el texto "Hola Mundo" en la pantalla del micro:bit con un retraso de 1500 ms entre cada letra
04 while True:                                                                              # Inicia un bucle infinito para ejecutar repetidamente el siguiente bloque de código
05       display.show(Image.HEART, delay=250, clear=True)    # Muestra una imagen de un corazón en la pantalla del micro:bit durante 250 ms, luego limpia la pantalla
