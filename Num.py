#!/usr/bin/python

def main():

    import random

    #Open a file named numbersmake.txt.
    outfile = open('numbersmake.txt', 'w')

    for count in range(12):
        num = random.randint(1, 100)
    	outfile.write(str(num))

    outfile.close()
    print('Data written to numbersmake.txt')

main()
