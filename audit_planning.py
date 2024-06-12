import csv
import xlsxwriter
from datetime import datetime

class AuditPlanning:
    def __init__(self):
        self.audit_plan = []
        self.audit_list = self.read_audit_list()

    def read_audit_list(self):
        
        #Reads the audit list from the CSV file and stores it in self.audit_list.
        
        audit_list = []
        try:
            with open('Audit_List.csv', mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    audit_list.append(row)
        except FileNotFoundError:
            print("Audit_List.csv file not found.")
        return audit_list

    def display_audit_numbers(self):
        
        #Displays the available audit numbers and their corresponding names.
        
        if not self.audit_list:
            print("No audits available.")
            return

        print("Available audits:")
        for audit in self.audit_list:
            print(f"Audit Number: {audit['Audit_Number']}, Audit Name: {audit['Audit_Name']}")

    def plan_audit(self):
        
        #Collects audit planning details from the user and writes the plan to an Excel file.
        
        self.display_audit_numbers()
        if not self.audit_list:
            return

        audit_number = self.get_valid_audit_number()
        audit_name = self.get_audit_name(audit_number)

        planned_date = input("Enter planned audit start date (YYYY-MM-DD): ")
        actual_date = input("Enter actual audit start date (YYYY-MM-DD) or press Enter to leave empty: ")
        diff_days = self.calculate_difference(planned_date, actual_date) if actual_date else None

        audit_plan = {
            'Audit_Number': audit_number,
            'Audit_Name': audit_name,
            'Audit_Started_Date': {
                'Planned_Date': planned_date,
                'Actual_Date': actual_date,
                'Difference_Days': diff_days
            },
            'Audit_Plan_Date': self.get_date_details('Audit Plan Date'),
            'Audit_Work_Date': self.get_date_details('Audit Work Date'),
            'Audit_Report_Date': self.get_date_details('Audit Report Date')
        }

        self.audit_plan.append(audit_plan)
        self.write_to_xlsx()
        self.write_to_audit_work(audit_plan)
        print(f"Audit plan for {audit_name} created successfully.")

    def get_valid_audit_number(self):
       #validation
        while True:
            audit_number = input("Enter audit number: ")
            if any(audit['Audit_Number'] == audit_number for audit in self.audit_list):
                return audit_number
            else:
                print("Wrong audit number. Please try again.")

    def get_audit_name(self, audit_number):
        
        #Retrieves the audit name corresponding to the given audit number.
        
        for audit in self.audit_list:
            if audit['Audit_Number'] == audit_number:
                return audit['Audit_Name']
        return None

    def calculate_difference(self, planned_date, actual_date):
        
        planned = datetime.strptime(planned_date, '%Y-%m-%d')
        actual = datetime.strptime(actual_date, '%Y-%m-%d')
        return (actual - planned).days

    def get_date_details(self, date_type):
        
        planned_date = input(f"Enter planned {date_type} (YYYY-MM-DD): ")
        actual_date = input(f"Enter actual {date_type} (YYYY-MM-DD) or press Enter to leave empty: ")
        diff_days = self.calculate_difference(planned_date, actual_date) if actual_date else None
        return {
            'Planned_Date': planned_date,
            'Actual_Date': actual_date,
            'Difference_Days': diff_days
        }

    def write_to_xlsx(self):
        
        #Writes audit planning details 
        
        workbook = xlsxwriter.Workbook('Audit_Plan.xlsx')
        worksheet = workbook.add_worksheet()

        row = 0
        col = 0

        if self.audit_plan:
            # Write headers
            headers = self.audit_plan[0].keys()
            for header in headers:
                worksheet.write(row, col, header)
                col += 1
            row += 1

            # Write data
            for plan in self.audit_plan:
                col = 0
                for key, value in plan.items():
                    if isinstance(value, dict):
                        details = f"Planned: {value['Planned_Date']}, Actual: {value['Actual_Date']}, Difference: {value['Difference_Days']} days"
                        worksheet.write(row, col, details)
                    else:
                        worksheet.write(row, col, value)
                    col += 1
                row += 1

        workbook.close()

    def write_to_audit_work(self, audit_plan):
        
        #Writes audit planning details
        with open('Audit_Work.csv', mode='w', newline='') as file:
            fieldnames = ['Audit_Number', 'Audit_Name', 'Audit_Started_Date_Actual']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({
                'Audit_Number': audit_plan['Audit_Number'],
                'Audit_Name': audit_plan['Audit_Name'],
                'Audit_Started_Date_Actual': audit_plan['Audit_Started_Date']['Actual_Date']
            })
