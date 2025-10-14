import os

# Recorre todas las carpetas desde donde se ejecute el script
for carpeta, subcarpetas, archivos in os.walk("."):
    for archivo in archivos:
        if archivo.endswith(".bak"):
            ruta = os.path.join(carpeta, archivo)
            os.remove(ruta)
            print(f"🗑️ Borrado: {ruta}")

print("✅ Todos los archivos .bak fueron eliminados.")
