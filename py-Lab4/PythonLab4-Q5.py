from datetime import date
dayFirst = date(2000, 2, 28)
dayLast = date(2001, 2, 28)
difference = dayLast - dayFirst
print(difference.days)