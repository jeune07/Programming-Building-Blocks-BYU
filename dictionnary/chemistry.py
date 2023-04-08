def make_periodic_table():
    periodic_table = [
        {"symbol": "H", "name": "Hydrogen", "atomic_mass": 1.008},
        {"symbol": "He", "name": "Helium", "atomic_mass": 4.003},
        {"symbol": "Li", "name": "Lithium", "atomic_mass": 6.941},
        {"symbol": "Be", "name": "Beryllium", "atomic_mass": 9.012},
        {"symbol": "B", "name": "Boron", "atomic_mass": 10.81},
        {"symbol": "C", "name": "Carbon", "atomic_mass": 12.01},
        {"symbol": "N", "name": "Nitrogen", "atomic_mass": 14.01},
        {"symbol": "O", "name": "Oxygen", "atomic_mass": 16.00},
        {"symbol": "F", "name": "Fluorine", "atomic_mass": 19.00},
        {"symbol": "Ne", "name": "Neon", "atomic_mass": 20.18},
        {"symbol": "Na", "name": "Sodium", "atomic_mass": 22.99},
        {"symbol": "Mg", "name": "Magnesium", "atomic_mass": 24.31},
        {"symbol": "Al", "name": "Aluminum", "atomic_mass": 26.98},
        {"symbol": "Si", "name": "Silicon", "atomic_mass": 28.09},
        {"symbol": "P", "name": "Phosphorus", "atomic_mass": 30.97},
        {"symbol": "S", "name": "Sulfur", "atomic_mass": 32.07},
        {"symbol": "Cl", "name": "Chlorine", "atomic_mass": 35.45},
        {"symbol": "Ar", "name": "Argon", "atomic_mass": 39.95},
        {"symbol": "K", "name": "Potassium", "atomic_mass": 39.10},
        {"symbol": "Ca", "name": "Calcium", "atomic_mass": 40.08},
        
    ]
    return periodic_table


def main():
    
    molecule = input("Enter the chemical formula for a molecule: ")
    mass = float(input("Enter the mass of the chemical sample in grams: "))

    
    periodic_table = make_periodic_table()

    
    for element in periodic_table:
        symbol = element["symbol"]
        count = molecule.count(symbol)
        if count > 0:
            name = element["name"]
            atomic_mass = element["atomic_mass"]
            total_mass = count * atomic_mass
            print(name, total_mass)

    
    print("Total mass of the molecule:", mass, "grams")


if __name__ == '__main__':
    main()
