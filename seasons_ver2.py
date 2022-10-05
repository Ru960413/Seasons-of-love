import datetime
import sys
import inflect

p = inflect.engine()

def main():
    birthday = input("Date of Birth: ")
    birth = get_birth(birthday)
    today = datetime.date.today()
    print(__sub__(today, birth))



# get the birthday and validate its format
def get_birth(birthday):
    try:
        year, month, day = birthday.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        birth = datetime.date(year, month, day)
        return birth

    # if the format is incorrect then exit via sys.exit
    except ValueError:
        print("Invalid date")
        sys.exit(1)



# substract and convert days to minutes in English
def __sub__(today, birth):
    difference = today - birth
    # Reference: https://stackoverflow.com/questions/27912803/how-to-get-total-hours-and-minutes-for-timedelta-in-python
    seconds = datetime.timedelta(days=difference.days).total_seconds()
    minutes = int(seconds/60)
    minutes_in_words = p.number_to_words(minutes, andword="").capitalize()

    return f"{minutes_in_words} minutes"




if __name__ == "__main__":
    main()