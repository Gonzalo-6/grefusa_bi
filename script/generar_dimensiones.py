import random
import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
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

# ------------------
# COMERCIALES POR ZONA
# ------------------

comerciales = df_empleados[
    df_empleados["puesto"] == "Comercial"
].reset_index(drop=True)

asignacion_zonas = {
    1: comerciales.iloc[0]["empleado_id"],   # Madrid Centro
    2: comerciales.iloc[1]["empleado_id"],   # Madrid Norte
    3: comerciales.iloc[2]["empleado_id"],   # Madrid Sur
    4: comerciales.iloc[3]["empleado_id"],   # Madrid Este
    5: comerciales.iloc[4]["empleado_id"],   # Madrid Oeste
    6: comerciales.iloc[5]["empleado_id"],   # Alcobendas
    7: comerciales.iloc[6]["empleado_id"],   # San Sebastián
    8: comerciales.iloc[7]["empleado_id"],   # Getafe
    9: comerciales.iloc[7]["empleado_id"],   # Leganés
    10: comerciales.iloc[8]["empleado_id"],  # Móstoles
    11: comerciales.iloc[8]["empleado_id"],  # Alcorcón
    12: comerciales.iloc[9]["empleado_id"]   # Fuenlabrada
}

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

    empleado_id = asignacion_zonas[zona_id]

    comercial = df_empleados.loc[
         df_empleados["empleado_id"] == empleado_id
    ].iloc[0]

    nombre_comercial = (
        comercial["nombre"]
        + " "
        + comercial["apellido"]
    )


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

    fecha_alta = fake.date_between(
        start_date="-10y",
        end_date=datetime(2025, 12, 31).date()
    )

    activo = random.choices(
        ["Sí", "No"],
        weights=[90, 10],
        k=1
    )[0]

    # Fecha de baja para clientes inactivos

    if activo == "No":

        fecha_baja = fake.date_between(
            start_date=fecha_alta,
            end_date=datetime(2025, 12, 31).date()
        )

    else:

        fecha_baja = None

    cliente = {
        "cliente_id": cliente_id,
        "nombre_cliente": nombre_cliente,
        "tipo_cliente": tipo_cliente,

        "zona_id": zona_id,
        "nombre_zona": nombre_zona,

        "empleado_id": empleado_id,
        "nombre_comercial": nombre_comercial,

        "activo": activo,
        "fecha_alta": fecha_alta,
        "fecha_baja": fecha_baja
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

print("\nNúmero de clientes:")
print(len(df_clientes))

print("\nTipos de cliente:")
print(
    df_clientes["tipo_cliente"]
    .value_counts()
)

print("\nClientes activos:")
print(
    df_clientes["activo"]
    .value_counts()
)

print("\nClientes por zona:")
print(
    df_clientes["nombre_zona"]
    .value_counts()
)

print("\nClientes con fecha de baja:")
print(
    df_clientes["fecha_baja"]
    .notna()
    .sum()
)
print(
    df_clientes[
        [
            "nombre_cliente",
            "nombre_zona",
            "nombre_comercial"
        ]
    ].head(20)
)

# ------------------
# PRODUCTOS
# ------------------

productos = []

catalogo_productos = {
    "Pipas": [
        "Pipas Original",
        "Pipas Tijuana",
        "Pipas Agua Sal",
        "Pipas XXL",
        "Pipas Gigantes"
    ],

    "Frutos Secos": [
        "Almendras",
        "Cacahuetes",
        "Anacardos",
        "Pistachos",
        "Avellanas",
        "Nueces"
    ],

    "Snacks": [
        "Gublins Jamón",
        "Gublins Queso",
        "Papa Delta Original",
        "Papa Delta Campesinas",
        "Papa Delta Barbacoa",
        "Snack Mix"
    ],

    "MisterCorn": [
        "MisterCorn Original",
        "MisterCorn BBQ",
        "MisterCorn Picante",
        "MisterCorn Queso"
    ],

    "Mix": [
        "Cocktail",
        "Mix Energy",
        "Mix Premium",
        "Mix Frutos Secos"
    ],

    "Palomitas": [
        "Palomitas Mantequilla",
        "Palomitas Dulces",
        "Palomitas Saladas"
    ]
}

popularidades = {
    "Pipas Original": 10,
    "Pipas Tijuana": 9,
    "Pipas Agua Sal": 8,

    "MisterCorn Original": 8,
    "MisterCorn BBQ": 7,

    "Cocktail": 6,

    "Palomitas Dulces": 3
}

temporadas = {
    "Pipas": "Todo el año",
    "Frutos Secos": "Invierno",
    "Snacks": "Todo el año",
    "MisterCorn": "Todo el año",
    "Mix": "Navidad",
    "Palomitas": "Verano"
}

rangos_coste = {
    "Pipas": (0.60, 1.20),
    "Frutos Secos": (1.00, 2.50),
    "Snacks": (0.70, 1.80),
    "MisterCorn": (0.80, 1.60),
    "Mix": (1.20, 2.80),
    "Palomitas": (0.50, 1.30)
}

producto_id = 1

for categoria, lista_productos in catalogo_productos.items():

    for nombre_producto in lista_productos:

        coste_min, coste_max = rangos_coste[categoria]

        coste = round(
            random.uniform(coste_min, coste_max),
            2
        )

        precio_venta = round(
            coste * random.uniform(1.6, 2.8),
            2
        )

        margen_bruto_pct = round(
            ((precio_venta - coste) / precio_venta) * 100,
            2
        )

        popularidad = popularidades.get(
            nombre_producto,
            5
        )

        producto = {
    "producto_id": producto_id,
    "nombre_producto": nombre_producto,
    "categoria": categoria,
    "marca": "Grefusa",
    "coste": coste,
    "precio_venta": precio_venta,
    "margen_bruto_pct": margen_bruto_pct,
    "popularidad": popularidad,
    "temporada_fuerte": temporadas[categoria]
}

        productos.append(producto)

        producto_id += 1

df_productos = pd.DataFrame(productos)

df_productos.to_csv(
    RUTA_RAW / "productos.csv",
    index=False,
    encoding="utf-8-sig"
)

print("productos.csv generado")
print(df_productos.head())

print("\nProductos por categoría:")
print(
    df_productos["categoria"]
    .value_counts()
)

print(
    df_productos[
        ["nombre_producto",
         "coste",
         "precio_venta",
         "margen_bruto_pct"]
    ]
)

# ------------------
# FECHAS
# ------------------



fechas = []

fecha_inicio = datetime(2021, 1, 1)
fecha_fin = datetime(2025, 12, 31)

fecha_actual = fecha_inicio

meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

meses_cortos = {
    1: "Ene",
    2: "Feb",
    3: "Mar",
    4: "Abr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Ago",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dic"
}

dias_semana = {
    0: "Lunes",
    1: "Martes",
    2: "Miércoles",
    3: "Jueves",
    4: "Viernes",
    5: "Sábado",
    6: "Domingo"
}

festivos_fijos = [
    (1, 1),
    (6, 1),
    (1, 5),
    (15, 8),
    (12, 10),
    (1, 11),
    (6, 12),
    (8, 12),
    (25, 12)
]

while fecha_actual <= fecha_fin:

    fecha_id = int(
        fecha_actual.strftime("%Y%m%d")
    )

    trimestre = ((fecha_actual.month - 1) // 3) + 1

    es_fin_semana = (
        "Sí"
        if fecha_actual.weekday() >= 5
        else "No"
    )

    es_festivo = (
        "Sí"
        if (
            fecha_actual.day,
            fecha_actual.month
        ) in festivos_fijos
        else "No"
    )

    # Vacaciones de empresa:
    # Del 24 de diciembre al 1 de enero incluidos

    vacaciones_empresa = (
        (fecha_actual.month == 12 and fecha_actual.day >= 24)
        or
        (fecha_actual.month == 1 and fecha_actual.day == 1)
    )

    if vacaciones_empresa:
        tipo_dia = "Vacaciones Empresa"

    elif es_festivo == "Sí":
        tipo_dia = "Festivo"

    elif fecha_actual.weekday() >= 5:
        tipo_dia = "Fin de semana"

    else:
        tipo_dia = "Laborable"

    registro = {
        "fecha_id": fecha_id,
        "fecha": fecha_actual.date(),
        "dia": fecha_actual.day,
        "mes": fecha_actual.month,
        "nombre_mes": meses[fecha_actual.month],
        "mes_corto": meses_cortos[fecha_actual.month],
        "trimestre": trimestre,
        "año": fecha_actual.year,
        "semana": fecha_actual.isocalendar().week,
        "dia_semana": dias_semana[
            fecha_actual.weekday()
        ],
        "es_fin_semana": es_fin_semana,
        "es_festivo": es_festivo,
        "tipo_dia": tipo_dia
    }

    fechas.append(registro)

    fecha_actual += timedelta(days=1)

df_fechas = pd.DataFrame(fechas)

df_fechas.to_csv(
    RUTA_RAW / "fechas.csv",
    index=False,
    encoding="utf-8-sig"
)

print("fechas.csv generado")
print(df_fechas.head())

print("\nNúmero de fechas:")
print(len(df_fechas))

print("\nTipos de día:")
print(
    df_fechas["tipo_dia"]
    .value_counts()
)