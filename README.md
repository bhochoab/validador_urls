# Validador de URLs

Este proyecto valida URLs desde un archivo de texto y guarda los resultados en un CSV.

## Pasos para trabajar con este proyecto

### 1. Clonar o crear el repositorio

```bash
git clone <REPO_URL> validador_urls
cd validador_urls
```

(Si no tenés repo todavía, crealo en GitHub y subí este contenido)

### 2. Crear entorno virtual y activarlo

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el validador

```bash
python main.py
```

Genera el archivo `resultados.csv` con los códigos de estado de cada URL.

### 5. Subir los cambios a GitHub

```bash
git init
git add .
git commit -m "Primer commit: proyecto validador de URLs"
git branch -M main
git remote add origin <REPO_URL>
git push -u origin main
```

📘 Recordá reemplazar `<REPO_URL>` con la URL real de tu repositorio en GitHub.
