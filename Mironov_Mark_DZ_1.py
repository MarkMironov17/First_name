duration = int(input())

while duration > 0:
  if duration < 60:
    print(f"{duration} сек")
    break
  elif 60 < duration < 3600:
    minutes = duration // 60
    duration %= 60
    print(f'{minutes} min:{duration} sec')
    break
  elif 86400 > duration > 3600:
    hours = duration // 3600
    duration %= 3600
    minutes = duration // 60
    duration %= 60
    print(f'{hours} час:{minutes} мин:{duration} сек')
    break
  else:
    days = duration // (24 * 3600)
    duration %= 24 * 3600
    hours = duration // 3600
    duration %= 3600
    minutes = duration // 60
    duration %= 60
    print(f'{days} дн {hours} час {minutes} мин {duration} сек')
    break



