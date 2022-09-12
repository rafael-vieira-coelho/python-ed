def main():
	temperaturas = [10, -4, 33, -20, 21]
	positivas = list(filter(lambda number: number > 0, temperaturas))
	print(positivas)

if __name__ == '__main__':
	main()
