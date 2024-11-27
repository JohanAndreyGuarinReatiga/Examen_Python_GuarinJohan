from menu.calculateTax import designCalculateTax

def designSeeList():
    print("""
    ---------------------------------------------------
                        TAXES TYPES
    ---------------------------------------------------
    1. IVA (10%)
    2. Impuesto Especial (5%)
    3. Impuesto Local (8%)
    4. Otro (Personalizado)

    ¿Desea calcular un impuesto ahora?
    1. Sí (Regresar al cálculo)
    2. No (Regresar al menú principal)
    ---------------------------------------------------
    """)
    choice = input("\tElija una opción (1-2): ")
    if choice == "1":
        designCalculateTax()
    else:
        return