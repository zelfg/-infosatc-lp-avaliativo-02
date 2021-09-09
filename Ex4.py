valor1 = input("Digite algo para o primeiro valor: ")
valor2 = input("Digite algo para o segundo valor: ")
valor3 = input("Digite algo para o terceiro valor: ")
valor4 = input("Digite algo para o quarto valor: ")
valor5 = input("Digite algo para o quinto valor: ")

lista = [valor1, valor2, valor3, valor4, valor5]

elemento = input("Qual valor você deseja saber a posição?: ")

print("A posição de {} é {}".format(elemento, lista.index(elemento)))