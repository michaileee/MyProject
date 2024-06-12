import csv
import pandas as pd
from datetime import datetime

class WorkProcess:
    def __init__(self):
        self.audit_work = []
        self.audit_list = self.read_audit_list()
        self.audit_plan_list = self.read_audit_plan_list()
        self.audit_work_list = self.read_audit_work_list()

    def read_audit_list(self):
        audit_list = []
        try:
            with open('Audit_List.csv', mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    audit_list.append(row)
        except FileNotFoundError:
            print("Audit_List.csv file not found.")
        return audit_list

    def read_audit_plan_list(self):
        audit_plan_list = []
        try:
            df = pd.read_excel('Audit_Plan.xlsx')
            for index, row in df.iterrows():
                audit_plan_list.append({
                    'Audit_Number': row['Audit_Number'],
                    'Audit_Name': row['Audit_Name'],
                    'Audit_Started_Date_Planned': row['Audit_Started_Date'].split(',')[0].split(':')[1].strip(),
                    'Audit_Plan_Date_Planned': row['Audit_Plan_Date'].split(',')[0].split(':')[1].strip(),
                    'Audit_Work_Date_Planned': row['Audit_Work_Date'].split(',')[0].split(':')[1].strip(),
                    'Audit_Report_Date_Planned': row['Audit_Report_Date'].split(',')[0].split(':')[1].strip()
                })
        except FileNotFoundError:
            print("Audit_Plan.xlsx file not found.")
        return audit_plan_list

    def read_audit_work_list(self):
        audit_work_list = []
        try:
            with open('Audit_Work.csv', mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    audit_work_list.append(row)
        except FileNotFoundError:
            print("Audit_Work.csv file not found.")
        return audit_work_list

    def display_audit_numbers(self):
        if not self.audit_list:
            print("No audits available.")
            return

        print("Available audits:")
        for audit in self.audit_list:
            print(f"Audit Number: {audit['Audit_Number']}, Audit Name: {audit['Audit_Name']}")

    def process_work(self):
        self.display_audit_numbers()
        if not self.audit_list:
            return

        audit_number = self.get_valid_audit_number()
        audit_name = self.get_audit_name(audit_number)
        audit_status = self.get_audit_status(audit_number)

        audit_plan = self.get_audit_plan(audit_number)
        if not audit_plan:
            print(f"No audit plan found for audit number {audit_number}.")
            return

        actual_dates = self.get_actual_dates(audit_plan)

        audit_conclusion = input("Enter audit conclusion: ")

        audit_work = {
            'Audit_Number': audit_number,
            'Audit_Name': audit_name,
            'Audit_Status': audit_status,
            'Audit_Conclusion': audit_conclusion,
            **actual_dates
        }

        self.audit_work.append(audit_work)
        self.update_audit_status(audit_number)
        self.write_to_csv()
        print(f"Audit work for {audit_name} processed successfully.")

    def get_valid_audit_number(self):
        while True:
            audit_number = input("Enter audit number: ")
            if any(audit['Audit_Number'] == audit_number for audit in self.audit_list):
                return audit_number
            else:
                print("Wrong audit number. Please try again.")

    def get_audit_name(self, audit_number):
        for audit in self.audit_list:
            if audit['Audit_Number'] == audit_number:
                return audit['Audit_Name']
        return None

    def get_audit_status(self, audit_number):
        for audit in self.audit_list:
            if audit['Audit_Number'] == audit_number:
                return audit['Audit_Status']
        return None

    def get_audit_plan(self, audit_number):
        for audit_plan in self.audit_plan_list:
            if audit_plan['Audit_Number'] == audit_number:
                return audit_plan
        return None

    def get_actual_dates(self, audit_plan):
        actual_dates = {}

        planned_date = audit_plan['Audit_Started_Date_Planned']
        actual_date = input(f"Enter actual audit start date (YYYY-MM-DD) for planned date {planned_date} or press Enter to leave empty: ")
        if actual_date:
            diff_days = self.calculate_difference(planned_date, actual_date)
            actual_dates['Audit_Started_Date_Actual'] = actual_date
            actual_dates['Audit_Started_Date_Difference'] = diff_days

        planned_date = audit_plan['Audit_Plan_Date_Planned']
        actual_date = input(f"Enter actual audit plan date (YYYY-MM-DD) for planned date {planned_date} or press Enter to leave empty: ")
        if actual_date:
            diff_days = self.calculate_difference(planned_date, actual_date)
            actual_dates['Audit_Plan_Date_Actual'] = actual_date
            actual_dates['Audit_Plan_Date_Difference'] = diff_days

        planned_date = audit_plan['Audit_Work_Date_Planned']
        actual_date = input(f"Enter actual audit work date (YYYY-MM-DD) for planned date {planned_date} or press Enter to leave empty: ")
        if actual_date:
            diff_days = self.calculate_difference(planned_date, actual_date)
            actual_dates['Audit_Work_Date_Actual'] = actual_date
            actual_dates['Audit_Work_Date_Difference'] = diff_days

        planned_date = audit_plan['Audit_Report_Date_Planned']
        actual_date = input(f"Enter actual audit report date (YYYY-MM-DD) for planned date {planned_date} or press Enter to leave empty: ")
        if actual_date:
            diff_days = self.calculate_difference(planned_date, actual_date)
            actual_dates['Audit_Report_Date_Actual'] = actual_date
            actual_dates['Audit_Report_Date_Difference'] = diff_days

        return actual_dates

    def calculate_difference(self, planned_date, actual_date):
        planned = datetime.strptime(planned_date, '%Y-%m-%d')
        actual = datetime.strptime(actual_date, '%Y-%m-%d')
        return (actual - planned).days

    def update_audit_status(self, audit_number):
        updated_audit_list = []
        for row in self.audit_list:
            if row['Audit_Number'] == audit_number:
                row['Audit_Status'] = 'In_Progress'
                row['Audit_Started_Date'] = datetime.now().strftime('%Y-%m-%d')
            updated_audit_list.append(row)

        with open('Audit_List.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=updated_audit_list[0].keys())
            writer.writeheader()
            writer.writerows(updated_audit_list)

    def write_to_csv(self):
        with open('Audit_Work.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.audit_work[0].keys())
            writer.writeheader()
            writer.writerows(self.audit_work)
