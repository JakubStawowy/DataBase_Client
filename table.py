class Table:
    """
    Table class
    this class stores table parameters (table name, number of columns, number of rows, column names with types, table content)
    """

    def __init__(self, table_name='', number_of_columns=0, number_of_rows=0, column_dict={}, content=[]):
        """
        Table class constructor

        :param table_name: table name (str)
        :param number_of_columns:  number of table columns (int)
        :param number_of_rows: number of table rows (int)
        :param column_dict: Column Dictionary (dict)
            (this dictionary stores column names with column types)
        :param content: table content (list)
        """
        self.__table_name = table_name
        self.__number_of_columns = number_of_columns
        self.__number_of_rows = number_of_rows
        self.__column_dict = column_dict.copy()
        self.__content = content.copy()

        self.__column_types_list = []
        self.__column_types_listp = []

        self.__type_dict = {'Tekst': 'str', 'Liczba całkowita': 'int', 'Liczba rzeczywista': 'float',
                            'Liczba porządkowa': 'int_auto_increment'}

        for value in self.__column_dict.values():
            self.__column_types_list.append(self.__type_dict[value])
            self.__column_types_listp.append(value)

        self.get_table_name = lambda: self.__table_name
        self.get_column_dict = lambda: self.__column_dict
        self.get_content = lambda: self.__content
        self.get_number_of_columns = lambda: self.__number_of_columns
        self.get_number_of_rows = lambda: self.__number_of_rows
        self.get_row = lambda index: self.__content[index]
        self.get_column_types_list = lambda: self.__column_types_list
        self.get_column_types_listp = lambda: self.__column_types_listp

    def number_of_rows_increment(self):
        """
        Number of rows increment function
        this function adds value 1 to table number of rows (this function is called after inserting new row into table)
        """
        self.__number_of_rows = self.__number_of_rows + 1

    def number_of_rows_deincrement(self):

        self.__number_of_rows = self.__number_of_rows - 1

    def remove_row(self, row_list):
        """
        Remove row function
        this function removes row from table content

        :param rowList: list of row content (list)
        """
        self.__content.remove(row_list)

    def add_row(self, content: list):
        """
        Add Row function
        this function inserts new row into table content

        :param content: row content (list)
        """
        self.__content.append(content)
        self.__number_of_rows = self.__number_of_rows + 1
        self.set_content(self.__content)

    def add_column(self, column_name: str, column_type: str):
        """
        Add column method
        this method increases number of columns in table and adds column name and type to column dictionary

        :param column_name: column name (str)
        :param column_type: columnt data type (str)
        """
        self.__column_dict[column_name] = column_type
        self.__number_of_columns = self.__number_of_columns + 1
        self.__column_types_list.append(self.__type_dict[column_type])
        self.__column_types_listp.append(column_type)

    def set_table_name(self, table_name: str):
        """
        Set table name method
        this method sets table name

        :param tableName: table name (str)
        """
        self.__table_name = table_name

    def set_number_of_rows(self, number_of_rows: int):

        self.__number_of_rows = number_of_rows

    def set_content(self, content: list):
        self.__content = content
        for index_1 in range(self.__number_of_columns):
            if self.__column_types_list[index_1] == 'int_auto_increment':
                counter = 1
                for index_2 in range(self.__number_of_rows):
                    self.__content[index_2][index_1] = str(counter)
                    counter = counter + 1

    def update_row(self, content: list, new_content: list):

        help_index = 0
        for row in self.__content:
            if row == content:
                self.__content[help_index] = new_content
            else:
                help_index = help_index + 1

    def get_row_index(self, content: list):
        help_index = 0
        for row in self.__content:
            if row == content:
                return help_index
            else:
                help_index = help_index + 1

    def __str__(self):
        return self.__table_name + "\n" + str(self.__number_of_columns) + '\n' + str(
            self.__number_of_rows) + '\n' + str(
            self.__column_dict) + '\n' + str(self.__content)
