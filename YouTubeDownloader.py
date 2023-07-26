'''
APP desenvolvido para downloads de vídeo mp4 e áudio mp3 diretamente do YoTube

Python version: 3.11.3
Pytube version: 15.0.0

* * * * * ANTES DE EXECUTAR O SEU PROGRAMA, FAZER CONFIGURAÇÕES ABAIXO * * * * *
• Linha 59: Alterar caminho padrão para o seu download mp3
• Linha 111: Baixar imagem PNG da internet, nomear como 'Python_YouTube' e alterar caminho correto
• Linha 116: Baixar imagem PNG da internet, nomear como 'download' e alterar caminho correto
'''

#= = = = = = = = = = = = = = = = = = = = = = = = IMPORTAR BIBLIOTECAS = = = = = = = = = = = = = = = = = = = = = = = 
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from pytube import YouTube, streams
import os
from pytube.exceptions import RegexMatchError

#= = = = = = = = = = = = = = = = = = = = = CONFIG JANELA TKINTER = = = = = = = = = = = = = = = = = = = = =
janelaYT = Tk()                 #INICAR A JANELA 'TK INTER'
janelaYT.geometry('630x210')    #Largura x Altura
janelaYT.resizable(width=None, height=None) #Largura e Altura PODEM ser redimensionadas.
janelaYT.title('YouTube Downloader')
janelaYT['bg'] = 'red'

#= = = = = = = = = = = = = = = = = = = = = = = = = FUNÇÕES = = = = = = = = = = = = = = = = = = = = = = = =
def video(link):
    if link:
        try:  
            mp4 = YouTube(link)
            titulo = Label(janelaYT, bg = 'red', text = (f'Baixando: {mp4.author} \r\n {mp4.title}'), font = 'arial 12 bold')
            titulo.grid(row = 1, column = 1)               
            stream = mp4.streams.get_highest_resolution()       #Baixar a melhor resolução do vídeo         
            pasta = filedialog.askdirectory()
            stream.download(pasta)                              #Baixar na pasta Download           
                        
            baixando = Label(janelaYT, bg = 'blue', text = 'Download Concluído!', font = 'arial 15 bold')
            baixando.grid(row = 2, column = 1, ipadx = 15, ipady = 5)                

        except RegexMatchError:
            baixando = Label(janelaYT, bg = 'blue', text = '  LINK INVÁLIDO!  ', font = 'arial 15 bold')
            baixando.grid(row = 2, column = 1, ipadx = 15, ipady = 5)             
    else: 
        baixando = Label(janelaYT, bg = 'blue', text = '  LINK INVÁLIDO!  ', font = 'arial 15 bold')
        baixando.grid(row = 2, column = 1, ipadx = 15, ipady = 5)

def musica(link):
    if link:
        try:  
            mp3 = YouTube(link)

            audio = mp3.streams.filter(only_audio=True).first() #Baixar áudio em formato MP3
            titulo = Label(janelaYT, bg = 'red', text = (f'Baixando: {mp3.author} \r\n {mp3.title}'), font = 'arial 12 bold')
            titulo.grid(row = 1, column = 1)             
            pasta = filedialog.askdirectory()
            destino = audio.download(pasta)                     #Baixar na pasta Download           
            destino = "C:/Users/CaiqueSF/Downloads"

            ArquivoSaida = audio.download(output_path=destino)
            base, ext = os.path.splitext(ArquivoSaida)

            ArquivoNovo = base + '.mp3'
            if os.path.exists(ArquivoNovo):
                os.remove(ArquivoNovo)
                os.rename(ArquivoSaida, ArquivoNovo)
            else:
                os.rename(ArquivoSaida, ArquivoNovo)

            baixando = Label(janelaYT, bg = 'blue', text = 'Download Concluído!', font = 'arial 15 bold')
            baixando.grid(row = 2, column = 1, ipadx = 15, ipady = 5)              

        except RegexMatchError:
            baixando = Label(janelaYT, bg = 'blue', text = '  LINK INVÁLIDO!  ', font = 'arial 15 bold')
            baixando.grid(row = 2, column = 1, ipadx = 15, ipady = 5)             
    else: 
        baixando = Label(janelaYT, bg = 'blue', text = '  LINK INVÁLIDO!  ', font = 'arial 15 bold')
        baixando.grid(row = 2, column = 1, ipadx = 15, ipady = 5)

