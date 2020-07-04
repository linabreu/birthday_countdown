#!/usr/bin/env python3

#days until birthday program using date and datetime objects

from datetime import date, datetime

def main():
    print("Birthday Countdown Program!")
    while True:
        print()
        #get birthday from user
        birthday_input = input("Enter date of birth (MM/DD/YYYY): ")
        print()

        #parse input into a date object
        birthday = datetime.strptime(birthday_input, "%m/%d/%Y")

        #print as a formatted string
        print( "Your birthday is ", birthday.strftime("%B %d, %Y"))
        print()

        #take the month and day from the user and convert them into a date for this year's birthday
        today = date.today()
        birth_month  = birthday.month
        birth_day = birthday.day
        birthday_date = date(today.year, birth_month, birth_day)

        #determine if thier birthday has passed, is coming up or is today
        if today > birthday_date:
            print("Your birthday has already passed this year!")
        elif today < birthday_date:
            countdown = (birthday_date - today).days
            print("Only ", countdown, " days until your birthday!")
        elif today == birthday_date:
            print("Happy Birthday!")
            
        #ask if they want do another countdown
        print()
        another = input("Would you like countdown the days until a different birthday? (y/n): ")
        print()
        if another.lower() !="y" or another.upper() !="Y": #make sure they can put in upper or lower case
            print("Thank you for using the Birthday Countdown!")
            break
        


if __name__ == "__main__":
    main()



