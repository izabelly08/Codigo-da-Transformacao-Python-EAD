from datetime import datetime


def aplicar_prova():
  print("=== AVALIAÇÃO CLI ===")
  avaliado = input("Nome do avaliado: ").strip()
  avaliador = input("Nome do avaliador: ").strip()
  data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")

  questoes = [
      {
          "p": (
              "1. Se um polvo tem 8 tentáculos e veste 2 sapatos em cada um,"
              " quantos sapatos usa?"
          ),
          "ops": ["A) 10", "B) 12", "C) 16", "D) 20"],
          "resp": "c",
      },
      {
          "p": (
              "2. Se 3 gatos caçam 3 ratos em 3 min, quanto tempo 100 gatos"
              " levam para 100 ratos?"
          ),
          "ops": ["A) 1 min", "B) 3 min", "C) 30 min", "D) 100 min"],
          "resp": "b",
      },
      {
          "p": (
              "3. Quantas pernas tem a soma de 2 aranhas (8 cada) e 3 galinhas"
              " (2 cada)?"
          ),
          "ops": ["A) 16", "B) 20", "C) 22", "D) 24"],
          "resp": "c",
      },
  ]

  pontos = 0
  for q in questoes:
    print(f"\n{q['p']}")
    for op in q["ops"]:
      print(op)

    while True:
      r = input("Resposta (A/B/C/D): ").strip().lower()
      if r in ["a", "b", "c", "d"]:
        break
      print("Opção inválida.")

    if r == q["resp"]:
      pontos += 1

  nota = (pontos / len(questoes)) * 10

  print("\n=== RESULTADO ===")
  print(f"Avaliado: {avaliado} | Avaliador: {avaliador}")
  print(f"Data: {data_hora}")
  print(f"Nota: {nota:.1f} / 10.0 ({pontos}/{len(questoes)} acertos)")

  # Salva o arquivo de log
  with open(f"resultado_{avaliado.replace(' ', '_').lower()}.txt", "w") as f:
    f.write(
        f"Avaliado: {avaliado}\nAvaliador: {avaliador}\nData: {data_hora}\nNota:"
        f" {nota:.1f}\n"
    )


if __name__ == "__main__":
  aplicar_prova()