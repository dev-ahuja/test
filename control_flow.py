# x = 30
# y = 20

# if x>y:
#     print('x is greater than y')
# else:
#     print('y is greater than x')

'''If Marks>=60% First Class
    Else if Marks>=50% Second Class
    Else if Marks >=40% Third Class
    Else print Failed
'''
marks=(input("What are your marks?: "))

if marks >=60:
    print("You have obtain a First Division ")
elif marks >= 50 or <= 60: #some correction is reqd.
    print("You have obtain a Second Division ")
elif marks >=40 and <=50:
    print("You have obtain a Third Division ")
else:
    print('You have failed')
    print('You have failed')