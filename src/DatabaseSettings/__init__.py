"""
this is a module which has a class for database settings
"""

class Database(object):
    """
    Database class to connect to SQL
    """
    def __init__(self, connect):
        """
        connection string to connect to sql server

        Args:
            connect (_type_): ser
        """
        self.connect = connect

    def connect(self) -> True:
        """
        connect to database

        Returns:
            _type_: Bool
        """
        print("connected")
        return True