# -*- coding: utf-8 -*-

from SinicAsterisk import asterisk


class TestSinicValidateCommands(object):

    def test_phone(self):
        phone = '18888888888'
        astphone = asterisk.phone(phone)
        assert astphone == '188****8888'

    def test_email_exist(self):
        identity_card = '320321198811118888'
        astidcard = asterisk.identity_card(identity_card)
        assert astidcard == '3203211988****8888'
