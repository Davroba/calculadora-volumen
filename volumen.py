
def calcular_volumen(largo, ancho, alto):
    return largo * ancho * alto

largo = 120
ancho = 80
alto = 50

densidad = 0.95  # g/cm3

volumen_mm3 = calcular_volumen(largo, ancho, alto)
volumen_cm3 = volumen_mm3 / 1000
masa = volumen_cm3 * densidad

print("Volumen:", volumen_cm3, "cm3")
print("Masa:", masa, "gramos")
