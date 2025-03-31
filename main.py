from tkinter import *
from tkinter import ttk
import funcoes
import interface

# Caminho do arquivo de tarefas
ARQUIVO_TAREFAS = "tarefas.json"

tarefas = funcoes.carregar_tarefas(ARQUIVO_TAREFAS)

def contar_tarefas(tarefas):
  concluidas = sum(tarefas.values())
  nao_concluidas = len(tarefas) - concluidas
  return concluidas, nao_concluidas

# Função para atualizar a lista de tarefas
def atualizar_lista():
  # Limpa o frame
  for widget in tarefas_card.winfo_children():
      widget.destroy()
  if len(tarefas) == 0:
    subtitulo = Label(
      tarefas_card, 
      text="""Ainda não há tarefas registradas. 
      Adicione uma nova tarefa no campo acima!""", 
      font=("Arial", 16, "bold"), 
      justify=CENTER,
      relief=RAISED, 
      bg='#1A202C', 
      fg='white',         
    )
    subtitulo.pack(pady=20)
  for tarefa, concluida in tarefas.items():
    # Cria um card para cada tarefa
    interface.tarefa_card(tarefas_card, concluida, tarefa, marcar_tarefa, editar_tarefa, excluir_tarefa)

  # Atualiza o scrollregion do canvas
  my_canvas.update_idletasks()
  my_canvas.configure(scrollregion=my_canvas.bbox("all"))

  # Contar tarefas e atualizar a exibição  
  concluidas, nao_concluidas = contar_tarefas(tarefas)
  contagem.config(text=f"Concluídas: {concluidas} | Não concluídas: {nao_concluidas}")

def marcar_tarefa(tarefa, var, checkbuttons, botoes): 
  # Atualiza o estado da tarefa no dicionário
  tarefas[tarefa] = var.get()
  funcoes.salvar(ARQUIVO_TAREFAS, tarefas)
  """
  (Atualiza o estilo visual diretamente no Checkbutton pq se usar a função atualizar lista
  a tela treme toda vez que seleciona ou deseleciona  
  """
  checkbox = checkbuttons[tarefa]  # Precisa manter uma referência ao checkbox
  checkbox.config(
      fg="#A0AEC0" if var.get() else "#2D3748",
      font=("Arial", 12, "overstrike" if var.get() else "normal"),
  )
  # Habilita ou desabilita os botões de Editar e Excluir
  btn_editar = botoes[0]
  btn_excluir = botoes[1]
  estado = 'disabled' if var.get() else "normal"
  btn_excluir.config(state=estado)
  btn_editar.config(state=estado)

  # Contar tarefas e atualizar a exibição
  concluidas, nao_concluidas = contar_tarefas(tarefas)
  contagem.config(text=f"Concluídas: {concluidas} | Não concluídas: {nao_concluidas}")

def adicionar_tarefa():
  funcoes.adicionar_tarefa(tarefas, input_tarefa, ARQUIVO_TAREFAS, atualizar_lista)  

def excluir_tarefa(tarefa):
  # Abre modal de confirmação de exclusão de tarefa
  interface.editor_modal(tarefas_card, 'EXCLUIR TAREFA', tarefa, excluir)

def excluir(tarefa, janela):
  funcoes.excluir_tarefa(tarefa,tarefas, ARQUIVO_TAREFAS, atualizar_lista, janela)

def editar_tarefa(tarefa):
  # Cria modal para editar tarefa
  interface.editor_modal(tarefas_card, 'EDITAR TAREFA', tarefa, salvar_edicao)

def salvar_edicao(input_edicao, tarefa_antiga, janela_edicao):
  funcoes.editar(tarefas, input_edicao, tarefa_antiga, janela_edicao, ARQUIVO_TAREFAS, atualizar_lista)
    
app = Tk()
app.title('ToDo List')
app.geometry('500x500')
app.configure(bg='#1A202C')

# Layout principal
# Card de entrada
titulo = Label(app, text='To Do List', font=("Arial", 20, "bold"), bg='#1A202C', fg='white')
titulo.pack(ipady=10)

input_tarefa = interface.entrada_card(app, adicionar_tarefa)

subtitulo = Label(app, text='Lista de tarefas', font=("Arial", 16, "bold"), bg='#1A202C', fg='white')
subtitulo.pack(pady=15)

quadro_principal = Frame(app, bg='#1A202C')
quadro_principal.pack(fill=BOTH, expand=1)

# Criar o canvas
my_canvas = Canvas(quadro_principal, bg='#1A202C')
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Adicionar a barra de rolagem ao canvas
my_scrollbar = ttk.Scrollbar(quadro_principal, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configurar o canvas para ter a barra de rolagem
my_canvas.configure(yscrollcommand=my_scrollbar.set)

# Criar o quadro secundário dentro do canvas
# Lista de tarefas
tarefas_card = interface.tarefas_card(my_canvas)

window_id = my_canvas.create_window((0, 0), window=tarefas_card, anchor="nw")

# Redimensionar o quadro secundário (tarefas)
def ajustar_largura(event):
    largura_canvas = my_canvas.winfo_width()
    my_canvas.itemconfig(window_id, width=largura_canvas)

# Vincular evento de redimensionamento ao canvas
my_canvas.bind('<Configure>', lambda e: [
  my_canvas.configure(scrollregion=my_canvas.bbox('all')),
  ajustar_largura(e)
])

contagem = Label(app, text='', font=("Arial", 16, "bold"), bg='#1A202C', fg='white')
contagem.pack(pady=10)

atualizar_lista()
app.mainloop()
