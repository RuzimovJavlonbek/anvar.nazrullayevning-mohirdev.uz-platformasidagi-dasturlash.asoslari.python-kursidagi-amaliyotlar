cars = list(('toyota' , 'mazda', 'hyundai','gm' , 'kia'))

for car in cars:
  if car != 'gm':
    print(car.title())
  else:
    print(car.upper())

input()
