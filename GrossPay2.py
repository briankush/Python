hour=float(input("Please enter your hours of working\n"))
rate=float (input("Enter the rate per hour\n"))
overtime =hour-40
if (hour>40):
    overtime*1.5
    gross_pay= 40 *rate + overtime * rate *1.5
else:
    gross_pay= hour * rate
print(f"Your gross pay is ksh {gross_pay}.Thankyou")