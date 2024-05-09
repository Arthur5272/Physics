import tkinter as tk

class fisica:
    #TODAS AS FUNÇÕES DE TODOS OS BOTOES DA TELA ROOT DEVEM FICAR AQUI
    def Botao_MU(self):
        #NOVA JANELA QUE CONTROLA AS INFORMAÇÕES DENTRO DO MOVIMENTO UNIFORME
        janelaMovimentoUniforme = tk.Tk()
        janelaMovimentoUniforme.title("ALTEREI AS INFORMAÇÕES DA JANELA")
        label = tk.Label(janelaMovimentoUniforme, text="ALTEREI AS INFORMAÇÕES DA JANELA")
        label.pack(padx=20, pady=10)
   
    


    #JANELA QUE CONTROLA AS INFORMAÇÕES DA TELA ROOT
    def __init__(self, root):
        self.root = root
        self.root.title("FÍSICA")
        

        #ATRIBUIÇÃO DO LABEL E BUTTON DA TELA ROOT
        self.MovimetnoUniforme= tk.Label(root, text="MOVIMENTO UNIFORME")
        self.MovimetnoUniforme.grid(row=1, column=1)
        self.BotaoMovimentoUniforme = tk.Button(root, text=("SELECIONAR"), command=self.Botao_MU )
        self.BotaoMovimentoUniforme.grid(row=1, column=2)



    

if __name__ == "__main__":
    root = tk.Tk()
    fisica = fisica(root)
    
    root.mainloop()
