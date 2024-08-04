"""work1.py"""

def extract_domains(email_list):
    return [email.split('@')[1] for email in email_list]

if __name__ == "__main__":
    emails = input("Введите список email-адресов через пробел: ").split()
    domains = extract_domains(emails)
    print(domains)
    