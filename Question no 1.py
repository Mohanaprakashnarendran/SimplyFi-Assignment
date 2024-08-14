def indian_currency_format(number):
  number = str(number)
  length = len(number)

  if length <= 3:
    return number

  formatted_number = ""
  for i, digit in enumerate(number[:5]):
    if (i + 1) % 2 == 0 and i != length - 1:
      formatted_number = digit + "," + formatted_number
    else:
      formatted_number = digit + formatted_number

  return formatted_number[::-1]

number = 504678
formatted_number = indian_currency_format(number)


print(formatted_number)
