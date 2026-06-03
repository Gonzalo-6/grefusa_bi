import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime
from pathlib import Path

# Ruta a data/raw
BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_RAW = BASE_DIR / "data" / "raw"

# ------------------
# DEPARTAMENTOS
# ------------------

departamentos = [
    "Dirección",
    "Ventas",
    "Distribución",
    "Almacén",
    "Contabilidad",
    "RRHH"
]

df_departamentos = pd.DataFrame({
    "departamento_id": range(1, len(departamentos) + 1),
    "nombre_departamento": departamentos
})

# Guardar CSV
df_departamentos.to_csv(
    RUTA_RAW / "departamentos.csv",
    index=False,
    encoding="utf-8-sig"
)

print("departamentos.csv generado")


# ------------------
# ZONAS
# ------------------

zonas = [
    "Madrid Centro",
    "Madrid Norte",
    "Madrid Sur",
    "Madrid Este",
    "Madrid Oeste",
    "Alcobendas",
    "San Sebastián de los Reyes",
    "Getafe",
    "Leganés",
    "Móstoles",
    "Alcorcón",
    "Fuenlabrada"
]

df_zonas = pd.DataFrame({
    "zona_id": range(1, len(zonas) + 1),
    "nombre_zona": zonas
})

df_zonas.to_csv(
    RUTA_RAW / "zonas.csv",
    index=False,
    encoding="utf-8-sig"
)

print("zonas.csv generado")