# Assignment 4: DaysInMonth.py
# Enter a month and year to receive the amount of days within that month and year


# Input month and year
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

# Statement for each month
if month == 1:
    print("January", year,"has 31 days")
# Define Leap Year calculation
IsLeapYear = ( year % 4 == 0)  and (not ( year % 100 == 0 ) or ( year % 400 == 0));
# If the year is a Leap Year and it is Month 2, print following string
if IsLeapYear and month == 2:
    print("February", year, "has 29 days")
# If the year is not a Leap Year but has Month 2, print following string
if month == 2 and not IsLeapYear :
    print( "February", year, "has 28 days")
if month == 3:
    print("March", year,"has 31 days")
if month == 4:
    print("April", year,"has 30 days")
if month == 5:
    print("May", year,"has 31 days")
if month == 6:
    print("June", year,"has 30 days")
if month == 7:
    print("July", year,"has 31 days")
if month == 8:
    print("August", year,"has 31 days")
if month == 9:
    print("September", year,"has 30 days")
if month == 10:
    print("October", year,"has 31 days")
if month == 11:
    print("November", year,"has 30 days")
if month == 12:
    print("December", year,"has 31 days")