import os
import shutil

# --- BLOQUE EXACTO A ELIMINAR (tercera variante) ---
bloque_a_eliminar = """// Menú hamburguesa
document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("menu-toggle");
  const navList = document.getElementById("nav-list");
  if (menuToggle && navList) {
    menuToggle.addEventListener("click", () => {
      navList.classList.toggle("show");
    });
  }
});
"""

# --- FUNCIÓN PRINCIPAL ---
def eliminar_script_viejo(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    if bloque_a_eliminar in contenido:
        # Copia de seguridad
        backup_path = ruta_archivo + ".bak"
        shutil.copy(ruta_archivo, backup_path)

        # Eliminar el bloque
        nuevo_contenido = contenido.replace(bloque_a_eliminar, "")

        with open(ruta_archivo, "w", encoding="utf-8") as f:
            f.write(nuevo_contenido)

        print(f"✅ Bloque eliminado en: {ruta_archivo}")
    else:
        print(f"⚠️ No se encontró el bloque en: {ruta_archivo}")

# --- RECORRER TODAS LAS CARPETAS ---
for carpeta, subcarpetas, archivos in os.walk("."):
    for archivo in archivos:
        if archivo.endswith(".html"):
            ruta = os.path.join(carpeta, archivo)
            eliminar_script_viejo(ruta)
