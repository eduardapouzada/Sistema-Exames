from graphics import *
import csv

def main():
    width = 1200
    height = 720
    win = GraphWin("MedLog", width, height)
    win.setBackground("#013719")

    background = Image(Point(600, 360), 'assets/background_inicial.png')
    background.draw(win)

    stime = time.time()
    while time.time() - stime < 1:
        win.update()
    background.undraw()
    login_paciente(win)    

def login_paciente(win):
    background = Image(Point(600,360), 'assets/background_loginPaciente.png')
    background.draw(win)

    login_name = Entry(Point(860,227), 30)
    login_name.setFill('white')
    login_name.setSize(16)
    login_name.draw(win)

    login_password = Entry(Point(860,325), 30)
    login_password.setFill('white')
    login_password.setSize(16)
    login_password.draw(win)
    
    senhaReal = ''
    #! While dos botões
    while True:
        time.sleep(0.1)
        text_name = login_name.getText()
        text_password = login_password.getText()

        senhaMascarada(win, text_password, senhaReal, login_password)
        
        #* Verifica se tem letra no campo CPF
        semLetras(win, text_name, login_name)
            
        mouse = win.checkMouse()
        if mouse:
            x = mouse.getX()
            y = mouse.getY()

            #* Do botão de fazer login como médico:
            if 745 <= x <= 900 and 680 <= y <= 700:
                limparItems(win)
                login_medico(win) 

            #* Do botão de entrar:
            if 550 <= x <= 1070 and 430 <= y <= 480:
                text_erro = Text(Point(800, 520), '')
                text_erro.setFill('red')
                text_erro.setSize(12)   
                text_erro.draw(win)

                if text_name.strip() != '' and len(text_name) == 11:
                    with open('arquivos/pacientes.csv', "r+", encoding="utf-8") as arquivo:
                        conteudo = arquivo.read()
                       
                        if text_name in conteudo and senhaReal in conteudo:
                            #* passa para a tela de pacientes
                            time.sleep(0.8)
                            limparItems(win)
                            tela_pacientes(win, text_name)
                        else: 
                            text_erro.setText('Usuário ou Senha incorretos. Tente novamente!')
                            time.sleep(2)
                            text_erro.undraw()
                else:
                    login_name.setText(text_name[:11])
                    text_erro.setText('Informe um CPF e Senha válidos.')
                    time.sleep(2)
                    text_erro.undraw()     

            #* Do botão para cadastrar pacientes:
            if 910 <= x <= 1030 and 600 <= y <= 630:
                limparItems(win)
                cadastro_paciente(win)

