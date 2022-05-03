"""
Tuples for intermediate format serialization.
"""

CODE_ATTRIBUTES = (
    "co_argcount",
    "co_posonlyargcount",
    "co_kwonlyargcount",
    "co_nlocals",
    "co_stacksize",
    "co_flags",
    "co_code",
    "co_consts",
    "co_names",
    "co_varnames",
    "co_filename",
    "co_name",
    "co_firstlineno",
    "co_lnotab",
    "co_freevars",
    "co_cellvars"
)

ITERABLES = (
    'list',
    'tuple',
    'set',
    'frozenset',
    'bytearray',
)

PRIMITIVES = (
    'int',
    'float',
    'complex',
    'bool',
    'str',
    'bytes',
    'NoneType',
)

CODE_FIELD_NAME = "__code__"
GLOBALS_FIELD_NAME = "__globals__"
DEFAULTS_FIELD_NAME = "__defaults__"
CLOSURE_FIELD_NAME = "__closure__"
CODE_NAMES_FIELD_NAME = "co_names"
