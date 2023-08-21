# Instagram Scraping App

Esta es una aplicación simple de scraping de Instagram que te permite descargar contenido de una cuenta objetivo. Utiliza las bibliotecas Selenium y wget para automatizar el proceso de descarga.

## Requisitos

- Python 3.x
- [Selenium](https://selenium-python.readthedocs.io/)
- [wget](https://pypi.org/project/wget/)

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala las bibliotecas requeridas ejecutando: `pip install selenium wget`

## Uso

1. Configura tus credenciales de Instagram en el archivo `constantes.py`:
   
   ```python
   IG_USERNAME = 'tu nombre de usuario'
   Target = 'cuenta de la que deseas descargar las imágenes'
