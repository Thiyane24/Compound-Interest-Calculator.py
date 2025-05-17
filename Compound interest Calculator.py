
principle = float(input("Enter your principle amount: "))
rate = float(input("Enter the interest rate in % :  "))
time = int(input("Enter the time in years: "))
total = principle * pow((1 + rate/100),time)
print(f"Your balance in {time} year/s is {total:.2f}MZN")

while principle <= 0 :
    principle = float(input("Enter your principle amount: "))
    if principle <= 0 :
        print("Principle can't be less or equal to 0.")
    else:
        break

        while rate <= 0 :
            rate = float(input("Enter the interest rate: "))
            if rate <= 0 :
                print("Rate can't be less or equal to 0.")
            else:
                break

                while time <= 0 :
                    time = int(input("Enter the time in years: "))
                    if time <= 0 :
                        print("Time can't be less or equal to 0.")
                    else:
                        break

