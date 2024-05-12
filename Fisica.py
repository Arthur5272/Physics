import tkinter as tk

class Physics:
    #TODAS AS FUNÇÕES DE TODOS OS BOTOES DA TELA ROOT DEVEM FICAR AQUI

    def __init__(
            self,
            root: tk.Tk,
            label: tk.Label,
            buttons: list[tk.Button],
    ) -> None:
        self.root = root
        self.label = label
        self.buttons = buttons

    def start_home(self):
        #INICIA A JANELA HOME
        self.root.mainloop()

    def cinematic_window(self):
        cinematic_window = tk.Toplevel(self.root)
        cinematic_window.title("Cinemática")
        cinematic_window.config(padx=10, pady=10, bg="#2C2C2C")
        cinematic_window.resizable(False, False)
        cinematic_window.iconbitmap("apple1.ico")

        cinematic_label = tk.Label(cinematic_window, 
            text="Qual conceito da Cinemática você deseja explorar?",
            justify="center", bg="#2C2C2C", foreground="#fff"
        )
        cinematic_label.grid(row=0, column=0, sticky="news")

    def dynamics_window(self):
        dynamics_window = tk.Toplevel(self.root)
        dynamics_window.title("Dinâmica")
        dynamics_window.config(padx=10, pady=10, bg="#2C2C2C")
        dynamics_window.resizable(False, False)
        dynamics_window.iconbitmap("apple1.ico")

        dynamics_label = tk.Label(dynamics_window, 
            text="Qual princípio da Dinâmica você deseja usar?",
            justify="center", bg="#2C2C2C", foreground="#fff"
        )
        dynamics_label.grid(row=0, column=0, sticky="news")

    def work_energy_power_window(self):
        work_energy_power_window = tk.Toplevel(self.root)
        work_energy_power_window.title("Trabalho, Energia e Potência")
        work_energy_power_window.config(padx=10, pady=10, bg="#2C2C2C")
        work_energy_power_window.resizable(False, False)
        work_energy_power_window.iconbitmap("apple1.ico")

        work_energy_power_label = tk.Label(work_energy_power_window, 
            text="Qual grandeza física você deseja calcular?",
            justify="center", bg="#2C2C2C", foreground="#fff"
        )
        work_energy_power_label.grid(row=0, column=0, sticky="news")

    def momentum_window(self):
        momentum_window = tk.Toplevel(self.root)
        momentum_window.title("Impulso e Quantidade de Movimento")
        momentum_window.config(padx=10, pady=10, bg="#2C2C2C")
        momentum_window.resizable(False, False)
        momentum_window.iconbitmap("apple1.ico")

        momentum_label = tk.Label(momentum_window, 
            text="Qual relação entre Impulso e Quantidade de Movimento você deseja analisar?",
            justify="center", bg="#2C2C2C", foreground="#fff"
        )
        momentum_label.grid(row=0, column=0, sticky="news")

    def hydrostatics_window(self):
        hydrostatics_window = tk.Toplevel(self.root)
        hydrostatics_window.title("Hidrostática")
        hydrostatics_window.config(padx=10, pady=10, bg="#2C2C2C")
        hydrostatics_window.resizable(False, False)
        hydrostatics_window.iconbitmap("apple1.ico")

        hydrostatics_label = tk.Label(hydrostatics_window, 
            text="Qual princípio da Hidrostática você deseja aplicar?",
            justify="center", bg="#2C2C2C", foreground="#fff"
        )
        hydrostatics_label.grid(row=0, column=0, sticky="news")

    def universal_gravitation_window(self):
        universal_gravitation_window = tk.Toplevel(self.root)
        universal_gravitation_window.title("Gravitação Universal")
        universal_gravitation_window.config(padx=10, pady=10, bg="#2C2C2C")
        universal_gravitation_window.resizable(False, False)
        universal_gravitation_window.iconbitmap("apple1.ico")

        universal_gravitation_label = tk.Label(universal_gravitation_window, 
            text="Qual grandeza física relacionada à Gravitação Universal você deseja calcular?",
            justify="center", bg="#2C2C2C", foreground="#fff"
        )
        universal_gravitation_label.grid(row=0, column=0, sticky="news")

    def thermodynamics_window(self):
        thermodynamics_window = tk.Toplevel(self.root)
        thermodynamics_window.title("Termodinâmica")
        thermodynamics_window.config(padx=10, pady=10, bg="#2C2C2C")
        thermodynamics_window.resizable(False, False)
        thermodynamics_window.iconbitmap("apple1.ico")

        thermodynamics_label = tk.Label(thermodynamics_window, 
            text="Escolha a opção que deseja realizar em Termodinâmica:",
            justify="center", bg="#2C2C2C", foreground="#fff"
        )
        thermodynamics_label.grid(row=0, column=0, sticky="news")

    def waves_and_optics_window(self):
        waves_and_optics_window = tk.Toplevel(self.root)
        waves_and_optics_window.title("Ondas e Ótica")
        waves_and_optics_window.config(padx=10, pady=10, bg="#2C2C2C")
        waves_and_optics_window.resizable(False, False)
        waves_and_optics_window.iconbitmap("apple1.ico")

        waves_and_optics_label = tk.Label(waves_and_optics_window, 
            text="Qual fenômeno de Ondas e Ótica você deseja estudar?",
            justify="center", bg="#2C2C2C", foreground="#fff"
        )
        waves_and_optics_label.grid(row=0, column=0, sticky="news")

    def electricity_window(self):
        electricity_window = tk.Toplevel(self.root)
        electricity_window.title("Eletricidade")
        electricity_window.config(padx=10, pady=10, bg="#2C2C2C")
        electricity_window.resizable(False, False)
        electricity_window.iconbitmap("apple1.ico")

        electricity_label = tk.Label(electricity_window, 
            text="Qual conceito de Eletricidade você deseja explorar?",
            justify="center", bg="#2C2C2C", foreground="#fff"
        )
        electricity_label.grid(row=0, column=0, sticky="news")

    def electromagnetism_window(self):
        electromagnetism_window = tk.Toplevel(self.root)
        electromagnetism_window.title("Eletromagnetismo")
        electromagnetism_window.config(padx=10, pady=10, bg="#2C2C2C")
        electromagnetism_window.resizable(False, False)
        electromagnetism_window.iconbitmap("apple1.ico")

        electromagnetism_label = tk.Label(electromagnetism_window, 
            text="Qual princípio do Eletromagnetismo você deseja aplicar?",
            justify="center", bg="#2C2C2C", foreground="#fff"
        )
        electromagnetism_label.grid(row=0, column=0, sticky="news")

    def config_buttons(self):
    # DANDO COMANDO PARA QUANDO OS BOTÕES DA PAGINA HOME FOREM ACIONADOS
        for button in self.buttons:
            if button["text"] == "Cinemática":
                button.config(command=self.cinematic_window)  # Call the function directly
            elif button["text"] == "Dinâmica":
                button.config(command=self.dynamics_window)
            elif button["text"] == "Trabalho, Energia e Potência":
                button.config(command=self.work_energy_power_window)
            elif button["text"] == "Impulso e Quantidade de Movimento":
                button.config(command=self.momentum_window)
            elif button["text"] == "Hidrostática":
                button.config(command=self.hydrostatics_window)
            elif button["text"] == "Gravitação Universal":
                button.config(command=self.universal_gravitation_window)
            elif button["text"] == "Termodinamica":
                button.config(command=self.thermodynamics_window)
            elif button["text"] == "Ondas e Ótica":
                button.config(command=self.waves_and_optics_window)
            elif button["text"] == "Eletricidade":
                button.config(command=self.electricity_window)
            elif button["text"] == "Eletromagnetismo":
                button.config(command=self.electromagnetism_window)


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
    label.grid(row=0, column=0, sticky="news")
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
        btn.grid(row=row, column=0, sticky='news', padx=5, pady=5)
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
    physics.config_buttons()
    physics.start_home()

if __name__ == "__main__":
    main()
