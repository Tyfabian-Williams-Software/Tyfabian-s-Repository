# Tyfabian Williams
# 2142655

oil_change = 35
tire_rotation = 19
car_wash = 7
car_wax = 12
no_service = 0
total = 0
print('Davy\'s auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12\n')

service_1 = input('Select first service:\n')
service_2 = input('Select second service:\n')
print()
print('Davy\'s auto shop invoice\n')


if service_1 == 'Oil change':
    total += oil_change
    print(f'Service 1: Oil change, ${oil_change}')
elif service_1 == 'Tire rotation':
    total += tire_rotation
    print(f'Service 1: Tire rotation, ${tire_rotation}')
elif service_1 == 'Car wash':
    total += car_wash
    print(f'Service 1: Car wash, ${car_wash}')
elif service_1 == 'Car wax':
    total += car_wax
    print(f'Service 1: Car wax, ${car_wax}')
elif service_1 == '-':
    total += no_service
    print('Service 1: No service')

if service_2 == 'Oil change':
    total += oil_change
    print(f'Service 2: Oil change, ${oil_change}')
elif service_2 == 'Tire rotation':
    total += tire_rotation
    print(f'Service 2: Tire rotation, ${tire_rotation}')
elif service_2 == 'Car wash':
    total += car_wash
    print(f'Service 2: Car wash, ${car_wash}')
elif service_2 == 'Car wax':
    total += car_wax
    print(f'Service 2: Car wax, ${car_wax}')
elif service_2 == '-':
    total += no_service
    print('Service 2: No service')

print()
print(f'Total: ${total}')
