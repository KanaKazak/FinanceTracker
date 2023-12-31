from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from datetime import datetime
from kivy.uix.spinner import Spinner
import os

expenses_file_path = 'C:\\Users\\Канагат\\Desktop\\Finance Tracker\\FinanceTracker\\expenses.txt'
if not os.path.isfile(expenses_file_path):
    with open(expenses_file_path, 'w'):
        pass 
incomes_file_path = 'C:\\Users\\Канагат\\Desktop\\Finance Tracker\\FinanceTracker\\incomes.txt'
if not os.path.isfile(incomes_file_path):
    with open(incomes_file_path, 'w'):
        pass 


def add_expense(name, date, category, amount):
    expense = f"{name},{date},{category},{amount}\n"
    with open(expenses_file_path, 'a') as file:
        file.write(expense)
    print("Expense added successfully!")

def add_income(name, date, category, amount):
    income = f"{name},{date},{category},{amount}\n"
    with open(incomes_file_path, 'a') as file:
        file.write(income)
    print("Income added successfully!")

def calculate_total_expenses():
    total = 0
    with open(expenses_file_path, 'r') as file:
        for line in file:
            _, _, _, amount = line.strip().split(',')
            total += float(amount)
    return total

def calculate_expenses_during_period(start_date, end_date):
    total = 0
    with open(expenses_file_path, 'r') as file:
        for line in file:
            _, date, _, amount = line.strip().split(',')
            expense_date = datetime.strptime(date, '%d-%m-%Y')
            if start_date <= expense_date <= end_date:
                total += float(amount)
    return total

def calculate_expenses_in_category(category):
    total = 0
    with open(expenses_file_path, 'r') as file:
        for line in file:
            _, _, expense_category, amount = line.strip().split(',')
            if expense_category.lower() == category.lower():
                total += float(amount)
    return total

def calculate_expenses_with_name(name):
    total = 0
    with open(expenses_file_path, 'r') as file:
        for line in file:
            expense_name, _, _, amount = line.strip().split(',')
            if expense_name.lower() == name.lower():
                total += float(amount)
    return total

def calculate_expenses_in_category_during_period(category, start_date, end_date):
    total = 0
    with open(expenses_file_path, 'r') as file:
        for line in file:
            _, date, expense_category, amount = line.strip().split(',')
            expense_date = datetime.strptime(date, '%d-%m-%Y')
            if start_date <= expense_date <= end_date and expense_category.lower() == category.lower():
                total += float(amount)
    return total

def calculate_expenses_with_name_during_period(name, start_date, end_date):
    total = 0
    with open(expenses_file_path, 'r') as file:
        for line in file:
            expense_name, date, _, amount = line.strip().split(',')
            expense_date = datetime.strptime(date, '%d-%m-%Y')
            if start_date <= expense_date <= end_date and expense_name.lower() == name.lower():
                total += float(amount)
    return total

def calculate_total_incomes_during_period(start_date, end_date):
    total = 0
    with open(incomes_file_path, 'r') as file:
        for line in file:
            _, date, _, amount = line.strip().split(',')
            income_date = datetime.strptime(date, '%d-%m-%Y')
            if start_date <= income_date <= end_date:
                total += float(amount)
    return total

def calculate_total_income():
    total = 0
    with open(incomes_file_path, 'r') as file:
        for line in file:
            _, date, _, amount = line.strip().split(',')
            total += float(amount)
    return total

class ExpenseTrackerApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation='vertical')
        self.create_menu()
        return self.main_layout

    def create_menu(self):
        menu_layout = GridLayout(cols=2, spacing=10)
        
        menu_layout.add_widget(Button(text="Record an Expense", on_press=self.record_expense))
        menu_layout.add_widget(Button(text="Record an Income", on_press=self.record_income))
        menu_layout.add_widget(Button(text="See Total Expenses", on_press=self.show_total_expenses))
        menu_layout.add_widget(Button(text="See Total Income", on_press=self.show_total_income))
        menu_layout.add_widget(Button(text="See Account", on_press=self.show_account))
        #menu_layout.add_widget(Button(text="Other", on_press=self.show_other_options))
        menu_layout.add_widget(Button(text="Exit", on_press=self.exit_app))

        self.main_layout.add_widget(menu_layout)

    def show_expenses_during_period(self, instance):  # Corrected method name
        # Add logic to get start_date and end_date from user input
        start_date = datetime.now()  # Replace with user input
        end_date = datetime.now()  # Replace with user input
        period_expenses = calculate_expenses_during_period(start_date, end_date)
        self.show_popup(f"Expenses during the specified period: {period_expenses}")

    def show_expenses_in_category(self, instance):
        # Add logic to get category from user input
        category = input("Enter the category to calculate the expenses for: ")
        category_expenses = calculate_expenses_in_category(category)
        self.show_popup(f"Expenses in category '{category}': {category_expenses}")

    def show_expenses_with_name(self, instance):
        # Add logic to get name from user input
        name = input("Enter the name to calculate the expenses for: ")
        name_expenses = calculate_expenses_with_name(name)
        self.show_popup(f"Expenses with name '{name}': {name_expenses}")

    def show_expenses_in_category_during_period(self, instance):
        # Add logic to get category, start_date, and end_date from user input
        category = input("Enter the category to calculate the expenses for: ")
        start_date = datetime.now()  # Replace with user input
        end_date = datetime.now()  # Replace with user input
        category_period_expenses = calculate_expenses_in_category_during_period(category, start_date, end_date)
        self.show_popup(f"Expenses in category '{category}' during the specified period: {category_period_expenses}")

    def show_expenses_with_name_during_period(self, instance):
        # Add logic to get name, start_date, and end_date from user input
        name = input("Enter the name to calculate the expenses for: ")
        start_date = datetime.now()  # Replace with user input
        end_date = datetime.now()  # Replace with user input
        name_period_expenses = calculate_expenses_with_name_during_period(name, start_date, end_date)
        self.show_popup(f"Expenses with name '{name}' during the specified period: {name_period_expenses}")

    def record_expense(self, instance):
        # Use TextInput for user input
        popup_layout = BoxLayout(orientation='vertical', spacing=10)

        expense_name_input = TextInput(hint_text="Expense Name")
        day_spinner = Spinner(text="Select Day", values=[str(i) for i in range(1, 32)], size_hint=(None, None), size=(200, 44))
        month_spinner = Spinner(text="Select Month", values=[str(i) for i in range(1, 13)], size_hint=(None, None), size=(200, 44))
        year_spinner = Spinner(text="Select Year", values=[str(i) for i in range(2023, 2031)], size_hint=(None, None), size=(200, 44))
        categories = ['Transport', 'Prepared food', 'Work', 'Necessity', 'Relationship', 'Indulgance', 'Misc']
        expense_category_input = Spinner(text="Select Category", values=categories, size_hint=(None, None), size=(200, 44))
        expense_amount_input = TextInput(hint_text="Expense Amount")

        popup_layout.add_widget(expense_name_input)
        popup_layout.add_widget(day_spinner)
        popup_layout.add_widget(month_spinner)
        popup_layout.add_widget(year_spinner)
        popup_layout.add_widget(expense_category_input)
        popup_layout.add_widget(expense_amount_input)

        submit_button = Button(text="Submit", on_press=lambda x: self.add_expense_popup(
    expense_name_input.text, f"{day_spinner.text}-{month_spinner.text}-{year_spinner.text}", expense_category_input.text, expense_amount_input.text
))

        popup_layout.add_widget(submit_button)

        self.popup = Popup(title='Record an Expense', content=popup_layout, size_hint=(None, None), size=(500, 400))
        self.popup.open()

    def add_expense_popup(self, name, date, category, amount):
        expense = f"{name},{date},{category},{amount}\n"
        try:
            with open(expenses_file_path, 'a') as file:
                file.write(expense)
            self.show_popup("Expense added successfully!", None)
        except Exception as e:
            self.show_popup(f"Error adding expense: {e}", None)


    def record_income(self, instance):
        popup_layout = BoxLayout(orientation='vertical', spacing=10)

        income_name_input = TextInput(hint_text="Income Name")
        day_spinner = Spinner(text="Select Day", values=[str(i) for i in range(1, 32)], size_hint=(None, None), size=(200, 44))
        month_spinner = Spinner(text="Select Month", values=[str(i) for i in range(1, 13)], size_hint=(None, None), size=(200, 44))
        year_spinner = Spinner(text="Select Year", values=[str(i) for i in range(2023, 2031)], size_hint=(None, None), size=(200, 44))
        categories = ['Work', 'Misc']
        income_category_input = Spinner(text="Select Category", values=categories, size_hint=(None, None), size=(200, 44))
        income_amount_input = TextInput(hint_text="Income Amount")

        popup_layout.add_widget(income_name_input)
        popup_layout.add_widget(day_spinner)
        popup_layout.add_widget(month_spinner)
        popup_layout.add_widget(year_spinner)
        popup_layout.add_widget(income_category_input)
        popup_layout.add_widget(income_amount_input)

        submit_button = Button(text="Submit", on_press=lambda x: self.add_income_popup(
            income_name_input.text, f"{day_spinner.text}-{month_spinner.text}-{year_spinner.text}",
            income_category_input.text, income_amount_input.text
        ))
        popup_layout.add_widget(submit_button)

        self.popup = Popup(title='Record an Income', content=popup_layout, size_hint=(None, None), size=(500, 400))
        self.popup.open()

    def add_income_popup(self, name, date, category, amount):
        income = f"{name},{date},{category},{amount}\n"
        with open(incomes_file_path, 'a') as file:
            print(f"Writing to income file: {income}")
            file.write(income)
        self.show_popup("Income added successfully!", "Income Details:\nName: {}\nDate: {}\nCategory: {}\nAmount: {}".format(name, date, category, amount))

    def show_total_incomes_during_period(self, instance):
        # Add logic to get start_date and end_date from user input
        start_date = datetime.now()  # Replace with user input
        end_date = datetime.now()  # Replace with user input
        period_incomes = calculate_total_incomes_during_period(start_date, end_date)
        self.show_popup(f"Incomes during the specified period: {period_incomes}")

    def show_total_expenses(self, instance):
        total_expenses = calculate_total_expenses()
        self.show_popup(f"Total expenses: {total_expenses}")

    def show_total_income(self, instance):
        total_income = calculate_total_income()
        self.show_popup(f"Total income: {total_income}")

    def show_account(self, instance):
        total_income = calculate_total_income()
        total_expenses = calculate_total_expenses()
        account_balance = total_income - total_expenses
        self.show_popup(f"Account Balance: {account_balance}")

    def show_other_options(self, instance):
        other_options_layout = BoxLayout(orientation='vertical', spacing=10)

        options = [
        "See expenses in a period",
        "See expenses in a category",
        "See expenses with a certain name",
        "See expenses in a category during a period",
        "See expenses with a certain name during a period",
        "Exit"
    ]

        for option in options:
            button = Button(text=option, on_press=lambda x, opt=option: self.handle_other_option(opt))
            other_options_layout.add_widget(button)

        self.show_popup("Other Options", other_options_layout)

    def handle_other_option(self, option):
    # Implement logic based on the selected option
        if option == "See expenses in a period":
            self.show_expenses_during_period(None)
        elif option == "See expenses in a category":
            self.show_expenses_in_category(None)
        elif option == "See expenses with a certain name":
            self.show_expenses_with_name(None)
        elif option == "See expenses in a category during a period":
            self.show_expenses_in_category_during_period(None)
        elif option == "See expenses with a certain name during a period":
            self.show_expenses_with_name_during_period(None)
        elif option == "Exit":
            self.exit_app(None)

    def show_popup(self, text, content=None):
        popup_layout = BoxLayout(orientation='vertical')
        popup_layout.add_widget(Label(text=text))
        if content is not None:
            if isinstance(content, str):
                popup_layout.add_widget(Label(text=content))
            else:
                popup_layout.add_widget(content)
        close_button = Button(text="Close", on_press=self.dismiss_popup)
        popup_layout.add_widget(close_button)

        self.popup = Popup(title='Expense Tracker', content=popup_layout, size_hint=(None, None), size=(400, 200))
        self.popup.open()
    def dismiss_popup(self, instance=None):
        if self.popup:
            self.popup.dismiss()
    def exit_app(self, instance):
        self.stop()
# Run the app
if __name__ == '__main__':
    ExpenseTrackerApp().run()