def login_medico(win):
    background = Image(Point(600,360), 'assets/background_loginMedico.png')
    background.draw(win)

    #! Entry para nome e senha
    login_name = Entry(Point(860,227), 30)
    login_name.setFill('white')
    login_name.setSize(16)
    login_name.draw(win)

    login_password = Entry(Point(860,325), 30)
    login_password.setFill('white')
    login_password.setSize(16)
    login_password.draw(win)
    
    senhaReal = ''
    #! Botões        
    #! While dos botões
    while True:
        time.sleep(0.1)
        text_name = login_name.getText()
        text_password = login_password.getText()

        #* Trata a senha com *
        senhaMascarada(win, text_password, senhaReal, login_password)

        #* Trata para permitir somente números
        semLetras(win, text_name, login_name)
        mouse = win.checkMouse()
        if mouse:
            x = mouse.getX()
            y = mouse.getY()

            #* Do botão de voltar
            if 1150 <= x <= 1190 and 20 <= y <= 50:
                limparItems(win)
                login_paciente(win)

            #* Do botão de login como Médico
            if 550 <= x <= 1070 and 430 <= y <= 480:
                with open('arquivos/pacientes.csv', "r+", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()
                    if text_name in conteudo and text_password in conteudo:
                        print('Opa, neste arquivo tem este nome e senha.')
                        limparItems(win)
                        win.setBackground('white')

                    else:
                        text_erro = Text(Point(800, 520), 'CRM ou Senha incorretos. Tente Novamente!')
                        text_erro.setFill('red')
                        text_erro.setSize(12)   
                        text_erro.draw(win)
                        time.sleep(2)
                        text_erro.undraw()

            #* Do botão de cadastrar como médico
            if 900 <= x <= 1030 and 600 <= y <= 625:
                limparItems(win)
                cadastro_medico(win)    

def cadastro_paciente(win):
    background = Image(Point(600, 360), 'assets/background_cadastroPaciente.png')
    background.draw(win)

    cadastro_name = Entry(Point(860,185), 30)
    cadastro_name.setFill('white')
    cadastro_name.setSize(16)
    cadastro_name.draw(win)

    cadastro_email = Entry(Point(860, 260), 30)
    cadastro_email.setFill('white')
    cadastro_email.setSize(16)
    cadastro_email.draw(win)

    cadastro_cpf = Entry(Point(860, 340), 30)
    cadastro_cpf.setFill('white')
    cadastro_cpf.setSize(16)
    cadastro_cpf.draw(win)

    cadastro_senha = Entry(Point(860, 410), 30)
    cadastro_senha.setFill('white')
    cadastro_senha.setSize(16)
    cadastro_senha.draw(win)

    cadastro_confirmaSenha = Entry(Point(860, 485), 30)
    cadastro_confirmaSenha.setFill('white')
    cadastro_confirmaSenha.setSize(16)
    cadastro_confirmaSenha.draw(win)

    while True:
        #!Botões
        mouse = win.checkMouse()
        if mouse:
            x = mouse.getX()
            y = mouse.getY()

            #* Do botão de cadastrar-se
            if 560 <= x <= 1060 and 630 <= y <= 680:
                text_name = cadastro_name.getText()
                text_email = cadastro_email.getText()
                text_cpf = cadastro_cpf.getText()
                text_senha = cadastro_senha.getText()
                text_confirmaSenha = cadastro_confirmaSenha.getText()

                with open('arquivos/pacientes.txt', 'a', encoding='utf-8') as arquivo:
                    conteudo = text_name + ', ' + text_email + ', ' + text_cpf + ', ' + text_senha + ', ' + text_confirmaSenha + ', \n' 
                    arquivo.write(conteudo)
                    print('o conteudo foi adicionado ao arquivo')

            #* Do botão de voltar
            if 1150 <= x <= 1190 and 10 <= y <= 50:
                limparItems(win)
                login_paciente(win)

def cadastro_medico(win):
    background = Image(Point(600, 360), 'assets/background_cadastroMedico.png')
    background.draw(win)

    cadastro_name = Entry(Point(860,190), 30)
    cadastro_name.setFill('white')
    cadastro_name.setSize(16)
    cadastro_name.draw(win)

    cadastro_email = Entry(Point(860, 260), 30)
    cadastro_email.setFill('white')
    cadastro_email.setSize(16)
    cadastro_email.draw(win)

    cadastro_cpf = Entry(Point(860, 330), 30)
    cadastro_cpf.setFill('white')
    cadastro_cpf.setSize(16)
    cadastro_cpf.draw(win)

    cadastro_crm = Entry(Point(860, 400), 30)
    cadastro_crm.setFill('white')
    cadastro_crm.setSize(16)
    cadastro_crm.draw(win)

    cadastro_senha = Entry(Point(860, 475), 30)
    cadastro_senha.setFill('white')
    cadastro_senha.setSize(16)
    cadastro_senha.draw(win)

    cadastro_confirmaSenha = Entry(Point(860, 540), 30)
    cadastro_confirmaSenha.setFill('white')
    cadastro_confirmaSenha.setSize(16)
    cadastro_confirmaSenha.draw(win)


    while True:
        mouse = win.checkMouse()
        if mouse:
            x = mouse.getX()
            y = mouse.getY()

            #* Do botão de voltar
            if 1150 <= x <= 1190 and 20 <= y <= 50:
                for item in win.items[:]:
                    item.undraw()
                login_medico(win)

def tela_pacientes(win, text_name):
    background = Image(Point(600, 360), 'assets/background_pacientes.png')
    background.draw(win)

    #* Entry da data e nome dos exames
    exame_paciente = Entry(Point(480, 235), 15)
    exame_paciente.setFill('white')
    exame_paciente.draw(win)

    data_paciente = Entry(Point(730, 235), 15)
    data_paciente.setFill('white')
    data_paciente.draw(win)

    #* Entry dos valores do Eritrograma 
    valor1_paciente = Entry(Point(265, 360), 6)
    valor1_paciente.setFill('white')
    valor1_paciente.draw(win)

    valor2_paciente = Entry(Point(265, 395), 6)
    valor2_paciente.setFill('white')
    valor2_paciente.draw(win)

    valor3_paciente = Entry(Point(265, 435), 6)
    valor3_paciente.setFill('white')
    valor3_paciente.draw(win)

    valor4_paciente = Entry(Point(265, 475), 6)
    valor4_paciente.setFill('white')
    valor4_paciente.draw(win)

    valor5_paciente = Entry(Point(265, 545), 6)
    valor5_paciente.setFill('white')
    valor5_paciente.draw(win)

    #* Entry dos valores de Leucograma 
    valor6_paciente = Entry(Point(550, 380), 6)
    valor6_paciente.setFill('white')
    valor6_paciente.draw(win)

    valor7_paciente = Entry(Point(550, 437), 6)
    valor7_paciente.setFill('white')
    valor7_paciente.draw(win)

    valor8_paciente = Entry(Point(550, 495), 6)
    valor8_paciente.setFill('white')
    valor8_paciente.draw(win)

    valor9_paciente = Entry(Point(760, 378), 6)
    valor9_paciente.setFill('white')
    valor9_paciente.draw(win)

    valor10_paciente = Entry(Point(760, 437), 6)
    valor10_paciente.setFill('white')
    valor10_paciente.draw(win)

    valor11_paciente = Entry(Point(760, 495), 6)
    valor11_paciente.setFill('white')
    valor11_paciente.draw(win)

    #* Entry dos valores das Plaquetas
    valor12_paciente = Entry(Point(1100, 370), 6)
    valor12_paciente.setFill('white')
    valor12_paciente.draw(win)

    while True: 
        mouse= win.getMouse()

        if mouse:
            x = mouse.getX()
            y = mouse.getY()

            #* Botão para editar um exame
            if 420 <= x <= 560 and 628 <= y <= 665:
                for item in win.items[:]:
                    item.undraw()
                win.setBackground('red')   

            #* Botão para cadastrar um novo exame
            if 630 <= x <= 780 and 628 <= y <= 665:
                text = Text(Point(600,605), 'Seu novo exame foi cadastrado com sucesso!')
                text.setFill('green')
                text.draw(win)
                time.sleep(1)
                for item in win.items[:]:
                    item.undraw()

                #* Pega o que foi digitado:  
                name_exame = exame_paciente.getText()
                data_exame = data_paciente.getText()    
                valorHemacias = valor1_paciente.getText()
                valorHemoglobina = valor2_paciente.getText()
                valorHematocrito = valor3_paciente.getText()
                valorVolume = valor4_paciente.getText()
                valorHemoglobinaCorp = valor5_paciente.getText()
                valorLeucocitos = valor6_paciente.getText()
                valorLeucocitosDif = valor7_paciente.getText()
                valorNeutrofilos = valor8_paciente.getText()
                valorMonocitos = valor9_paciente.getText()
                valorEosinofilos = valor10_paciente.getText()
                valorBasofilos = valor11_paciente.getText()
                valorPlaquetas = valor12_paciente.getText()

                with open('arquivos/exames.csv', 'a', encoding='utf-8') as exames:
                    conteudo = ",".join([str(text_name), name_exame, str(data_exame), 
                                         str(valorHemacias), str(valorHemoglobina), 
                                         str(valorHematocrito), str(valorVolume), str(valorHemoglobinaCorp),
                                         str(valorLeucocitos), str(valorLeucocitosDif), str(valorNeutrofilos), 
                                         str(valorMonocitos), str(valorEosinofilos), 
                                         str(valorBasofilos), str(valorPlaquetas)]) + "\n"
                    exames.write(conteudo)
                
            #* Botão para voltar
            if 1150 <= x <= 1190 and 20 <= y <= 50:
                for item in win.items[:]:
                    item.undraw()
                login_paciente(win)

def limparItems(win):
    for item in win.items[:]:
        item.undraw()

def senhaMascarada(win, text_password, senhaReal, login_password):
    if len(text_password) > len(senhaReal):
            senhaReal += text_password[len(senhaReal):]
    elif len(text_password) < len(senhaReal):
        senhaReal = senhaReal[:len(text_password)]

    login_password.setText('*' * len(senhaReal))

def semLetras(win, text_name, login_name):
    if not text_name.isdigit():
        login_name.setText("".join(filter(str.isdigit, text_name)))

main()

