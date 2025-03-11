
# Opening and reading a file === this reads only the file ===
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Opening and writing on a file === this allows us to write in the file and previous contents are deleted/
# can also create the file
with open("new_file.txt", mode="w") as file:
    file.write("New text added.")

# Appending a file === this allows us to write in the file and the new contents are just added to the file
with (open("my_file.txt", mode="a") as file):
    file.write("\nNew text added.")
