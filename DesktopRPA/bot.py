from botcity.core import DesktopBot
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():

    bot = DesktopBot()
    
    # Precisamos primeiro abrir o SiCalc
    bot.execute(r"C:\Program Files (x86)\Programas RFB\Sicalc Auto Atendimento\SicalcAA.exe")
    
    # Em seguida, precisamos fechar a janela de esclarecimento
    if not bot.find("janela_esclarecimento", matching=0.97, waiting_time=10000):
        not_found("janela_esclarecimento")
    bot.click_relative(221, 206) 
    
    # Identificando o menu funções para abrir o preenchimento da DARF
    if not bot.find("menu_funcoes", matching=0.97, waiting_time=10000):
        not_found("menu_funcoes")
    bot.click()
    
    if not bot.find("menu_preenchimento_darf", matching=0.97, waiting_time=10000):
        not_found("menu_preenchimento_darf")
    bot.click()
    
    # Neste momento, identificamos campo Cod Receita e vamos preencher com o valor
    if not bot.find("item_codigo_receita", matching=0.97, waiting_time=10000):
        not_found("item_codigo_receita")
    bot.click_relative(149, 9)    
    bot.paste("5629")

    # Precisamos pressionar tab para avançar e considerar um tempo para evitar erros
    bot.tab(wait = 1000)
    
    # Vamos começar a preencher os demais dados
    if not bot.find("item_periodo_apuracao", matching=0.97, waiting_time=10000):
        not_found("item_periodo_apuracao")
    bot.click_relative(12, 22)
    bot.paste("040121")

    if not bot.find("item_valor_reais", matching=0.97, waiting_time=10000):
        not_found("item_valor_reais")
    bot.click_relative(18, 26)
    bot.paste("1525")
    
    # Solicitando para calcular e gerar a DARF
    if not bot.find("botao_calcular", matching=0.97, waiting_time=10000):
        not_found("botao_calcular")
    bot.click()
    
    if not bot.find("botao_darf", matching=0.97, waiting_time=10000):
        not_found("botao_darf")
    bot.click()
    
    # Finaliza o preenchimento dos campos
    if not bot.find("item_nome", matching=0.97, waiting_time=10000):
        not_found("item_nome")
    bot.click_relative(22, 26)
    bot.paste("Petrobras")
    
    if not bot.find("item_telefone", matching=0.97, waiting_time=10000):
        not_found("item_telefone")
    bot.click_relative(13, 29)
    bot.paste("1199991234")
    
    if not bot.find("item_cnpj", matching=0.97, waiting_time=10000):
        not_found("item_cnpj")
    bot.click_relative(131, 10)
    bot.paste("33000167000101")
    
    if not bot.find("item_referencia", matching=0.97, waiting_time=10000):
        not_found("item_referencia")
    bot.click_relative(134, 11)
    bot.paste("0")

    # Começa o processo para salvar o PDF
    if not bot.find("botao_imprimir", matching=0.97, waiting_time=10000):
        not_found("botao_imprimir")
    bot.click()
    
    if not bot.find("item_arquivo", matching=0.97, waiting_time=10000):
        not_found("item_arquivo")
    bot.click_relative(74, 2)
    bot.paste(r"C:\temp\darfs\NF.pdf")
    
    if not bot.find("botao_salvar", matching=0.97, waiting_time=10000):
        not_found("botao_salvar")
    bot.click()  

    bot.wait(1000)

    # Aqui fechamos a primeira janela e depois fechamos o sicalc
    bot.alt_f4()
    bot.alt_f4()
    

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()

