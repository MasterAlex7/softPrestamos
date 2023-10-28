import re


def validar_rfc(rfc):
    if len(rfc) == 13:
        if re.match(r'^[A-Z]{4}[0-9]{6}[A-Z0-9]{3}$', rfc):
            return True
        else:
            return False
    else:
        return False