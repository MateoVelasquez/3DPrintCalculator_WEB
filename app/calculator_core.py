"""Módulo calculo principal

Contiene las funciones de calculo del programa.
"""
from math import pi, ceil
from typing import Dict


def language_dic() -> Dict:
    """Diccionario de lenguaje.

    Exporta un diccionario de lenguaje.

    Returns
    -------
    dict:
        Diccionario de lenguaje.
    """
    text_dic = {
        'MATERIAL_COST': "Costo del Material ($ / Kg)",
        'MATERIAL_DENSITY': 'Densidad del material (gr / cm^3)',
        'SPOOL_WEIGTH': 'Peso del núcleo de la bobina (gr)',
        'ELECTRIC_COST': 'Costo Eléctrico ( $ KW/h)',
        'PRINTER_POWER': 'Potencia de la impresora (W)',
        'PRINTER_PRICE': 'Precio de la impresora ($)',
        'AMORTIZATION': 'Amortización de la máquina (años)',
        'DAILY_PRINTER_TIME': 'Uso diario de la máquina (h)',
        'FAILURE_RATE': 'Porcentaje de fallos (%)',
        'WORKFORCE_COST': 'Costo de mano de obra',
        'ACCEPT': 'Aceptar',
        'CANCEL': 'Cancelar',
        'MAIN_TITLE': 'Calculadora de impresión 3D',
        'HOURS': 'Horas de impresión',
        'MINUTES': 'Minutos de impresión',
        'MATERIAL': 'Cantidad del material',
        'WORKMANTIME': 'Horas de mano de obra',
        'CALCULATE': 'Calcular',
        'MAT_UNIT': 'Unidad de medida del material'
    }
    return text_dic


def calculate_cost(hrs: int, mins: int, workhrs: float,
                   material: float, cfgdic: Dict) -> int:
    """Calcular costo.

    Función para calcular el costo de la impresión 3D.

    Parameters
    ----------
    hrs: int
        Hora estimada de impresión.
    mins: int
        Minutos estimados de impresión.
    workhrs: float
        Tiempo de mano de obra dedicado.
    material: float
        Material gastado en milímetros.
    cfgdic_in: Dict
        Diccionario de parámetros de configuración.

    Returns
    -------
    int:
        Costo total de la impresión 3D en la unidad configurada.
    """
    mat_in_mm = bool(int(cfgdic['measure_unit']))
    # Calculando los gramos de material.
    if mat_in_mm:
        gr = (float(cfgdic['material_density']) * pi * (1.75 / 20)**2 *
              material / 10)
    else:
        gr = material
    # Calculando tiempo completo de impresión:
    totalh = hrs + (mins / 60)
    # Calculando costo eléctrico.
    eleccost = (int(cfgdic['electric_cost']) / 1000 * totalh *
                int(cfgdic['printer_power']))
    # Calculando costo de material.
    matcost = gr * (int(cfgdic['material_cost']) /
                    (1000 - int(cfgdic['spool_weigth'])))
    # Calculando costo de mano de obra:
    workmancost = workhrs * int(cfgdic['workforce_cost'])
    # Calculando amortización de la maquina. 300 equivale a Num. de dias en uso
    amort = (int(cfgdic['printer_price']) /
             (int(cfgdic['amortization_years']) * 300 *
              int(cfgdic['daily_printer_time']))) * totalh
    # Sumando costo total de impresion.
    totalimpcost = eleccost + matcost + workmancost + amort
    # Calculando sobre porcentaje de fallas
    totalimpcost = totalimpcost * (1 + int(cfgdic['failure_rate_prcent']) / 100)
    return int(round(totalimpcost, 0))