#OPÇÃO POP-UP NÃO CHAMADA NA FUNÇÃO
#FUNÇÃO: Aviso de Donwload Concluído
def aviso():
    janelaYT_msg = Toplevel()
    janelaYT_msg.title('Aviso')
    janelaYT_msg.geometry('300x200')
    
    Label(janelaYT_msg, text = 'Download Concluído!', font = 'arial 12 bold', pady = 30).pack()
    Button(janelaYT_msg, text = 'OK', command = janelaYT_msg.destroy).pack()

#OPÇÃO POP-UP NÃO CHAMADA NA FUNÇÃO
#FUNÇÃO: Aviso de Erro
def aviso_erro():
    janelaYT_msg = Toplevel()
    janelaYT_msg.title('Aviso')
    janelaYT_msg.geometry('300x200')

    Label(janelaYT_msg, text = 'Insira um link válido!', font = 'arial 12 bold', pady = 30).pack()
    Button(janelaYT_msg, text = 'OK', command = janelaYT_msg.destroy).pack()

########################################## LINHA '0' ########################################## 
#Config TEXTO: 'INSIRA LINK'
InsiraLink = Label(janelaYT, bg = 'blue', text = 'Inserir Link', font = 'arial 14 bold')
InsiraLink.grid(row = 0, column = 0, padx = 5, pady = 20)

#Config CAMPO: PARA INSERIR O LINK
link = Entry(janelaYT, font = 'arial 16 bold', width = 30)
link.grid(row = 0, column = 1, padx = 1, pady = 20)

#Config Imagem: Arte do YouTube e Python
photoYTP = PhotoImage(file = r"C:/Users/CaiqueSF/ProjetosPortfolio/YTD_Files/Python_YouTube.png").subsample(15, 15)
Label(janelaYT, image = photoYTP).grid(row = 0, column = 2)

########################################## LINHA '1' ##########################################
#Config Imagem: Download no botao
photoDW = PhotoImage(file = r"C:/Users/CaiqueSF/ProjetosPortfolio/YTD_Files/download.png").subsample(15, 15)

#Config BOTÃO MÚSICA MP3: PARA INICAR O DOWNLOAD
bt1 = Button(janelaYT, bg = 'blue', text = ' MÚSICA MP3 ', font = 'arial 12 bold', command = lambda: musica(link.get()), image = photoDW, compound = BOTTOM)
bt1.grid(row = 1, column = 0, padx = 7, pady = 10)

#Config BOTÃO VÍDEO MP4: PARA INICAR O DOWNLOAD
bt2 = Button(janelaYT, bg = 'blue', text = ' VÍDEO MP4 ', font = 'arial 12 bold', command = lambda: video(link.get()), image = photoDW, compound = BOTTOM)
bt2.grid(row = 1, column = 2, ipadx = 1, ipady = 1, padx = 10, pady = 10)

status = Label(janelaYT, bg = 'red', text = '>      >      >      >      <      <      <      <')
status.grid(row = 1, column = 1, ipadx=10, ipady=5) 

########################################## LINHA '2' ##########################################    
baixando = Label(janelaYT, bg = 'blue', text = 'STATUS DOWNLOAD', font = 'arial 15 bold')
baixando.grid(row = 2, column = 1, ipadx = 15, ipady = 5) 

janelaYT.mainloop()    #EXIBIR A JANELA ATÉ FECHAR

#LEFT-> a imagem estará no lado esquerdo do botão
#RIGHT-> a imagem estará no lado direito do botão
#TOP-> a imagem estará no topo do botão
#BOTTOM-> a imagem estará na parte inferior do botão
#pyinstaller --onefile --noconsole .\YouTubeDownloader.py
