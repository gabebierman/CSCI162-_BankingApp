# Handles making the widgets work

class AccountController:

    def __init__(self, model, window, ui):
        self.model = model
        self.window = window
        self.ui = ui
        self.logged_in_username = None
        self.current_balance = None

        self.connect_buttons()
        self.set_banking_state(False)

    def connect_buttons(self):
        
        self.ui.buttonLogin.clicked.connect(self.handle_login)
        self.ui.buttonTransaction.clicked.connect(self.handle_transaction)
        self.ui.buttonLogout.clicked.connect(self.handle_logout)

    def set_banking_state(self, enabled):
        
        # TODO Hide widgets before login
        # TODO show them after successful login
        pass

    def handle_login(self):
        
        username = self.ui.inputUsername.text().strip()
        password = self.ui.inputPassword.text()

        # TODO Display an error in labelLoginStatus if username is empty
        # TODO Display an error in labelLoginStatus if password is empty
        # TODO Call model.authenticate_user(username, password)
        # TODO On failure, show an error in labelLoginStatus
        # TODO On success, get the balance and show it in labelActualAccountBalance
        # TODO Show a welcome message and clear previous login errors
        # TODO Call set_banking_state(True).
        pass

    def handle_transaction(self):
        amount_text = self.ui.inputAmount.text().strip()

        # TODO Check for non 0 amount and show the error in labelAccountFeedback
        # TODO Convert amount_text to a float
        # TODO Check value is greater than 0
        # TODO If radioDeposit is checked exec handle_deposit(amount).
        # TODO If radioWithdraw is checked exec handle_withdrawal(amount).
        # TODO Display an error if neither radio button is selected
        # TODO OR don't allow GO button to be pressed until there is a radio value
        pass

    def handle_deposit(self, amount):
        # TODO Call model.deposit(logged_in_username, amount)
        # TODO Refresh the balance with model.get_balance()
        # TODO Update labelActualAccountBalance
        # TODO Show a success message in labelAccountFeedback
        pass

    def handle_withdrawal(self, amount):
        # TODO Compare amount with the current database balance
        # TODO If amount is greater than balance, "Insufficient Funds"
        # TODO Call model.withdraw()
        # TODO Refresh and display the balance
        # TODO Show a success message in labelAccountFeedback
        pass

    def handle_logout(self):
        # TODO Set logged_in_username and current_balance to None
        # TODO Clear inputUsername and inputPassword
        # TODO Clear inputAmount and labelActualAccountBalance
        # TODO Clear labelLoginStatus and labelAccountFeedback
        # TODO Deselect radioDeposit and radioWithdraw
        # TODO Call set_banking_state(False)
        pass
