#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2021, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _       _____   _    _              _____   _   _    _____
  /\| |/\   / ____| | |  | |     /\     |_   _| | \ | |  / ____|
  \ ` ' /  | |      | |__| |    /  \      | |   |  \| | | (___
 |_     _| | |      |  __  |   / /\ \     | |   | . ` |  \___ \
  / , . \  | |____  | |  | |  / ____ \   _| |_  | |\  |  ____) |
  \/|_|\/   \_____| |_|  |_| /_/    \_\ |_____| |_| \_| |_____/



)





"""  # __banner__


class LIB:  # { The Object ABI : words }

    """


    """

    def __init__(self, e, t, **kwargs):
        t.c_cname = None
        t.c_chain = None
        t.c_chains = {}

        t.c_wallet = None
        t.c_wallets = {}

        t.c_testnet = True

    @staticmethod  ### C-VERIFY  ###
    def word_C_minus_VERIFY__R(e, t, c, x1):
        c.EXIT = True
        c.FAIL = True if x1 else False

    @staticmethod  ### C-RETURN  ###
    def word_C_minus_RETURN__R(e, t, c):
        c.EXIT = True
        c.FAIL = True

    @staticmethod  ### C-RIPEMD160  ###
    def word_C_minus_RIPEMD160__R_z2(e, t, c, z1):
        from cryptos import ripemd160
        return (ripemd160(z1), )

    @staticmethod  ### C-SHA256  ###
    def word_C_minus_SHA256__R_z2(e, t, c, z1):
        from cryptos import sha256
        return (sha256(z1), )

    @staticmethod  ### C-HASH160  ###
    def word_C_minus_HASH160__R_z2(e, t, c, z1):
        from cryptos import sha256, ripemd160
        return (ripemd160(sha256(z1)), )

    @staticmethod  ### C-HASH256  ###
    def word_C_minus_HASH256__R_z2(e, t, c, z1):
        from cryptos import sha256
        return (sha256(sha256(z1)), )

    @staticmethod  ### C-PRIV2PUB  ###
    def word_C_minus_PRIV2PUB__R_z2(e, t, c, z1):
        from cryptos import privkey_to_pubkey
        return (privkey_to_pubkey(z1),)

    @staticmethod  ### C-PRIV2ADDR  ###
    def word_C_minus_PRIV2ADDR__R_z2(e, t, c, z1):
        from cryptos import privkey_to_address
        return (privkey_to_address(z1),)

    @staticmethod  ### C-PUB2ADDR  ###
    def word_C_minus_PUB2ADDR__R_z2(e, t, c, z1):
        from cryptos import pubkey_to_address
        return (pubkey_to_address(z1),)

    @staticmethod  ### C-IS-PRIVKEY  ###
    def word_C_minus_IS_minus_PRIVKEY__R_b(e, t, c, z):
        from cryptos import is_privkey
        return (is_privkey(z),)

    @staticmethod  ### C-IS-PUBKEY  ###
    def word_C_minus_IS_minus_PUBKEY__R_b(e, t, c, z):
        from cryptos import is_pubkey
        return (is_pubkey(z),)

    @staticmethod  ### C-PUBKEY-FORMAT  ###
    def word_C_minus_PUBKEY_minus_FORMAT__R_b(e, t, c, z):
        from cryptos import get_pubkey_format
        return (get_pubkey_format(z),)

    @staticmethod  ### C-ENCODE-PUBKEY  ###
    def word_C_minus_PUBKEY_minus_FORMAT__R_z2(e, t, c, z1, s1):
        from cryptos import encode_pubkey
        return (encode_pubkey(z1, s1),)

    @staticmethod  ### C-TESTNET  ###
    def word_C_minus_TESTNET__R(e, t, c, x1):
        if x1 == None:
            return (t.c_testnet,)
        t.c_testnet = True if x1 else False

    @staticmethod  ### C-SEND  ###
    def word_C_minus_SEND__R_z2(e, t, c, z1, z2, n1):
        r = t.c_object.send(z1, z2, n1)
        return (r.get('data',{}), r.get('network',''), r.get('status',''))

    @staticmethod  ### C-OBJECT  ###
    def word_C_minus_OBJECT__R_o(e, t, c):
        return (t.c_object,)

    @staticmethod  ### C-SELECT  ###
    def word_C_minus_SELECT__R(e, t, c, x1):
        """

        T{ -> }T

        --END--

        Now the comments...

        """
        if not isinstance(x1, str):
            t.c_chain = x1
            t.c_cname = str(x1)
        else:
            cname = x1.lower()
            if cname in t.c_chains:
                t.c_cname = cname
                t.c_chain = t.c_chains[cname]
            else:
                import cryptos
                code = cname.split(':')[0]
                coin = None
                if code == 'dash':
                    coin = cryptos.Dash(testnet=t.c_testnet)
                elif code == 'doge':
                    coin = cryptos.Doge(testnet=t.c_testnet)
                elif code == 'btc':
                    coin = cryptos.Bitcoin(testnet=t.c_testnet)
                elif code == 'bcc':
                    coin = cryptos.BitcoinCash(testnet=t.c_testnet)
                elif code == 'btg':
                    coin = cryptos.BitcoinGold(testnet=t.c_testnet)
                elif code == 'ltc':
                    coin = cryptos.Litecoin(testnet=t.c_testnet)

                if coin == None:
                    raise RuntimeError

                t.c_cname = cname
                t.c_chain = coin
                t.c_chains[cname] = coin
                t.c_wallet = t.c_wallets.get(cname, None)

    @staticmethod  ### C-WORDS  ###
    def word_C_minus_WORDS__R_z(e, t, c):
        import os
        from cryptos import entropy_to_words
        return (entropy_to_words(os.urandom(16)),)

    @staticmethod  ### C-VALID ###
    def word_C_minus_VALID__R_b1_b2(e, t, c, s1):
        from cryptos import keystore
        r = keystore.bip39_is_checksum_valid(s1)
        return (r[0],r[1])

    @staticmethod  ### W-SELECT  ###
    def word_C_minus_WORDS__R(e, t, c, z1):
        """

        --END--


        """

        if z1 == None:
            del t.c_wallets[t.c_cname]
        else:
            if t.c_cname in t.c_wallets:
                t.c_wallet = t.c_wallets[t.c_cname]
            else:
                t.c_wallet = t.c_chain.wallet(z1)
                t.c_wallets[t.c_cname] = t.c_wallet

    @staticmethod  ### W-ROOT-D  ###
    def word_W_minus_ROOT_minus_D__R_z(e, t, c):
        return (t.c_wallet.keystore.root_derivation,)

    @staticmethod  ### W-XPRIV  ###
    def word_W_minus_XPRIV__R_z(e, t, c):
        return (t.c_wallet.keystore.keystore.xprv,)

    @staticmethod  ### W-XPRIV  ###
    def word_W_minus_XPRIV__R_z(e, t, c):
        return (t.c_wallet.keystore.keystore.xpub,)

    @staticmethod  ### W-NEW-RECEIVE  ###
    def word_W_minus_NEW_minus_RECEIVE__R_z(e, t, c):
        return (t.c_wallet.new_receiving_address(),)

    @staticmethod  ### W-NEW-CHANGE  ###
    def word_W_minus_NEW_minus_CHANGE__R_z(e, t, c):
        return (t.c_wallet.new_change_address(),)

    @staticmethod  ### W-PRIV-KEY  ###
    def word_W_minus_PRIV_minus_KEY__R_z2(e, t, c, z1):
        return (t.c_wallet.privkey(z1),)




