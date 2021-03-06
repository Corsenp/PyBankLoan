from tkinter import *
from tkinter.messagebox import *

class Loan():
    def __init__(self, dictionary):
        '''
        Init method for Loan class
        '''
        try:
            self.dictionary = dictionary
            self.firstname = dictionary.get("firstname")
            self.lastname = dictionary.get("lastname")
            self.social_security = dictionary.get("social_security")
            self.requested_loan = float(dictionary.get("requested_loan"))
            self.loan_duration = int(dictionary.get("loan_duration"))
            self.interest_rate = float(dictionary.get("interest_rate"))
            self.income = float(dictionary.get("income"))
            self.credit_score = int(dictionary.get("credit_score"))
            self.validation = True
        except ValueError as error:
            print("Value Error : {}".format(error))

    def calculate_annual_interest_payment(self):
        '''
        Method that will calculate the annual interest payments
        '''
        loan_years = self.loan_duration / 12
        if (loan_years == 0):
            loan_years = 1
        self.annual_interest_payment = self.requested_loan * self.interest_rate / loan_years
    
    def calculate_loan_to_income(self):
        '''
        Method that will calculate loan to income attribute
        '''
        self.loan_to_income = self.requested_loan / self.income
    
    def check_annual_interest_payment_validation(self):
        '''
        Method that will check the validation for the annual interest payment attribute
        '''
        self.calculate_annual_interest_payment()
        if self.annual_interest_payment > ((20 * self.income) / 100):
            self.validation = False
        return self.validation
    
    def check_loan_to_income_validation(self):
        '''
        Method that will check the validation for the loan to income attribute
        '''
        self.calculate_loan_to_income()
        if self.loan_to_income > 4:
            self.validation = False
        return self.validation
    
    def check_credit_score_validation(self):
        '''
        Method that will check the validation for the credit score attribute
        '''
        if self.credit_score < 600:
            self.validation = False
        return self.validation
    
    def check_loan_validity(self):
        self.check_loan_to_income_validation()
        self.check_annual_interest_payment_validation()
        self.check_credit_score_validation()
        return self.validation

class Application():
    def __init__(self):
        '''
        Init function of the Application class
        '''
        self.root = Tk()
        self.row = 0
        self.dictionary = {
            'firstname': "",
            'lastname': "",
            'social_security': "",
            'requested_loan': "",
            'loan_duration': "",
            'interest_rate': "",
            'income': "",
            'credit_score': "",
        }

    def firstname_field(self):
        '''
        Initialize firstname field
        '''
        firstname_label = Label(self.root, text="First Name:")
        self.firstname_entry = Entry()
        firstname_label.grid(row=self.row, column=0)
        self.row += 1
        self.firstname_entry.grid(row=self.row, column=0)
        self.row += 1
    
    def lastname_field(self):
        '''
        Initialize lastname field
        '''
        lastname_label = Label(self.root, text="Last Name:")
        self.lastname_entry = Entry()
        lastname_label.grid(row=self.row, column=0)
        self.row += 1
        self.lastname_entry.grid(row=self.row, column=0)
        self.row += 1

    def social_security_field(self):
        '''
        Initialize Social Security Field
        '''
        social_security_label = Label(self.root, text="Social Security Number:")
        self.social_security_entry = Entry()
        social_security_label.grid(row=self.row, column=0)
        self.row += 1
        self.social_security_entry.grid(row=self.row, column=0)
        self.row += 1
    
    def requested_loan_field(self):
        '''
        Initialize requested loan field
        '''
        requested_loan_label = Label(self.root, text="Requested Loan Amount: (only digits)")
        self.requested_loan_entry = Entry()
        requested_loan_label.grid(row=self.row, column=0)
        self.row += 1
        self.requested_loan_entry.grid(row=self.row, column=0)
        self.row += 1
    
    def loan_duration_field(self):
        '''
        Initialize loan duration field
        '''
        loan_duration_label = Label(self.root, text="Loan Duration: (in months)")
        self.loan_duration_entry = Entry()
        loan_duration_label.grid(row=self.row, column=0)
        self.row += 1
        self.loan_duration_entry.grid(row=self.row, column=0)
        self.row += 1
    
    def interest_rate_label_field(self):
        '''
        Initialize interest rate field
        '''
        interest_rate_label = Label(self.root, text="Interest Rate: ")
        self.interest_rate_entry = Entry()
        interest_rate_label.grid(row=self.row, column=0)
        self.row += 1
        self.interest_rate_entry.grid(row=self.row, column=0)
        self.row += 1

    def income_field(self):
        '''
        Initialize Income field
        '''
        income_label = Label(self.root, text="Income: (only digits)")
        self.income_entry = Entry()
        income_label.grid(row=self.row, column=0)
        self.row += 1
        self.income_entry.grid(row=self.row, column=0)
        self.row += 1

    def credit_score_field(self):
        '''
        Initialize credit score field
        '''
        credit_score_label = Label(self.root, text="Credit Score:")
        self.credit_score_entry = Entry()
        credit_score_label.grid(row=self.row, column=0)
        self.row += 1
        self.credit_score_entry.grid(row=self.row, column=0)
        self.row += 1

    def submit_button(self):
        '''
        Initialize submit button
        '''
        submit = Button(self.root, text="Submit", command=self.submit_function)
        submit.grid(row=self.row, column=0)
        self.row += 1

    def fill_dictionary(self):
        '''
        Fill dictionary with data from the form
        '''
        self.dictionary['firstname'] = self.firstname_entry.get()
        self.dictionary['lastname'] = self.lastname_entry.get()
        self.dictionary['social_security'] = self.social_security_entry.get()
        self.dictionary['credit_score'] = self.credit_score_entry.get()
        self.dictionary['income'] = self.income_entry.get()
        self.dictionary['interest_rate'] = self.interest_rate_entry.get()
        self.dictionary['loan_duration'] = self.loan_duration_entry.get()
        self.dictionary['requested_loan'] = self.requested_loan_entry.get()

    def submit_function(self):
        '''
        Submit function : will fill the dictionary with data and analyze it
        '''
        self.fill_dictionary()
        loan = Loan(self.dictionary)
        loan.check_loan_validity()
        if loan.validation == True:
            showinfo('Loan', 'The loan is approved')
        else:
            showwarning('Loan', 'The loan is rejected')

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
    application = Application()
    application.init_window()

main()