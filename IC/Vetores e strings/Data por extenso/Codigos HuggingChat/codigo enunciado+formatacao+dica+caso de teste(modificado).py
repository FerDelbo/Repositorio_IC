def date_to_words(date):
    day = date[0:2]
    m = int(date[2:4]) - 1
    y = date[4:8]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] # January, February, ... December
    return f"{day} {months[m]} {y}"

print(date_to_words("01092023"))  # Output: March 17, 1909
print(date_to_words("17031909"))  # Output: March 17, 1909
print(date_to_words("31021031"))   # Output: February 31, 1031