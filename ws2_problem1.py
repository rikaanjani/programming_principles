# Get user input
length = float(input("Length of park (m): "))
width = float(input("Width of park (m): "))
litres_per_square_metre = float(input("Litres per square metre: "))

# Calculate litres required
litres_required = length*width*litres_per_square_metre
print("Litres required = ", litres_required)
