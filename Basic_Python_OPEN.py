'''
Purpose: Understaning the Basics of file handling in python
Reqiurements: Importing Import os module  from the os module using functions os()
Basic syntax of open function:
open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

types of mode:
r=open the file for reading
w=open the file for writing, truncating the file first, meaing of trunctaing:"re-sizeing of the existing file
x=open for the exclusive creation,failing if the file already exists
a=appending the file, adding content at the end of the file,if file exists only
t=text mode 
b=binary mode
+=open for updating(reading and writing) 
'''
#creating the file with name dummy_file extention .txt

file_write=open("dummy_file.txt","w")
write_content=input("Enter some content for the file")
file_write.write(write_content)
file_write.close()

#Observation: while performing one operations to the file we cannot do another operation simulteniously to same file after closing the method we can do
#Reading file
file_read=open("dummy_file.txt","r")
s=file_read.read()
print(s)
file_read.close()

#Appending the file or adding content to the file if file exis

file_append=open("simple.txt","a")
