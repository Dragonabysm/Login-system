from tools import verifyDatas, openPopup, getHash
from server import verifyUser, Registration, addRegistration
from tkinter.ttk import Label

def sendLogin(email: str, password: str, screen, frame):
    verification = verifyDatas(email, password)

    if verification:
        try:
            if verifyUser(email, getHash(password)):
                frame.destroy()
                labelCorrect = Label(
                    screen, text='Login efetuado com exíto.', foreground='green', font=('Arial', 20))
                labelCorrect.pack()

        except:
            openPopup(f'Algum erro inesperado aconteceu.', screen)

    else:
        openPopup('Por favor. Digite um \n email válido.', screen)

def sendRegistration(email: str, password: str, screen, sendButton):
    verification = verifyDatas(email, password)

    if verification:
        try:
            registration = Registration(email=email, password=getHash(password))
            addRegistration(registration)
        except:
            openPopup(f'Algum erro inesperado aconteceu.', screen)
        else:
            labelCorrect = Label(
                screen, text='Cadastro efetuado com exíto.', foreground='green', font=('Arial', 8))
            labelCorrect.pack()
            sendButton.configure(state='disabled')
    else:
        openPopup('Por favor. Digite um \n email válido.', screen)
