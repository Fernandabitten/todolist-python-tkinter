from tkinter import *

def entrada_card(container, fn_adicionar):
  entrada_card = Frame(container, bg="#1A202C")
  entrada_card.pack(fill="x", pady=10)

  input_tarefa = Entry(
    entrada_card, 
    font=("Arial", 14), 
    bg="#2D3748", 
    fg="white", 
    borderwidth=0
  )
  input_tarefa.pack(side=LEFT, fill="x", expand=True, padx=20, ipady=5)

  botao_adicionar = Button(
    entrada_card, 
    text='ADICIONAR', 
    command=fn_adicionar, 
    bg='#2D3748', 
    fg='#23CF5C', 
    font=("Arial", 14),
    cursor="hand2",
    borderwidth=0,    
  )
  botao_adicionar.pack(side=RIGHT, padx=10)

  return input_tarefa

def tarefa_card(container, concluida, tarefa, fn_marcar, fn_editar, fn_excluir):
  checkbuttons = {}
  # Cria um card para a tarefa
  card = Frame(container, bg="#E2E8F0", pady=5, padx=10)
  card.pack(fill="x", pady=5, padx=20)

  # Variável para controlar o status da tarefa
  var = BooleanVar(value=concluida)
  checkbuttons[tarefa] = Checkbutton(
    card,
    text=tarefa,
    variable=var,
    onvalue=True,
    offvalue=False,
    command=lambda t=tarefa, v=var: fn_marcar(t, v, checkbuttons, [btn_deletar, btn_editar]),
    bg='#E2E8F0',
    fg='#2D3748' if not concluida else '#A0AEC0',
    font=('Arial', 12, 'overstrike' if concluida else 'normal'),
    anchor='w',
    cursor='hand2',
  )
  checkbuttons[tarefa].pack(side=LEFT)  

  btn_editar = Button(
    card,
    text='🖋️',
    command=lambda t=tarefa: fn_editar(tarefa),
    bg='#E2E8F0',
    fg='blue',
    borderwidth=0,
    font=("Arial", 12),
    padx=0,
    width=5,
    cursor='circle' if concluida else 'hand2',
    state="disabled" if concluida else "normal",
  )
  btn_editar.pack(side=RIGHT)

  btn_deletar = Button(
    card,
    text='🗑',
    command=lambda t=tarefa: fn_excluir(t),
    bg='#E2E8F0',
    fg='red',
    borderwidth=0,
    font=('Arial', 12),
    cursor='circle' if concluida else 'hand2',
    state='disabled' if concluida else 'normal',
  )
  btn_deletar.pack(side=RIGHT)

def tarefas_card(container):
  tarefas_card = Frame(container, bg='#1A202C')
  tarefas_card.pack(fill='both', expand=True)
  return tarefas_card

def editor_modal(container, titulo, tarefa, fn_salvar):
  janela_edicao = Toplevel(container, padx=30, pady=30)
  janela_edicao.title(titulo)

  if titulo == 'EDITAR TAREFA':
  # Campo de entrada para o novo nome
    input_edicao = Entry(janela_edicao, width=30, justify='center', font=('Arial', 14), borderwidth=0)
    input_edicao.pack(padx=10, pady=5)
    input_edicao.insert(0, tarefa)  # Preenche o input da edição com o nome da tarefa a ser editada

    botao_editar = Button(
      janela_edicao,
      text='Salvar',
      command=lambda: fn_salvar(input_edicao, tarefa, janela_edicao),
      bg='#23CF5C',
      fg='white',
      font=('Arial', 12, 'bold'),
      cursor='hand2',
      borderwidth=0,
    )
    botao_editar.pack(side=RIGHT, padx=10, pady=10)
    botao_cancelar = Button(
      janela_edicao,
      text='Cancelar',
      command=lambda:janela_edicao.destroy(),
      font=('Arial', 12, 'bold'),
      cursor='hand2',
      borderwidth=0,
      relief='solid',      # Contorno visível
      bd=1,                # Largura da borda
      fg='grey',           # Cor do texto
      bg=None,             # Cor de fundo transparente
      highlightthickness=0 # Remover bordas de foco 
    )
    botao_cancelar.pack(side=RIGHT, padx=10)
  else:
    simbolo_alerta = Label(
      janela_edicao,
      text=f'⚠️',
      fg='#FFD700',
      font=('Arial', 14),
    )
    simbolo_alerta.pack(pady=5)
    # Mensagem de confirmação para exclusão
    mensagem_confirmacao = Label(
      janela_edicao,
      text=f'Tem certeza que deseja excluir a tarefa: "{tarefa}"?\nEla não poderá ser recuperada.',
      fg='#000000',
      font=('Arial', 12),
      justify='center'
    )
    mensagem_confirmacao.pack(pady=10)

    botao_excluir = Button(
      janela_edicao,
      text='Excluir',
      command=lambda: fn_salvar(tarefa, janela_edicao),
      bg='#FF0000',
      fg='white',
      font=('Arial', 12, 'bold'),
      cursor='hand2',
      borderwidth=0,
    )
    botao_excluir.pack(side=RIGHT, padx=10)

    botao_cancelar = Button(
      janela_edicao,
      text='Cancelar',
      command=lambda:janela_edicao.destroy(),
      font=('Arial', 12, 'bold'),
      cursor='hand2',
      borderwidth=0,
      relief='solid',      # Contorno visível
      bd=1,                # Largura da borda
      fg='grey',           # Cor do texto
      bg=None,             # Cor de fundo transparente
      highlightthickness=0 # Remover bordas de foco 
    )
    botao_cancelar.pack(side=RIGHT, padx=10)


