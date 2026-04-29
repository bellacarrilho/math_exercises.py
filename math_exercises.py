# ---------------------------------------------------------
# ESTUDOS DE ENGENHARIA - REVISÃO DE MATEMÁTICA BÁSICA
# Objetivo: Automatizar cálculos de frações para conferir exercícios
# ---------------------------------------------------------

from fractions import Fraction

print("--- Calculadora de Frações para Engenharia ---")

# Exemplo de uma soma de frações que estudei hoje
f1 = Fraction(1, 4) # Representa 1/4
f2 = Fraction(2, 3) # Representa 2/3

resultado = f1 + f2

print(f"A soma de {f1} com {f2} é igual a: {resultado}")

# Outro exemplo: Transformar decimal em fração
decimal = 0.75
fracao_do_decimal = Fraction(decimal).limit_denominator()
print(f"O decimal {decimal} em fração é: {fracao_do_decimal}")

# ---------------------------------------------------------
# NOTAS DE ESTUDO:
# Hoje foquei em MMC e simplificação. 
# Este código ajuda-me a validar os resultados rapidamente.
# ---------------------------------------------------------
