# -*- coding: utf-8 -*-

import re


class SinicAsterisk(object):
    def __init__(self):
        pass

    def phone(self, message):
        length = len(message or '')
        if length == 11:
            message = re.sub(r'(\d{3})(\d{4})(\d{4})', r'\1****\3', message)
        return message

    def identity_card(self, message):
        length = len(message or '')
        if length == 18:
            message = re.sub(r'(\d{10})(\d{4})(\d{3}(\d|X|x))', r'\1****\3', message)
        elif length == 15:
            message = re.sub(r'(\d{8})(\d{4})(\d{3})', r'\1****\3', message)
        return message


asterisk = SinicAsterisk()
phone = asterisk.phone
identity_card = asterisk.identity_card
