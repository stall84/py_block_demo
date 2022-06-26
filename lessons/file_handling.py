
# open() method:
#      1st argument:  Pass the filename/path you want to open. This will return a file object.
#       2nd argument: Mode. Default is READ
#  Once you have the file open you can run write() or read() methods
# close() method: Close the file object once done, releases memory, prevent mem-leaks

# default mode is read

file = open('demo2.txt', mode='w')


file.write('Hello from Python!\n')      # Added newline character
# file.close()    # This close statement added after input created to demonstrate it's need

# Python interpreter will automatically close your file when the scrtpt ends (when end of file is reached)
# However consider a situation where we do something like:
# input = input('Waiting for user input...')

# Now the file will never be written to unless you use an explicit close statemen. Like:


# 'w'Write mode will always overwrite the file completely.
# Use 'a'Append in places where overwrite not wanted

file.write('Hello Again!\n')
file.write('Hello Again!\n')

file.close()

main_file = open('demo.txt', mode='r')
main = main_file.read()
print('demo_read?: ', main)

# The read() method will read-in and output the entire file as a single string. Not usually as
# useful as the readLines() method is since it will return a List of the line elements.
# Not to be confused with readLine() (missing the 's')


# An interesting way to let python manage the opening and closing of your files is the
# with - as code block.

# Python will open this file and store it in 'f' since you provided f to the 'as' portion of the block
# You can remove the close() statement from the bottom as this will be closed by python
with open('new_demo.txt', mode='r') as curr_file:
    line = curr_file.readline()
    print('1st f.readline() line: ', line)
    while line:
        print(line)
        line = curr_file.readline()
    print('\nDone!')
