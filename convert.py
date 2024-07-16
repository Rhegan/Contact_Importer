import csv

# Function to normalize phone numbers to international format if needed
def normalize_phone(phone):
    # Remove any leading or trailing whitespace
    phone = phone.strip()
    
    # Check if phone starts with '0' (regular South African format)
    if phone.startswith('0'):
        # Convert to international format
        phone = '+27' + phone[1:]
    
    # Check if phone starts with '27' (international format without '+')
    elif phone.startswith('27'):
        # If no '+' at the start, add it
        if not phone.startswith('+'):
            phone = '+' + phone
    
    # Check if phone starts with '+27' (international format with '+')
    elif phone.startswith('+27'):
        pass  # Do nothing as it is already in correct international format
    
    return phone

# Open the CSV file with semicolon delimiter
with open('contacts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    
    # Open the VCF file for writing
    with open('contacts.vcf', 'w') as vcf:
        for row in reader:
            address = row['Address']
            name = row['Name']
            surname = row['Surname']
            phone = row['Phone']
            
            # Format the phone number
            phone = normalize_phone(phone)
            
            vcard = f"""
BEGIN:VCARD
VERSION:3.0
FN:{name} {surname} {address}
TEL;TYPE=CELL:{phone}
ADR;TYPE=HOME:;;{address}
END:VCARD
"""
            vcf.write(vcard.strip() + "\n")

print("VCF file created successfully.")
