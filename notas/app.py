# Introdução para o usuário
print("📚 Calculador de Notas 📊")
print("Siga o passo a passo para calcular as notas ✍️")

# Declaro o peso de cada nota
weight_1 = 60
weight_2 = 20
weight_3 = 20

resultWeight = weight_1 + weight_2 + weight_3

# Média
average = 6

# Nome do aluno
name = input("👤 Qual o nome do aluno: ")

# Pergunta a primeira nota para o usuário
note_value_1 = float(input("✏️ Digite o valor da primeira nota: "))

# Pergunta a segunda nota para o usuário
note_value_2 = float(input("✏️ Digite o valor da segunda nota: "))

# Pergunta a terceira nota para o usuário
note_value_3 = float(input("✏️ Digite o valor da terceira nota: "))

# Cálculo do peso de cada nota
resultNote_1 = note_value_1 * weight_1
resultNote_2 = note_value_2 * weight_2
resultNote_3 = note_value_3 * weight_3

resultNote = resultNote_1 + resultNote_2 + resultNote_3

finalNote = resultNote / resultWeight

# Verifica aprovação ou reprovação
if finalNote > average: 
    print("🎉 O aluno(a) 🎓", name)
    print("📌 Tirou a nota:", finalNote)
    print("✅ Sendo assim, foi APROVADO! 🎊🎈")

else:
    print("⚠️ O aluno(a) 🎓", name)
    print("📌 Tirou a nota:", finalNote)
    print("❌ Sendo assim, foi REPROVADO. 😢")
