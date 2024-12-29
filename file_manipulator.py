import sys
import os


argv = sys.argv
# Check the value of index 1
if argv[1] == "reverse":
    # Check the argument
    if len(argv) != 4:
        print("Argument is wrong")
        sys.exit(1)
    if os.path.exists(argv[2]) == False:
        print(argv[2], "not found")
        sys.exit(1)
    # Execute the operation
    with open(argv[2], 'r') as f:
        lines = f.readlines()

    reversed_content = [line.strip()[::-1] for line in reversed(lines)]

    with open(argv[3], 'w') as f:
        f.write('\n'.join(reversed_content))

elif argv[1] == "copy":
    # Check the argument
    if len(argv) != 4:
        print("Argument is wrong")
        sys.exit(1)
    if os.path.exists(argv[2]) == False:
        print(argv[2], "not found")
        sys.exit(1)
    # Execute the operation
    with open(argv[2], 'r') as f:
        lines = f.read()
    with open(argv[3], 'w') as f:
        f.write(lines)

elif argv[1] == "duplicate-contents":
    # Check the argument
    if len(argv) != 5:
        print("Argument is wrong")
        sys.exit(1)
    if os.path.exists(argv[2]) == False:
        print(argv[2], "not found")
        sys.exit(1)
    if not argv[4].isdigit():
        print("Argument is wrong")
        sys.exit(1)
    # Execute the operation
    with open(argv[2], 'r') as f:
        lines = f.read()
    with open(argv[3], 'w') as f:
        f.write(lines * int(argv[4]))
    
elif argv[1] == "replace-string":
    # Check the argument
    if len(argv) != 5:
        print("Argument is wrong")
        sys.exit(1)
    if os.path.exists(argv[2]) == False:
        print(argv[2], "not found")
        sys.exit(1)
    # Execute the operation
    with open(argv[2], 'r') as f:
        lines = f.read()
    with open(argv[2], 'w') as f:
        f.write(lines.replace(argv[3], argv[4]))
else:
    print("Argument is wrong")
    sys.exit(1)