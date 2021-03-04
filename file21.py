# usage of __name__
# first code everything in functions;

def add():
    print('add')
def sub():
    print('sub')
def main():
    add()
    sub()
if __name__ == '__main__': # comment n compare file21 and file22
    main()