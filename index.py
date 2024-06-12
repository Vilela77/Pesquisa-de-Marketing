import PySimpleGUI as sg
import pandas as pd
import os
import subprocess

class telaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Código'), sg.Input(size=(20, 0), key='-CODIGO-')],
            [sg.Text('Como soube de nossos planos?')],
            [sg.Radio('[1] - Publicidade em televisão/rádio.', 'RADIO1', key='-RADIO1-')],
            [sg.Radio('[2] - Publicidade online ou Pesquisa online.', 'RADIO1', key='-RADIO2-')],
            [sg.Radio('[3] - Recomendação de amigos ou familiares.', 'RADIO1', key='-RADIO3-')],
            [sg.Radio('[4] - Busca boca a boca.', 'RADIO1', key='-RADIO4-')],
            [sg.Radio('[5] - Eventos ou feiras.', 'RADIO1', key='-RADIO5-')],
            [sg.Radio('[6] - Propagandas em lojas físicas, outdoor, Anuncios moveis.', 'RADIO1', key='-RADIO6-')],
            [sg.Radio('[7] - Panfletagem.', 'RADIO1', key='-RADIO7-')],
            [sg.Radio('[8] - Informado por técnicos.', 'RADIO1', key='-RADIO8-')],
            [sg.Button('Salvar')],
            [sg.Button('Abrir Dashboard')]
        ]

        # Janela
        self.janela = sg.Window("Dados do Usuário").Layout(layout)
        self.dados = {'Codigo': '', 'Selecao': ''}

    def iniciar(self):
        while True:
            evento, valores = self.janela.read()

            if evento == sg.WIN_CLOSED:
                break
            elif evento == 'Salvar':
                codigo = valores['-CODIGO-']
                selecao = self.get_selecao(valores)
                self.dados['Codigo'] = codigo
                self.dados['Selecao'] = selecao
                print(f'Código digitado: {codigo}')
                print(f'Opção Selecionada: {selecao}')
                # Limpar campo de código
                self.janela['-CODIGO-'].update(value='')
                # Desmarcar todos os Radio Buttons
                for i in range(1, 9):
                    self.janela[f'-RADIO{i}-'].update(value=False)
                self.salvar_dados_em_excel()
            elif evento == 'Abrir Dashboard':
                self.abrir_dashboard()

        self.janela.close()

    def get_selecao(self, valores):
        for i in range(1, 9):
            if valores[f'-RADIO{i}-']:
                return f'{i}'

    def abrir_dashboard(self):
        # Caminho para o script test_grafico.py
        dashboard_script = 'grafico.py'

        # Verificar se o arquivo existe antes de tentar abri-lo
        if os.path.exists(dashboard_script):
            subprocess.Popen(['python', dashboard_script])# quando tiver mexendo no codigo usa esse
            #executavel = r'grafico.exe' #para buildar

        # Chame o executável
            #subprocess.call([executavel]) #para buildar
        #else:
            #sg.popup_error(f"O arquivo {dashboard_script} não foi encontrado!")

    def salvar_dados_em_excel(self):
        # Lê o arquivo Excel existente, se houver
        try:
            df = pd.read_excel('planilha.xlsx')
        except FileNotFoundError:
            # Se o arquivo não existir, cria um DataFrame vazio
            df = pd.DataFrame(columns=['Codigo', 'Selecao'])

        # Adiciona os novos dados ao DataFrame
        novo_dado = pd.DataFrame([self.dados])
        df = pd.concat([df, novo_dado], ignore_index=True)

        # Salva o DataFrame de volta no arquivo Excel
        df.to_excel('planilha.xlsx', index=False)

if __name__ == "__main__":
    app = telaPython()
    app.iniciar()
