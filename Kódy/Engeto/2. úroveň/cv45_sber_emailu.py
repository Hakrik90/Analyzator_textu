my_str = '''Lorem ipsum dolor sit amet, consectetur adipiscing 
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc tristique
fringilla congue. Donec ante diam cnn@info.com, dapibus
lacinia vulputate vitae, ullamcorper in justo. Maecenas
massa purus, ultricies a dictum ut, dapibus vitae massa.
Cras abc@gmail.com vel libero felis. In augue elit, porttitor
nec molestie quis, auctor a quam. Quisque b2b@money.fr
pretium dolor et tempor feugiat. Morbi libero lectus,
porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
Pellentesque id dui viverra, auctor enim ut, fringilla est.
Maecenas gravida turpis nec ultrices aliquet.
'''

# Funkce pro posbirani emailu ze stringu
def email_in(text):
    text = text.split()
    emails = []
    for mail in text:
        if '@' in mail and '.' in mail:
            mail = mail.strip('.,!')
            emails.append(mail)

    return emails

# Funkce pro extrahovani emailu obsahujici cisla
def digit_mail(text):
    emails = []
    for mail in email_in(text):
        for m in mail:
            if m.isnumeric():
                emails.append(mail)
                break
    return emails

# Funkce pro extrahovani domen vsech emailu
def domains(text):
    domains = set()
    for mail in email_in(text):
        domains.add(mail.split('@')[-1])
    return list(domains)

print(digit_mail(my_str))