import os.path


def newpath(raw):
   return os.path.expandvars(os.path.normpath(raw))


def newpathrel(raw, base = os.path.dirname(__file__)):
   return newpath(os.path.join(base, newpath(raw)))
