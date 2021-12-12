![cubed4th Logo](/images/transparent_half.png)

# cubed4th

FORTH^3, relicensed with permission from https://github.com/p-unity

# -- THE FORTH-79 STANDARD --

The folling text was performed by OCR and contain mistakes.

# WORDS

NB: The words come from the FORTH-79 standard.  For the 2.0 release all the words that make sense will be implemented.  Its not currently noted anywhere which words have no implemention.

## Stack Manipulation

|   Name    |   Stack Effects   |   Description |
|   --------    | -------   | -------   |
|   DUP |   ( n - n n ) |   Duplicate top of stack  |
|   DROP    |   ( n - ) |   Discard Top of Stack    |
|   SWAP    |   ( n1 n2 - n2 n1 )   |   Exchange top two stack items    |
|   OVER    |   ( n1 n2 - n1 n2 n1 )    |   Make a copy of second item on top   |
|   ROT |   ( n1 n2 n3 - n2 n3 n1 ) |   Rotate third item to top "rote" |
|   [PICK](https://forth-standard.org/standard/core/PICK)   |   ( n1 - n2 ) |   Copy n1-th item to top (thus 1 PICK = DUP, 2 PICK = OVER)   |
|   ROLL    |   (n - )  |   Rotate the n1 - th item to top (thus 2 ROLL = SWAP, 3 ROLL = ROT    |
|   ?DUP    |   ( n - n (n) )   |   Dupliicate only if non-zero. "query-dup"    |
|   >R  |   ( n - ) |   Move top item to "return stack" for temporary storage (use caution). "to-r"     |
|   R>  |   ( - n ) |   Retrieve item from return stack. "r-from"   |
|   R@  |   ( - n ) |   Copy top of return stack onto stack. "r-fetch"  |
|   DEPTH   |   ( - n ) |   Count number of items in stack  |

# DEFINITIONS OF TERMS

These definitions, when in lower  case, are terms used within  this
Standard.  They present terms as specifically used within FORTH.

## A

### address, ~~byte~~ hashable object

An ~~unsigned  number~~ hashable object that locates an ~~8-bit byte~~ object in a  standard
~~FORTH  address space over {0..65,535}~~ Python dictionary.  ~~It  may   be a  native
machine address  or a representation  on  a  virtual  machine,
locating the  'addr-th' byte  within  the virtual byte address
space.~~  Address arithmetic is ~~modulo 65,536 without overflow~~ infinite positive, infinite negative and any string.

### address, compilation

The numerical  value  equivalent to a  FORTH word  definition,
which   is  compiled   for  that   definition.   The   address
interpreter  uses  this  value  to  locate  the  machine  code
corresponding to  each definition.   (May also  be called  the
code field address.)

### address, native machine

The natural address representation of the host computer.

### address, parameter field

The address of the first byte of memory associated with a word
definition  for the  storage of  compilation addresses  (in a
colon-definition), numeric data and text characters.

### arithmetic

~~All integer arithmetic is performed  with signed 16 or 32  bit
two's complement results, unless noted.~~  Numbers follow python rules
with integers being Decimal class, floating points being infinite procession
with support for complex numbers.  The to_number function shown here details
the various modes available to color4th:

```python

    def to_number(e, t, c, token):

        if not isinstance(token, str):
            return (True, token)

        if not token[0] in e.digits:
            return (False, None)

        if token in e.root.words or token in t.words:
            return (False, None)

        token = token.replace("_", "")

        base = t.base
        if token[0] == "#":
            token = token[1:]
        elif token[0] == "$":
            base = 16
            token = token[1:]
        elif token[0] == "%":
            base = 2
            token = token[1:]

        if token[0] == "-":
            if len(token) == 1:
                return (False, None)
            if not token[1].isdigit():
                return (False, None)

        if "j" in token:
            return (True, complex(token))
        else:
            if "." in token:
                if base == 10:
                    return (True, Decimal(token))
                else:
                    return (True, Decimal(int(token, base)))
            else:
                return (True, int(token, base))

```

## B

### block

The  unit  of  data from  mass  storage,  referenced by  block
number.  A  block must  contain 1024  bytes regardless  of the
minimum  data  unit  read/written  from  mass  storage.    The
translation from block number to device and physical record is
a function of the implementation.

### block buffer

A memory area where a mass storage block is maintained.

### byte

An assembly  of 8  bits.  In  reference to  memory, it  is the
storage capacity for 8 bits.

## C

### cell

A 16-bit memory  location.  The n-th  cell contains the  2n-th
and (2n+1)-th byte of the FORTH address space.  The byte order
is presently unspecified.

### character

A 7-bit  number which  represents a  terminal character.   The
ASCII character set is considered standard.  When contained in
a larger field, the higher order bits are zero.

### compilation

The action of accepting text  words from the input stream  and
placing   corresponding   compilation  addresses   in   a  new
dictionary entry.

## D

### defining word

A word that,  when executed, creates  a new dictionary  entry.
The new  word name  is taken  from the  input stream.   If the
input stream is exhausted before the new name is available, an
error condition exists.  Common defining words are:
:  CONSTANT  CREATE

### definition

See 'word definition'.

### dictionary

A structure of  word definitions  in  a computer memory.    In
systems with  a text  interpreter, the  dictionary entries are
organized in  vocabularies to  enable location  by name.   The
dictionary is extensible, growing toward high memory.

## E

### equivalent execution

For the  execution of  a standard  program, a  set of non-tine
dependent  inputs  will produce  the  same non-time  dependent
outputs on any FORTH Standard System with sufficient resources
to execute  the program.   Only standard  source code  will be
transportable.

### error condition

An exceptional condition which  requires action by the  system
other than the expected function.  Actions may be:

1.   ignore, and continue
2.   display a message
3.   execute a particular word
4.   interpret a block
5.   return control  to the text interpreter

A Standard System shall be  provided with a tabulation of  the
action  taken  for all  specified  error conditions.   General
error conditions:

1.   input stream exhausted before a required <name>.
2.   empty stack and full stack for the text interpreter.
3.   an unknown word, not a valid number for the text
interpreter.
4.   compilation of incorrectly nested conditionals.
5.   interpretation of words restricted to compilation.
6.   FORGETing within the system to a point that removes
a word required for correct execution.
7.   insufficient space remaining in the dictionary.

## F

### false

A zero number represents the false condition flag.

### flag

A number  that may have two logical states, zero and non-zero.
These  are  named  'true'  =  non-zero,  and  'false'  = zero.
Standard word definitions leave 1 for true, 0 for false.

## G

### glossary

A  set  of  word  definitions  given  in  a  natural  language
describing the corresponding computer execution action.

## H

## I

### immediate word

A  word  defined  to  automatically  execute  when encountered
during compilation, which handles exception cases to the usual
compilation.   See  IF LITERAL  ."  etc.

### input stream

A  sequence  of  characters  available  to  the  system,   for
processing  by  the   text  interpreter.   The   input  stream
conventionally may be taken from a terminal (via the  terminal
input buffer) and mass storage (via a block buffer).  >IN  and
BLK specify the input stream.  Words using or altering >IN and
BLK are responsible for  maintaining and restoring control  of
the input stream.

### interpreter, address

The (set of) word definitions which interprets (sequences  of)
FORTH compilation addresses  by executing the  word definition
specified for each one.

### interpreter, text

The (set of) word  definitions that repeatedly accepts  a word
name  from  the   input  stream,  locates   the  corresponding
dictionary  entry,  and  starts  the  address  interpreter  to
execute it.  Text in the input stream interpreted  as a number
leaves the corresponding  value on the   data stack.  When  in
the compile mode,  the addresses of  FORTH words are  compiled
into the  dictionary for  later interpretation  by the address
interpreter.  In this case, numbers are compiled, to be placed
on the data  stack when later  interpreted.  Numbers shall  be
accepted unsigned or negatively signed, according to BASE.

## J

## K

## L

### load

The  acceptance  of  text  from  a  mass  storage  device  and
execution   of  the   dictionary  definition   of  the   words
encountered.  This  is the  general method  for compilation of
new definitions into the dictionary.

## M

### mass storage

Data  is read  from mass  storage in  the form  of 1024  byte
blocks.  This data is  held in block buffers.   When indicated
as UPDATEd (modified) data will be ultimately written to  mass
storage.

## N

### number

When  values exist within a larger field, the high order  bits
are zero.  When stored in memory the byte order of a number is
unspecified.

### type range    minimum field

    bit  0..1  1
    character 0..1277
    byte 0..2558
    number    -32,768..32,76716
    positive number0..32,767 16
    unsigned numberO..65,535 16
    double number  -2,147,483,648..
       2,147,483,647    32
    positive double number   0..2,147,483,647    32
    unsigned double number   0..4,294,967,295    32

When represented on the stack, the higher 16-bits (with  sign)
of a double  number are most  accessible.  When in  memory the
higher 16-bits are at the lower address.  Storage extends over
four bytes toward high memory.  The byte order within each  16
-bit field is unspecified.

## O

### output, pictured

The use of numeric output primitives, which convert  numerical
values  into  text  strings.   The operators  are  used  in  a
sequence  which resembles a symbolic 'picture' of the  desired
text  format.    Conversion proceeds from low digit  to  high,
from high memory to low.

## P

### program

A  complete specification of execution to achieve  a  specific
function  (application  task) expressed in FORTH  source  code
form.

## Q

## R

### return

The   means  of  terminating  text  from  the  input   stream.
(Conventionally a null (ASCII 0) indicates end of text in  the
input  stream.   This character is left by  the  'return'  key
actuation  of the operator's terminal, as an absolute  stopper
to text interpretation.)

## S

### screen

Textual data  arranged for  editing.  By  convention, a screen
consists of  16 lines  (numbered 0  thru 15)  of 64 characters
each.  Screens usually contain program source text, but may be
used to view mass storage data.   The first  byte of  a screen
occupies the first byte of a mass storage block,  which is the
beginning point for text interpretation during a load.

### source definition

Text consisting of  word names suitable  for execution by  the
text interpreter.   Such text  is usually  arranged in screens
and maintained on a mass storage device.

### stack, data

A last in, first out list consisting of 16-bit binary  values.
This  stack  is  primarily used to  hold  intermediate  values
during  execution  of  word  definitions.   Stack  values  may
represent numbers, characters, addresses, boolean values, etc.

When the name 'stack' is used, it implies the data stack.

### stack, return

A last in, first out list which contains the machine addresses
of word definitions whose execution has not been completed  by
the address interpreter.  As a word definition passes  control
to  another  definition,  the return point is  placed  on  the
return stack.

The return stack may cautiously be used for other values, such
as   loop   control   parameters,   and   for   pointers   for
interpretation of text.

### string

A sequence of 8-bit bytes containing ASCII characters, located
in memory by an initial byte address and byte count.

## T

### transportability

This  term indicates that equivalent execution results when  a
program  is executed on other than the system on which it  was
created.  See 'equivalent execution'.

### true

A non-zero value represents the true condition flag.  Any non-
zero value will be accepted by a standard word as 'true';  all
standard words return one when leaving a ' true' flag.

## Q

## R

## S

## T

## U

### user area

An  area  in  memory  which  contains  the  storage  for  user
variables.

### variables, user

So  that the words of the FORTH vocabulary may  be  re-entrant
(to  different  users),  a copy of  each  system  variable  is
maintained in the user area.

## V

### vocabulary

An ordered list of word definitions.  Vocabulary lists are  an
advantage in reducing dictionary search time and in separating
different word definitions that may carry the sane name.

## W

### word

A sequence of characters terminated by at least one blank  (or
'return').   Words are usually obtained via the input  stream,
from a terminal or mass storage device.

### word definition

A   named   FORTH  execution  procedure  compiled   into   the
dictionary.  Its execution may be defined in terms of  machine
code, as a sequence of compilation addresses or other compiled
words.   If named, it nay be located by specifying  this  name
and the vocabulary in which it is located.

### word name

The  name  of  a  word definition.   Standard  names  must  be
distinguished by their length and first thirty-one characters,
and may not contain an ASCII null, blank, or 'return'.

### word set

A   group   of  FORTH  word  definitions  listed   by   common
characteristics.  The standard word sets consist of:

    Required Word Set
    Nucleus Words
    Interpreter Words
    Compiler Words
    Device Words

    Extension Word Sets
    32-bit Word Set
    Assembler Ward Set

Included as reference material only:
Reference Word Set

### word set, compiler

Words  which  add  new procedures to  the  dictionary  or  aid
compilation by adding compilation addresses or data structures
to the dictionary.

### word set, devices

Words  which  allow  access  to  mass  storage  and   computer
peripheral devices.

### word set, interpreter

Words  which  support  interpretation of text  input  from   a
terminal  or  mass  storage  by  execution  of   corresponding
dictionary entries, vocabularies, and terminal output.

### word set, nucleus

The FORTH words generally defined in machine  code that create
the  stacks  and fundamental stack  operators  (virtual  FORTH
machine).

### word set, reference

This set of words is provided as a reference document only, as
a  set of formerly standardized words and candidate words  for
standardization.

### word set, required

The  minimum words needed to compile and execute all  Standard
Programs.

### word, standard

A  named  FORTH procedure definition, formally   reviewed  and
accepted  by the Standards Team.  A serial  number  identifier
{100..999} indicates a Standard Word.  A functional alteration
of  a  Standard Word will require assignment of a  new  serial
number identifier.

The  serial number identifier has no required use, other  than
to  correlate  the definition name with  its  unique  Standard
definition.


## X

## Y

## Z







