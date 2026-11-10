"""
Sistema de Cadastro de Alunos
Disciplina: Design Profissional - Universidade Positivo
Integrantes: Murilo Mussi, Guilherme Rodrigues, Matheus Assalin
"""

import sys

# Estrutura de dados principal para armazenamento em memória
alunos = []


def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2


def definir_status(media):
    return "Aprovado" if media >= 7.0 else "Reprovado"


def buscar_aluno_por_ra(ra):
    for aluno in alunos:
        if aluno['ra'] == ra:
            return aluno
    return None


def exibir_menu():
    print("\n" + "=" * 40)
    print("      SISTEMA DE CADASTRO DE ALUNOS      ")
    print("=" * 40)
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Buscar Aluno por R.A.")
    print("4. Editar Aluno")
    print("5. Apagar Aluno")
    print("6. Relatório de Desempenho (Médias)")
    print("7. Sair")
    print("=" * 40)


def cadastrar_aluno():
    print("\n--- CADASTRO DE ALUNO ---")
    ra = input("Digite o R.A. do aluno: ").strip()

    if not ra:
        print("Erro: O R.A. não pode ser vazio.")
        return

    # Validação de R.A. duplicado
    for aluno in alunos:
        if aluno['ra'] == ra:
            print(f"Erro: Já existe um aluno cadastrado com o R.A. {ra}.")
            return

    nome = input("Digite o nome completo do aluno: ").strip()
    if not nome:
        print("Erro: O nome não pode ser vazio.")
        return

    try:
        nota1 = float(input("Digite a Nota 1 (0 a 10): "))
        nota2 = float(input("Digite a Nota 2 (0 a 10): "))
        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            print("Erro: As notas devem ser valores entre 0 e 10.")
            return
    except ValueError:
        print("Erro: Entrada inválida para as notas. Digite valores numéricos.")
        return

    media = calcular_media(nota1, nota2)
    status = definir_status(media)

    aluno = {
        'ra': ra,
        'nome': nome,
        'nota1': nota1,
        'nota2': nota2,
        'media': media,
        'status': status
    }

    alunos.append(aluno)
    print(f"\nAluno '{nome}' cadastrado com sucesso!")


def listar_alunos():
    print("\n--- LISTA DE ALUNOS ---")
    if not alunos:
        print("Nenhum aluno cadastrado no sistema.")
        return

    for i, aluno in enumerate(alunos, 1):
        print(f"{i}. R.A.: {aluno['ra']} | Nome: {aluno['nome']} | Média: {aluno['media']:.2f} | Status: {aluno['status']}")


def buscar_aluno():
    print("\n--- BUSCA DE ALUNO POR R.A. ---")
    if not alunos:
        print("Nenhum aluno cadastrado no sistema.")
        return

    ra_busca = input("Digite o R.A. do aluno desejado: ").strip()
    encontrado = False

    for aluno in alunos:
        if aluno['ra'] == ra_busca:
            print("\nAluno Encontrado:")
            print(f"  R.A.: {aluno['ra']}")
            print(f"  Nome: {aluno['nome']}")
            print(f"  Nota 1: {aluno['nota1']:.2f}")
            print(f"  Nota 2: {aluno['nota2']:.2f}")
            print(f"  Média: {aluno['media']:.2f}")
            print(f"  Situação: {aluno['status']}")
            encontrado = True
            break

    if not encontrado:
        print(f"Nenhum aluno encontrado com o R.A. '{ra_busca}'.")


def editar_aluno():
    print("\n--- EDIÇÃO DE ALUNO ---")
    if not alunos:
        print("Nenhum aluno cadastrado no sistema.")
        return

    ra = input("Digite o R.A. do aluno que deseja editar: ").strip()
    aluno = buscar_aluno_por_ra(ra)

    if aluno is None:
        print(f"Nenhum aluno encontrado com o R.A. '{ra}'.")
        return

    print(f"Aluno atual: {aluno['nome']} | Nota 1: {aluno['nota1']:.2f} | Nota 2: {aluno['nota2']:.2f}")

    novo_nome = input(f"Digite o novo nome [{aluno['nome']}]: ").strip()
    if not novo_nome:
        novo_nome = aluno['nome']

    try:
        nota1 = input(f"Digite a nova Nota 1 [{aluno['nota1']:.2f}]: ").strip()
        nota1 = float(nota1) if nota1 else aluno['nota1']

        nota2 = input(f"Digite a nova Nota 2 [{aluno['nota2']:.2f}]: ").strip()
        nota2 = float(nota2) if nota2 else aluno['nota2']

        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            print("Erro: As notas devem ser valores entre 0 e 10.")
            return
    except ValueError:
        print("Erro: Entrada inválida para as notas. Digite valores numéricos.")
        return

    aluno['nome'] = novo_nome
    aluno['nota1'] = nota1
    aluno['nota2'] = nota2
    aluno['media'] = calcular_media(nota1, nota2)
    aluno['status'] = definir_status(aluno['media'])

    print(f"Aluno '{aluno['nome']}' atualizado com sucesso!")


def apagar_aluno():
    print("\n--- EXCLUSÃO DE ALUNO ---")
    if not alunos:
        print("Nenhum aluno cadastrado no sistema.")
        return

    ra = input("Digite o R.A. do aluno que deseja apagar: ").strip()
    aluno = buscar_aluno_por_ra(ra)

    if aluno is None:
        print(f"Nenhum aluno encontrado com o R.A. '{ra}'.")
        return

    alunos.remove(aluno)
    print(f"Aluno '{aluno['nome']}' removido com sucesso!")


def relatorio_desempenho():
    print("\n--- RELATÓRIO DE DESEMPENHO ---")
    if not alunos:
        print("Nenhum dado disponível para gerar relatório.")
        return

    total_alunos = len(alunos)
    aprovados = sum(1 for a in alunos if a['status'] == "Aprovado")
    reprovados = total_alunos - aprovados
    media_geral = sum(a['media'] for a in alunos) / total_alunos

    print(f"Total de Alunos Cadastrados: {total_alunos}")
    print(f"Alunos Aprovados: {aprovados}")
    print(f"Alunos Reprovados: {reprovados}")
    print(f"Média Geral da Turma: {media_geral:.2f}")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-7): ").strip()

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            buscar_aluno()
        elif opcao == '4':
            editar_aluno()
        elif opcao == '5':
            apagar_aluno()
        elif opcao == '6':
            relatorio_desempenho()
        elif opcao == '7':
            print("\nEncerrando o Sistema de Cadastro de Alunos... Até logo!")
            sys.exit()
        else:
            print("\nOpção inválida! Por favor, escolha um número de 1 a 7.")


if __name__ == "__main__":
    main()