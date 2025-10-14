import os
import re
import shutil

# --- CONFIGURACIÓN ---
# Este es el nuevo bloque que querés insertar en lugar del menú viejo
nuevo_menu = '''
  <nav class="navbar">
    <div id="menu-container"></div>
    <script>
      fetch("/menu.html")
        .then(response => response.text())
        .then(data => {
          document.getElementById("menu-container").innerHTML = data;
        });
    </script>
  </nav>
'''

# --- FUNCIÓN PARA REEMPLAZAR EL MENÚ ---
def reemplazar_menu_en_archivo(ruta_archivo):
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Busca el bloque <nav> ... </nav> completo
    patron = re.compile(r"<nav class=\"navbar\">.*?</nav>", re.DOTALL)

    if re.search(patron, contenido):
        # Guarda una copia de seguridad
        backup_path = ruta_archivo + ".bak"
        shutil.copy(ruta_archivo, backup_path)

        # Reemplaza el bloque por el nuevo menú
        nuevo_contenido = re.sub(patron, nuevo_menu, contenido)

        # Guarda el archivo actualizado
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            f.write(nuevo_contenido)

        print(f"✅ Menú reemplazado en: {ruta_archivo}")
    else:
        print(f"⚠️ No se encontró menú en: {ruta_archivo}")

# --- RECORRE TODAS LAS CARPETAS ---
for carpeta, subcarpetas, archivos in os.walk("."):
    for archivo in archivos:
        if archivo.endswith(".html"):
            ruta = os.path.join(carpeta, archivo)
            reemplazar_menu_en_archivo(ruta)
