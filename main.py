def execute_text(arg):
    if arg == None:
        raise ValueError("Received TEXT without any text to print")

    text = "".join(arg)
    print(text)


def execute(command, arg):
    if command.lower() == "text":
        execute_text(arg)
    else:
        raise ValueError("Unknown command " + command)


def eval(line):
    line = line.strip()
    line = line.split(" ", 1)

    if len(line) == 1:
        execute(line[0], None)
    else:
        execute(line[0], line[1])


program = open('PROGRAM', 'r')
lines = program.readlines()
[eval(line) for line in lines if line.strip() != ""]
