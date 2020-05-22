import sys
import gdb

# Update module path.
dir_ = '/home/conan/.conan/data/glib/2.64.0/bincrafters/stable/package/f328e8721181dbb381ed842e289123010efd816c/share/glib-2.0/gdb'
if not dir_ in sys.path:
    sys.path.insert(0, dir_)

from glib_gdb import register
register (gdb.current_objfile ())
