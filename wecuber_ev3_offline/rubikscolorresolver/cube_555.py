corner_tuples = (
    (1, 26, 105),
    (5, 101, 80),
    (21, 51, 30),
    (25, 76, 55),
    (126, 50, 71),
    (130, 75, 96),
    (146, 125, 46),
    (150, 100, 121),
)

edge_orbit_id = {
    2: 0,
    3: 1,
    4: 0,
    6: 0,
    11: 1,
    16: 0,
    10: 0,
    15: 1,
    20: 0,
    22: 0,
    23: 1,
    24: 0,  # Upper
    27: 0,
    28: 1,
    29: 0,
    31: 0,
    36: 1,
    41: 0,
    35: 0,
    40: 1,
    45: 0,
    47: 0,
    48: 1,
    49: 0,  # Left
    52: 0,
    53: 1,
    54: 0,
    56: 0,
    61: 1,
    66: 0,
    60: 0,
    65: 1,
    70: 0,
    72: 0,
    73: 1,
    74: 0,  # Front
    77: 0,
    78: 1,
    79: 0,
    81: 0,
    86: 1,
    91: 0,
    85: 0,
    90: 1,
    95: 0,
    97: 0,
    98: 1,
    99: 0,  # Right
    102: 0,
    103: 1,
    104: 0,
    106: 0,
    111: 1,
    116: 0,
    110: 0,
    115: 1,
    120: 0,
    122: 0,
    123: 1,
    124: 0,  # Back
    127: 0,
    128: 1,
    129: 0,
    131: 0,
    136: 1,
    141: 0,
    135: 0,
    140: 1,
    145: 0,
    147: 0,
    148: 1,
    149: 0,  # Down
}


center_groups = (
    ("centers", (13, 38, 63, 88, 113, 138)),
    (
        "x-centers",
        (
            7,
            9,
            13,
            17,
            19,  # Upper
            32,
            34,
            38,
            42,
            44,  # Left
            57,
            59,
            63,
            67,
            69,  # Front
            82,
            84,
            88,
            92,
            94,  # Right
            107,
            109,
            113,
            117,
            119,  # Back
            132,
            134,
            138,
            142,
            144,  # Down
        ),
    ),
    (
        "t-centers",
        (
            8,
            12,
            13,
            14,
            18,  # Upper
            33,
            37,
            38,
            39,
            43,  # Left
            58,
            62,
            63,
            64,
            68,  # Front
            83,
            87,
            88,
            89,
            93,  # Right
            108,
            112,
            113,
            114,
            118,  # Back
            133,
            137,
            138,
            139,
            143,  # Down
        ),
    ),
)
