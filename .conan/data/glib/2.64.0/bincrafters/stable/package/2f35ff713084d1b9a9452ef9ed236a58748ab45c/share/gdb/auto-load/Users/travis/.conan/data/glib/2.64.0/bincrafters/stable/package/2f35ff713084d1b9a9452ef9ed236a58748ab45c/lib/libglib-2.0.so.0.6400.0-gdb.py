import sys
import gdb

# Update module path.
dir_ = '/Users/travis/.conan/data/glib/2.64.0/bincrafters/stable/package/2f35ff713084d1b9a9452ef9ed236a58748ab45c/share/glib-2.0/gdb'
if not dir_ in sys.path:
    sys.path.insert(0, dir_)

from glib_gdb import register
register (gdb.current_objfile ())
