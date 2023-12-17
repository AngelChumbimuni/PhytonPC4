# Guardar el texto en un archivo
with open('texto.txt', 'w') as archivo:
    texto = "En el ámbito del desarrollo de software, la colaboración es fundamental. La colaboración eficiente impulsa la eficacia y mejora la calidad del código. La calidad del código, a su vez, es esencial para la mantenibilidad del sistema. Mantener un sistema sin problemas es esencial para la satisfacción del cliente. La satisfacción del cliente, por supuesto, es un objetivo clave para cualquier equipo de desarrollo. Desarrollar estrategias para fomentar la colaboración continua y mejorar la calidad del código es una práctica que beneficia a todos los miembros del equipo y contribuye al éxito general del proyecto"
    archivo.write(texto)

# Leer el archivo y contar la palabra "la"
with open('texto.txt', 'r') as archivo:
    contenido = archivo.read()
    cantidad_la = contenido.lower().count('la')

print(f'La palabra "la" aparece {cantidad_la} veces en el archivo.')

# Ingresar texto por teclado y agregar al final del archivo
nuevo_texto = input("Ingrese un texto para agregar al final del archivo: ")

with open('texto.txt', 'a') as archivo:
    archivo.write('\n' + nuevo_texto)

print('Texto agregado exitosamente al final del archivo.')