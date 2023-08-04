""" 
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
"""
import datetime

def friday_thirteen(year: int, month: int) -> bool:
    try:
        # weekday() return day of the week, where Monday == 0 ... Sunday == 6.
        return datetime.date(year,month,13).weekday() == 4
    except: 
        return False

print(friday_thirteen(2023,10))
print(friday_thirteen(2024,2))