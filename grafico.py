from Tkinter import *   #importa a bibioteca gráfica
 
root = Tk()             #cria a aplicação raiz. É uma janela com barra de título, botão para
                        #fechar,aumentar, etc.. Deve ser sempre o primeiro objeto a ser criado,
                        # e deve ser único em uma aplicação
 
w = Label(root, text="Tudo bem até aqui!")    #cria um label com o texto especificado
w.pack()                                      #insere na tela
 
root.mainloop()  
loop                            #inicializa o loop
