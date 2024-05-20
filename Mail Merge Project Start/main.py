PLACEHOLDER = "[Name]"

with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    # print(names_list)

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contain = letter.read()
    for name in names_list:
        strip_name = name.strip()
        final_letter = letter_contain.replace(PLACEHOLDER, strip_name)
        print(final_letter)
        with open(f"./Output/ReadyToSend/news_for_{strip_name}.txt", "w") as complete_mail:
            complete_mail.write(final_letter)
