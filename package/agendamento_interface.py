import tkinter as tk
from tkinter import ttk, messagebox
from package.banco import CadastroSimulado, BancoDados

class AgendamentoUI:
    def __init__(self, master, agendamentos):
        self.master = master
        self.janela = tk.Toplevel(master)
        self.janela.title("Agendamento")
        self.janela.geometry("500x500")
        self.janela.configure(bg="white")
        
        self.agendamentos = agendamentos
        self.cliente_encontrado = None
        self.tipo_animal = None
        self.idade_animal = None
        self.peso_animal = None
        
        self._criar_widgets_busca_cliente()

    def _criar_widgets_busca_cliente(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        tk.Label(self.janela, text="Digite o nome do cliente:", bg="white").pack(pady=10)
        self.entrada_cliente = tk.Entry(self.janela, width=30)
        self.entrada_cliente.pack()
        tk.Button(self.janela, text="Buscar Cliente", command=self._buscar_cliente).pack(pady=15)

    def _buscar_cliente(self):
        nome = self.entrada_cliente.get().strip()
        if not nome:
            messagebox.showwarning("Campo vazio", "Por favor, informe o nome do cliente.")
            return
        
        if not CadastroSimulado.existe_nome(nome):
            messagebox.showerror("Cliente não encontrado", "Cliente não cadastrado. Faça o cadastro primeiro.")
            return
        
        self.cliente_encontrado = nome
        self._criar_widgets_info_animal()

    def _criar_widgets_info_animal(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        tk.Label(self.janela, text=f"Cliente: {self.cliente_encontrado}", bg="white", justify="left").pack(pady=5)
        tk.Label(self.janela, text="Informações do Animal:", font=('Arial', 10, 'bold'), bg="white").pack(pady=10)
        
        tk.Label(self.janela, text="Tipo do animal:", bg="white").pack()
        self.tipo_var = tk.StringVar()
        tipos = ["Cachorro", "Gato", "Hamster"]
        self.cb_tipo = ttk.Combobox(self.janela, textvariable=self.tipo_var, values=tipos, state="readonly")
        self.cb_tipo.current(0)
        self.cb_tipo.pack(pady=5)
        
        tk.Label(self.janela, text="Idade (anos):", bg="white").pack()
        self.entrada_idade = tk.Entry(self.janela, width=10)
        self.entrada_idade.pack(pady=5)
        
        tk.Label(self.janela, text="Peso (kg):", bg="white").pack()
        self.entrada_peso = tk.Entry(self.janela, width=10)
        self.entrada_peso.pack(pady=5)
        
        tk.Button(self.janela, text="Continuar", command=self._validar_animal).pack(pady=20)

    def _validar_animal(self):
        self.tipo_animal = self.cb_tipo.get()
        self.idade_animal = self.entrada_idade.get()
        self.peso_animal = self.entrada_peso.get()
        
        if not self.idade_animal.isdigit() or int(self.idade_animal) <= 0:
            messagebox.showerror("Idade inválida", "Informe uma idade válida em anos.")
            return
        
        try:
            peso = float(self.peso_animal)
            if peso <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Peso inválido", "Informe um peso válido em kg.")
            return
        
        self._criar_widgets_servicos()

    def _criar_widgets_servicos(self):
        for widget in self.janela.winfo_children():
            widget.destroy()
        
        info = f"""Cliente: {self.cliente_encontrado}
Animal: {self.tipo_animal}, {self.idade_animal} anos, {self.peso_animal}kg"""
        tk.Label(self.janela, text=info, bg="white", justify="left").pack(pady=10)
        
        tk.Label(self.janela, text="Selecione os serviços:", font=('Arial', 10, 'bold'), bg="white").pack(pady=10)
        
        self.banho_var = tk.BooleanVar()
        self.tosa_var = tk.BooleanVar()
        tk.Checkbutton(self.janela, text="Banho - R$60", variable=self.banho_var, bg="white").pack(anchor="w", padx=20)
        tk.Checkbutton(self.janela, text="Tosa - R$80", variable=self.tosa_var, bg="white").pack(anchor="w", padx=20)
        
        tk.Button(self.janela, text="Confirmar Agendamento", command=self._confirmar_agendamento).pack(pady=20)

    def _confirmar_agendamento(self):
        servicos = []
        if self.banho_var.get():
            servicos.append("Banho")
        if self.tosa_var.get():
            servicos.append("Tosa")
        
        if not servicos:
            messagebox.showwarning("Nenhum serviço", "Selecione pelo menos um serviço.")
            return
        
        agendamento = {
            "cliente": self.cliente_encontrado,
            "animal": {
                "tipo": self.tipo_animal,
                "idade": self.idade_animal,
                "peso": self.peso_animal
            },
            "servicos": servicos
        }
        
        self.agendamentos.append(agendamento)
        BancoDados.salvar_agendamentos(self.agendamentos)  # 🔹 Salva imediatamente
        messagebox.showinfo("Sucesso", "Agendamento confirmado com sucesso!")
        self.janela.destroy()
