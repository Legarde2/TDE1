def arquivo(texto):
  with open(texto, 'r') as file:
      linhas = file.readlines()

  numero = int(linhas[0].strip())
  resultado = []
  tipo = 1

  for _ in range(numero):
      tipoOperacao = linhas[tipo].strip()
      conjunto1 = linhas[tipo + 1].strip()
      conjunto2 = linhas[tipo + 2].strip()
      resultados = operacao(tipoOperacao, conjunto1, conjunto2)
      resultado.append(resultados)
      tipo += 3

  return resultado

def operacao(tipo, conjunto1, conjunto2):
  conjunto1 = set(item.strip() for item in conjunto1.split(','))
  conjunto2 = set(item.strip() for item in conjunto2.split(','))

  if tipo == 'U':
    resultado = conjunto1.union(conjunto2)
    operacao = "União"

  elif tipo == 'I':
    resultado = conjunto1.intersection(conjunto2)
    operacao = "Interseção"

  elif tipo == 'D':
    resultado = conjunto1.difference(conjunto2)
    operacao = "Diferença"

  elif tipo == 'C':
    resultado = []
    for a in conjunto1:
      for b in conjunto2:
        resultado.append((a, b))
    operacao = "Produto cartesiano"
    resultado = ', '.join([f"({a}, {b})" for a, b in resultado])
  return "operação: ", operacao, "conjunto 1: ", conjunto1, "conjunto 2: ", conjunto2, "resultado: ", resultado

def main():
  texto = 'texto3'
  resultado = arquivo(texto)

  for saida in resultado:
    print(saida)


if __name__ == "__main__":
  main()
