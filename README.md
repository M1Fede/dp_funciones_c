# dp_funciones_c
Es una librería que contiene funciones propias, utilizadas en el repositorio 'Reporte-rendimiento'.

Contiene funciones útiles para tre tipos de ALYCS:
1) Composición de cartera: Genera un dataframe con la composición de cartera del cliente elegido, para una fecha indicada y desde una máquina con el permiso para hacerlo. Este dataframe contiene el ticket, las cantidades, los precios en la fecha indicada, y las operaciones mep realizadas hasta el momento (claro que también especifica la liquidez).
2) Honorarios: Calcula los honorarios que debe para el cliente en cualquier fecha indicada, aunque siempre respeta la 'fecha de corte' donde el cliente cumple los 30 días desde el último pago. El honorario calculado es ajustado por los depósitos y retiros que el cliente realizó durante los últimos 30 días posteriores al último pago. Además, los honorarios varían de acuerdo al valor del portafolio y su composición de acuerdo a la clase de activos que componen la cartera.
3) Rendimiento bruto y neto. Calcula en rendimiento bruto y neto para un período particular. Este código calcula el rendimiento neto sólo con un honorario, no con todos los que corresponden al período de análisis. 
4) Rendimiento bruto y neto estilizado. Realiza lo mismo que el código anterior, pero lo hace teniendo en cuenta todos los honorarios pagados durante el período elegido (asume cobro mensual de honorarios).
5) Archivo ejecutable: Script útil para generar una interfaz para que no sea necesario utilizar el entorno de desarrollo para calcular honorarios, por ejemplo.
6) Movimientos. Genera un dataframe con los retiros y los depósitos que el cliente realizó durante el período indicado.
7) Operaciones. Genera un dataframe con las operaciones históricas que el cliente realizó.
8) Split de acciones. Genera un dataframe útil para incoporar los split ocurridos en el mercado.
9) Gráficas. Genera tres tipos de gráficas, una de torta para la composición, otra de barras para los rendimientos mensuales, y otra de líneas para la evolución en pesos y en dólares de la cartera.
10) No recuerdo si hay más.
