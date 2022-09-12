def ehPositivo(numero):
	return numero > 0

def main():
	temperaturas = [10, -4, 33, -20, 21]
	positivas = list(filter(ehPositivo, temperaturas))
	print(positivas)

if __name__ == '__main__':
	main()
