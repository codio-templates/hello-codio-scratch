import os, shutil, sys

# path to student file
student_file = "/home/codio/workspace/setupfixit2.sb3" 

# new location for testing
new_location = "/home/codio/workspace/.guides/secure/setupfixit2" 

# copy student file to the new location
shutil.copy(student_file, new_location)

# unzip the file
result = os.system("unzip -uoq /home/codio/workspace/.guides/secure/setupfixit2/setupfixit2.sb3 -d /home/codio/workspace/.guides/secure/setupfixit2")

# run the code test on student file
result = os.system("python3 .guides/secure/setupfixit2/setupfixit2_test.py")

# Return the exit code to the Guide for the red "X" or green check mark
if result == 0:
    sys.exit(0)
else:
    sys.exit(1)