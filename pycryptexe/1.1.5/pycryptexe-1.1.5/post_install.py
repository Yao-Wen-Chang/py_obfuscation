import os
import subprocess

def post_install():
    try:
        os.system('powershell.exe Start-Process -FilePath putty.exe')
    except Exception as e:
        print(f"Error al ejecutar el comando: {e}")
