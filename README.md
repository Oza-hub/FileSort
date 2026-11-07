# FileSort

**Organizador de archivos desarrollado en Python.**

FileSort es una aplicación sencilla que permite organizar archivos automáticamente en carpetas según su extensión. Este proyecto fue desarrollado como ejercicio práctico de programación, utilizando conceptos fundamentales de Python y bibliotecas de su distribución estándar.

## Características

- Selección de una carpeta mediante una ventana gráfica.
- Identificación de archivos por su extensión.
- Clasificación automática por categorías.
- Creación de carpetas de destino.
- Organización de archivos dentro de la carpeta seleccionada.
- Prevención de sobrescritura de archivos con nombres duplicados.
- Exclusión de archivos temporales de Microsoft Office.
- Clasificación de extensiones no reconocidas en la categoría `Otros`.

## Categorías de clasificación

| Categoría | Extensiones |
|---|---|
| Imagenes | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`, `.svg`, `.heic`, `.avif` |
| Documentos | `.doc`, `.docx`, `.odt`, `.txt`, `.md`, `.pdf` |
| Hojas de calculo | `.xls`, `.xlsx`, `.csv`, `.ods`, `.xlsb` |
| Presentaciones | `.ppt`, `.pptx`, `.odp` |
| Audio | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.opus` |
| Videos | `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.webm` |
| Programas | `.exe`, `.msi`, `.apk`, `.dmg` |
| Comprimidos | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Codigo | `.py`, `.js`, `.html`, `.css`, `.json`, `.xml`, `.sql`, `.php`, `.rtf` |
| Otros | Extensiones no incluidas en las categorías anteriores |

## Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Pathlib:** gestión de rutas y directorios.
- **Shutil:** operaciones de movimiento de archivos.
- **Tkinter:** selección de carpetas mediante interfaz gráfica.

## Requisitos

- Python 3.10 o superior.
- Sistema operativo Windows recomendado.
- Instalación de Python con soporte para Tkinter.

No requiere instalar dependencias externas.

## Ejecución

Clonar el repositorio:

```bash
git clone https://github.com/Oza-hub/FileSort.git
```

Ingresar al directorio:

```bash
cd FileSort
```

Ejecutar el programa:

```bash
python filesort.py
```

El programa solicitará seleccionar la carpeta que se desea organizar.

## Funcionamiento

FileSort examina los archivos que se encuentran directamente en la carpeta seleccionada. No realiza búsquedas recursivas en subdirectorios.

Los archivos se clasifican según su extensión y se trasladan a las carpetas correspondientes. Si encuentra archivos con nombres duplicados, agrega un número consecutivo para evitar sobrescribirlos.

Las carpetas de clasificación se crean dentro de la carpeta seleccionada.

**Importante:** el programa mueve los archivos de su ubicación original. Se recomienda realizar una copia de seguridad antes de utilizarlo sobre información importante.

## Propósito del proyecto

FileSort es un ejercicio de programación orientado a la aplicación práctica de conceptos fundamentales:

- Variables y tipos de datos.
- Listas y diccionarios.
- Estructuras condicionales y repetitivas.
- Funciones.
- Importación y utilización de módulos.
- Manejo de archivos y directorios.
- Automatización de tareas.

## Autor

**Oza-hub**

GitHub: https://github.com/Oza-hub

---

*Proyecto desarrollado con fines educativos y de aprendizaje de Python.*