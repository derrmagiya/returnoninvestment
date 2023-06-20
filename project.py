class Returnoninvestmentcalculator:
    def __init__(self, purchase_price, monthly_rental_income, annual_expenses):
        self.purchase_price = purchase_price
        self.monthly_rental_income = monthly_rental_income
        self.annual_expenses = annual_expenses

    def calculate_cash_flow(self):
        monthly_expenses = self.annual_expenses / 12
        monthly_cash_flow = self.monthly_rental_income - monthly_expenses
        return monthly_cash_flow

    def calculate_roi(self):
        initial_investment = self.purchase_price
        annual_cash_flow = self.calculate_cash_flow() * 12
        roi = annual_cash_flow / initial_investment * 100
        return roi


while True:
    print("Welcome to the return on investment calculator!")
    purchase_price = float(input("Enter the purchase price (0 to exit): "))
    
    if purchase_price == 0:
        print("Thank you for using the Rental Property Calculator,Unlocking the Potential of Rental Properties! Goodbye!")
        break
    
    monthly_rental_income = float(input("Enter the monthly rental income: "))
    annual_expenses = float(input("Enter the annual expenses: "))

    calculator = Returnoninvestmentcalculator(purchase_price, monthly_rental_income, annual_expenses)
    roi = calculator.calculate_roi()

    print("ROI: {:.2f}%".format(roi))
    print()