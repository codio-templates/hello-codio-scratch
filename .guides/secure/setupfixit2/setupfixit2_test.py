import sys


json_file = ".guides/secure/setupfixit2/project.json"

has_goto = False
with open(json_file, "r") as code:
  student_code = code.readlines()
  
  
for line in student_code:
    if "motion_goto" in line:
      has_goto = True
      
if has_goto:
  print("Nice job using the go to block!")
  sys.exit(0)
else:
  print("Use the go to block to position the cat at the starting point")
  sys.exit(1)