<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Aplicar Formato Condicional en Excel con Python</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 15px;
            border-left: 3px solid #0078D4;
        }
        .note {
            background-color: #ffffcc;
            padding: 10px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <h1>Aplicar Formato Condicional en Excel con Python</h1>
    <p>Este documento proporciona una guía sobre cómo utilizar la biblioteca <code>openpyxl</code> en Python para aplicar formato condicional en un archivo Excel. El formato condicional cambia la apariencia de las celdas basado en ciertas condiciones, como el valor de la celda.</p>
    
    <h2>Instalación de <code>openpyxl</code></h2>
    <p>Primero, asegúrate de tener instalada la biblioteca <code>openpyxl</code>. Si no la tienes, puedes instalarla usando pip:</p>
    <pre>pip install openpyxl</pre>
    
    <h2>Creando un Archivo Excel y Aplicando Formato Condicional</h2>
    <p>A continuación, se muestra cómo crear un archivo Excel y aplicar formato condicional para cambiar el color de las celdas basado en sus valores:</p>
    <pre>
from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import PatternFill

wb = Workbook()
ws = wb.active

# Asumiendo que has agregado tus datos aquí
ws['A1'] = 'Estado'
ws['A2'] = 'Verdadero'
ws['A3'] = 'Falso'

# Aplica el formato condicional
ws.conditional_formatting.add('A2:A3',
    CellIsRule(operator='equal', formula=['"Verdadero"'], fill=PatternFill(start_color='00FF00', end_color='00FF00', fill_type='solid')))
ws.conditional_formatting.add('A2:A3',
    CellIsRule(operator='equal', formula=['"Falso"'], fill=PatternFill(start_color='FF0000', end_color='FF0000', fill_type='solid')))

wb.save('resultados_ping.xlsx')
    </pre>

    <div class="note">
        <strong>Nota:</strong> Este código aplica formato condicional a las celdas A2 y A3 basado en si su contenido es "Verdadero" o "Falso". Las celdas con "Verdadero" se llenarán de verde, y las celdas con "Falso" de rojo.
    </div>

    <h2>Conclusión</h2>
    <p>Usando <code>openpyxl</code>, puedes automatizar no solo la creación de archivos Excel y la adición de datos, sino también la aplicación de formatos condicionales complejos. Esto puede ser especialmente útil para reportes que requieran un análisis visual rápido de los datos.</p>
</body>
</html>