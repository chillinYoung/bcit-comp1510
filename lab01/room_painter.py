# Comp1510 202010 Lab 01
# Young Kim (A01087377)

COVERAGE = 400 / 4 # square feets per cans

# get the user inputs for length, width, and height of the room
length = int(input('Enter length of the room in feet: '))
width = int(input('Enter width of the room in feet: '))
height = int(input('Enter height of the room in feet: '))

# get the user input for the nunber of coats
coats = int(input('Enter the number of coats to enter: '))

# calculate the surface area to paint and the number of cans they need
surface_area = (length * width) + (2 * length * height) + (2 * width * height)
coverage_needed = surface_area * coats
cans_of_paint_required = coverage_needed / COVERAGE

print('You need to buy ' + str(cans_of_paint_required) + ' cans of paint!')

