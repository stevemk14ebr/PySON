# PySON
Simple class to convert a JSON string or Python dictionary into relational classes

I wrote this for personal use to deal with a rather large JSON string and it worked well.  That said I did not write it to follow any specification.


Help on module pyson:

NAME
    pyson

FILE
    g:\scripts\pyson\pyson.py

DESCRIPTION
    PySON:   Simple easy to use class to convert JSON string
             or Python dict into accessable classes/members.
             Tested on Python 2.7
             
    Date:    12-15-2018
    By:      zoomgod
    Version: 0.0001 serious alphaware
    
    Contact me:
    Unknown Cheats: https://www.unknowncheats.me/forum/members/146787.html
    GitHub: https://github.com/therealzoomgod

CLASSES
    __builtin__.object
        PySON
    exceptions.Exception(exceptions.BaseException)
        PySONException
    
    class PySON(__builtin__.object)
     |  Convert a JSON string or dictionary into class objects.
     |  
     |  Methods
     |  -------
     |  setValue    Set a value, raise exception if strict type checking is enabled
     |  getValue    Returns value or None
     |  getNames    Returns a list of member names
     |  getCount    Returns count of members
     |  getName     Returns member name class is based on
     |  getFQN      Returns full name reflecting the parent instances
     |  dump        Dump all FQN from here down to any file type object
     |  toJSON      Returns a JSON string reflecting current values including child members.
     |  toDict      Returns a dict object reflecting current values including child members.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, schema, parent=None, name='')
     |      Args:
     |      -----------
     |      schema : JSON string or Python dict
     |      parent : Parent instance, used internally
     |      name   : Key name this instance represents, used internally
     |  
     |  __repr__(self)
     |  
     |  dump(self, logger=<idlelib.PyShell.PseudoOutputFile object>)
     |      Create a dump of full path name and value for this and all child instances.
     |  
     |  getCount(self)
     |      Returns number of members at this level
     |  
     |  getFQN(self)
     |      Full path to the instance
     |  
     |  getName(self)
     |      Returns class member name, used internally
     |  
     |  getNames(self)
     |      Returns a list of member names at this level
     |  
     |  getValue(self, name)
     |      Return value or raise a PySONException
     |  
     |  setValue(self, name, value, strict=True)
     |      Set a value, optionally enforce type checking
     |  
     |  toDict(self)
     |      Create a dict object based on current values
     |  
     |  toJSON(self)
     |      Create a JSON string based on current values
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class PySONException(exceptions.Exception)
     |  Exception class for PySON
     |  
     |  Method resolution order:
     |      PySONException
     |      exceptions.Exception
     |      exceptions.BaseException
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, value)
     |  
     |  __str__(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from exceptions.Exception:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from exceptions.BaseException:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __getslice__(...)
     |      x.__getslice__(i, j) <==> x[i:j]
     |      
     |      Use of negative indices is not supported.
     |  
     |  __reduce__(...)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __setstate__(...)
     |  
     |  __unicode__(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from exceptions.BaseException:
     |  
     |  __dict__
     |  
     |  args
     |  
     |  message
