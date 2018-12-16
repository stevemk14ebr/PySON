"""
PySON:   Simple easy to use class to convert JSON string
         or Python dict into accessable classes/members.
         Tested on Python 2.7
         
Date:    12-15-2018
By:      zoomgod
Version: 0.0001 serious alphaware

Contact me:
Unknown Cheats: https://www.unknowncheats.me/forum/members/146787.html
GitHub: https://github.com/therealzoomgod
"""

import sys, json

#
# Types currently supported for conversion
#
from types import BooleanType, IntType, LongType, FloatType, StringType, UnicodeType, ListType, DictType, NoneType

class PySONException(Exception):
    """Exception class for PySON"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

PySONExceptionType = type(PySONException)

class PySON(object):
    """
    Convert a JSON string or dictionary into class objects.

    Methods
    -------
    setValue    Set a value, raise exception if strict type checking is enabled
    getValue    Returns value or None
    getNames    Returns a list of member names
    getCount    Returns count of members
    getName     Returns member name class is based on
    getFQN      Returns full name reflecting the parent instances
    dump        Dump all FQN from here down to any file type object
    toJSON      Returns a JSON string reflecting current values including child members.
    toDict      Returns a dict object reflecting current values including child members.
    """

    def __init__(self, schema, parent = None, name = ""):
        """
        Args:
        -----------
        schema : JSON string or Python dict
        parent : Parent instance, used internally
        name   : Key name this instance represents, used internally
        """
        
        object.__init__(self)
        
        self.__parent = parent

        self.__my_class_name = name
        self.__my_type = type(self)
        
        if parent:
            nm = parent.getName()
            if nm != "":
                self.__my_fqn = "%s.%s" % (parent.getFQN(), name)
            else:
                self.__my_fqn = "%s" % (name)
        else:
            self.__my_fqn = name

        #
        # Object types that are handled
        #
        self.__my_supported_types = [self.__my_type, BooleanType, IntType, LongType, FloatType, StringType, DictType, ListType, UnicodeType, NoneType]

        #
        # member name to object type mapping
        #
        self.__my_property_types = {}

        #
        # member names
        #
        self.__my_property_names = []

        #
        # If a string is passed it should be a valid JSON string
        # The JSON string will be loaded into a dict object
        if type(schema) in [StringType, UnicodeType]:
            schema = json.loads(schema)
        
        #
        # Turn dictionary into class members
        #
        self.__load(schema)

    def setValue(self, name, value, strict = True):
        """Set a value, optionally enforce type checking"""

        t = self.__my_property_types.get(name, None)
        
        if t == None:
            raise PySONException("Class member %s not found" % name)
        
        if strict:
            if not type(value) is t:
                raise PySONException("Invalid type (strict enabled)")
            
        self.__dict__[name] = value
        
    def getValue(self, name):
        """Return value or raise a PySONException"""
        if name in self.__my_property_names:
            return self.__dict__[name]
        raise PySONException("Class member %s not found" % name)

    def getNames(self):
        """Returns a list of member names at this level"""
        return self.__my_property_names
        
    def getCount(self):
        """Returns number of members at this level"""
        return len(self.__my_property_names)
    
    def getName(self):
        """Returns class member name, used internally"""
        return self.__my_class_name

    def getFQN(self):
        """Full path to the instance"""
        return self.__my_fqn

    def dump(self, logger = sys.stdout):
        """Create a dump of full path name and value for this and all child instances."""
        
        def info(k, v, hint=''):

            t = self._type(v, k)
            
            if t is self.__my_type:
                v.dump(logger)
            elif t is ListType:
                [ info(k, v[i], "[%i]" % i) for i in range(0, len(v)) ]
            elif t in [StringType, UnicodeType]:
                logger.write('%s.%s%s = "%s"\n' % (self.__my_fqn, k, hint, v))
            else:
                logger.write('%s.%s%s = %s\n' %  (self.__my_fqn, k, hint, v))

        ordered = self.__my_property_names
        ordered.sort()
        for i in range(0, len(ordered)):
            k = ordered[i]
            v = self.__dict__[k]
            info(k, v)

    def toJSON(self):
        """Create a JSON string based on current values"""
    
        def append(v):

            t = self._type(v)
            
            if t is self.__my_type:
                return v.toJSON()
            elif t is ListType:
                return '[' + ",".join([ append(v[i]) for i in range(0, len(v)) ]) + ']'
            elif t is BooleanType:
                if v: return '"true"'
                else: return '"false"'
            elif t is NoneType:
                v = "null"
            elif t in [UnicodeType, StringType]:
                return '\"%s\"' % v
            
            return '%s' % v

        out = '{'

        cnt = len(self.__my_property_names)
        for i in range(0, cnt):
            k = self.__my_property_names[i]
            out = out + ('\"%s\":' % (k)) + append(self.__dict__[k])
            if i < cnt-1: out = out + ","

        out = out + '}'

        return out
    
    def toDict(self):
        """Create a dict object based on current values"""
    
        def toTyped(v):
            
            t = type(v)
            
            if t is self.__my_type:
                return v.toDict()
            elif t is ListType:
                return [ toTyped(v[i]) for i in range(0, len(v)) ]
            else:
                return v

        out = {}
        for k in self.__my_property_names:
            obj = self.__dict__[k]
            out[k] = toTyped(obj)
            
        return out

    def __repr__(self):
        return self.toJSON()

    def _type(self, v, k = ""):
        t = type(v)
        if not t in self.__my_supported_types:
            raise PySONException("Unsupported type %s (%s-%s)" % (t, `k`, `v`))
        return t

    def __load(self, d):

        def fromTyped(k, v, index = None):
        
            entryType = self._type(v, k)
        
            if entryType is DictType:
                key = k
                if index != None:
                    key = "%s[%i]" % (key, index)
                return PySON(name=key, parent=self, schema=v)
            elif entryType is ListType:
                return [ fromTyped(k, v[i], i) for i in range(0, len(v)) ]
            elif v == "true":
                v = True
            elif v == "false":
                v = False
                
            return v
        
        for k, v in d.items():
            self.__dict__[k] = fromTyped(k, v)
            t = self._type(v, k)
            self.__my_property_types[k] = t
            self.__my_property_names.append(k)


