import sys

numeric_digits_and_words_dict = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
}

#function to part one
def extract_numeric_digits_from_string(input_str):
        extracted_digits = ""
        for char in input_str:
                if char.isdigit():
                        extracted_digits += char
        return extracted_digits

#function to part two
def extract_numeric_digits_and_numeric_words_from_string(input_str):
        extracted_digits = ""
        i = 0
        i_ant = i
        while i < len(input_str):
                if input_str[i].isdigit():
                        extracted_digits += input_str[i]
                else:
                        for digit, word in numeric_digits_and_words_dict.items():
                                if input_str.startswith(word, i):
                                        extracted_digits += digit
                                        i = i+len(word) - 1
                                        print("here")
                                        break
                if i == i_ant:
                        i += 1
                i_ant = i      
        return extracted_digits


#Solution starts here

file = open('input.txt', 'r')
lines = file.readlines()

#To solve the first part, change it to True. Otherwise keep false to solve part two.
part_two = True

sum = 0

for line in lines:
        extracted_digits = ""
        calibration_values = ""
        if part_two == False:
                extracted_digits = extract_numeric_digits_from_string(line)
        else:
                extracted_digits = extract_numeric_digits_and_numeric_words_from_string(line)

        calibration_values = extracted_digits[0] + extracted_digits[(len(extracted_digits))- 1]
        #for debug purposes
        print(line.strip())
        print(extracted_digits)
        print(calibration_values)

        sum += int(calibration_values)
        print()

#Result
print()
print("Sum Result: ")
print(sum)




        
