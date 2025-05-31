import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

from package.cadastro import CadastroClientes
from package.agendamento_interface import AgendamentoUI
from package.historico_interface import HistoricoJanela
from package.banco import BancoDados, CadastroSimulado  # Importar os dois


class PetShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu PetShop")
        self.root.geometry("500x600")
        self.root.configure(bg="#add8e6")

        # Carrega os agendamentos salvos
        self.agendamentos = BancoDados.carregar_agendamentos()

        self.criar_interface()

    def criar_interface(self):
        tk.Label(
            self.root,
            text="Bem-vindo ao PetShop Virtual",
            font=("Arial", 18, "bold"),
            bg="#add8e6",
            fg="navy"
        ).pack(pady=15)

        try:
            imagem_original = Image.open("e-commerce-pet-shop-dicas-para-se-destacar-e-aumentar-as-vendas.jpg")
            imagem_redimensionada = imagem_original.resize((400, 200))
            imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
            label = tk.Label(self.root, image=imagem_tk, bg="#add8e6")
            label.image = imagem_tk
            label.pack(pady=10)
        except Exception as e:
            tk.Label(self.root, text="Imagem não carregada.", font=("Arial", 12), bg="#add8e6", fg="red").pack(pady=10)
            print("Erro ao carregar imagem:", e)

        frame = tk.Frame(self.root, bg="#add8e6")
        frame.pack(expand=True)

        botoes = [
            ("Cadastro", self.abrir_cadastro_clientes),
            ("Agendamento de Serviços", self.abrir_agendamento),
            ("Histórico de Atendimentos", self.abrir_historico),
            ("Limpar Dados Salvos", self.limpar_dados_salvos),  # Novo botão aqui
            ("Sair", self.fechar_aplicacao)
        ]
        for texto, comando in botoes:
            ttk.Button(frame, text=texto, command=comando).pack(pady=10, ipadx=20, ipady=5)

    def abrir_cadastro_clientes(self):
        CadastroClientes(self.root)

    def abrir_agendamento(self):
        AgendamentoUI(self.root, self.agendamentos)

    def abrir_historico(self):
        HistoricoJanela(self.root)

    def limpar_dados_salvos(self):
        resposta = messagebox.askyesno(
            "Confirmação",
            "Deseja realmente apagar TODOS os dados salvos? Esta ação é irreversível."
        )
        if resposta:
            BancoDados.limpar_agendamentos()
            CadastroSimulado.limpar_clientes()
            self.agendamentos.clear()  # limpa a lista em memória também
            messagebox.showinfo("Sucesso", "Todos os dados foram apagados com sucesso!")

    def fechar_aplicacao(self):
        BancoDados.salvar_agendamentos(self.agendamentos)
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = PetShopApp(root)
    root.protocol("WM_DELETE_WINDOW", app.fechar_aplicacao)
    root.mainloop()
