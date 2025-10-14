import os
import re
import shutil

# --- BLOQUES ---
bloque_viejo = re.compile(
    r'<nav class="navbar">\s*<div id="menu-container"></div>\s*<script>\s*fetch\("/catalogo/menu\.html"\)\s*\.then\(response => response\.text\(\)\)\s*\.then\(data => {\s*document\.getElementById\("menu-container"\)\.innerHTML = data;\s*}\);\s*</script>\s*</nav>',
    re.DOTALL
)

bloque_nuevo = '''<nav class="navbar">
    <div id="menu-container"></div>
    <script>
      fetch("/catalogo/menu.html")
        .then(response => response.text())
        .then(data => {
          document.getElementById("menu-container").innerHTML = data;

    // JS del menú hamburguesa, ejecutado después de insertar el HTML
    const menuToggle = document.getElementById("menu-toggle");
    const navList = document.getElementById("nav-list");
    if (menuToggle && navList) {
      menuToggle.addEventListener("click", () => {
        navList.classList.toggle("show");
      });
    }
  })
  .catch(err => console.error("Error cargando el menú:", err));
    </script>
  </nav>'''

# --- FUNCIÓN PARA REEMPLAZAR ---
def reemplazar_menu(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    if re.search(bloque_viejo, contenido):
        # Guardar copia de seguridad
        backup_path = ruta_archivo + ".bak"
        shutil.copy(ruta_archivo, backup_path)

        nuevo_contenido = re.sub(bloque_viejo, bloque_nuevo, contenido)

        with open(ruta_archivo, "w", encoding="utf-8") as f:
            f.write(nuevo_contenido)

        print(f"✅ Reemplazado en: {ruta_archivo}")
    else:
        print(f"⚠️ No se encontró el bloque en: {ruta_archivo}")

# --- RECORRER TODAS LAS CARPETAS ---
for carpeta, subcarpetas, archivos in os.walk("."):
    for archivo in archivos:
        if archivo.endswith(".html"):
            ruta = os.path.join(carpeta, archivo)
            reemplazar_menu(ruta)
