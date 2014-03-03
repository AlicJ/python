#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alic Jiang
#
# Created:     02/03/2014
# Copyright:   (c) Alic Jiang 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Add GUI!!!

def leap(year):
    leap = False
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    elif year % 4 ==0:
        leap = True
    return leap


def days(month, year):
    small_month = [4, 6, 9, 11]
    if month in small_month:
        return 30
    elif month == 2:
        if leap(year):
            return 29
        else:
            return 28
    else:
        return  31


def main():
    startDay, startMonth, startYear = eval(input("Enter the start date (in dd,mm,yyyy format seperated by comma): "))
    endDay, endMonth, endYear = eval(input("Enter the end date (in dd,mm,yyyy format seperated by comma): "))

##    startDay = eval(input("Input the start day: "))
##    startMonth = eval(input("Input the start month: "))
##    startYear = eval(input("Input the start year: "))
##
##    endDay = eval(input("Input the end day: "))
##    endMonth = eval(input("Input the end month: "))
##    endYear = eval(input("Input the end year: "))

    dayCount = 0
    yearDiff = False
    monthDiff = False

    # if there is a difference between years
    if endYear != startYear:


        # add the days left in the start month
        dayCount += days(startMonth, startYear) - startDay
        print("adding days for",startMonth, startYear, "dayCount =", dayCount)
        # add the days before the deadline in the end month
        dayCount += endDay - 1
        print("adding days for",endMonth, startYear, "dayCount =", dayCount)

        # add the days left in the start year
        for i in range(startMonth + 1, 12+1, 1):
            dayCount += days(i, startYear)
            print("adding days for",i, startYear, "dayCount =", dayCount)
        # add days before the deadline in the end year
        for i in range(1, endMonth, 1):
            dayCount += days(i, endYear)
            print("adding days for",i, endYear, "dayCount =", dayCount)

        # if the difference between years are greater than 2
        if endYear - startYear >= 2:
            for i in range(1, endYear - startYear, 1):
                print("add days for", startYear + i)
                if leap(startYear + i):
                    dayCount += 366
                    print("adding days for", startYear + i, "dayCount =", dayCount)
                else:
                    dayCount += 365
                    print("adding days for", startYear + i, "dayCount =", dayCount)
        # if they are neighbor years
        else:
            # add the days left in the start month
            dayCount += days(startMonth, startYear) - startDay
            print("adding days for",startMonth, startYear, "dayCount =", dayCount)
            # add the days before the deadline in the end month
            dayCount += endDay - 1
            print("adding days for",endMonth, startYear + 1, "dayCount =", dayCount)

    # if they are in the same year
    else:

        # if there is a difference between month
        if endMonth != startMonth:

            # add the days left in the start month
            dayCount += days(startMonth, startYear) - startDay
            print("adding days for",startMonth, startYear, "dayCount =", dayCount)
            # add the days before the deadline in the end month
            dayCount += endDay - 1
            print("adding days for",endMonth, startYear, "dayCount =", dayCount)


            if endMonth - startMonth >= 2:
                monthDiff = True
                # add the days between the two months
                for i in range(1, endMonth - startMonth, 1):
                    print("add das for", startMonth + i)
                    dayCount += days(startMonth + i, startYear)
                    print("adding days for",startMonth + i, startYear, "dayCount =", dayCount)


        # if they are in the same month:
        else:
            dayCount = endDay - startDay - 1



    print("There are", dayCount, "days between", startDay, startMonth, startYear, "and", endDay, endMonth, endYear)


if __name__ == '__main__':
    main()
