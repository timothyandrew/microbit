import time


def to_int(s):
    try:
        return int(s)
    except TypeError:
        return None
    except ValueError:
        return None


def execute_clear():
    print("----> CLEARING SCREEN")


def execute_image(arg):
    if arg == None:
        raise ValueError("Received IMAGE without an arg")

    print("----> DISPLAYING IMAGE: " + arg)


def execute_off(arg):
    n = to_int(arg)

    if n == None:
        raise ValueError("OFF needs a number")

    print("----> SWITCHING OFF LED #" + str(n))


def execute_on(arg):
    n = to_int(arg)

    if n == None:
        raise ValueError("ON needs a number")

    print("----> SWITCHING ON LED #" + str(n))


def execute_print(arg):
    if arg == None:
        raise ValueError("Received PRINT without an arg")

    text = "".join(arg)
    print(text)


def execute_boolean(b):
    if b.lower() == "dark":
        return True
    elif b.lower() == "bright":
        return True
    elif b.lower() == "clap":
        return True
    elif b.lower() == "buttona":
        return True
    elif b.lower() == "buttonb":
        return True
    elif b.lower() == "buttontop":
        return True
    else:
        raise ValueError("Unknown boolean " + b)


def execute_conditional(arg):
    args = arg.split(" ")
    args = [arg for arg in args if arg != ""]
    is_negative = False

    if args[0].lower() == "not":
        is_negative = True
        args.pop(0)

    if len(args) < 2:
        raise ValueError("IF needs at least a boolean and a command")

    boolean = args.pop(0)
    conditional = execute_boolean(boolean)
    conditional = (not conditional) if is_negative else conditional

    if is_negative:
        print(f"----> Boolean NOT {boolean} evaluated to {conditional}")
    else:
        print(f"----> Boolean {boolean} evaluated to {conditional}")

    command = args.pop(0)

    if conditional:
        execute(command, " ".join(args))


def execute_sleep(arg):
    n = to_int(arg)

    if n == None:
        time.sleep(500 / 1000)
        return

    time.sleep(n / 1000)


def execute(command, arg):
    if command.lower() == "print":
        execute_print(arg)
    elif command.lower() == "clear":
        execute_clear()
    elif command.lower() == "on":
        execute_on(arg)
    elif command.lower() == "off":
        execute_off(arg)
    elif command.lower() == "image":
        execute_image(arg)
    elif command.lower() == "if":
        execute_conditional(arg)
    elif command.lower() == "sleep":
        execute_sleep(arg)
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

while True:
    [eval(line) for line in lines if line.strip() != ""]
