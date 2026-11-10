"""Interface gráfica para o Sistema de Cadastro de Alunos."""

import tkinter as tk
from tkinter import messagebox, ttk

import sistema_alunos


BACKGROUND = "#f4f6fb"
SURFACE = "#ffffff"
TEXT = "#202b3c"
MUTED = "#718096"
PRIMARY = "#4656d6"
SIDEBAR = "#18233b"
GREEN = "#138a65"
RED = "#d34b58"


class SistemaAlunosApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Alunos | Sistema de Cadastro")
        self.geometry("1120x720")
        self.minsize(900, 600)
        self.configure(bg=BACKGROUND)

        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self._configure_styles()
        self._build_layout()
        self.show_view("students")

    def _configure_styles(self):
        self.style.configure(
            "Treeview",
            background=SURFACE,
            fieldbackground=SURFACE,
            foreground=TEXT,
            rowheight=38,
            borderwidth=0,
            font=("Segoe UI", 10),
        )
        self.style.configure(
            "Treeview.Heading",
            background="#f7f8fc",
            foreground=MUTED,
            font=("Segoe UI Semibold", 9),
            relief="flat",
            padding=(10, 11),
        )
        self.style.map(
            "Treeview",
            background=[("selected", "#e7eaff")],
            foreground=[("selected", TEXT)],
        )
        self.style.configure(
            "Primary.TButton",
            background=PRIMARY,
            foreground="#ffffff",
            padding=(15, 10),
            borderwidth=0,
            font=("Segoe UI Semibold", 10),
        )
        self.style.map(
            "Primary.TButton",
            background=[("active", "#3544bd"), ("pressed", "#2e3ca9")],
        )
        self.style.configure(
            "Nav.TButton",
            background=SIDEBAR,
            foreground="#c2cadd",
            anchor="w",
            padding=(18, 12),
            borderwidth=0,
            font=("Segoe UI", 10),
        )
        self.style.map(
            "Nav.TButton",
            background=[("active", "#263552")],
            foreground=[("active", "#ffffff")],
        )

    def _build_layout(self):
        self.sidebar = tk.Frame(self, bg=SIDEBAR, width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        brand = tk.Frame(self.sidebar, bg=SIDEBAR)
        brand.pack(fill="x", padx=20, pady=(27, 38))
        tk.Label(
            brand,
            text="SA",
            bg=PRIMARY,
            fg="#ffffff",
            font=("Segoe UI Semibold", 12),
            width=3,
            height=1,
            pady=6,
        ).pack(side="left")
        tk.Label(
            brand,
            text="Portal do Aluno",
            bg=SIDEBAR,
            fg="#ffffff",
            font=("Segoe UI Semibold", 12),
        ).pack(side="left", padx=10)

        tk.Label(
            self.sidebar,
            text="MENU PRINCIPAL",
            bg=SIDEBAR,
            fg="#8995ad",
            font=("Segoe UI Semibold", 8),
        ).pack(anchor="w", padx=22, pady=(0, 10))
        ttk.Button(
            self.sidebar,
            text="  Alunos",
            style="Nav.TButton",
            command=lambda: self.show_view("students"),
        ).pack(fill="x", padx=10, pady=2)
        ttk.Button(
            self.sidebar,
            text="  Relatórios",
            style="Nav.TButton",
            command=lambda: self.show_view("reports"),
        ).pack(fill="x", padx=10, pady=2)

        tk.Label(
            self.sidebar,
            text="Cadastro acadêmico\nNotas e desempenho da turma",
            bg=SIDEBAR,
            fg="#8995ad",
            justify="left",
            font=("Segoe UI", 9),
        ).pack(side="bottom", anchor="w", padx=22, pady=22)

        self.main_area = tk.Frame(self, bg=BACKGROUND)
        self.main_area.pack(side="left", fill="both", expand=True)
        self._build_topbar()

        self.views = {
            "students": self._build_students_view(),
            "reports": self._build_reports_view(),
        }

    def _build_topbar(self):
        topbar = tk.Frame(self.main_area, bg=SURFACE, height=68)
        topbar.pack(fill="x")
        topbar.pack_propagate(False)
        tk.Label(
            topbar,
            text="Sistema de Cadastro de Alunos",
            bg=SURFACE,
            fg=TEXT,
            font=("Segoe UI Semibold", 12),
        ).pack(side="left", padx=28)
        tk.Label(
            topbar,
            text="Universidade Positivo",
            bg=SURFACE,
            fg=MUTED,
            font=("Segoe UI", 9),
        ).pack(side="right", padx=28)

    def _build_students_view(self):
        view = tk.Frame(self.main_area, bg=BACKGROUND)
        heading = tk.Frame(view, bg=BACKGROUND)
        heading.pack(fill="x", padx=30, pady=(28, 20))
        title_block = tk.Frame(heading, bg=BACKGROUND)
        title_block.pack(side="left")
        tk.Label(
            title_block,
            text="Alunos",
            bg=BACKGROUND,
            fg=TEXT,
            font=("Segoe UI Semibold", 22),
        ).pack(anchor="w")
        tk.Label(
            title_block,
            text="Gerencie os cadastros e acompanhe o desempenho da turma.",
            bg=BACKGROUND,
            fg=MUTED,
            font=("Segoe UI", 10),
        ).pack(anchor="w", pady=(3, 0))
        ttk.Button(
            heading,
            text="+  Novo aluno",
            style="Primary.TButton",
            command=self.open_student_form,
        ).pack(side="right", anchor="center")

        self.student_metrics = tk.Frame(view, bg=BACKGROUND)
        self.student_metrics.pack(fill="x", padx=30, pady=(0, 20))
        self.metric_values = {}
        self._build_metric(self.student_metrics, self.metric_values, "Alunos cadastrados", "total", PRIMARY)
        self._build_metric(self.student_metrics, self.metric_values, "Aprovados", "approved", GREEN)
        self._build_metric(self.student_metrics, self.metric_values, "Reprovados", "failed", RED)
        self._build_metric(self.student_metrics, self.metric_values, "Média da turma", "average", "#d39128")

        table_card = tk.Frame(view, bg=SURFACE, highlightthickness=1, highlightbackground="#e8ebf2")
        table_card.pack(fill="both", expand=True, padx=30, pady=(0, 26))
        table_heading = tk.Frame(table_card, bg=SURFACE)
        table_heading.pack(fill="x", padx=20, pady=(18, 14))
        tk.Label(
            table_heading,
            text="Lista de alunos",
            bg=SURFACE,
            fg=TEXT,
            font=("Segoe UI Semibold", 12),
        ).pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *_: self.refresh_students())
        search = tk.Entry(
            table_heading,
            textvariable=self.search_var,
            bg="#f7f8fc",
            fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            font=("Segoe UI", 10),
            width=27,
        )
        search.pack(side="right", ipady=8, padx=(10, 0))
        tk.Label(
            table_heading,
            text="Buscar por nome ou R.A.",
            bg=SURFACE,
            fg=MUTED,
            font=("Segoe UI", 9),
        ).pack(side="right")

        actions = tk.Frame(table_heading, bg=SURFACE)
        actions.pack(side="left", padx=(0, 10))
        ttk.Button(actions, text="Editar", command=self.edit_selected_student).pack(side="left", padx=(0, 8))
        ttk.Button(actions, text="Excluir", command=self.delete_selected_student).pack(side="left")

        table_frame = tk.Frame(table_card, bg=SURFACE)
        table_frame.pack(fill="both", expand=True, padx=20, pady=(0, 18))
        columns = ("ra", "nome", "nota1", "nota2", "media", "status")
        self.student_table = ttk.Treeview(table_frame, columns=columns, show="headings")
        headings = {
            "ra": ("R.A.", 105, "w"),
            "nome": ("Nome do aluno", 260, "w"),
            "nota1": ("Nota 1", 85, "center"),
            "nota2": ("Nota 2", 85, "center"),
            "media": ("Média", 85, "center"),
            "status": ("Situação", 125, "center"),
        }
        for column, (label, width, anchor) in headings.items():
            self.student_table.heading(column, text=label)
            self.student_table.column(column, width=width, anchor=anchor)
        self.student_table.tag_configure("Aprovado", foreground=GREEN)
        self.student_table.tag_configure("Reprovado", foreground=RED)
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.student_table.yview)
        self.student_table.configure(yscrollcommand=scrollbar.set)
        self.student_table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.student_table.bind("<Double-1>", self.show_student_details)
        self.empty_label = tk.Label(
            table_frame,
            text="",
            bg=SURFACE,
            fg=MUTED,
            font=("Segoe UI", 10),
        )
        self.empty_label.place(relx=0.5, rely=0.55, anchor="center")
        self.refresh_students()
        return view

    def _build_reports_view(self):
        view = tk.Frame(self.main_area, bg=BACKGROUND)
        tk.Label(
            view,
            text="Relatórios",
            bg=BACKGROUND,
            fg=TEXT,
            font=("Segoe UI Semibold", 22),
        ).pack(anchor="w", padx=30, pady=(28, 4))
        tk.Label(
            view,
            text="Resumo do desempenho acadêmico da turma.",
            bg=BACKGROUND,
            fg=MUTED,
            font=("Segoe UI", 10),
        ).pack(anchor="w", padx=30, pady=(0, 22))

        self.report_metrics = tk.Frame(view, bg=BACKGROUND)
        self.report_metrics.pack(fill="x", padx=30)
        self.report_metric_values = {}
        self._build_metric(self.report_metrics, self.report_metric_values, "Total de alunos", "total", PRIMARY)
        self._build_metric(self.report_metrics, self.report_metric_values, "Aprovados", "approved", GREEN)
        self._build_metric(self.report_metrics, self.report_metric_values, "Reprovados", "failed", RED)
        self._build_metric(self.report_metrics, self.report_metric_values, "Média geral", "average", "#d39128")

        chart_card = tk.Frame(view, bg=SURFACE, highlightthickness=1, highlightbackground="#e8ebf2")
        chart_card.pack(fill="x", padx=30, pady=20)
        tk.Label(
            chart_card,
            text="Distribuição de resultados",
            bg=SURFACE,
            fg=TEXT,
            font=("Segoe UI Semibold", 12),
        ).pack(anchor="w", padx=22, pady=(20, 4))
        tk.Label(
            chart_card,
            text="Percentual de alunos aprovados e reprovados",
            bg=SURFACE,
            fg=MUTED,
            font=("Segoe UI", 9),
        ).pack(anchor="w", padx=22)
        self.report_chart = tk.Canvas(
            chart_card,
            height=40,
            bg=SURFACE,
            highlightthickness=0,
        )
        self.report_chart.pack(fill="x", padx=22, pady=(18, 8))
        legend = tk.Frame(chart_card, bg=SURFACE)
        legend.pack(fill="x", padx=22, pady=(0, 20))
        tk.Label(legend, text="● Aprovados", bg=SURFACE, fg=GREEN, font=("Segoe UI", 9)).pack(side="left")
        tk.Label(legend, text="● Reprovados", bg=SURFACE, fg=RED, font=("Segoe UI", 9)).pack(
            side="left", padx=22
        )
        self.refresh_reports()
        return view

    def _build_metric(self, parent, values, title, key, accent):
        card = tk.Frame(parent, bg=SURFACE, highlightthickness=1, highlightbackground="#e8ebf2")
        card.pack(side="left", fill="both", expand=True, padx=(0, 12))
        tk.Frame(card, bg=accent, width=4).pack(side="left", fill="y")
        content = tk.Frame(card, bg=SURFACE)
        content.pack(side="left", padx=15, pady=14)
        tk.Label(content, text=title, bg=SURFACE, fg=MUTED, font=("Segoe UI", 9)).pack(anchor="w")
        value_label = tk.Label(
            content,
            text="0",
            bg=SURFACE,
            fg=TEXT,
            font=("Segoe UI Semibold", 19),
        )
        value_label.pack(anchor="w", pady=(4, 0))
        values[key] = value_label

    def _get_stats(self):
        alunos = sistema_alunos.alunos
        total = len(alunos)
        approved = sum(1 for aluno in alunos if aluno["status"] == "Aprovado")
        average = sum(aluno["media"] for aluno in alunos) / total if total else 0
        return {
            "total": total,
            "approved": approved,
            "failed": total - approved,
            "average": average,
        }

    def refresh_students(self):
        stats = self._get_stats()
        for key, label in self.metric_values.items():
            label.configure(text=f"{stats[key]:.2f}" if key == "average" else str(stats[key]))

        if not hasattr(self, "student_table"):
            return
        for item in self.student_table.get_children():
            self.student_table.delete(item)
        query = self.search_var.get().strip().casefold()
        visible_students = [
            aluno
            for aluno in sistema_alunos.alunos
            if query in aluno["nome"].casefold() or query in aluno["ra"].casefold()
        ]
        for aluno in visible_students:
            self.student_table.insert(
                "",
                "end",
                values=(
                    aluno["ra"],
                    aluno["nome"],
                    f"{aluno['nota1']:.2f}",
                    f"{aluno['nota2']:.2f}",
                    f"{aluno['media']:.2f}",
                    aluno["status"],
                ),
                tags=(aluno["status"],),
            )
        if not visible_students:
            self.empty_label.configure(
                text="Nenhum aluno cadastrado." if not sistema_alunos.alunos else "Nenhum aluno encontrado."
            )
            self.empty_label.lift()
        else:
            self.empty_label.configure(text="")

    def refresh_reports(self):
        if not hasattr(self, "report_metric_values"):
            return
        stats = self._get_stats()
        for key, label in self.report_metric_values.items():
            label.configure(text=f"{stats[key]:.2f}" if key == "average" else str(stats[key]))
        self._draw_report_chart(stats)

    def _draw_report_chart(self, stats):
        canvas = self.report_chart
        canvas.delete("all")
        canvas.update_idletasks()
        width = max(canvas.winfo_width(), 300)
        y1, y2 = 4, 28
        canvas.create_rectangle(0, y1, width, y2, fill="#edf0f6", outline="")
        if stats["total"]:
            approved_width = width * stats["approved"] / stats["total"]
            canvas.create_rectangle(0, y1, approved_width, y2, fill=GREEN, outline="")
            canvas.create_rectangle(approved_width, y1, width, y2, fill=RED, outline="")

    def show_view(self, name):
        if hasattr(self, "active_view"):
            self.active_view.pack_forget()
        self.active_view = self.views[name]
        self.active_view.pack(fill="both", expand=True)
        if name == "students":
            self.refresh_students()
        else:
            self.refresh_reports()

    def open_student_form(self):
        dialog = tk.Toplevel(self)
        dialog.title("Cadastrar aluno")
        dialog.configure(bg=SURFACE)
        dialog.resizable(False, False)
        dialog.transient(self)
        dialog.grab_set()

        tk.Label(
            dialog,
            text="Novo aluno",
            bg=SURFACE,
            fg=TEXT,
            font=("Segoe UI Semibold", 17),
        ).grid(row=0, column=0, columnspan=2, sticky="w", padx=24, pady=(22, 3))
        tk.Label(
            dialog,
            text="Preencha os dados e as duas notas do aluno.",
            bg=SURFACE,
            fg=MUTED,
            font=("Segoe UI", 9),
        ).grid(row=1, column=0, columnspan=2, sticky="w", padx=24, pady=(0, 15))

        fields = (
            ("R.A.", "ra"),
            ("Nome completo", "nome"),
            ("Nota 1 (0 a 10)", "nota1"),
            ("Nota 2 (0 a 10)", "nota2"),
        )
        entries = {}
        for row, (label, key) in enumerate(fields, start=2):
            tk.Label(
                dialog,
                text=label,
                bg=SURFACE,
                fg=TEXT,
                font=("Segoe UI Semibold", 9),
            ).grid(row=row, column=0, sticky="w", padx=24, pady=6)
            entry = tk.Entry(
                dialog,
                width=34,
                bg="#f7f8fc",
                fg=TEXT,
                insertbackground=TEXT,
                relief="flat",
                font=("Segoe UI", 10),
            )
            entry.grid(row=row, column=1, padx=(5, 24), pady=6, ipady=8, sticky="ew")
            entries[key] = entry

        buttons = tk.Frame(dialog, bg=SURFACE)
        buttons.grid(row=6, column=0, columnspan=2, sticky="e", padx=24, pady=(18, 22))
        ttk.Button(buttons, text="Cancelar", command=dialog.destroy).pack(side="left", padx=(0, 8))
        ttk.Button(
            buttons,
            text="Cadastrar aluno",
            style="Primary.TButton",
            command=lambda: self._save_student(dialog, entries),
        ).pack(side="left")
        entries["ra"].focus_set()

    def _save_student(self, dialog, entries, editing_ra=None):
        ra = entries["ra"].get().strip()
        nome = entries["nome"].get().strip()
        if not ra:
            messagebox.showerror("Dados inválidos", "O R.A. não pode ser vazio.", parent=dialog)
            entries["ra"].focus_set()
            return
        if any(aluno["ra"] == ra and aluno["ra"] != editing_ra for aluno in sistema_alunos.alunos):
            messagebox.showerror("R.A. duplicado", f"Já existe um aluno com o R.A. {ra}.", parent=dialog)
            entries["ra"].focus_set()
            return
        if not nome:
            messagebox.showerror("Dados inválidos", "O nome não pode ser vazio.", parent=dialog)
            entries["nome"].focus_set()
            return
        try:
            nota1 = float(entries["nota1"].get().strip())
            nota2 = float(entries["nota2"].get().strip())
        except ValueError:
            messagebox.showerror("Notas inválidas", "Digite valores numéricos para as duas notas.", parent=dialog)
            return
        if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            messagebox.showerror("Notas inválidas", "As notas devem estar entre 0 e 10.", parent=dialog)
            return

        media = (nota1 + nota2) / 2
        status = "Aprovado" if media >= 7.0 else "Reprovado"

        if editing_ra is None:
            sistema_alunos.alunos.append({
                "ra": ra,
                "nome": nome,
                "nota1": nota1,
                "nota2": nota2,
                "media": media,
                "status": status,
            })
            message_text = f"Aluno '{nome}' cadastrado com sucesso."
        else:
            for aluno in sistema_alunos.alunos:
                if aluno["ra"] == editing_ra:
                    aluno["ra"] = ra
                    aluno["nome"] = nome
                    aluno["nota1"] = nota1
                    aluno["nota2"] = nota2
                    aluno["media"] = media
                    aluno["status"] = status
                    break
            message_text = f"Aluno '{nome}' atualizado com sucesso."

        dialog.destroy()
        self.refresh_students()
        self.refresh_reports()
        messagebox.showinfo("Operação concluída", message_text, parent=self)

    def edit_selected_student(self):
        selection = self.student_table.selection()
        if not selection:
            messagebox.showwarning("Seleção necessária", "Selecione um aluno na tabela para editar.", parent=self)
            return
        values = self.student_table.item(selection[0], "values")
        aluno = next((item for item in sistema_alunos.alunos if item["ra"] == values[0]), None)
        if aluno is None:
            messagebox.showerror("Aluno não encontrado", "Não foi possível localizar o aluno selecionado.", parent=self)
            return

        dialog = tk.Toplevel(self)
        dialog.title("Editar aluno")
        dialog.configure(bg=SURFACE)
        dialog.resizable(False, False)
        dialog.transient(self)
        dialog.grab_set()

        tk.Label(
            dialog,
            text="Editar aluno",
            bg=SURFACE,
            fg=TEXT,
            font=("Segoe UI Semibold", 17),
        ).grid(row=0, column=0, columnspan=2, sticky="w", padx=24, pady=(22, 3))
        tk.Label(
            dialog,
            text="Atualize os dados e as notas do aluno.",
            bg=SURFACE,
            fg=MUTED,
            font=("Segoe UI", 9),
        ).grid(row=1, column=0, columnspan=2, sticky="w", padx=24, pady=(0, 15))

        fields = (
            ("R.A.", "ra", aluno["ra"]),
            ("Nome completo", "nome", aluno["nome"]),
            ("Nota 1 (0 a 10)", "nota1", str(aluno["nota1"])),
            ("Nota 2 (0 a 10)", "nota2", str(aluno["nota2"])),
        )
        entries = {}
        for row, (label, key, default) in enumerate(fields, start=2):
            tk.Label(dialog, text=label, bg=SURFACE, fg=TEXT, font=("Segoe UI Semibold", 9)).grid(
                row=row, column=0, sticky="w", padx=24, pady=6
            )
            entry = tk.Entry(
                dialog,
                width=34,
                bg="#f7f8fc",
                fg=TEXT,
                insertbackground=TEXT,
                relief="flat",
                font=("Segoe UI", 10),
            )
            entry.insert(0, default)
            entry.grid(row=row, column=1, padx=(5, 24), pady=6, ipady=8, sticky="ew")
            entries[key] = entry

        buttons = tk.Frame(dialog, bg=SURFACE)
        buttons.grid(row=6, column=0, columnspan=2, sticky="e", padx=24, pady=(18, 22))
        ttk.Button(buttons, text="Cancelar", command=dialog.destroy).pack(side="left", padx=(0, 8))
        ttk.Button(
            buttons,
            text="Salvar alterações",
            style="Primary.TButton",
            command=lambda: self._save_student(dialog, entries, editing_ra=aluno["ra"]),
        ).pack(side="left")
        entries["ra"].focus_set()

    def delete_selected_student(self):
        selection = self.student_table.selection()
        if not selection:
            messagebox.showwarning("Seleção necessária", "Selecione um aluno na tabela para excluir.", parent=self)
            return
        values = self.student_table.item(selection[0], "values")
        aluno = next((item for item in sistema_alunos.alunos if item["ra"] == values[0]), None)
        if aluno is None:
            messagebox.showerror("Aluno não encontrado", "Não foi possível localizar o aluno selecionado.", parent=self)
            return
        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            f"Deseja realmente excluir o aluno '{aluno['nome']}' (R.A. {aluno['ra']})?",
            parent=self,
        )
        if not confirmar:
            return
        sistema_alunos.alunos[:] = [item for item in sistema_alunos.alunos if item["ra"] != aluno["ra"]]
        self.refresh_students()
        self.refresh_reports()
        messagebox.showinfo("Aluno excluído", f"Aluno '{aluno['nome']}' removido com sucesso.", parent=self)

    def show_student_details(self, _event):
        selection = self.student_table.selection()
        if not selection:
            return
        values = self.student_table.item(selection[0], "values")
        messagebox.showinfo(
            "Detalhes do aluno",
            f"R.A.: {values[0]}\n"
            f"Nome: {values[1]}\n"
            f"Nota 1: {values[2]}\n"
            f"Nota 2: {values[3]}\n"
            f"Média: {values[4]}\n"
            f"Situação: {values[5]}",
            parent=self,
        )


if __name__ == "__main__":
    SistemaAlunosApp().mainloop()
