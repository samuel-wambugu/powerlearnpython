# File Creation:
# Create a Python script (file_handling_assignment.py) that does the following:
# Creates a new text file named "my_file.txt" in write mode ('w').
# Write at least three lines of text to the file, including a mix of strings and numbers.
with open("my_file.txt", 'w') as f :
        f.write("hello my name is samuel")
        f.write("\nI am a student at powerlearningprojects in year 1 sem 2")
        f.write("\n Also a kisii university computer science student, and ths 1st university")

# File Reading and Display:
# Enhance your script to read the contents of "my_file.txt" and display them on the console.
with open("my_file.txt", 'r') as file :
       for luck in file:
            print(luck)

# File Appending:
# Modify the script to open "my_file.txt" in append mode ('a').
# Append three additional lines of text to the existing content.
with open("my_file.txt", 'a') as file1:
       file1.write("\n Hello, this is line 1")
       file1.write("\n 12345 is a number on line 2")
       file1.write("\n Line 3 contains a mix of text and numbers like 6789")




# Error Handling:
# Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError).
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")