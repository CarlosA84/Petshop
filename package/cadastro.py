import tkinter as tk
from tkinter import messagebox
from package.banco import CadastroSimulado


class CadastroClientes:
    def __init__(self, master):
        self.janela = tk.Toplevel(master)
        self.janela.title("Cadastro de Clientes")
        self.janela.geometry("350x200")
        self.janela.configure(bg="white")

        self._criar_widgets()

    def _criar_widgets(self):
        tk.Label(self.janela, text="Nome completo*:", font=("Arial", 10), bg="white").pack(pady=5)
        self.entrada_nome = tk.Entry(self.janela, width=30)
        self.entrada_nome.pack()

        tk.Label(self.janela, text="CPF (11 dígitos)*:", font=("Arial", 10), bg="white").pack(pady=5)
        self.entrada_cpf = tk.Entry(self.janela, width=30)
        self.entrada_cpf.pack()

        tk.Button(self.janela, text="Confirmar Cadastro", command=self._confirmar).pack(pady=15)

    def _validar_cpf(self, cpf):
        return cpf.isdigit() and len(cpf) == 11

    def _confirmar(self):
        nome = self.entrada_nome.get().strip()
        cpf = self.entrada_cpf.get().strip()

        if not nome or not cpf:
            messagebox.showwarning("Campo obrigatório", "Preencha todos os campos.")
            return

        if not self._validar_cpf(cpf):
            messagebox.showerror("CPF inválido", "O CPF deve conter 11 dígitos numéricos.")
            return

        if CadastroSimulado.existe_cpf(cpf):
            messagebox.showerror("Erro", "CPF já cadastrado.")
            return

        CadastroSimulado.adicionar(nome, cpf)

        messagebox.showinfo("Sucesso", f"Cliente cadastrado:\nNome: {nome}\nCPF: {cpf}")
        self.janela.destroy()


# Teste isolado
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    CadastroClientes(root)
    root.mainloop()
