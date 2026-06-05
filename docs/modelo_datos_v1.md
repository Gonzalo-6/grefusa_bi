# Modelo de Datos v1

## Descripción del proyecto

Tras analizar varias alternativas para el proyecto, se decidió desarrollar una plataforma de Business Intelligence para una distribuidora de snacks.

El objetivo es construir un sistema de análisis empresarial capaz de proporcionar información sobre ventas, clientes, empleados, productividad y absentismo mediante un dashboard interactivo desarrollado con Python.

La solución estará compuesta por:

- Archivos CSV para la generación inicial de datos.
- Procesos ETL desarrollados con Pandas.
- Base de datos PostgreSQL.
- Dashboard interactivo con Dash y Plotly.
- Automatizaciones mediante n8n.

## Alcance de la primera versión

La primera versión del proyecto permitirá analizar:

- Ventas.
- Clientes.
- Productos.
- Empleados.
- Productividad.
- Ausencias.

Quedan fuera del MVP:

- Vehículos.
- Rutas de reparto.
- Gestión de stock.
- Compras a proveedores.

Estas funcionalidades podrán incorporarse en futuras versiones.

## Entidades definitivas del MVP
1. Departamentos
Representa la estructura de la empresa.
Campo	Tipo	Descripción
departamento_id	int	Identificador
nombre_departamento	string	Nombre
responsable	string	Responsable
Ejemplos:
Ventas
Logística
Almacén
Administración
RRHH
________________________________________
2. Empleados
Representa a los trabajadores.
Campo	Tipo
empleado_id	int
nombre	string
apellido	string
sexo	string
fecha_nacimiento	date
fecha_alta	date
departamento_id	int
puesto	string
salario	decimal
estado	string
Estado:
Activo
Baja
Vacaciones
Puestos:
Comercial
Repartidor
Mozo almacén
Administrativo
Supervisor
________________________________________
3. Clientes
Representa a los negocios que compran productos.
Campo	Tipo
cliente_id	int
nombre_cliente	string
tipo_cliente	string
zona	string
ciudad	string
fecha_alta	date
Tipos:
Bar
Restaurante
Gasolinera
Supermercado
Kiosco
Tienda
________________________________________
4. Productos
Productos distribuidos.
Campo	Tipo
producto_id	int
nombre_producto	string
marca	string
categoria	string
coste	decimal
precio_venta	decimal
Categorías:
Pipas
Frutos secos
Snacks
Palomitas
Mix
________________________________________
5. Fechas
Tabla fundamental para BI.
fecha_id
fecha
dia
mes
nombre_mes
mes_corto
trimestre
año
semana
dia_semana
es_fin_semana
es_festivo
tipo_dia
________________________________________
Tablas de hechos
Aquí ocurre el negocio.
________________________________________
6. Ventas
Cada fila será un producto vendido.
Campo	Tipo
venta_id	int
fecha_id	int
cliente_id	int
producto_id	int
empleado_id	int
cantidad	int
importe	decimal
beneficio	decimal
Ejemplo:
05/03/2025
Bar Pepe
Pipas G
10 cajas
120 €
________________________________________
7. Ausencias
Campo	Tipo
ausencia_id	int
fecha_id	int
empleado_id	int
tipo_ausencia	string
horas_ausencia	decimal
Tipos:
Vacaciones
Baja médica
Permiso
Formación
________________________________________
8. Productividad
Aquí mediremos el rendimiento.
Campo	Tipo
productividad_id	int
fecha_id	int
empleado_id	int
pedidos_entregados	int
clientes_visitados	int
ventas_generadas	decimal
horas_trabajadas	decimal


## KPIs que podremos construir
Dirección
•	Facturación total 
•	Beneficio total 
•	Margen % 
•	Clientes activos 
________________________________________
Comercial
•	Ventas por comercial 
•	Ventas por zona 
•	Clientes captados 
________________________________________
RRHH
•	Tasa de absentismo 
•	Horas perdidas 
•	Productividad por empleado 
•	Productividad por departamento 
________________________________________
Productos
•	Top ventas 
•	Top rentabilidad 
•	Productos con menor rotación 
________________________________________


## Estructura de carpetas recomendada
Desde el principio.
proyecto_bi_distribuidora/

│
├── data/
│   ├── raw/
│   ├── processed/
│
├── dashboard/
│
├── etl/
│
├── database/
│
├── docs/
│
├── diario_proyecto/
│
└── notebooks/
________________________________________


## tabla productos

Campo	            Tipo	Descripción
producto_id     	int	    Identificador del producto
nombre_producto	    string	Nombre comercial
categoria	        string	Categoría del producto
marca	            string	Marca
coste	            decimal	Coste unitario
precio_venta	    decimal	Precio unitario de venta
margen_bruto_pct	decimal	Margen bruto expresado en porcentaje (58.79 = 58,79 %)
popularidad	        int	    Índice relativo de popularidad
temporada_fuerte	string	Época de mayor demanda