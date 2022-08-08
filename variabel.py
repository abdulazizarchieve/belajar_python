#latihan 1
my_name = 'Abdul Aziz'
my_age = 23 #thn
my_height = 69 # cm
my_weight = 60 # kg
my_eyes = 'Brown'
my_teeth = 'white'
my_hair = 'Black'


print('my name is', my_name)
print(f"He's {my_height} cm tall")
print(f"He's {my_weight} kg heavy")
print(f"He's got {my_eyes} and {my_hair} hair")
print("His teeth are usually {} depending on the coffe.". format(my_teeth))
print(f"If i add {my_age}, {my_height},and {my_weight} then I get, {my_age + my_height + my_weight}")



cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print('There are', cars, 'cars available.')
print('There are only', drivers, 'drivers available')
print('There will be', cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, 'to carpool today.')
print('we need to put about', average_passengers_per_car, 'in each car')

