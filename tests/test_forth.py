#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) https://github.com/scott91e1 ~ 2021 - 2021

__banner__ = r""" (


  _            _              ______ ____  _____ _______ _    _
 | |          | |            |  ____/ __ \|  __ \__   __| |  | |
 | |_ ___  ___| |_           | |__ | |  | | |__) | | |  | |__| |
 | __/ _ \/ __| __|          |  __|| |  | |  _  /  | |  |  __  |
 | ||  __/\__ \ |_           | |   | |__| | | \ \  | |  | |  | |
  \__\___||___/\__|          |_|    \____/|_|  \_\ |_|  |_|  |_|
                     ______
                    |______|
)





"""  # __banner__


class TestFORTH:

    options = {}

    def test_0000(self):
        r"""
        1 2 3
        """
        e = FORTH.Engine(self.test_0000.__doc__, **self.options)
        assert e.root.stack == [1, 2, 3]
        assert e.root.memory == {}

    def test_0001(self):
        r"""
        'Hello 'World
        """
        e = FORTH.Engine(self.test_0001.__doc__, **self.options)
        assert e.root.stack == ["Hello", "World"]
        assert e.root.memory == {}

    def test_0002(self):
        r"""
        123 456 !
        """
        e = FORTH.Engine(self.test_0002.__doc__, **self.options)
        assert e.root.stack == []
        assert e.root.memory == {456: 123}

    def test_0003(self):
        r"""
        123 'FOO_1 !
        'Baz 'FOO_2 !
        """
        e = FORTH.Engine(self.test_0003.__doc__, **self.options)
        assert e.root.stack == []
        assert e.root.memory == {"FOO_1": 123, "FOO_2": "Baz"}

    def test_1000(self):
        r"""
        T{ 'Hello 'World DROP -> ("Hello") }T
        """
        e = FORTH.Engine(self.test_1000.__doc__, **self.options)
        assert e.root.test["f"] == 0

    def test_BASIC_ASSUMPTIONS(self):
        e = FORTH.Engine(self.BASIC_ASSUMPTIONS, **self.options)
        assert e.root.test["f"] == 0

    BASIC_ASSUMPTIONS = r"""

T{ -> }T               \ START WITH CLEAN SLATE
( TEST IF ANY BITS ARE SET; ANSWER IN BASE 1 )
T{ : BITSSET? IF 0 0 ELSE 0 THEN ; -> }T
T{  0 BITSSET? -> 0 }T      ( ZERO IS ALL BITS CLEAR )
T{  1 BITSSET? -> 0 0 }T      ( OTHER NUMBER HAVE AT LEAST ONE BIT )
T{ -1 BITSSET? -> 0 0 }T

    """

    def test_BOOLEANS_INVERT(self):
        e = FORTH.Engine(self.BOOLEANS_INVERT, **self.options)
        assert e.root.test["f"] == 0

    BOOLEANS_INVERT = r"""

T{ 0 0 AND -> 0 }T
T{ 0 1 AND -> 0 }T
T{ 1 0 AND -> 0 }T
T{ 1 1 AND -> 1 }T

T{ 0 INVERT 1 AND -> 1 }T
T{ 1 INVERT 1 AND -> 0 }T

0    CONSTANT 0S
0 INVERT CONSTANT 1S

T{ 0S INVERT -> 1S }T
T{ 1S INVERT -> 0S }T

T{ 0S 0S AND -> 0S }T
T{ 0S 1S AND -> 0S }T
T{ 1S 0S AND -> 0S }T
T{ 1S 1S AND -> 1S }T

T{ 0S 0S OR -> 0S }T
T{ 0S 1S OR -> 1S }T
T{ 1S 0S OR -> 1S }T
T{ 1S 1S OR -> 1S }T

T{ 0S 0S XOR -> 0S }T
T{ 0S 1S XOR -> 1S }T
T{ 1S 0S XOR -> 1S }T
T{ 1S 1S XOR -> 0S }T

        """

    def test_LSHIFT_RSHIFT(self):
        e = FORTH.Engine(self.LSHIFT_RSHIFT, **self.options)
        assert e.root.test["f"] == 0

    LSHIFT_RSHIFT = r"""

0    CONSTANT 0S
0 INVERT CONSTANT 1S
1S 1 RSHIFT INVERT CONSTANT MSB
T{ : BITSSET? IF 0 0 ELSE 0 THEN ; -> }T

( )

( WE TRUST 1S, INVERT, AND BITSSET?; WE WILL CONFIRM RSHIFT LATER )
1S 1 RSHIFT INVERT CONSTANT MSB
# T{ MSB BITSSET? -> 0 0 }T

T{ 0S 2* -> 0S }T
T{ 1 2* -> 2 }T
T{ 4000 2* -> 8000 }T
T{ 1S 2* 1 XOR -> 1S }T
T{ MSB 2* -> 0S }T

T{ 0S 2/ -> 0S }T
T{ 1 2/ -> 0 }T
T{ 4000 2/ -> 2000 }T
T{ 1S 2/ -> 1S }T            \ MSB PROPOGATED
T{ 1S 1 XOR 2/ -> 1S }T
T{ MSB 2/ MSB AND -> MSB }T

T{ 1 0 LSHIFT -> 1 }T
T{ 1 1 LSHIFT -> 2 }T
T{ 1 2 LSHIFT -> 4 }T
# T{ 1 F LSHIFT -> 8000 }T         \ BIGGEST GUARANTEED SHIFT
T{ 1S 1 LSHIFT 1 XOR -> 1S }T
T{ MSB 1 LSHIFT -> 0 }T

T{ 1 0 RSHIFT -> 1 }T
T{ 1 1 RSHIFT -> 0 }T
T{ 2 1 RSHIFT -> 1 }T
T{ 4 2 RSHIFT -> 1 }T
# T{ 8000 F RSHIFT -> 1 }T         \ BIGGEST
T{ MSB 1 RSHIFT MSB AND -> 0 }T      \ RSHIFT ZERO FILLS MSBS
T{ MSB 1 RSHIFT 2* -> MSB }T

        """

    def test_COMPARISONS(self):
        e = FORTH.Engine(self.COMPARISONS, **self.options)
        assert e.root.test["f"] == 0

    COMPARISONS = r"""

0    CONSTANT 0S
0 INVERT CONSTANT 1S
1S 1 RSHIFT INVERT CONSTANT MSB
T{ : BITSSET? IF 0 0 ELSE 0 THEN ; -> }T

( )

T{ 0 0= -> <TRUE> }T
T{ 1 0= -> <FALSE> }T
T{ 2 0= -> <FALSE> }T
T{ -1 0= -> <FALSE> }T

T{ 0 0 = -> <TRUE> }T
T{ 1 1 = -> <TRUE> }T
T{ -1 -1 = -> <TRUE> }T
T{ 1 0 = -> <FALSE> }T
T{ -1 0 = -> <FALSE> }T
T{ 0 1 = -> <FALSE> }T
T{ 0 -1 = -> <FALSE> }T

T{ 0 0< -> <FALSE> }T
T{ -1 0< -> <TRUE> }T
T{ 1 0< -> <FALSE> }T

T{ 0 1 < -> <TRUE> }T
T{ 1 2 < -> <TRUE> }T
T{ -1 0 < -> <TRUE> }T
T{ -1 1 < -> <TRUE> }T
T{ 0 0 < -> <FALSE> }T
T{ 1 1 < -> <FALSE> }T
T{ 1 0 < -> <FALSE> }T
T{ 2 1 < -> <FALSE> }T
T{ 0 -1 < -> <FALSE> }T
T{ 1 -1 < -> <FALSE> }T

T{ 0 1 > -> <FALSE> }T
T{ 1 2 > -> <FALSE> }T
T{ -1 0 > -> <FALSE> }T
T{ -1 1 > -> <FALSE> }T
T{ 0 0 > -> <FALSE> }T
T{ 1 1 > -> <FALSE> }T
T{ 1 0 > -> <TRUE> }T
T{ 2 1 > -> <TRUE> }T
T{ 0 -1 > -> <TRUE> }T
T{ 1 -1 > -> <TRUE> }T

T{ 0 1 U< -> <TRUE> }T
T{ 1 2 U< -> <TRUE> }T
T{ 0 0 U< -> <FALSE> }T
T{ 1 1 U< -> <FALSE> }T
T{ 1 0 U< -> <FALSE> }T
T{ 2 1 U< -> <FALSE> }T

T{ 0 1 MIN -> 0 }T
T{ 1 2 MIN -> 1 }T
T{ -1 0 MIN -> -1 }T
T{ -1 1 MIN -> -1 }T
T{ 0 0 MIN -> 0 }T
T{ 1 1 MIN -> 1 }T
T{ 1 0 MIN -> 0 }T
T{ 2 1 MIN -> 1 }T
T{ 0 -1 MIN -> -1 }T
T{ 1 -1 MIN -> -1 }T

T{ 0 1 MAX -> 1 }T
T{ 1 2 MAX -> 2 }T
T{ -1 0 MAX -> 0 }T
T{ -1 1 MAX -> 1 }T
T{ 0 0 MAX -> 0 }T
T{ 1 1 MAX -> 1 }T
T{ 1 0 MAX -> 1 }T
T{ 2 1 MAX -> 2 }T
T{ 0 -1 MAX -> 0 }T
T{ 1 -1 MAX -> 1 }T

        """

    def test_STACK_OPS(self):
        e = FORTH.Engine(self.STACK_OPS, **self.options)
        assert e.root.test["f"] == 0

    STACK_OPS = r"""

T{ 1 2 2DROP -> }T
T{ 1 2 2DUP -> 1 2 1 2 }T
T{ 1 2 3 4 2OVER -> 1 2 3 4 1 2 }T
T{ 1 2 3 4 2SWAP -> 3 4 1 2 }T
T{ 0 ?DUP -> 0 }T
T{ 1 ?DUP -> 1 1 }T
T{ -1 ?DUP -> -1 -1 }T
T{ DEPTH -> 0 }T
T{ 0 DEPTH -> 0 1 }T
T{ 0 1 DEPTH -> 0 1 2 }T
T{ 0 DROP -> }T
T{ 1 2 DROP -> 1 }T
T{ 1 DUP -> 1 1 }T
T{ 1 2 OVER -> 1 2 1 }T
T{ 1 2 3 ROT -> 2 3 1 }T
T{ 1 2 SWAP -> 2 1 }T

    """

    def test_RETURN_STACK(self):
        e = FORTH.Engine(self.RETURN_STACK, **self.options)
        assert e.root.test["f"] == 0

    RETURN_STACK = r"""

0 CONSTANT 0S
0 INVERT CONSTANT 1S

( )

T{ : GR1 >R R> ; -> }T
T{ : GR2 >R R@ R> DROP ; -> }T
T{ 123 GR1 -> 123 }T
T{ 123 GR2 -> 123 }T
T{ 1S GR1 -> 1S }T   ( RETURN STACK HOLDS CELLS )

    """

    def test_ADD_SUBTRACT(self):
        e = FORTH.Engine(self.ADD_SUBTRACT, **self.options)
        assert e.root.test["f"] == 0

    ADD_SUBTRACT = r"""

T{ 0 5 + -> 5 }T
T{ 5 0 + -> 5 }T
T{ 0 -5 + -> -5 }T
T{ -5 0 + -> -5 }T
T{ 1 2 + -> 3 }T
T{ 1 -2 + -> -1 }T
T{ -1 2 + -> 1 }T
T{ -1 -2 + -> -3 }T
T{ -1 1 + -> 0 }T
# T{ MID-UINT 1 + -> MID-UINT+1 }T

T{ 0 5 - -> -5 }T
T{ 5 0 - -> 5 }T
T{ 0 -5 - -> 5 }T
T{ -5 0 - -> -5 }T
T{ 1 2 - -> -1 }T
T{ 1 -2 - -> 3 }T
T{ -1 2 - -> -3 }T
T{ -1 -2 - -> 1 }T
T{ 0 1 - -> -1 }T
# T{ MID-UINT+1 1 - -> MID-UINT }T

T{ 0 1+ -> 1 }T
T{ -1 1+ -> 0 }T
T{ 1 1+ -> 2 }T
# T{ MID-UINT 1+ -> MID-UINT+1 }T

T{ 2 1- -> 1 }T
T{ 1 1- -> 0 }T
T{ 0 1- -> -1 }T
# T{ MID-UINT+1 1- -> MID-UINT }T

T{ 0 NEGATE -> 0 }T
T{ 1 NEGATE -> -1 }T
T{ -1 NEGATE -> 1 }T
T{ 2 NEGATE -> -2 }T
T{ -2 NEGATE -> 2 }T

T{ 0 ABS -> 0 }T
T{ 1 ABS -> 1 }T
T{ -1 ABS -> 1 }T
# T{ MIN-INT ABS -> MID-UINT+1 }T

    """

    def test_MULTIPLY(self):
        e = FORTH.Engine(self.MULTIPLY, **self.options)
        assert e.root.test["f"] == 0

    MULTIPLY = r"""

# T{ 0 S>D -> 0 0 }T
# T{ 1 S>D -> 1 0 }T
# T{ 2 S>D -> 2 0 }T
# T{ -1 S>D -> -1 -1 }T
# T{ -2 S>D -> -2 -1 }T
# T{ MIN-INT S>D -> MIN-INT -1 }T
# T{ MAX-INT S>D -> MAX-INT 0 }T

# T{ 0 0 M* -> 0 S>D }T
# T{ 0 1 M* -> 0 S>D }T
# T{ 1 0 M* -> 0 S>D }T
# T{ 1 2 M* -> 2 S>D }T
# T{ 2 1 M* -> 2 S>D }T
# T{ 3 3 M* -> 9 S>D }T
# T{ -3 3 M* -> -9 S>D }T
# T{ 3 -3 M* -> -9 S>D }T
# T{ -3 -3 M* -> 9 S>D }T
# T{ 0 MIN-INT M* -> 0 S>D }T
# T{ 1 MIN-INT M* -> MIN-INT S>D }T
# T{ 2 MIN-INT M* -> 0 1S }T
# T{ 0 MAX-INT M* -> 0 S>D }T
# T{ 1 MAX-INT M* -> MAX-INT S>D }T
# T{ 2 MAX-INT M* -> MAX-INT 1 LSHIFT 0 }T
# T{ MIN-INT MIN-INT M* -> 0 MSB 1 RSHIFT }T
# T{ MAX-INT MIN-INT M* -> MSB MSB 2/ }T
# T{ MAX-INT MAX-INT M* -> 1 MSB 2/ INVERT }T

T{ 0 0 * -> 0 }T            \ TEST IDENTITIES
T{ 0 1 * -> 0 }T
T{ 1 0 * -> 0 }T
T{ 1 2 * -> 2 }T
T{ 2 1 * -> 2 }T
T{ 3 3 * -> 9 }T
T{ -3 3 * -> -9 }T
T{ 3 -3 * -> -9 }T
T{ -3 -3 * -> 9 }T

# T{ MID-UINT+1 1 RSHIFT 2 * -> MID-UINT+1 }T
# T{ MID-UINT+1 2 RSHIFT 4 * -> MID-UINT+1 }T
# T{ MID-UINT+1 1 RSHIFT MID-UINT+1 OR 2 * -> MID-UINT+1 }T

# T{ 0 0 UM* -> 0 0 }T
# T{ 0 1 UM* -> 0 0 }T
# T{ 1 0 UM* -> 0 0 }T
# T{ 1 2 UM* -> 2 0 }T
# T{ 2 1 UM* -> 2 0 }T
# T{ 3 3 UM* -> 9 0 }T

# T{ MID-UINT+1 1 RSHIFT 2 UM* -> MID-UINT+1 0 }T
# T{ MID-UINT+1 2 UM* -> 0 1 }T
# T{ MID-UINT+1 4 UM* -> 0 2 }T
# T{ 1S 2 UM* -> 1S 1 LSHIFT 1 }T
# T{ MAX-UINT MAX-UINT UM* -> 1 1 INVERT }T

    """

    def test_HERE(self):
        e = FORTH.Engine(self.HERE, **self.options)
        assert e.root.test["f"] == 0

    HERE = r"""

0 CONSTANT 0S
0 INVERT CONSTANT 1S

( )

HERE 1 ALLOT
HERE
CONSTANT 2NDA
CONSTANT 1STA
T{ 1STA 2NDA U< -> <TRUE> }T      \ HERE MUST GROW WITH ALLOT
T{ 1STA 1+ -> 2NDA }T         \ ... BY ONE ADDRESS UNIT
( MISSING TEST: NEGATIVE ALLOT )

\ Added by GWJ so that ALIGN can be used before , (comma) is tested
1 ALIGNED CONSTANT ALMNT   \ -- 1|2|4|8 for 8|16|32|64 bit alignment
ALIGN
T{ HERE 1 ALLOT ALIGN HERE SWAP - ALMNT = -> <TRUE> }T
\ End of extra test

HERE 1 ,
HERE 2 ,
CONSTANT 2ND
CONSTANT 1ST
T{ 1ST 2ND U< -> <TRUE> }T         \ HERE MUST GROW WITH ALLOT
T{ 1ST CELL+ -> 2ND }T         \ ... BY ONE CELL
T{ 1ST 1 CELLS + -> 2ND }T
T{ 1ST @ 2ND @ -> 1 2 }T
T{ 5 1ST ! -> }T
T{ 1ST @ 2ND @ -> 5 2 }T
T{ 6 2ND ! -> }T
T{ 1ST @ 2ND @ -> 5 6 }T

( TODO

T{ 1ST 2@ -> 6 5 }T
{ 2 1 1ST 2! -> }T
T{ 1ST 2@ -> 2 1 }T
T{ 1S 1ST !  1ST @ -> 1S }T      \ CAN STORE CELL-WIDE VALUE

)

HERE 1 C,
HERE 2 C,
CONSTANT 2NDC
CONSTANT 1STC
T{ 1STC 2NDC U< -> <TRUE> }T      \ HERE MUST GROW WITH ALLOT
T{ 1STC CHAR+ -> 2NDC }T         \ ... BY ONE CHAR
T{ 1STC 1 CHARS + -> 2NDC }T
T{ 1STC C@ 2NDC C@ -> 1 2 }T
T{ 3 1STC C! -> }T
T{ 1STC C@ 2NDC C@ -> 3 2 }T
T{ 4 2NDC C! -> }T
T{ 1STC C@ 2NDC C@ -> 3 4 }T

ALIGN 1 ALLOT HERE ALIGN HERE 3 CELLS ALLOT
CONSTANT A-ADDR  CONSTANT UA-ADDR
T{ UA-ADDR ALIGNED -> A-ADDR }T
T{    1 A-ADDR C!  A-ADDR C@ ->    1 }T
T{ 1234 A-ADDR  !  A-ADDR  @ -> 1234 }T
T{ 123 456 A-ADDR 2!  A-ADDR 2@ -> 123 456 }T
T{ 2 A-ADDR CHAR+ C!  A-ADDR CHAR+ C@ -> 2 }T
T{ 3 A-ADDR CELL+ C!  A-ADDR CELL+ C@ -> 3 }T
T{ 1234 A-ADDR CELL+ !  A-ADDR CELL+ @ -> 1234 }T
T{ 123 456 A-ADDR CELL+ 2!  A-ADDR CELL+ 2@ -> 123 456 }T


#
# TODO (BITS does not terminate)
#
# 1S 1 RSHIFT INVERT CONSTANT MSB
#
# : BITS ( X -- U )
#    0 SWAP BEGIN DUP WHILE DUP MSB AND IF >R 1+ R> THEN 2* REPEAT DROP ;
# ( CHARACTERS >= 1 AU, <= SIZE OF CELL, >= 8 BITS )
# T{ 1 CHARS 1 < -> <FALSE> }T
# T{ 1 CHARS 1 CELLS > -> <FALSE> }T
#
# ( CELLS >= 1 AU, INTEGRAL MULTIPLE OF CHAR SIZE, >= 16 BITS )
# T{ 1 CELLS 1 < -> <FALSE> }T
# T{ 1 CELLS 1 CHARS MOD -> 0 }T
#
# T{ 1S BITS 10 < -> <FALSE> }T
#

    """

    def test_COMPILE(self):
        e = FORTH.Engine(self.COMPILE, **self.options)
        assert e.root.test["f"] == 0


    COMPILE = r""" """

    FIXME_COMPILE = r"""

T{ : GT1 123 ; -> }T
T{ ' GT1 EXECUTE -> 123 }T
T{ : GT2 ['] GT1 ; IMMEDIATE -> }T
T{ GT2 EXECUTE -> 123 }T
HERE 3 C, CHAR G C, CHAR T C, CHAR 1 C, CONSTANT GT1STRING
HERE 3 C, CHAR G C, CHAR T C, CHAR 2 C, CONSTANT GT2STRING
T{ GT1STRING FIND -> ' GT1 -1 }T
T{ GT2STRING FIND -> ' GT2 1 }T
( HOW TO SEARCH FOR NON-EXISTENT WORD? )
T{ : GT3 GT2 LITERAL ; -> }T
T{ GT3 -> ' GT1 }T
T{ GT1STRING COUNT -> GT1STRING CHAR+ 3 }T

# TODO
#
# T{ : GT4 POSTPONE GT1 ; IMMEDIATE -> }T
# T{ : GT5 GT4 ; -> }T
# T{ GT5 -> 123 }T

T{ : GT6 345 ; IMMEDIATE -> }T
T{ : GT7 POSTPONE GT6 ; -> }T
T{ GT7 -> 345 }T

# TODO
#
# T{ : GT8 STATE @ ; IMMEDIATE -> }T
# T{ GT8 -> 0 }T
# T{ : GT9 GT8 LITERAL ; -> }T
# T{ GT9 0= -> <FALSE> }T

    """

    def test_IF_BEGIN_WHILE_RECURSE(self):
        e = FORTH.Engine(self.IF_BEGIN_WHILE_RECURSE, **self.options)
        assert e.root.test["f"] == 0

    IF_BEGIN_WHILE_RECURSE = r"""

T{ : GI1 IF 123 THEN ; -> }T
T{ : GI2 IF 123 ELSE 234 THEN ; -> }T
T{ 0 GI1 -> }T
T{ 1 GI1 -> 123 }T
T{ -1 GI1 -> 123 }T
T{ 0 GI2 -> 234 }T
T{ 1 GI2 -> 123 }T
T{ -1 GI1 -> 123 }T

T{ : GI3 BEGIN DUP 5 < WHILE DUP 1+ REPEAT ; -> }T
T{ 0 GI3 -> 0 1 2 3 4 5 }T
T{ 4 GI3 -> 4 5 }T
T{ 5 GI3 -> 5 }T
T{ 6 GI3 -> 6 }T

T{ : GI4 BEGIN DUP 1+ DUP 5 > UNTIL ; -> }T
T{ 3 GI4 -> 3 4 5 6 }T
T{ 5 GI4 -> 5 6 }T
T{ 6 GI4 -> 6 7 }T

# TODO
#
# T{ : GI5 BEGIN DUP 2 >
#          WHILE DUP 5 < WHILE DUP 1+ REPEAT 123 ELSE 345 THEN ; -> }T
# T{ 1 GI5 -> 1 345 }T
# T{ 2 GI5 -> 2 345 }T
# T{ 3 GI5 -> 3 4 5 123 }T
# T{ 4 GI5 -> 4 5 123 }T
# T{ 5 GI5 -> 5 123 }T

# TODO
#
# T{ : GI6 ( N -- 0,1,..N ) DUP IF DUP >R 1- RECURSE R> THEN ; -> }T
# T{ 0 GI6 -> 0 }T
# T{ 1 GI6 -> 0 1 }T
# T{ 2 GI6 -> 0 1 2 }T
# T{ 3 GI6 -> 0 1 2 3 }T
# T{ 4 GI6 -> 0 1 2 3 4 }T

    """

    def test_DO_LOOP(self):
        e = FORTH.Engine(self.DO_LOOP, **self.options)
        assert e.root.test["f"] == 0

    DO_LOOP = r"""

T{ : GD1 DO I LOOP ; -> }T
T{ 4 1 GD1 -> 1 2 3 }T
T{ 2 -1 GD1 -> -1 0 1 }T

T{ : GD2 DO I -1 +LOOP ; -> }T
T{ 1 4 GD2 -> 4 3 2 1 }T
T{ -1 2 GD2 -> 2 1 0 -1 }T

T{ : GD3 DO 1 0 DO J LOOP LOOP ; -> }T
T{ 4 1 GD3 -> 1 2 3 }T
T{ 2 -1 GD3 -> -1 0 1 }T

T{ : GD4 DO 1 0 DO J LOOP -1 +LOOP ; -> }T
T{ 1 4 GD4 -> 4 3 2 1 }T
T{ -1 2 GD4 -> 2 1 0 -1 }T

T{ : GD5 123 SWAP 0 DO I 4 > IF DROP 234 LEAVE THEN LOOP ; -> }T
T{ 1 GD5 -> 123 }T
T{ 5 GD5 -> 123 }T
T{ 6 GD5 -> 234 }T

# TODO
#
# T{ : GD6  ( PAT: T{0 0},{0 0}{1 0}{1 1},{0 0}{1 0}{1 1}{2 0}{2 1}{2 2} )
#    0 SWAP 0 DO
#       I 1+ 0 DO I J + 3 = IF I UNLOOP I UNLOOP EXIT THEN 1+ LOOP
#     LOOP ; -> }T
# T{ 1 GD6 -> 1 }T
# T{ 2 GD6 -> 3 }T
# T{ 3 GD6 -> 4 1 2 }T

    """

    def test_DEFINING_WORDS(self):
        e = FORTH.Engine(self.DEFINING_WORDS, **self.options)
        assert e.root.test["f"] == 0

    XXXDEFINING_WORDS = r""" """

    DEFINING_WORDS = r"""

T{ 123 CONSTANT X123 -> }T
T{ X123 -> 123 }T
T{ : EQU CONSTANT ; -> }T
T{ X123 EQU Y123 -> }T
T{ Y123 -> 123 }T

T{ VARIABLE V1 -> }T
T{ 123 V1 ! -> }T
T{ V1 @ -> 123 }T

# TODO
#
# T{ : NOP : POSTPONE ; ; -> }T
# T{ NOP NOP1 NOP NOP2 -> }T
# T{ NOP1 -> }T
# T{ NOP2 -> }T
(
T{ : DOES1 DOES> @ 1 + ; -> }T
T{ : DOES2 DOES> @ 2 + ; -> }T
T{ CREATE CR1 -> }T
T{ CR1 -> HERE }T
T{ ' CR1 >BODY -> HERE }T
T{ 1 , -> }T
T{ CR1 @ -> 1 }T
)
# TODO
#
# T{ DOES1 -> }T
# T{ CR1 -> 2 }T
# T{ DOES2 -> }T
# T{ CR1 -> 3 }T

# TODO - Not sure double does> is needed...
#
# T{ : WEIRD: CREATE DOES> 1 + DOES> 2 + ; -> }T
# T{ WEIRD: W1 -> }T
# T{ ' W1 >BODY -> HERE }T
# T{ W1 -> HERE 1 + }T
# T{ W1 -> HERE 2 + }T

    """

    def test_EVALUATE(self):
        e = FORTH.Engine(self.EVALUATE, **self.options)
        assert e.root.test["f"] == 0

    EVALUATE = r"""

( TODO

: GE1 S" 123" ; IMMEDIATE
: GE2 S" 123 1+" ; IMMEDIATE
: GE3 S" : GE4 345 ;" ;
: GE5 EVALUATE ; IMMEDIATE

T{ GE1 EVALUATE -> 123 }T         \ TEST EVALUATE IN INTERP. STATE
T{ GE2 EVALUATE -> 124 }T
T{ GE3 EVALUATE -> }T
T{ GE4 -> 345 }T

T{ : GE6 GE1 GE5 ; -> }T         \ TEST EVALUATE IN COMPILE STATE
T{ GE6 -> 123 }T
T{ : GE7 GE2 GE5 ; -> }T
T{ GE7 -> 124 }T

)

    """

    def test_SOURCE(self):
        e = FORTH.Engine(self.SOURCE, **self.options)
        assert e.root.test["f"] == 0

    SOURCE = r"""

( TODO

: GS1 S" SOURCE" 2DUP EVALUATE
       >R SWAP >R = R> R> = ;
T{ GS1 -> <TRUE> <TRUE> }T

VARIABLE SCANS
: RESCAN?  -1 SCANS +! SCANS @ IF 0 >IN ! THEN ;

T{ 2 SCANS !
345 RESCAN?
-> 345 345 }T

: GS2  5 SCANS ! S" 123 RESCAN?" EVALUATE ;
T{ GS2 -> 123 123 123 123 123 }T

: GS3 WORD COUNT SWAP C@ ;
T{ BL GS3 HELLO -> 5 CHAR H }T
T{ CHAR " GS3 GOODBYE" -> 7 CHAR G }T
T{ BL GS3
DROP -> 0 }T            \ BLANK LINE RETURN ZERO-LENGTH STRING

: GS4 SOURCE >IN ! DROP ;
T{ GS4 123 456
-> }T

)

    """

    def test_FILL_MOVE(self):
        e = FORTH.Engine(self.FILL_MOVE, **self.options)
        assert e.root.test["f"] == 0

    FILL_MOVE = r"""

CREATE FBUF 00 C, 00 C, 00 C,
CREATE SBUF 12 C, 34 C, 56 C,
: SEEBUF FBUF C@  FBUF CHAR+ C@  FBUF CHAR+ CHAR+ C@ ;

T{ FBUF 0 20 FILL -> }T
T{ SEEBUF -> 00 00 00 }T

T{ FBUF 1 20 FILL -> }T
T{ SEEBUF -> 20 00 00 }T

T{ FBUF 3 20 FILL -> }T
T{ SEEBUF -> 20 20 20 }T

T{ FBUF FBUF 3 CHARS MOVE -> }T      \ BIZARRE SPECIAL CASE
T{ SEEBUF -> 20 20 20 }T

T{ SBUF FBUF 0 CHARS MOVE -> }T
T{ SEEBUF -> 20 20 20 }T

T{ SBUF FBUF 1 CHARS MOVE -> }T
T{ SEEBUF -> 12 20 20 }T

T{ SBUF FBUF 3 CHARS MOVE -> }T
T{ SEEBUF -> 12 34 56 }T

( TODO

T{ FBUF FBUF CHAR+ 2 CHARS MOVE -> }T
T{ SEEBUF -> 12 12 34 }T

T{ FBUF CHAR+ FBUF 2 CHARS MOVE -> }T
T{ SEEBUF -> 12 34 34 }T

)

    """


