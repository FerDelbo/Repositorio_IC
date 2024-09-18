# filename: date_to_words.py
import datetime

date_str = input("Enter a date in the format \"ddmmyyyy\": ")
d = datetime.datetime.strptime(date_str, "%d%m%Y")

print(f"{d.strftime('%d')} of {d.strftime('%B')} {d.strftime('%Y')}")
