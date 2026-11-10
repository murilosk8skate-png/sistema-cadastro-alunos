import unittest
from unittest import mock

import sistema_alunos


class SistemaAlunosTestes(unittest.TestCase):
    def setUp(self):
        sistema_alunos.alunos.clear()

    def test_editar_aluno_atualiza_dados_e_media(self):
        sistema_alunos.alunos.append({
            "ra": "123",
            "nome": "Ana",
            "nota1": 5.0,
            "nota2": 6.0,
            "media": 5.5,
            "status": "Reprovado",
        })

        respostas = iter(["123", "Ana Paula", "8", "9"])
        with mock.patch("builtins.input", side_effect=lambda prompt="": next(respostas)):
            sistema_alunos.editar_aluno()

        self.assertEqual(len(sistema_alunos.alunos), 1)
        aluno = sistema_alunos.alunos[0]
        self.assertEqual(aluno["nome"], "Ana Paula")
        self.assertEqual(aluno["nota1"], 8.0)
        self.assertEqual(aluno["nota2"], 9.0)
        self.assertEqual(aluno["media"], 8.5)
        self.assertEqual(aluno["status"], "Aprovado")

    def test_apagar_aluno_remove_do_cadastro(self):
        sistema_alunos.alunos.extend([
            {"ra": "111", "nome": "Bruno", "nota1": 7.0, "nota2": 7.0, "media": 7.0, "status": "Aprovado"},
            {"ra": "222", "nome": "Carla", "nota1": 4.0, "nota2": 5.0, "media": 4.5, "status": "Reprovado"},
        ])

        with mock.patch("builtins.input", return_value="111"):
            sistema_alunos.apagar_aluno()

        self.assertEqual(len(sistema_alunos.alunos), 1)
        self.assertEqual(sistema_alunos.alunos[0]["ra"], "222")


if __name__ == "__main__":
    unittest.main()
