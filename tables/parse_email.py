import imaplib
import email
from datetime import datetime


def iridium_sbd_email(imap_server, username, mail_pass):
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, mail_pass)
    imap.select("INBOX")
    res, msgs = imap.search(None, "UNSEEN")
    msgs_list = []
    sub_list = []
    for num in msgs[0].split():
        res, msg = imap.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(msg[0][1])
        sub_list.append(msg['Subject'])
        for part in msg.walk():
            if part.get_content_disposition() == 'attachment':
                payload = part.get_payload(decode=True)
                payload_bin = ''.join(f'{x:08b}' for x in payload)
                msgs_list.append(payload_bin)
    return [msgs_list, sub_list]


def gonets_email(imap_server, username, mail_pass):
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(username, mail_pass)
    imap.select("INBOX")
    res, msgs = imap.search(None, "ALL")
    data_list = []
    for num in msgs[0].split():
        res, msg = imap.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(msg[0][1])
        payload = msg.get_payload(decode=False)
        data_split = payload.split('=\r\n')
        data = (data_split[0][-2:] + data_split[1] + data_split[2][:-6]).split(';')
        date_email = datetime.strptime(msg['Date'][:-6], '%d %b %Y %H:%M:%S')
        data.append(date_email)
        data_list.append(data)
    return data_list


def parse2float(data: str, bits: int, pos: int, prec: float, st: float):
    if pos + bits < len(data):
        result = prec * int(data[pos:(pos+bits)], 2) + st
        n = 1 if len(str(prec)) == 1 else len(str(prec+1)) - 2
        return float(f"%.{n}f" % result)
    raise ValueError('Not enough bits!')