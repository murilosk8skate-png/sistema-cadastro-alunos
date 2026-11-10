# Sistema de Cadastro de Alunos

## Descrição do Projeto
Este projeto foi desenvolvido como atividade prática da disciplina de **Design Profissional** da **Universidade Positivo**. O objetivo principal é simular um ambiente real de desenvolvimento colaborativo de software, aplicando práticas de controle de versão com Git e hospedagem de código no GitHub.

O programa consiste em um sistema de terminal para cadastro, busca e gerenciamento de notas de alunos, calculando médias e gerando estatísticas gerais de desempenho.

## Integrantes da Equipe
* **Murilo Mussi** - *Desenvolvedor / Cadastro de alunos*
* **Guilherme Rodrigues** - *Desenvolvedor / Interface Gráfica*
* **Matheus Assalin** - *Desenvolvedor / Funcionalidade de editar e remover aluno*

## Funcionalidades
- **Cadastro de Alunos**: Registro de R.A., Nome, Nota 1 e Nota 2.
- **Validações de Entrada**: Impedimento de R.A. duplicado, nomes vazios e notas fora do intervalo [0, 10].
- **Listagem Geral**: Exibição simplificada de todos os alunos cadastrados.
- **Consulta por R.A.**: Busca individual detalhada.
- **Relatório de Desempenho**: Apresentação da quantidade de aprovados, reprovados e média geral da turma.

## Instruções de Execução

### Pré-requisitos
- Python 3.8 ou superior instalado.
- Terminal / Prompt de Comando ou Visual Studio Code.

### Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/murilosk8skate-png/sistema-cadastro-alunos.git
   ```

## Interface gráfica (Tkinter)

Além do sistema de terminal, o projeto inclui uma interface gráfica independente para cadastrar, consultar e acompanhar o desempenho dos alunos. A interface utiliza a mesma estrutura de dados e as mesmas regras de validação do programa de terminal.

Execute a partir da pasta do projeto:

```bash
python sistema_alunos_gui.py
```

O Tkinter faz parte da biblioteca padrão do Python. Os dados permanecem em memória durante a execução, como no programa de terminal; ao fechar o aplicativo, os cadastros não são gravados em arquivo.
