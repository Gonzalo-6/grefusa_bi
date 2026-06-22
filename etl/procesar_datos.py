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

df_productividad = pd.read_csv(
    RUTA_RAW / "productividad.csv"
)

df_ausencias = pd.read_csv(
    RUTA_RAW / "ausencias.csv"
)

print("\nDatos RAW cargados correctamente")

# ------------------
# DIMENSIONES
# ------------------

dim_cliente = df_clientes.copy()

dim_departamento = df_departamentos.copy()

dim_empleado = df_empleados.copy()

dim_fecha = df_fechas.copy()

dim_producto = df_productos.copy()

dim_zona = df_zonas.copy()

# ------------------
# HECHOS
# ------------------

fact_ventas = df_ventas.copy()

fact_productividad = df_productividad.copy()

fact_ausencias = df_ausencias.copy()

# ------------------
# EXPORTAR DIMENSIONES
# ------------------

dim_cliente.to_csv(
    RUTA_PROCESSED / "dim_cliente.csv",
    index=False
)

dim_departamento.to_csv(
    RUTA_PROCESSED / "dim_departamento.csv",
    index=False
)

dim_empleado.to_csv(
    RUTA_PROCESSED / "dim_empleado.csv",
    index=False
)

dim_fecha.to_csv(
    RUTA_PROCESSED / "dim_fecha.csv",
    index=False
)

dim_producto.to_csv(
    RUTA_PROCESSED / "dim_producto.csv",
    index=False
)

dim_zona.to_csv(
    RUTA_PROCESSED / "dim_zona.csv",
    index=False
)

# ------------------
# EXPORTAR HECHOS
# ------------------

fact_ventas.to_csv(
    RUTA_PROCESSED / "fact_ventas.csv",
    index=False
)

fact_productividad.to_csv(
    RUTA_PROCESSED / "fact_productividad.csv",
    index=False
)

fact_ausencias.to_csv(
    RUTA_PROCESSED / "fact_ausencias.csv",
    index=False
)

# ------------------
# VALIDACIÓN
# ------------------

print("\nPROCESO ETL FINALIZADO")

print("\nDIMENSIONES")

print("Clientes:", len(dim_cliente))
print("Departamentos:", len(dim_departamento))
print("Empleados:", len(dim_empleado))
print("Fechas:", len(dim_fecha))
print("Productos:", len(dim_producto))
print("Zonas:", len(dim_zona))

print("\nHECHOS")

print("Ventas:", len(fact_ventas))
print("Productividad:", len(fact_productividad))
print("Ausencias:", len(fact_ausencias))