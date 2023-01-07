# This is implementation of Continue and if else
# Program that print square of number from 1 to 10 except 5
for i in range (1,11):
    if i == 5:
        continue
    else:
        print ('square of {} is {}'.format(i,i*i))
