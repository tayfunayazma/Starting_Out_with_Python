# this program calculates an object's kinetic energy

def main():
    mass = float(input("Enter the mass of an object in kgs: "))
    velocity = float(input("Enter the object's velocity in meters per second: "))
    energy = kinetics_energy(mass, velocity)
    print("The object's kinetic energy is", format(energy, ",.2f"), "joule")
    
def kinetics_energy(m, v):
    return (1/2)*m*v**2

# call the main function    
main()