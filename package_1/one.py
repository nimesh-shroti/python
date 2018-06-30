def m1():
    print("Inside m1 of module one.py")

def m1_2():
    print("Inside m1_2 of module one.py")

print( __name__ )
if __name__ == '__main__':
    m1()
    print("ye call hoga....")