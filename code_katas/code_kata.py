# Esempio di script Python ben scritto 3

def calculate_square_area(side_length):
    """Calcola l'area di un quadrato."""
    if side_length <= 0:
        raise ValueError("La lunghezza del lato deve essere positiva.")
    return side_length ** 2

def main():
    """Funzione principale."""
    try:
        side_length = float(input("Inserisci la lunghezza del lato del quadrato: "))
        area = calculate_square_area(side_length)
        print(f"L'area del quadrato è: {area}")
    except ValueError as e:
        print(f"Errore: {e}")
    except Exception as e:
        print(f"Si è verificato un errore imprevisto: {e}")

if _name_ == "_main_":
    main()
