import csv

class AuditGroup:
    def __init__(self):
        pass

    def create_group(self):
        audit_number = input("Enter audit number: ")
        group_members = input("Enter group members (comma separated): ").split(',')

        # Updating the Audit List with group members
        self.update_audit_group(audit_number, group_members)

    def update_audit_group(self, audit_number, group_members):
        updated_audit_list = []
        with open('Audit_List.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Audit_Number'] == audit_number:
                    row['Audit_Group'] = group_members
                updated_audit_list.append(row)

        with open('Audit_List.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=updated_audit_list[0].keys())
            writer.writeheader()
            writer.writerows(updated_audit_list)
        print(f"Audit group for audit number {audit_number} updated successfully.")
