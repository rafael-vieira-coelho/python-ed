def main():
	temperaturas = [10, -4, 33, -20, 21]
	positivas = []
	for temp in temperaturas: 
		if temp > 0:
			positivas.append(temp)
	print(positivas)

if __name__ == '__main__':
	main()
