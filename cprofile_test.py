"""Code to profile palingram.py"""

import cProfile
import palingram

cProfile.run(palingram.find_palingrams())
