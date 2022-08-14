from imap_tools import MailBox
from logowanie import nazwau, haslo, poczta

# get all attachments from INBOX and save them to files
with MailBox(poczta).login(nazwau, haslo, 'INBOX') as mailbox:
    for msg in mailbox.fetch():
        for att in msg.attachments:
            print(att.filename, att.content_type)
            with open('C:\\Users\\Tomek\\Downloads\\python mail 0.0.1\\{}'.format(att.filename), 'wb') as f:
                f.write(att.payload)