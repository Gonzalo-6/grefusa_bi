import random
import pandas as pd
from pathlib import Path

# ------------------
# RUTAS
# ------------------

BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_RAW = BASE_DIR / "data" / "raw"

# ------------------
# CARGAR DIMENSIONES
# ------------------

df_clientes = pd.read_csv(
    RUTA_RAW / "clientes.csv"
)

df_productos = pd.read_csv(
    RUTA_RAW / "productos.csv"
)

df_empleados = pd.read_csv(
    RUTA_RAW / "empleados.csv"
)

df_fechas = pd.read_csv(
    RUTA_RAW / "fechas.csv"
)

print("Clientes:", len(df_clientes))
print("Productos:", len(df_productos))
print("Empleados:", len(df_empleados))
print("Fechas:", len(df_fechas))

# ------------------
# FUNCIONES
# ------------------

def cliente_puede_comprar(cliente, fecha_pedido):

    fecha_alta = pd.to_datetime(
        cliente["fecha_alta"]
    )

    if fecha_pedido < fecha_alta:
        return False

    if cliente["activo"] == "Sí":
        return True

    if pd.isna(cliente["fecha_baja"]):
        return False

    fecha_baja = pd.to_datetime(
        cliente["fecha_baja"]
    )

    return fecha_pedido <= fecha_baja

def calcular_peso_producto(producto, fecha_pedido):

    peso = producto["popularidad"]

    mes = fecha_pedido.month

    categoria = producto["categoria"]

    # Verano
    if mes in [6, 7, 8]:

        if categoria == "Palomitas":
            peso *= 4

    # Invierno
    if mes in [12, 1, 2]:

        if categoria == "Frutos Secos":
            peso *= 4

    # Navidad
    if mes == 12:

        if categoria == "Mix":
            peso *= 9

    return peso

# ------------------
# FILTRAR FECHAS
# ------------------

df_fechas_validas = df_fechas[
    df_fechas["tipo_dia"] == "Laborable"
].copy()

print(
    "Fechas válidas:",
    len(df_fechas_validas)
)

# ------------------
# FILTRAR COMERCIALES
# ------------------

df_comerciales = df_empleados[
    df_empleados["puesto"] == "Comercial"
].copy()

print(
    "Comerciales:",
    len(df_comerciales)
)

#------------------
# CLIENTES
#------------------

while True:

    cliente = df_clientes.sample(1).iloc[0]

    fecha = df_fechas_validas.sample(1).iloc[0]

    fecha_pedido = pd.to_datetime(
        fecha["fecha"]
    )

    if cliente_puede_comprar(
        cliente,
        fecha_pedido
    ):
        break

print("\nCliente prueba:")
print(cliente)

print(df_clientes.columns.tolist())

print("\nClientes inactivos:")

print(
    df_clientes["activo"]
    .value_counts()
)

# ------------------
# CONFIGURACIÓN
# ------------------

NUM_PEDIDOS_PRUEBA = 1000

rangos_cantidad = {
    "Bar": (2, 12),
    "Restaurante": (2, 10),
    "Gasolinera": (5, 20),
    "Tienda": (4, 20),
    "Supermercado": (10, 50)
}

ventas = []

venta_id = 1
pedido_id = 100001



# ------------------
# PEDIDOS DE PRUEBA
# ------------------

for _ in range(NUM_PEDIDOS_PRUEBA):

    while True:

        cliente = df_clientes.sample(1).iloc[0]

        fecha = df_fechas_validas.sample(1).iloc[0]

        fecha_pedido = pd.to_datetime(
             fecha["fecha"]
        )

        if cliente_puede_comprar(
            cliente,
            fecha_pedido
        ):
            
            break



    num_productos = random.choices(
        [1, 2, 3, 4, 5, 6],
        weights=[10, 25, 30, 20, 10, 5],
        k=1
    )[0]

    pesos_productos = df_productos.apply(
        lambda x: calcular_peso_producto(
            x,
            fecha_pedido
        ),
        axis=1
    )

    productos_pedido = df_productos.sample(
        n=num_productos,
        replace=True,
        weights=pesos_productos
    )

    estado_pedido = random.choices(
        ["Entregado", "Incidencia", "Cancelado"],
        weights=[97, 2, 1],
        k=1
    )[0]

    dias_entrega = random.choice([1, 2, 3])

    fecha_entrega = pd.to_datetime(
        fecha["fecha"]
    ) + pd.Timedelta(days=dias_entrega)

    for _, producto in productos_pedido.iterrows():

        minimo, maximo = rangos_cantidad[
            cliente["tipo_cliente"]
        ]

        cantidad = random.randint(
            minimo,
            maximo
        )

        precio_unitario = producto["precio_venta"]

        coste_unitario = producto["coste"]

        importe = round(
            cantidad * precio_unitario,
            2
        )

        coste_total = round(
            cantidad * coste_unitario,
            2
        )

        beneficio = round(
            importe - coste_total,
            2
        )

        ventas.append({

            "venta_id": venta_id,

            "pedido_id": pedido_id,

            "fecha_id": fecha["fecha_id"],

            "fecha_entrega": fecha_entrega.date(),

            "cliente_id": cliente["cliente_id"],

            "empleado_id": cliente["empleado_id"],

            "producto_id": producto["producto_id"],

            "cantidad": cantidad,

            "precio_unitario": precio_unitario,

            "coste_unitario": coste_unitario,

            "importe": importe,

            "coste_total": coste_total,

            "beneficio": beneficio,

            "estado_pedido": estado_pedido,

            "dias_entrega": dias_entrega
        })

        venta_id += 1

    pedido_id += 1

df_ventas = pd.DataFrame(ventas)

df_ventas["fecha"] = pd.to_datetime(
    df_ventas["fecha_id"].astype(str),
    format="%Y%m%d"
)

df_ventas["mes"] = df_ventas["fecha"].dt.month

df_estacionalidad = df_ventas.merge(
    df_productos[
        ["producto_id", "categoria"]
    ],
    on="producto_id"
)



print("\nVENTAS DE PRUEBA")
print(df_ventas.head(20))

print("\nNúmero de líneas:")
print(len(df_ventas))

print("\nNúmero de pedidos:")
print(df_ventas["pedido_id"].nunique())

print("\nEstado pedidos:")
print(
    df_ventas["estado_pedido"]
    .value_counts()
)

print("\nProductos seleccionados:")

#print(
#    df_ventas["producto_id"]
#   .value_counts()
#)

print(
    df_ventas.groupby("producto_id")
    .size()
    .sort_values(ascending=False)
)

print(
    pd.crosstab(
        df_estacionalidad["mes"],
        df_estacionalidad["categoria"]
    )
)

 