import csv
import random
import datetime

class AuditRegister:
    def __init__(self):
        self.audit_list = []

    def register_audit(self):
        audit_number = self.generate_audit_number()
        audit_name = input("Enter audit name: ")
        audit_status = "Submitted"
        audit_type = input("Enter audit type (Financial_Audit, Compliance_Audit, Performance_Audit): ")
        audit_start_date = datetime.date.today()
        audit_end_date = datetime.date.today()
        audit_entity = input("Enter audit entity: ")
        audit_group = []

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
        self.write_to_csv(audit)
        print(f"Audit {audit_name} registered successfully.")

    def generate_audit_number(self):
        return str(random.randint(10000, 99999))

    def write_to_csv(self, audit):
        with open('Audit_List.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=audit.keys())
            writer.writerow(audit)
