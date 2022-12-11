# ============================================================================ #

# First paragraph f"""{FP_}text{_FP}""".
FP_ = """<mark class="first-paragraph">"""
_FP = """</mark>"""

# Non-breaking paragraph f"""{NBP_}text{_NBP}""".
NBP_ = """<mark class="non-breaking-paragraph">"""
_NBP = """</mark>"""

# Mini name f"""{MN_}text{_MN}"""..
MN_ = """<mark class="mini-name">"""
_MN = """</mark>"""

# Tooltip f"""{TT_}text{_TT_}description{_TT}""".
TT_ = """<mark class="tooltip">"""
_TT_ = """<span class="tip">"""
_TT = """</span></mark>"""

# Link f"""{A_}url{_A_}text{_A}""".
A_ = """<a href=\""""
_A_ = """\">"""
_A = """</a>"""

# Italic f"""{I_}text{_i}""".
I_ = """<i>"""
_I = """</i>"""


# Italic link f"""{IA_}url{_IA_}text{_IA}""".
IA_ = f"""{I_}{A_}"""
_IA_ = f"""{_A_}"""
_IA = f"""{_I}{_A}"""

# Bold f"""{B_}text{_B}""".
B_ = """<b>"""
_B = """</b>"""

# ============================================================================ #

THREE_D_PRINTING = """3D printing is the construction of physical objects from a digital 3D model file."""