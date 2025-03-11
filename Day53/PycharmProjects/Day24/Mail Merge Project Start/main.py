with open("Input/Letters/starting_letter.txt") as letter:
    letter_names = letter.read()
    with open("Input/Names/invited_names.txt") as invited:
        people = invited.readlines()
        for each_name in people:
            cleaned_name = each_name.strip()
            invited_ppl = letter_names.replace("[name]", f"{cleaned_name}")
            with open(f"output/ReadyToSend/letter_for_{cleaned_name}.txt", mode="w") as finished:
                finished.write(invited_ppl)
