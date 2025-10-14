import os
import re
import shutil

# --- CONFIGURACIÓN ---
# Bloque de JS viejo (el que queremos reemplazar)
bloque_viejo = re.compile(
    r'<script>\s*const menuToggle = document\.getElementById\(\'menu-toggle\'\);\s*'
    r'const navList = document\.getElementById\(\'nav-list\'\);\s*'
    r'menuToggle\.addEventListener\(\'click\', \(\) => {\s*navList\.classList\.toggle\(\'show\'\);\s*}\);\s*'
    r'</script>',
    re.DOTALL
)

# Bloque nuevo (lo que querés poner en su lugar)
bloque_nuevo = """<script>
document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("menu-toggle");
  const navList = document.getElementById("nav-list");
  if (menuToggle && navList) {
    menuToggle.addEventListener("click", () => {
      navList.classList.toggle("show");
    });
  }
});
</script>"""

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

        print(f"✅ Script reemplazado en: {ruta_archivo}")
    else:
        print(f"⚠️ No se encontró el script viejo en: {ruta_archivo}")

# --- RECORRER TODAS LAS CARPETAS ---
for carpeta, subcarpetas, archivos in os.walk("."):
    for archivo in archivos:
        if archivo.endswith(".html"):
            ruta = os.path.join(carpeta, archivo)
            reemplazar_script_en_archivo(ruta)
