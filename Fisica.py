import tkinter as tk

class Physics:
    #TODAS AS FUNÇÕES DE TODOS OS BOTOES DA TELA ROOT DEVEM FICAR AQUI

    def __init__(
            self,
            root: tk.Tk,
            label: tk.Label,
            buttons: list[tk.Button]
    ) -> None:
        self.root = root
        self.label = label
        self.buttons = buttons

    def start_home(self):
        #INICIA A JANELA HOME
        self.root.mainloop()

def make_home_root() -> tk.Tk:
    #CRIANDO UMA INTERFACE HOME
    root = tk.Tk()
    root.title("Physics")
    root.config(padx=10, pady=10, bg="#2C2C2C")
    root.resizable(False, False)
    root.iconbitmap("apple1.ico")
    return root

def make_home_label(root) -> tk.Label:
    #CRIANDO UM TEXTO NA PAGINA HOME
    label = tk.Label(
        root, text="Qual tipo de problema iremos resolver?",
        justify="center", bg="#2C2C2C", foreground="#fff"
    )
    label.grid(row=0, column=0, columnspan=3, sticky="news")
    return label

def make_home_buttons(root) -> list[tk.Button]:
    # BUTÕES DE NAVEGAÇÃO NA PAGINA HOME
    button_texts: list[str] = [
        "Cinemática",
        "Dinâmica",
        "Trabalho, Energia e Potência",
        "Impulso e Quantidade de Movimento",
        "Hidrostática",
        "Gravitação Universal",
        "Termodinamica",
        "Ondas e Ótica",
        "Eletricidade",
        "Eletromagnetismo"
    ]

    buttons: list[tk.Button] = []

    for row, text in enumerate(button_texts, start=2):
        btn = tk.Button(root, text=text)
        btn.grid(row=row, column=0, columnspan=3, sticky='news', padx=5, pady=5)
        btn.config(
            font=("Times New Roman", 10, "bold"),
            pady=10, padx=100, width=1, bg="#545454", bd=0, foreground="#fff",
            cursor="hand2", highlightthickness=0, highlightcolor="#ccc",
            activebackground="#ccc", highlightbackground="#ccc"
        )
        buttons.append(btn)
    return buttons

def main():
    #EXECUTA PAGINA HOME
    root = make_home_root()
    label = make_home_label(root)
    buttons = make_home_buttons(root)
    physics = Physics(root, label, buttons)
    physics.start_home()

if __name__ == "__main__":
    main()
