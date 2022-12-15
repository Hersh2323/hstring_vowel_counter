# goal is to count total vowel letters in input string

while True:
    try:
        goal_string_var = str(input("Enter a string of text: "))
    except ValueError:
        print("USER INPUT ERROR: Please enter a floating point number.")
        continue
    else:
        break

goal_string = goal_string_var
goal_string_length = len(goal_string)
print(goal_string_length)

vowel_counter = int(0)
for char in goal_string:
    if char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U':
        vowel_counter = vowel_counter+1

print('Input string(' + goal_string + ') has a total of: ' + str(vowel_counter) + ' letters containing A, E, I, O, U')