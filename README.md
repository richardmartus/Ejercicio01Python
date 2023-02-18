# Ejercicio01-T1A1
## Etapa 01. Descripción del problema
Se requiere un programa para convertir una cantidad de dinero en otros tipos de monedas (al menos a cinco tipos de monedas distintas). 
## Etapa 02. Definición de la solución
~~~ Entrada
  float moneda, conversion
  String Movimiento, secondMovimiento, answer
  double conversion
  bool endConversion
  list rules
  
- Proceso
  Solicitar cantidad a convertir
  Solicitar moneda a convertir
  Solicitar moneda para procesar conversión
   
  Si el monto es mayor o igual que cero entonces se convertirá a la moneda deseada
  Si el monto es menor que cero entonces se cancela la operación
 
- Salida
  
  +----------+---------------+---------------------+------------------+
  | CANTIDAD | MONEDA ORIGEN |    MONEDA DESTINO   | CANT. CONVERTIDA |
  +----------+---------------+---------------------+------------------+
  |    1000  |       UY      |        US           |       26.0       |
  +----------+---------------+---------------------+------------------+
  |    1000  |       UY      |        BR           |      140.0       |
  +----------+---------------+---------------------+------------------+
  
  ~~~
## Etapa 03. Diseño la solución
![Diagrama](https://github.com/richardmartus/Ejercicio01Python/blob/main/.idea/Diagrama%20de%20clases01.png)


## Etapa 04. Desarrollo de la solución
Código disponeble en el archivo main.py

## Etapa 05. Depuración y Pruebas

## Etapa 06. Documentación