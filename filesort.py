from pathlib import Path
import shutil
from tkinter import Tk, filedialog


#=====================================
# CONFIGURACION DEL PROGRAMA
#=====================================

MODO_PRUEBA = False


#=====================================
# FUNCIONES DEL PROGRAMA
#=====================================

def seleccionar_carpeta():

    ventana = Tk()
    ventana.withdraw()

    ruta = filedialog.askdirectory(
        title="Seleccionar la carpeta que desea organizar"
    )

    ventana.destroy()

    if not ruta:
        print("No se seleccionó ninguna carpeta. Programa cancelado.")
        raise SystemExit

    return Path(ruta)


def clasificar_archivo(archivo):

    extension = archivo.suffix.lower()

    for categoria, lista_extensiones in extensiones.items():
        if extension in lista_extensiones:
            return categoria

    return "Otros"


#=====================================
# DICCIONARIO DE EXTENSIONES
#=====================================

extensiones = {
    "Imagenes": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".webp", ".svg", ".heic", ".avif"
    ],

    "Documentos": [
        ".doc", ".docx", ".odt", ".txt", ".md", ".pdf"
    ],

    "Hojas de calculo": [
        ".xls", ".xlsx", ".csv", ".ods", ".xlsb"
    ],

    "Presentaciones": [
        ".ppt", ".pptx", ".odp"
    ],

    "Audio": [
        ".mp3", ".wav", ".flac", ".aac", ".ogg", ".opus"
    ],

    "Videos": [
        ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".webm"
    ],

    "Programas": [
        ".exe", ".msi", ".apk", ".dmg"
    ],

    "Comprimidos": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ],

    "Codigo": [
        ".py", ".js", ".html", ".css", ".json",
        ".xml", ".sql", ".php", ".rtf"
    ]
}


#=====================================
# PRUEBA DEL DICCIONARIO
#=====================================

for categoria, lista_extensiones in extensiones.items():

    for extension in lista_extensiones:

        if not extension.startswith("."):
            print(f"Error: {extension} no tiene punto inicial")

        if extension != extension.lower():
            print(f"Error: {extension} contiene mayúsculas")


#=====================================
# SELECCIONAR CARPETA DE ORIGEN
#=====================================

carpeta_descargas = seleccionar_carpeta()

print(carpeta_descargas)

if carpeta_descargas.is_dir():
    print("La carpeta Descargas existe")

else:
    print("ERROR: La carpeta Descargas no existe")
    raise SystemExit


#=====================================
# OBTENER ARCHIVOS DEL PRIMER NIVEL
#=====================================

archivos = list(carpeta_descargas.iterdir())


#=====================================
# PROCESAMIENTO DE ARCHIVOS
#=====================================

for archivo in archivos:

    # Ignorar directorios
    if archivo.is_file():

        print("\nArchivo:", archivo.name)

        #============================
        # IDENTIFICAR ARCHIVOS TEMPORALES
        #============================

        if archivo.name.startswith(("~$", "~WRL")):
            print("Archivo temporal detectado. Se omite.")
            print("-----------------------")
            continue

        #============================
        # CLASIFICAR ARCHIVO
        #============================

        categoria = clasificar_archivo(archivo)

        print("Categoria:", categoria)

        #===============================
        # CONSTRUIR CARPETA DE DESTINO
        #===============================

        carpeta_destino = carpeta_descargas / categoria

        destino = carpeta_destino / archivo.name

        # Buscar un nombre disponible
        contador = 1

        while destino.exists():

            nuevo_nombre = f"{archivo.stem}_{contador}{archivo.suffix}"

            destino = carpeta_destino / nuevo_nombre

            contador += 1

        print("Destino final:", destino)

        #================================
        # EJECUTAR O SIMULAR EL MOVIMIENTO
        #================================

        if MODO_PRUEBA:

            print("SIMULACION: archivo preparado para mover.")

        else:

            carpeta_destino.mkdir(exist_ok=True)

            shutil.move(str(archivo), str(destino))

            print("ARCHIVO MOVIDO:", destino)

        print("---------------------")
        print("Carpeta destino:", carpeta_destino)