import myModule as m #ejemplos para entender la teoría del archivo de modulos
from random import *

#Escriba una función que genere un random_user_id de seis dígitos/caracteres.
#La función debe devolver un string con el id generado.
def random_user_id():
    user_id = ''
    for i in range(6):
        user_id += str(randint(0, 9))
    return user_id
print(random_user_id())
#Modifique la tarea anterior. Declare una función llamada user_id_gen_by_user. No acepta parámetros
# , pero acepta dos entradas mediante input(). Una de las entradas es el número de caracteres y la otra, el número de ID que se generarán. 
# La función debe devolver una lista de ID generados.
def user_id_gen_by_user():
    user_id_list = []
    num_ids = int(input("Ingrese el número de IDs que desea generar: "))
    num_chars = int(input("Ingrese el número de caracteres para cada ID: "))
    for i in range(num_ids):
        user_id = ''
        for j in range(num_chars):
            user_id += str(randint(0, 9))
        user_id_list.append(user_id)
    return user_id_list
print(user_id_gen_by_user())
# Escriba una función llamada rgb_color_gen. Esta generará colores RGB (tres valores de 0 a 255 cada uno).r = randint(0, 255)
def rgb_color_gen():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)
print(rgb_color_gen())
# Nivel2
# Escriba una función list_of_hexa_colors que devuelva cualquier número de colores hexadecimales en una matriz (seis números hexadecimales escritos después de
#. El sistema de numeración hexadecimal está formado por 16 símbolos, del 0 al 9 y las primeras 6 letras del alfabeto, af. Consulte la tarea 6 para ver ejemplos de salida).
def list_of_hexa_colors():
    hex_colors = []
    for i in range(10):
        hex_color = '#'
        for j in range(6):
            hex_color += choice('0123456789abcdef')
        hex_colors.append(hex_color)
    return hex_colors
print(list_of_hexa_colors())