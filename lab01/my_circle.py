# Comp1510 202010 Lab 01
# Young Kim (A01087377)

PI = 3.14159

# get input from user for radius
radius = float(input('Please enter radius: '))
double_radius = radius * 2

# calculate and print out circumference and area using radius recieved from user
circumference = 2 * PI * radius
print('The circumference is: ' + str(circumference))

area = PI * (radius**2)
print('The area is: ' + str(area))
print()

# circumference and area with doubled radius and how many times increased
double_rad_circumference = 2 * PI * double_radius
double_rad_area = PI * (double_radius**2)

inc_circumference = double_rad_circumference / circumference
inc_area = double_rad_area / area

print('The circumference with doubled radius is: ' + str(double_rad_circumference))
print('The area with doubled radius is: ' + str(double_rad_area))

print('If radius is doubled, circumference increased ' + str(inc_circumference) + ' times')
print(', and area increased ' + str(inc_area) + ' times.')


