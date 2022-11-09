#!/usr/bin/env python3
"""Dictionary, char_name
   {key: value, key:value, ...} """

def main():

    # save user's input to var char_name
    char_name = input("Which character do you want to know about? Please choose Starlord, Mystique, or Hulk\n>")
    char_name = char_name.capitalize()

    # stats
    char_stat = input("What stat do you want to know about? Please choose real name, powers, or archenemy\n>")
    char_stat = char_stat.lower()

    # data
    marvelchars = {
        "Starlord":
            {"real name": "peter quill",
            "powers": "dance moves",
            "archenemy": "Thanos"},

        "Mystique":
            {"real name": "raven darkholme",
            "powers": "shape shifter",
            "archenemy": "Professor X"},

        "Hulk":
            {"real name": "bruce banner",
            "powers": "super strength",
            "archenemy": "adrenaline"}
        }

    # use char_name and char_stat to pull values from dict
    print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat].title()}")


# call main function
if __name__ == "__main__":
    main()

