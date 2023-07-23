# The datetime module supplies classes for manipulating dates and times. 

from datetime import date

def test_datetime():

  today = date.today()
  assert today

  yesterday = date(2023, 5, 28)
  assert yesterday.day == 28
  assert yesterday.month == 5
  assert yesterday.year == 2023
  assert yesterday.ctime() == 'Sun May 28 00:00:00 2023'
  assert yesterday.strftime(
    '%m-%d-%y. %d %b %Y is a %A on the %d day of %B.'
  ) == '05-28-23. 28 May 2023 is a Sunday on the 28 day of May.'

  # Calendar arithmetic.
  birthday = date(2000, 12, 23)
  age = today - birthday
  print(age.days)

test_datetime()