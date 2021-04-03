# Assignment 3: Payroll.py
# A program that prints out the Payroll dependent on inputs.
def calculate(worked, pay, fedtax, statetax):
    worked = float(worked)
    gross = worked * pay
    fedwitholding = fedtax * gross
    statewitholding = statetax * gross
    total = statewitholding + fedwitholding
    return worked, gross, fedwitholding, statewitholding, total

def main():
    # enter inputs
    name = input("Enter employee ’s name : ")
    hours_worked = int(input("Enter number of hours worked in a week : "))
    hourly_pay = float(input("Enter hourly pay rate : "))
    federal_tax = float(input("Enter federal tax withholding rate : "))
    fedtax = str(float(federal_tax * 100)) + '%'
    state_tax = float(input("Enter state tax withholding rate : "))
    sttax = str(float(state_tax * 100)) + '%'
    worked, gross, fedwitholding, statewitholding, total = calculate(hours_worked, hourly_pay, federal_tax, state_tax)

    # print the final statements
    print("Employee Name :", name)
    print("Hours Worked :", worked)
    print("Pay Rate : $" + str(hourly_pay))
    print("Gross Pay : $" + str(gross))
    print("Deductions:")
    fedwitholding = "{:.2f}".format(fedwitholding)
    print(" Federal Withholding " + '(' + fedtax + ')' + ': $' + str(fedwitholding))
    statewitholding = "{:.2f}".format(statewitholding)
    print(" State Withholding " + '(' + sttax + ')' + ': $' + str(statewitholding))
    totall = "{:.2f}".format(total)
    print(" Total Deductions: $" + str(totall))
    netpay = gross - total
    netpay = "{:.2f}".format(netpay)
    print("Net Pay: $" + str(netpay))

main()


