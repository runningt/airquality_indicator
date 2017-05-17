from __future__ import absolute_import, division, print_function, unicode_literals
import builtins
import sys
if sys.version_info < (3,):
    BUILTIN_OPEN = '__builtin__.open'
else:
    BUILTIN_OPEN = 'builtins.open'
