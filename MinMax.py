# Assignment 5: MinMax.py
# Enter several numbers and output the maximum and minimum values of the total numbers entered

final = []

# initial entered
entered = input("Enter an integer or type 'stop' to end: ")
if entered == 'stop':
    print('You did not enter any numbers.')
else:
    while entered != 'stop':
        entered_int = int(entered)
        final.append(entered_int)
        entered = input("Enter an integer or type 'stop' to end: ")

    max = max(final)
    min = min(final)

    print("The maximum is", max)
    print("The minimum is", min)