import pandas as pd
from pathlib import Path

# ------------------
# RUTAS
# ------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RUTA_RAW = BASE_DIR / "data" / "raw"
RUTA_PROCESSED = BASE_DIR / "data" / "processed"

# ------------------
# CREAR CARPETA
# ------------------

RUTA_PROCESSED.mkdir(
    parents=True,
    exist_ok=True
)

print("Carpeta processed preparada")


# ------------------
# CARGAR CSV RAW
# ------------------

df_clientes = pd.read_csv(
    RUTA_RAW / "clientes.csv"
)

df_departamentos = pd.read_csv(
    RUTA_RAW / "departamentos.csv"
)

df_empleados = pd.read_csv(
    RUTA_RAW / "empleados.csv"
)

df_fechas = pd.read_csv(
    RUTA_RAW / "fechas.csv"
)

df_productos = pd.read_csv(
    RUTA_RAW / "productos.csv"
)

df_zonas = pd.read_csv(
    RUTA_RAW / "zonas.csv"
)

df_ventas = pd.read_csv(
    RUTA_RAW / "ventas.csv"
)

#df_productividad = pd.read_csv(
#    RUTA_RAW / "productividad.csv"
#)

#df_ausencias = pd.read_csv(
#    RUTA_RAW / "ausencias.csv"
#)

print("Datos RAW cargados")

print("clientes")
df_clientes = pd.read_csv(
    RUTA_RAW / "clientes.csv"
)

print("departamentos")
df_departamentos = pd.read_csv(
    RUTA_RAW / "departamentos.csv"
)

print("empleados")
df_empleados = pd.read_csv(
    RUTA_RAW / "empleados.csv"
)

print("fechas")
df_fechas = pd.read_csv(
    RUTA_RAW / "fechas.csv"
)

print("productos")
df_productos = pd.read_csv(
    RUTA_RAW / "productos.csv"
)

print("zonas")
df_zonas = pd.read_csv(
    RUTA_RAW / "zonas.csv"
)

print("ventas")
df_ventas = pd.read_csv(
    RUTA_RAW / "ventas.csv"
)

#print("productividad")
#df_productividad = pd.read_csv(
#    RUTA_RAW / "productividad.csv"
#)

#print("ausencias")
#df_ausencias = pd.read_csv(
#    RUTA_RAW / "ausencias.csv"
#)