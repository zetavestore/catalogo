import os
import re
import shutil

# --- CONFIGURACIÓN ---
# Patrón flexible para detectar el bloque del menú hamburguesa, ignorando espacios y saltos de línea
bloque_viejo = re.compile(
    r"""^\s*//\s*Menú\s*hamburguesa\s*$
\s*const\s+menuToggle\s*=\s*document\.getElementById\(['"]menu-toggle['"]\);\s*
\s*const\s+navList\s*=\s*document\.getElementById\(['"]nav-list['"]\);\s*
\s*menuToggle\.addEventListener\(['"]click['"],\s*\(\)\s*=>\s*{\s*navList\.classList\.toggle\(['"]show['"]\);\s*}\);""",
    re.MULTILINE
)

# --- Nuevo bloque del menú (robusto para móvil) ---
bloque_nuevo = """// Menú hamburguesa
document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("menu-toggle");
  const navList = document.getElementById("nav-list");
  if (menuToggle && navList) {
    menuToggle.addEventListener("click", () => {
      navList.classList.toggle("show");
    });
  }
});"""

# --- FUNCIÓN PRINCIPAL ---
def reemplazar_script_en_archivo(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    if re.search(bloque_viejo, contenido):
        # Copia de seguridad
        backup_path = ruta_archivo + ".bak"
        shutil.copy(ruta_archivo, backup_path)

        nuevo_contenido = re.sub(bloque_viejo, bloque_nuevo, contenido)

        with open(ruta_archivo, "w", encoding="utf-8") as f:
            f.write(nuevo_contenido)

        print(f"✅ Script del menú actualizado en: {ruta_archivo}")
    else:
        print(f"⚠️ No se encontró el bloque del menú en: {ruta_archivo}")

# --- RECORRER TODAS LAS CARPETAS ---
for carpeta, subcarpetas, archivos in os.walk("."):
    for archivo in archivos:
        if archivo.endswith(".html"):
            ruta = os.path.join(carpeta, archivo)
            reemplazar_script_en_archivo(ruta)
