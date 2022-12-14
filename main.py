from tkinter.ttk import Label, Frame, Button, Entry, Style
from tkinter import Tk, StringVar, Toplevel
from senders import sendLogin, sendRegistration


class ApplicationLogin():
    """ The base of this code """
    def __init__(self, geometry: str):
        self.screen = Tk('Application', sync=True)
        self.screen.geometry(geometry)
        self.screen.title('Application Login')
        self.screen.resizable(False, False)
        self.setupScreenStyle()

    def setupScreenStyle(self):
        self.frame = Frame(self.screen)

        # Style section
        labelStyle = Style()
        labelStyle.configure("LabelStyle.TLabel", font=(
            'sans-serif', 15), padding=10)

        buttonStyle = Style()
        buttonStyle.configure("ButtonStyle.TButton",
                              width=20, padding=10, font=('sans-serif', 13))

        self.textLogin = Label(
            self.frame,
            text='Já tem uma conta? Faça login.',
            justify='center',
            style='LabelStyle.TLabel'
        )

        self.textLogin.pack(pady=(40, 0))

        self.buttonLogin = Button(
            self.frame,
            text='Fazer login',
            style='ButtonStyle.TButton',
            command=self.makeLogin
        )

        self.buttonLogin.pack()

        self.textRegistration = Label(
            self.frame,
            text='Ainda não tem uma? Cadastre-se.',
            justify='center',
            style='self.LabelStyle.TLabel'
        )

        self.textRegistration.pack(pady=(100, 0))

        self.buttonRegistration = Button(
            self.frame,
            text='Fazer Cadastro',
            style='ButtonStyle.TButton',
            command=self.makeRegistration
        )

        self.buttonRegistration.pack()
        self.frame.pack()

    def runApplication(self):
        self.screen.mainloop()

    def makeRegistration(self):
        self.frame.destroy()
        del self.frame
        self.frame = Frame(self.screen)

        titleLabel = Label(self.frame, text='Cadastro', font=('Arial', 25))
        titleLabel.pack(pady=(40, 0))

        self.email = StringVar(value='Email: ')
        self.password = StringVar(value='Senha: ')

        entryEmail = Entry(
            self.frame,
            textvariable=self.email,
            font=('Arial', 15)
        )

        # Placeholder addapted
        entryEmail.bind(
            '<FocusIn>',
            lambda _: self.email.set('')
            if not self.email.get() != 'Email: '
            else ...
        )

        # Placeholder addapted
        entryEmail.bind(
            '<FocusOut>',
            lambda _: self.email.set('Email: ')
            if not self.email.get()
            else ...
        )

        entryPassword = Entry(
            self.frame,
            textvariable=self.password,
            font=('Arial', 15)
        )

        # Placeholder addapted
        entryPassword.bind(
            '<FocusIn>',
            lambda _: self.password.set('')
            if not self.password.get() != 'Senha: '
            else ...
        )

        # Placeholder addapted
        entryPassword.bind(
            '<FocusOut>',
            lambda _: self.password.set('Senha: ')
            if not self.password.get()
            else ...
        )

        self.sendButton = Button(
            self.frame,
            default='normal',
            command=lambda: sendRegistration(self.email.get(), self.password.get(), self.screen, self.sendButton),
            text='Cadastrar'
        )

        entryEmail.pack(pady=(20, 40), ipadx=30, ipady=10)
        entryPassword.pack(pady=(0, 30), ipadx=30, ipady=10)
        self.sendButton.pack(ipadx=100, ipady=10)
        self.frame.pack()

    def makeLogin(self):
        self.frame.destroy()
        del self.frame
        self.frame = Frame(self.screen)

        titleLabel = Label(self.frame, text='Login', font=('Arial', 25))
        titleLabel.pack(pady=(40, 0))

        self.email = StringVar(value='Email: ')
        self.password = StringVar(value='Senha: ')

        entryEmail = Entry(
            self.frame,
            textvariable=self.email,
            font=('Arial', 15)
        )

        # Placeholder addapted
        entryEmail.bind(
            '<FocusIn>',
            lambda _: self.email.set('')
            if not self.email.get() != 'Email: '
            else ...
        )

        # Placeholder addapted
        entryEmail.bind(
            '<FocusOut>',
            lambda _: self.email.set('Email: ')
            if not self.email.get()
            else ...
        )

        entryPassword = Entry(
            self.frame,
            textvariable=self.password,
            font=('Arial', 15)
        )

        # Placeholder addapted
        entryPassword.bind(
            '<FocusIn>',
            lambda _: self.password.set('')
            if not self.password.get() != 'Senha: '
            else ...
        )

        # Placeholder addapted
        entryPassword.bind(
            '<FocusOut>',
            lambda _: self.password.set('Senha: ')
            if not self.password.get()
            else ...
        )

        self.sendButton = Button(
            self.frame,
            default='normal',
            command=lambda: sendLogin(self.email.get(), self.password.get(), self.screen, self.frame),
            text='Login'
        )

        entryEmail.pack(pady=(20, 40), ipadx=30, ipady=10)
        entryPassword.pack(pady=(0, 30), ipadx=30, ipady=10)
        self.sendButton.pack(ipadx=100, ipady=10)
        self.frame.pack()

app = ApplicationLogin('500x400+100+100')
app.runApplication()
