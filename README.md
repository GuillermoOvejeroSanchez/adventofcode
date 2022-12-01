# Advent of Code (2022)
Python and Scala solutions to the Advent of Code problems.
Check out https://adventofcode.com.

## Running

1. make start
2. Fill .env with AOC_SESSION=XXX (Search for it in https://adventofcode.com/ Cookies 🍪)
3. make help to showcase all examples


## Usage

```
Usage: make <command>
1) To show your advent calendar:
 calendar            Show the calendars

2) To work on problems:
login to https://adventofcode.com, then copy your session cookie, and export 
it in your console like this

 export AOC_SESSION=73a37e9a72a...

- then run the app with

 make problem year=X day=Y  Prepares a folder for the given day, updates the input,
                            the readme and creates a solution template.
 make today-problem         Shortcut to the above.

- then you're ready to code!
```