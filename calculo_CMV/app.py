print("🧮 Calculadora de CMV 📊")
print("📢 Siga o passo a passo para descobrir o valor do CMV do produto e seu lucro 💰")



productName = input("📝 Insira o nome do produto: ")
productPrice = float(input("💲 Qual o valor de venda deste produto: "))
productCost = float(input("💰 Qual o custo deste produto em reais (R$): "))

cmv = productCost / productPrice * 100
profit = productPrice - productCost

print("🍔 O produto:", productName)
#round é usado para arredondar numeros e o numero que coloco depois é quantas casas eu quero depois da virgula
print("📊 Tem o CMV aproximado em:", round(cmv, 2), "%")
print("💵 Seu lucro sobre este produto é de: R$", round(profit, 2))







