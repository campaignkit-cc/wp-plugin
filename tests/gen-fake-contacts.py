import csv
from faker import Faker

fake = Faker()

# Generate fake contacts
contacts = []
for _ in range(100):
    contact = [
        fake.first_name(),
        fake.last_name(),
        fake.email(),
        fake.address().replace("\n", ", "),
        fake.postcode(),
        fake.city(),
        fake.state(),
        fake.country(),
        fake.phone_number(),
    ]
    contacts.append(contact)

# Write contacts to CSV file
filepath = "fake-contacts.csv"
with open(filepath, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["first_name", "last_name", "email", "address_line_1", "postal_code", "city", "state", "country", "phone"])
    writer.writerows(contacts)
