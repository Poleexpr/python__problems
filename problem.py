import re

text = 'A222BC96'

pattern = r'([A-Z]{1})(\d{3})([A-Z]{2})(\d{2,})'
result = re.findall(pattern, text)

if(len(result) > 0):
  message = f"Номер {result[0][0]}{result[0][1]}{result[0][2]} валиден. Регион: {result[0][3]}."
  print(message)
else:
  print('Номер не валиден')



  




