import math

def calculate_cone(diameter, height):
    radius = diameter / 2

    surface_area = math.pi * radius * (radius + math.sqrt(height**2 + radius**2))

    volume = (math.pi * radius**2 * height) / 3
    
    return surface_area, volume

def main():
    diameter = float(input("Diameter of the cone's base: "))
    height = float(input("Height of the cone: "))
    
    surface_area, volume = calculate_cone(diameter, height)
    
    print(f"Surface Area is {surface_area:.4f}")
    print(f"Volume is {volume:.4f}")

if __name__ == "__main__":
    main()
