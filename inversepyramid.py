def pyramid(char, odd_number):
  space = " " 
  space_numb = 0
  while odd_number > -1:
    print space_numb*space, char*odd_number
    if char == "%":
      space_numb += 3
      odd_number -= 2
    elif char == "=":
      space_numb += 2
      odd_number -= 2
    else:
      space_numb += 1
      odd_number -= 2