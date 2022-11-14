#!/usr/bin/env python3
"""Crayons custom"""

## Installs the crayons package.
## python3 -m pip install crayons
## import statements ALWAYS go up top
import crayons


def main():
    """run time code. Always indent under function"""

    # print 'red string' in red
    print(crayons.red('red string'))

    # Red White and Blue text
    #print('{} white {}'.format(crayons.red('red'), crayons.blue('blue'))) # format string (old ver of str templating)
    print(f"{crayons.red('red')} white {crayons.blue('blue')}")

    crayons.disable() # disables the crayons package

    # this line should NOT have color as crayons is disabled
    print(f"{crayons.red('red')} white {crayons.blue('blue')}")

    crayons.DISABLE_COLOR = False # re-enables the crayons package

    # This line will print in color because color is enabled
    print(f"{crayons.red('red')} white {crayons.blue('blue')}")  # f-string (newest version of string templating)

    # print 'red string' in red
    print(crayons.red('red string', bold=True))

    # print 'yellow string' in yellow
    print(crayons.yellow('yellow string', bold=True))

    # print 'magenta string' in magenta
    print(crayons.magenta('magenta string', bold=True))

    # print 'white string' in white
    print(crayons.white('white string', bold=True))

    # The available colors from the crayons package are: red, green, yellow, blue, black, magenta, cyan, and white. Write a line at the end that prints your name in (at least) two colors.
    print(f"{crayons.red('My')} {crayons.green('name')} {crayons.yellow('is')} {crayons.blue('James')} {crayons.magenta('Isaacs')}")


# this condition is only true if our script is run directly
# it is NOT true if our code is imported into another script
if __name__ == "__main__":
    main()

