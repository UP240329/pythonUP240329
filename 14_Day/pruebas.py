from collections import Counter

# Suponemos que el archivo paises1.py tiene la lista 'paises' que contiene la información de los países.
import paises1 as paises

def contarTop10IdiomasPorUbicacion():
    idiomasPorUbicacion = {}

    # Iteramos sobre cada país en la lista 'paises'
    for pais in paises.paises:  # Accediendo a la lista 'paises' dentro de paises1.py
        if "languages" in pais and "region" in pais:
            region = pais["region"]  # Región (ubicación geográfica) del país
            idiomas = pais["languages"]  # Lista de idiomas hablados en el país
            
            # Aseguramos que la región esté en el diccionario
            if region not in idiomasPorUbicacion:
                idiomasPorUbicacion[region] = []
            
            # Añadimos los idiomas hablados en el país a la lista correspondiente
            idiomasPorUbicacion[region].extend(idiomas)
    
    # Ahora, clasificamos los idiomas más hablados globalmente por ubicación
    idiomasClasificadosPorUbicacion = {}

    # Contamos los idiomas por región usando Counter
    for region, idiomas in idiomasPorUbicacion.items():
        idiomasClasificadosPorUbicacion[region] = Counter(idiomas).most_common(10)

    return idiomasClasificadosPorUbicacion

# Función para mostrar solo los diez idiomas más hablados por ubicación
def mostrarTop10IdiomasPorUbicacion():
    idiomasPorUbicacion = contarTop10IdiomasPorUbicacion()

    for region, idiomas in idiomasPorUbicacion.items():
        print(f"\nTop 10 idiomas más hablados en la región: {region}")
        for idioma, count in idiomas:
            print(f"{idioma}: {count}")

# Ejecutar la función para mostrar los resultados
mostrarTop10IdiomasPorUbicacion()


