input_number_num = int(input("Please input a number: "))
num_digits = len(str(input_number_num))
result = 0
for digit in str(input_number_num):
  exp = int(digit) ** num_digits
  result += exp

if result == input_number_num:
  print("This is a Armstrong number")
else:
  print("This is not a Armstrong number")
