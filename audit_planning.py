import csv
import xlsxwriter
from datetime import datetime

class AuditPlanning:
    def __init__(self):
        self.audit_plan = []

    def plan_audit(self):
        audit_number = input("Enter audit number: ")
        audit_name = self.get_audit_name(audit_number)
        
        planned_date = input("Enter planned audit date (YYYY-MM-DD): ")
        actual_date = input("Enter actual audit date (YYYY-MM-DD): ")
        diff_days = self.calculate_difference(planned_date, actual_date)
        
        audit_plan = {
            'Audit_Number': audit_number,
            'Audit_Name': audit_name,
            'Planned_Date': planned_date,
            'Actual_Date': actual_date,
            'Difference_Days': diff_days
        }
        
        self.audit_plan.append(audit_plan)
        self.write_to_xlsx(audit_plan)
        print(f"Audit plan for {audit_name} created successfully.")

    def get_audit_name(self, audit_number):
        with open('Audit_List.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Audit_Number'] == audit_number:
                    return row['Audit_Name']
        return None

    def calculate_difference(self, planned_date, actual_date):
        planned = datetime.strptime(planned_date, '%Y-%m-%d')
        actual = datetime.strptime(actual_date, '%Y-%m-%d')
        return (actual - planned).days

    def write_to_xlsx(self, audit_plan):
        workbook = xlsxwriter.Workbook('Audit_Plan.xlsx')
        worksheet = workbook.add_worksheet()

        row = 0
        col = 0

        for key, value in audit_plan.items():
            worksheet.write(row, col, key)
            worksheet.write(row, col + 1, value)
            row += 1

        workbook.close()
