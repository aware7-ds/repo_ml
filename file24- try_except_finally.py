# try,except,finally

# standard format- use it while taking inputs , for file systems,db connections

def err():
    c = 0
    try:
        print('open')
        a = int(input('enter num:'))
        b = int(input('enter num:'))
        c = a / b
        return c
    except ValueError as e:
        print('invalid Input')
    except Exception as e:
        print('Error type:',e)
    finally:
        print('closed')
res = err()
print('op:',res)


