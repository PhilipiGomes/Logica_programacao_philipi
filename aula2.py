nome = input('Digite seu nome de usuário: ')
email = input('Digite seu e-mail: ')
telefone = input('Digite seu telefone: ')
autonomia_gasolina = float(input("Informe a autonomia do seu carro para gasolina (em km/l): "))
autonomia_alcool = float(input("Informe a autonomia do seu carro para álcool (em km/l): "))
CasaTrabalho = input("Informe a distância da sua casa até o seu trabalho: ")
preco_gasolina = float(input("Informe o preço da gasolina (em reais): "))
preco_alcool = float(input("Informe o preço do álcool (em reais): "))
num_dias = input("Informe quantos dias no mês voce faz esse trajeto: ")
total_km = CasaTrabalho * 2 * num_dias
l_gasolina_mes = total_km / autonomia_gasolina
l_alcool_mes = total_km / autonomia_alcool
preco_total_gasolina = l_gasolina_mes * preco_gasolina
preco_total_alcool = l_alcool_mes * preco_alcool

print(f"Nome: {nome}")
print(f"E-mail: {email}")
print(f"Telefone: {telefone}")
print("\n")
print(f"Seu gasto mensal de gasolina será de: R${preco_total_gasolina:.2f}")
print(f"Seu gasto mensal de álcool sera de: R${preco_total_alcool:.2f}")
print(f"O total de kilometros que voce roda por mês é: {total_km} km")
print(f"Seu consumo total de gasolina por mês será de: {l_gasolina_mes:.2f} km")
print(f"Seu consumo total de álcool por mês será de: {l_alcool_mes:.2f} km")





