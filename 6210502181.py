print("Wiphoothorn")
def std_id_to_binary(num):
	binary = ""
	while num > 0:
		binary = str(num % 2) + binary
		num = num // 2
	return binary
	
std_id = int(input("Enter a std_id: "))
binary = std_id_to_binary(std_id)
print("The binary representation of {} is {}".format(std_id, binary))
