import sys

file = open('input.txt', 'r')
lines = file.readlines()

sum = 0

for line in lines:
        all_digits = ""
        calibration_values = ""
        print(line.strip())
        for char in line:
                if char.isdigit():
                        all_digits += char
        print(all_digits)

        calibration_values = all_digits[0] + all_digits[(all_digits.__len__()) - 1]
        print(calibration_values)
        sum += int(calibration_values)
        print()

print()
print(sum)



                
        
