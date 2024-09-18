# filename: date_in_words.py
ddmmyyyy = input("Enter a date in the format ddmmyyyy: ")
dd = int(ddmmyyyy[:2])
mm = int(ddmmyyyy[2:4])
yyyy = int(ddmmyyyy[4:])
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(f"{dd} {months[mm - 1]} {yyyy}")
