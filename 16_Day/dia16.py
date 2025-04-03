import datetime
#Obtenga el día, mes, año, hora, minuto y marca de tiempo actuales del módulo datetime
ahora=datetime.datetime.now()
print("Fecha y hora actuales:", ahora)
#Formatee la fecha actual utilizando este formato: "%m/%d/%Y, %H:%M:%S")
formatoAhora=ahora.strftime("%m/%d/%Y, %H:%M:%S")
print("Formato de fecha y hora:", formatoAhora)
#Hoy es 5 de diciembre de 2019. Cambie esta cadena de tiempo a hora
from datetime import datetime
dateString = "5 December, 2019"
print("dateString =", dateString)
dateObject = datetime.strptime(dateString, "%d %B, %Y")
print("dateObject =", dateObject)
#Calcula la diferencia horaria entre ahora y el año nuevo.
from datetime import datetime, timedelta, date
today = date(year=2025, month=4, day=2)
newYear = date(year=2026, month=1, day=1)
time= newYear - today
print("Time left for new year: ", time) 
#Calcula la diferencia horaria entre el 1 de enero de 1970 y la actualidad.
today = date(year=2025, month=4, day=2)
old = date(year=1972, month=1, day=1)
times= today- old
print(times)
#Piensa, ¿para qué puedes usar el módulo datetime? Ejemplos
#Análisis de series temporales
#Para obtener una marca de tiempo de cualquier actividad en una aplicación
#Agregar publicaciones a un blog
print('se puede usar datetime para manipular trabajos remotos en diferentes zonas horarias')
