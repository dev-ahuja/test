#Exception Handling.
try:
    data = {'A':1,'B':3,'C':9}
    print(data['D'])
except KeyError:
    print('Exception in code')
except ZeroDivisionError:
    print('Zero Division Error')
finally:
    print('Finally called...')
