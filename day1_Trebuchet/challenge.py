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

#function to solve part one
def extract_numeric_digits_from_string(input_str):
        extracted_digits = ""
        for char in input_str:
                if char.isdigit():
                        extracted_digits += char
        return extracted_digits

#function to solve part two
def extract_numeric_digits_and_numeric_words_from_string(input_str):
        extracted_digits = ""
        i = 0
        i_ant = i
        while i < len(input_str):
                digit_found = False
                for digit, word in numeric_digits_and_words_dict.items():
                        if input_str.startswith(digit, i):
                                digit_found = True
                                i += 1
                        elif input_str.startswith(word, i):
                                digit_found = True
                                i += (len(word) - 1)

                        if digit_found == True:
                                extracted_digits += digit
                                break
                if i == i_ant:
                        i += 1
                i_ant = i
                                
        return extracted_digits



#Puzzle solution starts here

file = open('input.txt', 'r')
lines = file.readlines()

#To solve the first part, change it to False. Otherwise keep True to solve part two.
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
        sum += int(calibration_values)

        #for debug purposes
        print(line.strip())
        print(extracted_digits)
        print(calibration_values)
        print()
        
#Result
print("Result: ")
print(sum)




        
