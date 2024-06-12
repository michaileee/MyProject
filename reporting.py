import csv

class Reporting:
    def __init__(self):
        pass

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
        audit_number = input("Enter audit number: ")
        with open('Audit_List.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Audit_Number'] == audit_number:
                    print(f"Audit Number: {row['Audit_Number']}")
                    print(f"Audit Name: {row['Audit_Name']}")
                    print(f"Audit Group: {row['Audit_Group']}")

    def audit_plan_report(self):
        # Implement similar to audit_list_report for Audit_Plan.xlsx
        pass

    def audit_work_report(self):
        # Implement similar to audit_list_report for audit_work
        pass
