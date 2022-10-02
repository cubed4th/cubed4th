#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) 2021 - 2023, Scott.McCallum@HQ.UrbaneINTER.NET

__banner__ = r""" (

     _      _    _               _____   _    _   ______    _____
  /\| |/\  | |  | |     /\      / ____| | |  | | |  ____|  / ____|
  \ ` ' /  | |__| |    /  \    | (___   | |__| | | |__    | (___
 |_     _| |  __  |   / /\ \    \___ \  |  __  | |  __|    \___ \
  / , . \  | |  | |  / ____ \   ____) | | |  | | | |____   ____) |
  \/|_|\/  |_|  |_| /_/    \_\ |_____/  |_|  |_| |______| |_____/



)







"""  # __banner__


class LIB:  # { The Object ABI : words }

    """


    """

    def __init__(self, e, t, **kwargs):
        t.h_name = None
        t.h_hash = None
        t.h_hashes = {}
        t.h_algo = None
        t.h_algos = {}

    @staticmethod  ### H-DIGEST-SIZE  ###
    def word_H_m_DIGEST_m_SIZE__R_n(e, t, c):
        return (t.h_t.digest_size,)

    @staticmethod  ### H-BLOCK-SIZE  ###
    def word_H_m_BLOCK_m_SIZE__R_n(e, t, c):
        return (t.h_object.block_size,)

    @staticmethod  ### H-UPDATE ###
    def word_H_m_UPDATE__R(e, t, c, s1):
        t.h_hash.update(s1.encode())

    @staticmethod  ### H-DIGEST ###
    def word_H_m_DIGEST__R(e, t, c):
        return (t.h_hash.hexdigest(),)

    @staticmethod  ### H-OBJECT ###
    def word_H_m_OBJECT__R_x(e, t, c):
        return (t.h_hash,)

    @staticmethod  ### H-SELECT ###
    def word_H_m_SELECT__R(e, t, c, x1):

        if not isinstance(x1, str):
            t.h_hash = x1
            t.h_name = ''
            t.h_algo = None
        else:
            hname = x1.lower()
            if hname in t.h_hashes:
                t.h_name = hname
                t.h_hash = t.h_hashes[hname]
                t.h_algo = t.h_algos[hname]
            else:
                import hashlib
                algo_name = hname.split(':')[0]
                algo = None

                if algo_name[:5] == 'sha3_':
                    size = algo_name[5:]
                    algo = hashlib.sha3_256 if size == '256' else algo
                    algo = hashlib.sha3_224 if size == '224' else algo
                    algo = hashlib.sha3_348 if size == '348' else algo
                    algo = hashlib.sha3_512 if size == '512' else algo

                elif algo_name[:3] == 'sha':
                    size = algo_name[3:]
                    algo = hashlib.sha256 if size == '256' else algo
                    algo = hashlib.sha224 if size == '224' else algo
                    algo = hashlib.sha348 if size == '348' else algo
                    algo = hashlib.sha512 if size == '512' else algo

                elif algo_name[:6] == 'shake_':
                    size = algo_name[3:]
                    algo = hashlib.shake128 if size == '128' else algo
                    algo = hashlib.shake256 if size == '256' else algo

                if algo == None:
                    raise RuntimeError("Unknown hash algo")

                t.h_name = hname
                t.h_algo = algo
                t.h_algos[hname] = algo
                t.h_hash = algo()
                t.h_hashes[hname] = t.h_hash


