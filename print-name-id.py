def decimal_to_binary(decimal):
  binary = ""
  while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal = decimal // 2
  return binary
  
print("chawin khongprasongsiri")
decimal_number = 6210500391
binary_number = decimal_to_binary(decimal_number)
print(binary_number)  
