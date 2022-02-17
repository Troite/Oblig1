import fileinput

file = input("Enter filename: ")  # Input for the filename

old = input(
    "Enter old string to be replaced: "
)  # Input for the old string you want to replace

new = input(
    "Enter the new string to replace the old string: "
)  # Input for the new string you want to put in


fin = open(file, "rt")  # Opens the input file in read text mode

data = fin.read()  # Reads the file to the variable "data"

data = data.replace(
    old, new
)  # Replaces all occurrences of the "Old" string with the "New" string

fin.close()  # Closes the input file

fin = open(
    file, "wt"
)  # This time we do the same as above, but open it in read mode to "physically" change the old and new strings

fin.write(data)  # Writes the "data" string we have from above into the "old" string

fin.close()
