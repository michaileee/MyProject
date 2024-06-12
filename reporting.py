import csv
import pandas as pd

class Reporting:
    def __init__(self):
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

    def generate_report(self):
        print("1. Audit_List_Report")
        print("2. Choose_Audit_With_Auditor")
        print("3. Audit_Plan_Report")
        print("4. Audit_Work_Report")

        choice = input("Choose an option to generate report: ")

        if choice == '1':
            self.audit_list_report()
        elif choice == '2':
            self.choose_audit_with_auditor()
        elif choice == '3':
            self.audit_plan_report()
        elif choice == '4':
            self.audit_work_report()
        else:
            print("Invalid choice. Please try again.")

    def audit_list_report(self):
        with open('Audit_List.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))

    def choose_audit_with_auditor(self):
        auditor_name = input("Enter auditor's name: ").strip()
        auditor_surname = input("Enter auditor's surname: ").strip()

        found = False
        for audit in self.audit_list:
            audit_group = audit['Audit_Group']
            if audit_group:
                auditors = [auditor.strip() for auditor in audit_group.strip('[]').replace("'", "").split(',')]
                for auditor in auditors:
                    name, surname = auditor.split()
                    if name == auditor_name and surname == auditor_surname:
                        print(f"Audit Number: {audit['Audit_Number']}")
                        print(f"Audit Name: {audit['Audit_Name']}")
                        print(f"Audit Status: {audit['Audit_Status']}")
                        print(f"Audit Type: {audit['Audit_Type']}")
                        print(f"Audit Start Date: {audit['Audit_Start_Date']}")
                        print(f"Audit End Date: {audit['Audit_End_Date']}")
                        print(f"Audit Entity: {audit['Audit_Entity']}")
                        print(f"Audit Group: {audit['Audit_Group']}")
                        found = True
                        break
            if found:
                break
        if not found:
            print(f"No audit found for auditor {auditor_name} {auditor_surname}.")

    def audit_plan_report(self):
        audit_number = input("Enter audit number: ").strip()

        found = False
        for audit_plan in self.audit_plan_list:
            if audit_plan['Audit_Number'] == audit_number:
                print(f"Audit Number: {audit_plan['Audit_Number']}")
                print(f"Audit Name: {audit_plan['Audit_Name']}")
                print(f"Audit Started Date: {audit_plan['Audit_Started_Date_Planned']}")
                print(f"Audit Plan Date: {audit_plan['Audit_Plan_Date_Planned']}")
                print(f"Audit Work Date: {audit_plan['Audit_Work_Date_Planned']}")
                print(f"Audit Report Date: {audit_plan['Audit_Report_Date_Planned']}")
                found = True
                break
        if not found:
            print(f"No audit plan found for audit number {audit_number}.")

    def audit_work_report(self):
        audit_number = input("Enter audit number: ").strip()

        found = False
        for audit_work in self.audit_work_list:
            if audit_work['Audit_Number'] == audit_number:
                print(f"Audit Number: {audit_work['Audit_Number']}")
                print(f"Audit Name: {audit_work['Audit_Name']}")
                print(f"Audit Status: {audit_work['Audit_Status']}")
                print(f"Audit Conclusion: {audit_work['Audit_Conclusion']}")
                print(f"Audit Started Date (Actual): {audit_work.get('Audit_Started_Date_Actual', 'N/A')}")
                print(f"Audit Started Date Difference: {audit_work.get('Audit_Started_Date_Difference', 'N/A')} days")
                print(f"Audit Plan Date (Actual): {audit_work.get('Audit_Plan_Date_Actual', 'N/A')}")
                print(f"Audit Plan Date Difference: {audit_work.get('Audit_Plan_Date_Difference', 'N/A')} days")
                print(f"Audit Work Date (Actual): {audit_work.get('Audit_Work_Date_Actual', 'N/A')}")
                print(f"Audit Work Date Difference: {audit_work.get('Audit_Work_Date_Difference', 'N/A')} days")
                print(f"Audit Report Date (Actual): {audit_work.get('Audit_Report_Date_Actual', 'N/A')}")
                print(f"Audit Report Date Difference: {audit_work.get('Audit_Report_Date_Difference', 'N/A')} days")
                found = True
                break
        if not found:
            print(f"No audit work found for audit number {audit_number}.")