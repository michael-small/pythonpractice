def invertedPyramid(char, odd_number):
    space = " "
    space_numb = 0
    while odd_number > -1:
        print space_numb*space, char*odd_number
        space_numb += 1
        odd_number -= 2
