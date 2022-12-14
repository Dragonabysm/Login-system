from hashlib import blake2b
from tkinter import Toplevel
from tkinter.ttk import Label
from regex.regex import Regex

def openPopup(msg: str, screen) -> None:
    popup = Toplevel(screen, background='black')
    popup.title('Error')
    popup.resizable(False, False)
    labelError = Label(popup, text=msg, font=(
        'Arial', 20), foreground='red', justify='center', background='black')
    labelError.pack(pady=80, padx=40)

def verifyDatas(email: str, password: str) -> bool:
    emailRegex = Regex('.*@.*\..*')
    verification = email and password \
        and password != 'Senha: ' and \
        email != 'Email: '

    if verification:
        if emailRegex.match(email):
            return True
        return False
    return False

def getHash(password: str):
    return blake2b(password.encode(), digest_size=48, usedforsecurity=True).hexdigest()