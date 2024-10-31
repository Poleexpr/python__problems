from datetime import datetime

def get_date(date_string):
  try:
    date_the_moscow_times = datetime.strptime( date_string, '%A, %B %d, %Y' )
    return date_the_moscow_times
  except: 
    pass

  try:
    date_the_guardian = datetime.strptime( date_string, '%A, %m.%d.%y' )
    return date_the_guardian
  except: 
    pass

  try:
    date_daily_news = datetime.strptime( date_string, '%A, %d %B %Y' )
    return date_daily_news
  except: 
    pass
  

print(get_date('Wednesday, October 2, 2002'))
print(get_date('Friday, 11.10.13'))
print(get_date('Thursday, 18 August 1977'))


