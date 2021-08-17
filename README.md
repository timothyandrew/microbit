# microbit

This repo contains a python interpreter (`main.py`) for a tiny language intended for kids too young to write Python directly. Here are a few examples:

Pulsing heart:

```
show heart
wait
show small heart
wait
```

Music:

```
show music
play birthday
```

## Reference

- Booleans
	- `buttona`
	- `buttonb`
- Commands
	- `show <image>`
	- `print <text>`
	- `play <song>`
	- `wait <optional_ms>`
	- `clear`
- Control flow
	- `if <boolean> <command>`
	- `if not <boolean> <command>`
