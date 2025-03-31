# Sistema de Gerenciamento de Tarefas

Este projeto foi desenvolvido como parte do Projeto Final da disciplina de Lógica de Programação no curso Técnico em Informática para Internet do Instituto Federal de Educação, Ciência e Tecnologia do Ceará (IFCE).
O objetivo é criar um aplicativo simples de controle de tarefas utilizando Python e a biblioteca Tkinter para interface gráfica.
O sistema permite adicionar, editar, excluir e marcar tarefas como concluídas, além de oferecer rolagem para listas extensas de tarefas.

## Funcionalidades Principais

- **Adicionar Tarefas:**
  Insira novas tarefas por meio de um campo de texto e botão dedicado.

- **Marcar como Concluído:**
  Altere o estilo visual das tarefas concluídas (texto tachado e cor mais clara).

- **Editar Tarefas:**
  Edite o nome de uma tarefa existente usando uma janela modal.

- **Excluir Tarefas:**
  Remova tarefas selecionadas com confirmação prévia.

- **Rolagem:**
  Navegue por listas extensas com um sistema de rolagem integrado.

- **Controle de Tarefas Concluídas e Não Concluídas:**
  O aplicativo exibe um contador na parte inferior da interface, mostrando o número de tarefas concluídas e não concluídas em tempo real.

- **Persistência de Dados:**
  Salve e carregue as tarefas automaticamente em um arquivo JSON.

## Tecnologias Utilizadas

- Linguagem: Python 3.x
- Biblioteca Gráfica: Tkinter
- Armazenamento de Dados: JSON

## Estrutura do Projeto

A organização dos arquivos segue boas práticas de modularização para facilitar a manutenção e a escalabilidade do código:

```
TODOLIST
├── 📜 funcoes.py          # Lida com operações relacionadas a    dados (salvar, carregar, etc.)
├── 📜 interface.py        # Contém funções para criar e estilizar componentes gráficos, como cards, modais e barra de rolagem.
├── 📜 main.py             # Gerencia o fluxo principal do programa
├── 📜 tarefas.json        # Armazena os dados das tarefas
└── 📜 README.md           # Documentação do projeto
```

## Desafios Enfrentados

1. **Atualização Dinâmica da Interface:**

- **Problema:** A reconstrução completa da lista ao alterar o estado das tarefas causava "tremores" na tela.
- **Solução:** Atualizar apenas os elementos necessários diretamente.

2. **Sincronização entre Dados e Interface:**

- **Problema:** Garantir que as alterações nos botões (Checkbuttons) fossem refletidas no dicionário de dados.
- **Solução:** Manter referências diretas entre os botões e os dados associados.

3. **Rolagem Funcional:**

- **Problema:** O sistema de rolagem não atualizava corretamente após mudanças na lista.
- **Solução:** Utilizar update_idletasks() para processar alterações antes de ajustar o scrollregion.

4. **Exclusão com Confirmação**

- **Problema:** Implementar uma janela modal para confirmar exclusões sem interromper o fluxo do programa.
- **Solução:** Criar uma janela modal personalizada que pausa interações com a janela principal até a confirmação.

## Como executar

1. Certifique-se de ter o Python 3.x instalado em seu sistema.

2. Clone este repositório:

```
git clone https://github.com/Fernandabitten/todolist-python-tkinter.git
```

3. Navegue até o diretório do projeto:

```
cd todolist-python-tkinter
```

4. Execute o arquivo principal:

```
python main.py
```

## Transformar em um Aplicativo para Área de Trabalho (Desktop)

Se você deseja executar este projeto como um aplicativo diretamente na sua área de trabalho, sem precisar abrir o código Python, siga os passos abaixo:

1. **Instalar o PyInstaller**
   O PyInstaller é uma ferramenta que converte scripts Python em executáveis (.exe). Para instalá-lo, execute o seguinte comando n

```
pip install pyinstaller
```

2. **Criar o Executável**
   No terminal, navegue até o diretório onde está localizado o arquivo principal do projeto (main.py). Em seguida, execute o comando:

```
pyinstaller --onefile --windowed --icon=<seu-icone.ico> main.py
```

- --onefile: Gera um único arquivo executável.
- --windowed: Oculta o terminal ao executar o aplicativo.
- --icon=<seu-icone.ico>: Adiciona um ícone personalizado ao aplicativo (opcional).

O executável será gerado na pasta dist, localizada no diretório do projeto.

3. **Executar e Distribuir**

- Localize o arquivo gerado na pasta dist.
- Você pode movê-lo para sua área de trabalho ou compartilhar com outros usuários.

4. **Compatibilidade de Executáveis**
   Caso compartilhe o executável com outros usuários, vale lembrar que os executáveis gerados pelo PyInstaller são específicos para o sistema operacional onde foram criados.

- Windows: Os executáveis gerados no Windows funcionarão apenas em sistemas Windows.
- macOS: Para criar um executável para macOS, é necessário rodar o PyInstaller diretamente em um macOS.
- Linux: Da mesma forma, executáveis para Linux devem ser gerados em um sistema Linux.

Se você deseja gerar um executável para outro sistema (Windows, macOS ou Linux), será necessário rodar o PyInstaller diretamente nesse sistema ou utilizar uma máquina virtual que simule o ambiente desejado.

## Requisitos do projeto

- O aplicativo deve permitir adicionar, listar, excluir e marcar tarefas como concluídas.

- As tarefas são armazenadas em um dicionário no formato:

```
{
    ""Estudar Python": True
}
```

Onde a chave é o nome da tarefa e o valor indica se está concluída (True) ou não (False).

## Melhorias Futuras

- Implementar suporte para categorias ou prioridades nas tarefas.

- Adicionar notificações ou lembretes para tarefas pendentes.

- Exportar/importar listas de tarefas em formatos diferentes (CSV ou Excel).

## Licença

Este projeto está licenciado sob os termos da Licença MIT. Você é livre para usar, modificar e distribuir este software, desde que mantenha os créditos ao autor original.

## Capturas de Tela

| ![image](https://github.com/user-attachments/assets/1e73acf4-31ea-48b3-b3b2-165bb49c9e65) | ![image](https://github.com/user-attachments/assets/1f6e29b3-456a-479a-8e1f-026dfb26a97e) |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| ![image](https://github.com/user-attachments/assets/620ae486-7ede-4cd2-a325-4d1a89832afd) | ![image](https://github.com/user-attachments/assets/15bff5a3-5ab2-4779-b114-74e522c184b5) |



