#!/usr/bin/env python
def interact():
    print('hello guy')
    while True:
        try:
            reply = input('Enter a number> ')
        except EOFError:
            break
        else:
            num = int(reply)
            print("%d squared is %d" % (num, num ** 2))
    print('bye')
if __name__ == '__main__':
    interact()
