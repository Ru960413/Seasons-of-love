# implement a program that prompts the user for their date of birth in YYYY-MM-DD format 
# and then sings prints how old they are in minutes, rounded to the nearest integer,
# using English words instead of numerals

# Exit via sys.exit if the user does not input a date in YYYY-MM-DD format. 
# Ensure that your program will not raise any exceptions.
import datetime
import sys
import inflect

p = inflect.engine()

def main():
    # print(type(__sub__()))
    days = __sub__()
    # Refernce: https://stackoverflow.com/questions/27912803/how-to-get-total-hours-and-minutes-for-timedelta-in-python
    seconds = datetime.timedelta(days=days).total_seconds()
    minutes = int(seconds/60)
    minutes_in_words = p.number_to_words(minutes, andword="").capitalize()
    print(f"{minutes_in_words} minutes")



# get the birthday and validate its format
def get_birth():
    try:
        year, month, day = input("Date of Birth: ").split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        birth = datetime.date(year, month, day)
        return birth

    # if the format is incorrect then exit via sys.exit
    except ValueError:
        print("Invalid date")
        sys.exit(1)



# substraction
def __sub__():
    today = datetime.date.today()
    birth = get_birth()
    difference = today - birth
    return difference.days




if __name__ == "__main__":
    main()