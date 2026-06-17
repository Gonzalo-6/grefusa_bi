import random
import pandas as pd
from pathlib import Path

# ------------------
# RUTAS
# ------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RUTA_RAW = BASE_DIR / "data" / "raw"

# ------------------
# CARGAR VENTAS
# ------------------

df_ventas = pd.read_csv(
    RUTA_RAW / "ventas.csv"
)



# ------------------
# AGRUPAR VENTAS
# ------------------

df_productividad = (
    df_ventas
    .groupby(
        ["fecha_id", "empleado_id"],
        as_index=False
    )
    .agg(
        pedidos_gestionados=(
            "pedido_id",
            "nunique"
        ),
        importe_vendido=(
            "importe",
            "sum"
        )
    )
)

# ------------------
# OBJETIVOS
# ------------------

objetivos = []

for _ in range(len(df_productividad)):

    objetivo = random.randint(
        600,
        1800
    )

    objetivos.append(objetivo)

df_productividad["objetivo_diario"] = objetivos

df_productividad["cumplimiento_pct"] = round(
    (
        df_productividad["importe_vendido"]
        /
        df_productividad["objetivo_diario"]
    ) * 100,
    2
)

# ------------------
# ID PRODUCTIVIDAD
# ------------------

df_productividad.insert(
    0,
    "productividad_id",
    range(
        1,
        len(df_productividad) + 1
    )
)

# ------------------
# EXPORTAR
# ------------------

df_productividad.to_csv(
    RUTA_RAW / "productividad.csv",
    index=False,
    encoding="utf-8-sig"
)


#--------------------
#COMPROBAR REGISTROS
#--------------------

print("Ventas cargadas:")
print(len(df_ventas))

print("\nproductividad.csv generado")

print(df_productividad.head())

print("\nNúmero registros:")
print(len(df_productividad))
