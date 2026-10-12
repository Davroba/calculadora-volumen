
def calcular_volumen(largo, ancho, alto):
    return largo * ancho * alto

largo = 120
ancho = 80
alto = 50

volumen_mm3 = calcular_volumen(largo, ancho, alto)
volumen_cm3 = volumen_mm3 / 1000

print("Volumen en mm³:", volumen_mm3)
print("Volumen en cm³:", volumen_cm3)
