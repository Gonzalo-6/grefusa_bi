import random

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

zonas_madrid = {
    1: "Madrid Centro",
    2: "Madrid Norte",
    3: "Madrid Sur",
    4: "Madrid Este",
    5: "Madrid Oeste",
    6: "Alcobendas",
    7: "San Sebastián de los Reyes",
    8: "Getafe",
    9: "Leganés",
    10: "Móstoles",
    11: "Alcorcón",
    12: "Fuenlabrada"
}

pesos_zonas = [
    15,  # Madrid Centro
    12,  # Madrid Norte
    12,  # Madrid Sur
    10,  # Madrid Este
    10,  # Madrid Oeste
    8,   # Alcobendas
    8,   # San Sebastián
    7,   # Getafe
    7,   # Leganés
    5,   # Móstoles
    3,   # Alcorcón
    3    # Fuenlabrada
]
df_zonas = pd.DataFrame({
    "zona_id": range(1, len(zonas_madrid) + 1),
    "nombre_zona": list(zonas_madrid.values()),
    "peso": pesos_zonas
})

# Guardar CSV

df_zonas.to_csv(
    RUTA_RAW / "zonas.csv",
    index=False,
    encoding="utf-8-sig"
)

print("zonas.csv generado")

# ------------------
# EMPLEADOS
# ------------------


fake = Faker("es_ES")

empleados = []

puestos = {
    "Dirección": ["Director General"],
    "RRHH": ["Técnico RRHH"],
    "Contabilidad": ["Contable"],
    "Ventas": ["Comercial"],
    "Distribución": ["Repartidor"],
    "Almacén": ["Mozo de almacén"]
}

salarios = {
    "Director General": (45000, 60000),
    "Técnico RRHH": (25000, 32000),
    "Contable": (24000, 32000),
    "Comercial": (22000, 40000),
    "Repartidor": (21000, 30000),
    "Mozo de almacén": (20000, 28000)
}

distribucion_empleados = {
    "Dirección": 2,
    "RRHH": 2,
    "Contabilidad": 3,
    "Ventas": 10,
    "Distribución": 10,
    "Almacén": 3
}

empleado_id = 1

for departamento, cantidad in distribucion_empleados.items():

    for _ in range(cantidad):

        puesto = puestos[departamento][0]

        salario_min, salario_max = salarios[puesto]

        sexo = random.choice(["Hombre", "Mujer"])

        if sexo == "Hombre":
            nombre = fake.first_name_male()
        else:
            nombre = fake.first_name_female()

        apellido = fake.last_name()

        empleado = {
            "empleado_id": empleado_id,
            "nombre": nombre,
            "apellido": apellido,
            "sexo": sexo,
            "fecha_nacimiento": fake.date_between(
                start_date="-60y",
                end_date="-20y"
            ),
            "fecha_alta": fake.date_between(
                start_date="-15y",
                end_date="today"
            ),
            "departamento_id": list(distribucion_empleados.keys()).index(departamento) + 1,
            "departamento": departamento,
            "puesto": puesto,
            "salario": round(
                random.uniform(salario_min, salario_max),
                2
            ),
            "estado": random.choices(
                ["Activo", "Vacaciones", "Baja"],
                weights=[90, 5, 5],
                k=1
            )[0]
        }

        empleados.append(empleado)

        empleado_id += 1


df_empleados = pd.DataFrame(empleados)

df_empleados.to_csv(
    RUTA_RAW / "empleados.csv",
    index=False,
    encoding="utf-8-sig"
)

print("empleados.csv generado")
print(df_empleados.head())

# ------------------
# CLIENTES
# ------------------

clientes = []

for cliente_id in range(1, 2001):

    zona_id = random.choices(
        list(zonas_madrid.keys()),
        weights=pesos_zonas,
        k=1
    )[0]

    nombre_zona = zonas_madrid[zona_id]

    tipo_cliente = random.choices(
        ["Bar", "Restaurante", "Gasolinera", "Tienda", "Supermercado"],
        weights=[45, 15, 10, 20, 10],
        k=1
    )[0]

    nombre_cliente = (
        tipo_cliente +
        " " +
        fake.last_name()
    )

    cliente = {
        "cliente_id": cliente_id,
        "nombre_cliente": nombre_cliente,
        "tipo_cliente": tipo_cliente,
        "zona_id": zona_id,
        "nombre_zona": nombre_zona,
        "fecha_alta": fake.date_between(
            start_date="-10y",
            end_date="today"
        ),
        "activo": random.choices(
            ["Sí", "No"],
            weights=[90, 10],
            k=1
        )[0]
    }

    clientes.append(cliente)
    
df_clientes = pd.DataFrame(clientes)

df_clientes.to_csv(
    RUTA_RAW / "clientes.csv",
    index=False,
    encoding="utf-8-sig"
)

print("clientes.csv generado")
print(df_clientes.head())


print(len(df_clientes))

print(
    df_clientes["tipo_cliente"]
    .value_counts()
)

print(
    df_clientes["activo"]
    .value_counts()
)

print("\nClientes por zona:")
print(
    df_clientes["nombre_zona"]
    .value_counts()
)