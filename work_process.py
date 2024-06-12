import csv
from datetime import datetime

class WorkProcess:
    def __init__(self):
        self.audit_work = []

    def process_work(self):
        audit_number = input("Enter audit number: ")
        audit_name = self.get_audit_name(audit_number)
        audit_status = self.get_audit_status(audit_number)
        audit_conclusion = input("Enter audit conclusion: ")

        audit_work = {
            'Audit_Number': audit_number,
            'Audit_Name': audit_name,
            'Audit_Status': audit_status,
            'Audit_Conclusion': audit_conclusion
        }

        self.audit_work.append(audit_work)
        self.update_audit_status(audit_number)
        print(f"Audit work for {audit_name} processed successfully.")

    def get_audit_name(self, audit_number):
        with open('Audit_List.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Audit_Number'] == audit_number:
                    return row['Audit_Name']
        return None

    def get_audit_status(self, audit_number):
        with open('Audit_List.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Audit_Number'] == audit_number:
                    return row['Audit_Status']
        return None

    def update_audit_status(self, audit_number):
        updated_audit_list = []
        with open('Audit_List.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Audit_Number'] == audit_number:
                    row['Audit_Status'] = 'In_Progress'
                    row['Audit_Started_Date'] = datetime.now().strftime('%Y-%m-%d')
                updated_audit_list.append(row)

        with open('Audit_List.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=updated_audit_list[0].keys())
            writer.writeheader()
            writer.writerows(updated_audit_list)
        print(f"Audit status for audit number {audit_number} updated successfully.")
