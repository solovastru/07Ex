#1 create file

create_file = open("names.txt", "w")
names = ["Ada", "Alan", "Isabella","Lizbeth", "Abigail", "Meltem", "Gülcan"]
create_file.write(",".join(names)) #what does join stand for?why does it work with it?
create_file.close()


#2
def transform_to_row(input_file, output_file):
    with open(input_file, 'r') as input, open(output_file, 'w') as output:
        contents = input.read()
        words = contents.split(',')
        for word in words:
            output.write(word.strip() + '\n')

print("Transformed")
transform_to_row("names.txt", "output.txt")


#3
def add_greeting(input_file, output_file):
    with open(input_file, "r") as input, open(output_file, "w") as output:
        contents = input.read()
        words = contents.split("\n")
        for word in words:
            output.write(f"Hello {word}\n")

print("Greeting added")
add_greeting('output.txt', 'greetings.txt')

#4
def strip_greeting(input_file, output_file):
    with open(input_file, "r") as f_input, open(output_file,"w") as f_output:
        content = f_input.read()
        new_content = content.replace("Hello ", "")
        f_output.write(new_content)

print("Greetings stripped")

strip_greeting("greetings.txt", "nogreetings.txt")


# combine files

data = data2 = ""
def combine_files(file1, file2, output_file):
    with open("output.txt", "r") as fp:
        data = fp.read()

    with open("greetings.txt", "r") as fp:
        data2 = fp.read()

    data += "\n"
    data += data2

    with open("combined.txt", "w") as fp:
        fp.write(data)






