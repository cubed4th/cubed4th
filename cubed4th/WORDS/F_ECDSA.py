#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2021, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _      ______    _____   _____     _____
  /\| |/\  |  ____|  / ____| |  __ \   / ____|     /\
  \ ` ' /  | |__    | |      | |  | | | (___      /  \
 |_     _| |  __|   | |      | |  | |  \___ \    / /\ \
  / , . \  | |____  | |____  | |__| |  ____) |  / ____ \
  \/|_|\/  |______|  \_____| |_____/  |_____/  /_/    \_\



)







"""  # __banner__


class LIB:  #

    """


    """

    def __init__(self, e, t, **kwargs):

        t.e_cname = None
        t.e_curve = None
        t.e_curves = {}
        t.e_skeys = {}
        t.e_vkeys = {}

    @staticmethod  ### E-GENERATE  ###
    def word_E_m_GENERATE__R(e, t, c):
        from ecdsa import SigningKey
        sk = SigningKey.generate(curve=t.e_curve)
        t.e_skeys[t.e_cname] = sk
        t.e_vkeys[t.e_cname] = sk.verifying_key

    @staticmethod  ### E-SKEY-SAVE ###
    def word_E_m_SKEY_m_SAVE__R_z(e, t, c):
        return (t.e_skeys[t.e_cname].to_pem(),)

    @staticmethod  ### E-SKEY-LOAD ###
    def word_E_m_SKEY_m_LOAD__R(e, t, c, z1):
        from ecdsa import SigningKey
        sk = SigningKey.from_pem(z1)
        t.e_skeys[t.e_cname] = sk
        t.e_vkeys[t.e_cname] = sk.verifying_key

    @staticmethod  ### E-VKEY-SAVE ###
    def word_E_m_SKEY_m_SAVE__R_z(e, t, c):
        return (t.e_vkeys[t.e_cname].to_pem(),)

    @staticmethod  ### E-VKEY-LOAD ###
    def word_E_m_VKEY_m_LOAD__R(e, t, c, z1):
        from ecdsa import VerifyingKey
        vk = VerifyingKey.from_pem(z1)
        t.e_vkeys[t.e_cname] = vk

    @staticmethod  ### E-SIGN ###
    def word_E_m_SIGN__R_z2(e, t, c, z1):
        return (t.e_skeys[t.e_cname].sign_deterministic(z1),)

    @staticmethod  ### E-SIGN-RANDOM ###
    def word_E_m_SIGN_m_RANDOM__R_z2(e, t, c, z1):
        return (t.e_skeys[t.e_cname].sign(z1),)

    @staticmethod  ### E-VERIFY ###
    def word_E_m_VERIFY__R_b(e, t, c, z1):
        return (t.e_skeys[t.e_cname].verify(z1),)

    @staticmethod  ### E-SELECT  ###
    def word_E_m_SELECT__R(e, t, c, x1):
        """

        T{ -> }T

        --END--

        Now the comments...

        """
        if not isinstance(x1, str):
            t.c_curve = x1
            t.c_cname = str(x1)
        else:
            cname = x1.lower()
            if cname == 'bitcoin':
                cname = 'secp256k1'
            if cname in t.c_chains:
                t.c_cname = cname
                t.c_curve = t.c_curves[cname]
            else:
                import ecdsa
                name = cname.split(':')[0]
                curve = None

                if name[:4] == 'secp':
                    for tail in ['256k1', '128r1', '160r1']:
                        print(name[4:])
                        if not name[4:] == tail: continue
                        exec(f"curve = ecdsa.SECP{tail}")
                        break

                elif name[:4] == 'nist':
                    for tail in ['256p', '192p', '384p', '521p']:
                        if not name[4:] == tail: continue
                        exec(f"curve = ecdsa.NIST{tail}")
                        break

                elif name[:10] == 'brainpoolp':
                    for tail in ['256r1', '512r1', '384r1', '160r1']:
                        if not name[:10] == tail: continue
                        exec(f"curve = ecdsa.BRAINPOOLP{size}")
                        break

                if curve == None:
                    raise RuntimeError("Unknown curve (add it. or typo?)")

                t.e_cname = cname
                t.e_curve = curve
                t.e_curves[cname] = curve




