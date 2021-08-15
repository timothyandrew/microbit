from microbit import *


def to_int(s):
    try:
        return int(s)
    except TypeError:
        return None
    except ValueError:
        return None


def execute_clear():
    display.clear()

def execute_image(arg):
    if arg == None:
        raise ValueError("Received IMAGE without an arg")

    to_image = { 
        "heart": Image.HEART,
        "small heart": Image.HEART_SMALL,
        "happy": Image.HAPPY,
        "smile": Image.SMILE,
        "sad": Image.SAD,
        "confused": Image.CONFUSED,
        "angry": Image.ANGRY,
        "asleep": Image.ASLEEP,
        "surprised": Image.SURPRISED,
        "silly": Image.SILLY,
        "meh": Image.MEH,
        "yes": Image.YES,
        "no": Image.NO,
        "arrow": Image.ARROW_E,
        "triangle": Image.TRIANGLE,
        "chess": Image.CHESSBOARD,
        "diamond": Image.DIAMOND,
        "square": Image.SQUARE,
        "rabbit": Image.RABBIT,
        "cow": Image.COW,
        "music": Image.MUSIC_QUAVER,
        "christmas": Image.XMAS,
        "pacman": Image.PACMAN,
        "target": Image.TARGET,
        "tshirt": Image.TSHIRT,
        "roller skate": Image.ROLLERSKATE,
        "duck": Image.DUCK,
        "house": Image.HOUSE,
        "tortoise": Image.TORTOISE,
        "butterfly": Image.BUTTERFLY,
        "ghost": Image.GHOST,
        "sword": Image.SWORD,
        "giraffe": Image.GIRAFFE,
        "skull": Image.SKULL,
        "umbrella": Image.UMBRELLA,
    }

    display.show(to_image[arg.lower()])

def execute_print(arg):
    if arg == None:
        raise ValueError("Received PRINT without an arg")

    display.scroll(arg)

def execute_boolean(b):
    if b.lower() == "dark":
        return display.read_light_level() < 5
    elif b.lower() == "bright":
        return display.read_light_level() > 5
    elif b.lower() == "buttona":
        return button_a.is_pressed()
    elif b.lower() == "buttonb":
        return button_b.is_pressed()
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

    command = args.pop(0)

    if conditional:
        execute(command, " ".join(args))


def execute_sleep(arg):
    n = to_int(arg)

    if n == None:
        sleep(1000)
        return

    sleep(n)


def execute(command, arg):
    if command.lower() == "print":
        execute_print(arg)
    elif command.lower() == "clear":
        execute_clear()
    elif command.lower() == "show":
        execute_image(arg)
    elif command.lower() == "if":
        execute_conditional(arg)
    elif command.lower() == "wait":
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


with open('PROGRAM') as file:
    program = file.read()

lines = program.split('\n')

while True:
    [eval(line) for line in lines if line.strip() != ""]
