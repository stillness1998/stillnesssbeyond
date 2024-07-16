# complex_numbers.py

def main():
    # Creating complex numbers using literals
    z1 = 3 + 2j
    z2 = complex(4, -1)  # Using the complex() factory function

    # Accessing real and imaginary parts
    print(f"z1 = {z1} (Real part: {z1.real}, Imaginary part: {z1.imag})")
    print(f"z2 = {z2} (Real part: {z2.real}, Imaginary part: {z2.imag})")

    # Basic arithmetic operations
    addition_result = z1 + z2
    subtraction_result = z1 - z2
    multiplication_result = z1 * z2
    division_result = z1 / z2

    print(f"z1 + z2 = {addition_result}")
    print(f"z1 - z2 = {subtraction_result}")
    print(f"z1 * z2 = {multiplication_result}")
    print(f"z1 / z2 = {division_result}")

    # Calculating the magnitude (absolute value) of a complex number
    magnitude_z1 = abs(z1)
    print(f"Magnitude of z1: {magnitude_z1}")

    # Converting between rectangular and polar coordinates
    polar_z1 = cmath.polar(z1)
    print(f"Polar form of z1: {polar_z1}")

if __name__ == "__main__":
    import cmath  # Import the complex math module
    main()
