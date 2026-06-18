import random
import pandas as pd
from pathlib import Path

# ------------------
# RUTAS
# ------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RUTA_RAW = BASE_DIR / "data" / "raw"

# ------------------
# CARGAR EMPLEADOS
# ------------------

df_empleados = pd.read_csv(
    RUTA_RAW / "empleados.csv"
)

# ------------------
# CONFIGURACIÓN
# ------------------

NUM_AUSENCIAS = 120

ausencias = []

# ------------------
# GENERAR AUSENCIAS
# ------------------

for ausencia_id in range(
    1,
    NUM_AUSENCIAS + 1
):

    empleado = df_empleados.sample(
        1
    ).iloc[0]

    tipo_ausencia = random.choices(
        [
            "Vacaciones",
            "Baja Médica",
            "Permiso",
            "Formación"
        ],
        weights=[60, 25, 10, 5],
        k=1
    )[0]

    fecha_inicio = pd.Timestamp(
        random.choice(
            pd.date_range(
                "2021-01-01",
                "2025-12-31"
            )
        )
    )

    if tipo_ausencia == "Vacaciones":

        dias = random.choice(
        [15, 20, 22, 25, 30]
    )

    elif tipo_ausencia == "Baja Médica":

        dias = random.randint(2, 30)

    elif tipo_ausencia == "Permiso":

        dias = random.randint(1, 3)

    else:

        dias = random.randint(1, 5)

    fecha_fin = (
        fecha_inicio
        + pd.Timedelta(days=dias)
    )

    ausencias.append({

        "ausencia_id": ausencia_id,

        "empleado_id":
            empleado["empleado_id"],

        "fecha_inicio":
            fecha_inicio.date(),

        "fecha_fin":
            fecha_fin.date(),

        "tipo_ausencia":
            tipo_ausencia,

        "dias_ausencia":
            dias
    })

# ------------------
# DATAFRAME
# ------------------

df_ausencias = pd.DataFrame(
    ausencias
)

# ------------------
# EXPORTAR
# ------------------

df_ausencias.to_csv(
    RUTA_RAW / "ausencias.csv",
    index=False,
    encoding="utf-8-sig"
)

print("ausencias.csv generado")

print(df_ausencias.head())

print("\nNúmero registros:")
print(len(df_ausencias))

print("\nTipos ausencia:")
print(
    df_ausencias["tipo_ausencia"]
    .value_counts()
)


print(
    df_ausencias.groupby("tipo_ausencia")
    ["dias_ausencia"]
    .agg(["count", "mean", "min", "max"])
)