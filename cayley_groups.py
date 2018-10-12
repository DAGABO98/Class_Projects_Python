class BaseCayleyGroup(object):

    def __init__(self):
        raise TypeError("You can't make an instance of this class")

    def __eq__(self, other):
        return self.get_value()== other.get_value()

    def __mul__(self, other):
        t = self.get_cayley_table()
        key = (self.get_value(), other.get_value())
        result = t[key]
        return result

    def __str__(self):
        return self.__class__.__name__ + "({})".format(self.get_value())

class CayleyMod5(BaseCayleyGroup):
    """
    Implement addition mod 5. Since this is a group, '*' is the group operator.
    """

    __symbols = {0, 1, 2, 3, 4}     # Attribute of class -- group symbols
    __table = None                  # Attribute of class -- Cayley Table for class.

    def __init__(self, v):

        # Not strictly the correct approach. Should probably return an error, but OK.
        self.__value = v % len(CayleyMod5.__symbols)

        if CayleyMod5.__table is None:
            """
            If we have not initialized the table for the class, generate the table.
            This approach is kind of awkward and general solutions would do something better.
            """
            symbols = CayleyMod5.__symbols

            # For each pair of symbols, compute addition mod 5.
            temp = [(k, v) for k in symbols for v in symbols]
            CayleyMod5.__table = dict({((i, j), (i + j) % 5) for i, j in temp})

    @classmethod # Method on class. HINT: Base class calls.
    def get_cayley_table(cls):
        return CayleyMod5.__table

    # Method on instance. HINT: base class calls.
    def get_value(self):
        return self.__value

class CayleyOneAndI(BaseCayleyGroup):

    # These are class level properties/attributes. The values are the same for all instances of the class.
    __symbols = {1+0j, -1-0j, 0+1j, -0-1j}      # Valid symbols for the group.
    __table = None                              # Will hold the Cayley table.

    def __init__(self, v):

        # Make sure that the input value is a valid symbol.
        if not v in CayleyOneAndI.__symbols:
            raise ValueError("Invalid symbol. Valid symbols are: {}".format(CayleyOneAndI.__symbols))

        self.__value = v

        if CayleyOneAndI.__table is None:
            """
            This generates the table. For any pair of numbers in the symbol table, the result is simply
            complex number multiplication. So, we use a comprehension. This is kind of a hack and we will
            see cleaner approaches for the OO pattern in future lectures
            """
            temp = [(k, v) for k in CayleyOneAndI.__symbols for v in CayleyOneAndI.__symbols]
            CayleyOneAndI.__table = dict({((i, j), i*j) for i, j in temp})

    @classmethod # Our first use of a decorator. This is a method on the class object, not an instance.
    def get_cayley_table(cls):
        """
        Returns the Cayley table. HINT: the base class that you implement calls this method.
        :return:
        """
        return CayleyOneAndI.__table

    def get_value(self):
        """
        HINT: the base class you implement calls this method. The value is an attribute of the instance.
        :return: The value of the group element as a symbol (complex number).
        """
        return self.__value
