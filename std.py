#!/usr/bin/python
def interact():
    print('Hello Stream world!')
    while True:
        try:
            reply = input('Enter a Number>>> ')
        except EOFError:
            break
        except KeyboardInterrupt:
            print('KeyboardInterrupt')
            #raise KeyboardInterrupt
            break
        else:
            try:
                num = int(reply)
                print("%d squared is %d " % (num, num ** 2 ))
            except ValueError:
                print('you put a wrong type, please input again..')
    print("bye")
if __name__ == "__main__":
    interact()
