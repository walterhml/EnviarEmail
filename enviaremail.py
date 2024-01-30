import pyautogui
import time

# todas informações que precisa colocar em algum lugar futuro
site = 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox'
distinatarioDoEmail = 'walthersouza144@gmail.com'
assunto = 'Portifolio para Vaga de Dev'
apresentação = 'Olá me chamo Walter e estou caminhando para se tornar um desenvolvedor Full-Stack, para trazer soluções com as minhas habilidades e lógica de programação avançada, tenho como foco o Back-end o principal lado que quero atuar, mas também me orgulho de ser Front-End, e garanto que também consigo desenvolver de uma maneira muito eficiente. gosto e tenho uma ampla visão de qualidade de software, e venho também estudando tudo sobre a área QA. tento sempre estar a frente do mercado, conhecendo novas linguagens, ferramentas e tudo que possa me ajudar a ser um bom progamador.'

# execução dos comandos

# entrar no google e colocar o diretorio do site que iremos colocar as informações
pyautogui.press('win')  # windows
time.sleep(3)

pyautogui.write('chrome') # google
time.sleep(3)

pyautogui.press('backspace')
pyautogui.press('enter')
time.sleep(5)

pyautogui.click(x=670, y=80) # mouse e click na barra de pesquisa
time.sleep(3)

pyautogui.typewrite(site)
time.sleep(3)        
            # texto que se encontra na variavel
pyautogui.press('enter')
time.sleep(5)

# achar posição do formulario com o scroll do mouse
pyautogui.click(x=42, y=266)
time.sleep(3)   # aqui depois de ja estar no gmail, click para enviar um email para alguem

# localizar campos para colocar informações
pyautogui.click(x=1302, y=466)
time.sleep(2.5)
pyautogui.typewrite(distinatarioDoEmail)  #primeiro campo do destinatario
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)

# segundo campo assunto
pyautogui.click(x=1258, y=546)
time.sleep(4)
pyautogui.typewrite(assunto)
time.sleep(3)
# terceiro campo apresentação
pyautogui.click(x=1343, y=651)
time.sleep(3)
pyautogui.typewrite(apresentação)
time.sleep(5)


# clicar no botão de anexar arquivo e escolher o curriculo

pyautogui.click(x=1380, y=981)  # clicar no btn de anexar arquivo
time.sleep(3)

pyautogui.click(x=352, y=303) # clicar no curriculo na pasta
time.sleep(2)

pyautogui.click(x=740, y=556) # clicar em abrir
time.sleep(5)

# clicar no botão para enviar o email

pyautogui.click(x=1237, y=965) # clicar no botao enviar/send, para enviar email ao destinatario.
time.sleep(4)

# por fim fechar o google

pyautogui.click(x=1895, y=24)