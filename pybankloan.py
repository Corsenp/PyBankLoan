from tkinter import *

class Loan:
    def __init__(self, dictionary):
        try:
            self.firstname = dictionary.get("firstname")
            self.lastname = dictionary.get("lastname")
            self.socialSecurity = dictionary.get("socialSecurity")
            self.requestedLoan = dictionary.get("requestedLoan")
            self.loanDuration = dictionary.get("loanDuration")
            self.interestRate = dictionary.get("interestRate")
            self.income = dictionary.get("income")
            self.creditScore = dictionary.get("creditScore")
        except:
            print("Incorrect dictionary")
            sys.exit(1)

class Application:
    def __init__(self):
        '''
        Init function of the Application class
        '''
        self.root = Tk()
        self.row = 0
        self.dictionary = {
            'firstname': "",
            'lastname': "",
            'socialSecurity': "",
            'requestedLoan': "",
            'loanDuration': "",
            'interestRate': "",
            'income': "",
            'creditScore': "",
        }
    
    def firstname_field(self):
        '''
        Initialize firstname field
        '''
        firstnameLabel = Label(self.root, text="First Name:")
        self.firstnameEntry = Entry()
        firstnameLabel.grid(row=self.row, column=0)
        self.row += 1
        self.firstnameEntry.grid(row=self.row, column=0)
        self.row += 1
    
    def lastname_field(self):
        '''
        Initialize lastname field
        '''
        lastnameLabel = Label(self.root, text="Last Name:")
        self.lastnameEntry = Entry()
        lastnameLabel.grid(row=self.row, column=0)
        self.row += 1
        self.lastnameEntry.grid(row=self.row, column=0)
        self.row += 1

    def social_security_field(self):
        '''
        Initialize Social Security Field
        '''
        socialSecurityLabel = Label(self.root, text="Social Security Number:")
        self.socialSecurityEntry = Entry()
        socialSecurityLabel.grid(row=self.row, column=0)
        self.row += 1
        self.socialSecurityEntry.grid(row=self.row, column=0)
        self.row += 1
    
    def requested_loan_field(self):
        '''
        Initialize requested loan field
        '''
        requestedLoanLabel = Label(self.root, text="Requested Loan Amount:")
        self.requestedLoanEntry = Entry()
        requestedLoanLabel.grid(row=self.row, column=0)
        self.row += 1
        self.requestedLoanEntry.grid(row=self.row, column=0)
        self.row += 1
    
    def loan_duration_field(self):
        '''
        Initialize loan duration field
        '''
        loanDurationLabel = Label(self.root, text="Loan Duration:")
        self.loanDurationEntry = Entry()
        loanDurationLabel.grid(row=self.row, column=0)
        self.row += 1
        self.loanDurationEntry.grid(row=self.row, column=0)
        self.row += 1
    
    def interest_rate_label_field(self):
        '''
        Initialize interest rate field
        '''
        interestRateLabel = Label(self.root, text="Interest Rate:")
        self.interestRateEntry = Entry()
        interestRateLabel.grid(row=self.row, column=0)
        self.row += 1
        self.interestRateEntry.grid(row=self.row, column=0)
        self.row += 1

    def income_field(self):
        '''
        Initialize Income field
        '''
        incomeLabel = Label(self.root, text="Income:")
        self.incomeEntry = Entry()
        incomeLabel.grid(row=self.row, column=0)
        self.row += 1
        self.incomeEntry.grid(row=self.row, column=0)
        self.row += 1

    def credit_score_field(self):
        '''
        Initialize credit score field
        '''
        creditScoreLabel = Label(self.root, text="Credit Score:")
        self.creditScoreEntry = Entry()
        creditScoreLabel.grid(row=self.row, column=0)
        self.row += 1
        self.creditScoreEntry.grid(row=self.row, column=0)
        self.row += 1

    def submit_button(self):
        '''
        Initialize submit button
        '''
        submit = Button(self.root, text="Submit", command=self.submit_function)
        submit.grid(row=self.row, column=0)
        self.row += 1

    def submit_function(self):
        '''
        Submit function : will fill the dictionary with data and analyze it
        '''
        self.dictionary['firstname'] = self.firstnameEntry.get()
        self.dictionary['lastname'] = self.lastnameEntry.get()
        self.dictionary['socialSecurity'] = self.socialSecurityEntry.get()
        self.dictionary['creditScore'] = self.creditScoreEntry.get()
        self.dictionary['income'] = self.incomeEntry.get()
        self.dictionary['interestRate'] = self.interestRateEntry.get()
        self.dictionary['loanDuration'] = self.loanDurationEntry.get()
        self.dictionary['requestedLoan'] = self.requestedLoanEntry.get()
        print(self.dictionary)

    def init_window(self):
        '''
        Initialize the Tkinter window by calling all other element/fields
        '''
        self.firstname_field()
        self.lastname_field()
        self.social_security_field()
        self.requested_loan_field()
        self.loan_duration_field()
        self.interest_rate_label_field()
        self.income_field()
        self.credit_score_field()
        self.submit_button()
        self.root.mainloop()

def main():
    '''
    Main function
    '''
    #open_window()
    application = Application()
    application.init_window()
    print(application.dictionary)

main()