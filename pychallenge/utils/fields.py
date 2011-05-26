class Field():
    """
    Base field class for all fields
    """

    def __init__(self, value=None):
        """
        :param value: the field value
        :type value: variable
        """
        self.value = value

    def clean(self, value):
        """
        :param value: clean `value`
        :type value: variable
        :return: cleans up the value and returns the cleaned data
        """
        return value

    def get_value(self):
        """
        value stores the field value
        :return: returns the value of that field
        """
        return self._value

    def set_value(self, value):
        """
        :param value: this is the setter function for the value
        :type value: variable
        """
        self._value = self.clean(value)

    value = property(get_value, set_value)

    def __str__(self):
        """
        :return: This returns a string formatted field-object
        """
        return '<%s "%s">' % (
            str(self.__class__.__name__),
            (self.value)
        )

class Numeric(Field):
    """
    This field class matches the SQLite field type "NUMERIC"
    """
    pass

class Text(Field):
    """
    This field class matches the SQLite field type "TEXT"
    """
    pass

class PK(Field):
    """
    This field class matches the SQLite field type "INTEGER PRIMARY KEY"
    """
    pass

class FK(Numeric):
    """
    This field class matches the SQLite field type "NUMERIC" and will be used
    for foreign key validation.
    """

    def __init__(self, ref_table, value=None):
        """
        :param ref_table: defines the foreign table
        :type ref_table: String
        """
        self.ref_table = ref_table
        self.value = self.clean(value)
