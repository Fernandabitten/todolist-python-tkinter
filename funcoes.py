
from tkinter import messagebox
from tkinter import *
import json
import os

def carregar_tarefas(nome_arquivo):
  if os.path.exists(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8' ) as file:
      return json.load(file)
  return {}

def salvar(nome_arquivo, tarefas):
    with open(nome_arquivo, "w", encoding="utf-8") as file:
      json.dump(tarefas, file, indent=4, ensure_ascii=False)

def adicionar_tarefa(tarefas, input_tarefa, nome_arquivo, atualizar_lista):
  tarefa = input_tarefa.get().strip().title()
  
  if tarefa: 
    if tarefa in tarefas:  
      messagebox.showinfo('Tarefa Existente', f'A tarefa "{tarefa}" já existe na lista!')
    else:
      tarefas[tarefa] = False
      input_tarefa.delete(0, END)
      salvar(nome_arquivo, tarefas)
      atualizar_lista()
  else:
    messagebox.showwarning('Campo Vazio', 'Por favor, digite uma tarefa antes de adicionar!')

def excluir_tarefa(tarefa, tarefas, nome_arquivo, atualizar_lista, janela):  
  del tarefas[tarefa]
  salvar(nome_arquivo, tarefas)
  atualizar_lista()
  janela.destroy()

def editar(tarefas, input_edicao, tarefa_antiga, janela_edicao,nome_arquivo, atualizar_lista):
  nova_tarefa = input_edicao.get().strip().title()
  if nova_tarefa and nova_tarefa != tarefa_antiga:
    if nova_tarefa not in tarefas:
      tarefas[nova_tarefa] =  tarefas.pop(tarefa_antiga)
      salvar(nome_arquivo, tarefas)
      atualizar_lista()
      janela_edicao.destroy() 
    else:
      messagebox.showinfo('Tarefa Existente', 'Uma tarefa com esse nome já existe.!') 
  elif not nova_tarefa:
    messagebox.showwarning('Campo Vazio', 'O nome da tarefa não pode estar vazio.')
  else:
    janela_edicao.destroy()  # Fecha a janela se nenhuma alteração foi feita
  