# Classes may be derived from multiple classes (multiple inheritance).

def test_multiple_inheritance():

  class Clock: 
    time = '11:23 PM'

    def get_time(self):
      return self.time
  

  class Calendar:
    date = '05/26/2023'

    def get_date(self):
      return self.date
  
  # Multiple inheritance
  class CalendarClock(Clock, Calendar):
    pass
  
  calendar_clock = CalendarClock()
  assert calendar_clock.get_date() == '05/26/2023'
  assert calendar_clock.get_time() == '11:23 PM'

test_multiple_inheritance()