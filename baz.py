import sys, select

while True:
    try:
        if select.select([sys.stdin,],[],[],2.0)[0]:
            line = sys.stdin.next()
            print("Got:", line)
        else:
            print("No data for 2 secs")

    except StopIteration:
        print('EOF!')
        break
