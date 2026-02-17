def create_phone_number(numbers):
   numbers = numbers = [str(x) for x in numbers]
   phone_number = f"({''.join(numbers[:3])}) {''.join(numbers[3:6])}-{''.join(numbers[6:])}"
   return phone_number

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))