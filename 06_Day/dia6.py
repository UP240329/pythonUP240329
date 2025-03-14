#Create an empty tuple
emptyTuple=()
print(len(emptyTuple))
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
tpl=('Moni','Ximena','Nydia','Luis','Jorge')
print(tpl)
#Unir tuplas de hermanos y hermanas y asignarlas a hermanos
hermanos1=('Jorge','Luis','Carlos')
hermanas2=('Moni','Ximena','Nydia')
hermanos=hermanos1+hermanas2
print(hermanos)
#¿Cuántos hermanos tienes?
print('Tengo {} hermanos'.format(len(hermanos)))
#Modifica la tupla de hermanos y agrega el nombre
#  de tu padre y madre y asígnalo a family_members
familymembers=hermanos+('Victoria','Fernando')
print(familymembers)
#Nivel2
#Desempaquetar hermanos y padres de family_members
her1,her2,her3,her4,her5,her6,ma,pa=familymembers
print(her1,her2,her3,her4,her5,her6,ma,pa)
#Crea tuplas de frutas, verduras y productos animales. 
# Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.
frutas=('manzana','pera','uva','fresa')
verduras=('lechuga','espinaca','acelga','brocoli')
productosanimales=('pollo','res','cerdo','pescado')
foodStuffTp=frutas+verduras+productosanimales
print(foodStuffTp)
#Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
foodStuffTp=list(foodStuffTp)
#Extraiga el elemento o los elementos
# del medio de la tupla food_stuff_tp o de la lista food_stuff_lt.
print(foodStuffTp[4:8])
#Separa los primeros tres elementos
#  y los últimos tres elementos de la lista food_staff_lt
print(foodStuffTp[0:3],foodStuffTp[9:12])
#Eliminar la tupla food_staff_tp por completo
del foodStuffTp
#Comprueba si un elemento existe en una tupla:
#Comprueba si 'Estonia' es un país nórdico
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

#REVISADO
print("Revisado")