from cubed4th import FORTH

try:
    from icecream import ic
except ImportError:  # Graceful fallback if IceCream isn't installed.
    ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)  # noqa

builtins = __import__("builtins")
setattr(builtins, "ic", ic)

#
# \ From: John Hayes S1I
# \ Subject: core.fr
# \ Date: Mon, 27 Nov 95 13:10
#
# \ (C) 1995 JOHNS HOPKINS UNIVERSITY / APPLIED PHYSICS LABORATORY
# \ MAY BE DISTRIBUTED FREELY AS LONG AS THIS COPYRIGHT NOTICE REMAINS.
# \ VERSION 1.2
# \ THIS PROGRAM TESTS THE CORE WORDS OF AN ANS FORTH SYSTEM.
# \ THE PROGRAM ASSUMES A TWO'S COMPLEMENT IMPLEMENTATION WHERE
# \ THE RANGE OF SIGNED NUMBERS IS -2^(N-1) ... 2^(N-1)-1 AND
# \ THE RANGE OF UNSIGNED NUMBERS IS 0 ... 2^(N)-1.
# \ I HAVEN'T FIGURED OUT HOW TO TEST KEY, QUIT, ABORT, OR ABORT"...
# \ I ALSO HAVEN'T THOUGHT OF A WAY TO TEST ENVIRONMENT?...
#
