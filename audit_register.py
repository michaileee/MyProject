import csv
import random
import datetime

class AuditRegister:
    def __init__(self):
        self.audit_list = []

    def register_audit(self):
        audit_number = self.generate_audit_number()
        audit_name = input("Enter audit name: ")

        valid_statuses = ['Submitted', 'Started', 'In_Progress', 'Completed', 'Archived']
        while True:
            audit_status = input(f"Enter audit status {valid_statuses}: ")
            if audit_status in valid_statuses:
                break
            else:
                raise Exception("Invalid audit status. Please try again.")

        audit_type = input("Enter audit type (Financial_Audit, Compliance_Audit, Performance_Audit): ")
        audit_start_date = input("Enter audit start date (YYYY-MM-DD) or press Enter for today's date: ")
        audit_start_date = audit_start_date if audit_start_date else datetime.date.today().strftime('%Y-%m-%d')

        audit_end_date = input("Enter audit end date (YYYY-MM-DD) or press Enter for today's date: ")
        audit_end_date = audit_end_date if audit_end_date else datetime.date.today().strftime('%Y-%m-%d')

        audit_entity = input("Enter audit entity: ")
        audit_group = input("Enter audit group members (comma separated) or press Enter to leave empty: ")
        audit_group = audit_group.split(',') if audit_group else []

        audit = {
            'Audit_Number': audit_number,
            'Audit_Name': audit_name,
            'Audit_Status': audit_status,
            'Audit_Type': audit_type,
            'Audit_Start_Date': audit_start_date,
            'Audit_End_Date': audit_end_date,
            'Audit_Entity': audit_entity,
            'Audit_Group': audit_group
        }

        self.audit_list.append(audit)
        self.write_to_csv()
        self.print_audit_list()
        print(f"Audit {audit_name} registered successfully.")

    def generate_audit_number(self):
        return str(random.randint(10000, 99999))

    def write_to_csv(self):
        with open('Audit_List.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.audit_list[0].keys())
            writer.writeheader()
            for audit in self.audit_list:
                writer.writerow(audit)

    def print_audit_list(self):
        for audit in self.audit_list:
            for key, value in audit.items():
                print(f"{key: <20} : {value}")
            print()
