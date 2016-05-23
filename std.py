#!/usr/bin/python
def interact():
    print('Hello Stream world!')
    while True:
        try:
            reply = input('Enter a Number>>> ')
        except EOFError:
            break
        except KeyboardInterrupt:
            break
        else:
            num = int(reply)
            print("%d squared is %d " % (num, num ** 2 ))
    print("bye")
if __name__ == "__main__":
    interact()
