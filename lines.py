#!/usr/bin/python3
##
##  lines.py
##  Count Lines in a file
##
##  Created by Darius Miclaus on 25/03/2021.
##

# Main Function
def main():
    with open('extensions.txt') as file:
    	print(sum(1 for _ in file))

# Run main when starting
if __name__ == "__main__":
    main()
