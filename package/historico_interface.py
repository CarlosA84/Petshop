import tkinter as tk
from tkinter import ttk
from package.banco import BancoDados

class HistoricoJanela:
    def __init__(self, master):
        self.janela = tk.Toplevel(master)
        self.janela.title("Histórico de Atendimentos")
        self.janela.geometry("500x400")
        self.janela.configure(bg="white")

        tk.Label(
            self.janela,
            text="📜 Histórico de Agendamentos",
            font=("Arial", 14, "bold"),
            bg="white",
        ).pack(pady=10)

        frame_texto = tk.Frame(self.janela, bg="white")
        frame_texto.pack(padx=10, pady=10, fill="both", expand=True)

        caixa_texto = tk.Text(
            frame_texto,
            width=60,
            height=15,
            wrap="word",
            font=("Arial", 10),
        )
        caixa_texto.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame_texto, command=caixa_texto.yview)
        scrollbar.pack(side="right", fill="y")

        caixa_texto.config(yscrollcommand=scrollbar.set)

        agendamentos = BancoDados.carregar_agendamentos()

        if not agendamentos:
            caixa_texto.insert(tk.END, "⚠️ Nenhum agendamento encontrado.\n")
        else:
            for idx, ag in enumerate(agendamentos, start=1):
                linha = (
                    f"{idx}. 🐾 Cliente: {ag.get('cliente', 'Não informado')}\n"
                    f"   🐕 Animal: {ag.get('animal', {}).get('tipo', 'Não informado')}, "
                    f"{ag.get('animal', {}).get('idade', '?')} anos, "
                    f"{ag.get('animal', {}).get('peso', '?')}kg\n"
                    f"   Serviços: {', '.join(ag.get('servicos', []))}\n"
                    f"---------------------------------------------\n"
                )
                caixa_texto.insert(tk.END, linha)

        caixa_texto.config(state="disabled")
