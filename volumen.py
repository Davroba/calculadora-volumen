
def calcular_volumen(largo, ancho, alto):
    return largo * ancho * alto

largo = 120
ancho = 80
alto = 50

densidad = 0.95  # g/cm3
precio_kg = 2.50  # euros por kg

volumen_mm3 = calcular_volumen(largo, ancho, alto)
volumen_cm3 = volumen_mm3 / 1000

masa_gramos = volumen_cm3 * densidad
masa_kg = masa_gramos / 1000

coste = masa_kg * precio_kg

print("Volumen:", volumen_cm3, "cm3")
print("Masa:", masa_gramos, "gramos")
print("Coste del material:", coste, "euros")
