import random
from table import Table


class ProjectModel:
    """
    Project Model class
    this class stores data and logical methods
    """

    def __init__(self):
        """
        Model Class constructor
        private parameter __tableStructure list is used to storage tables
        """
        self.__table_structure = []
        self.__table_names = []
        self.__type_dict = {'Tekst': 'str', 'Liczba całkowita': 'int', 'Liczba rzeczywista': 'float',
                            'Liczba porządkowa': 'int'}
        self.get_structure = lambda: self.__table_structure
        self.get_type_dict = lambda: self.__type_dict

    def add_table(self, table: Table):
        """
        Adding table method
        This method adds new table classes to model's table structure

        :param table: Table class

        """
        if table.get_table_name() in self.__table_names:
            raise Exception('Tabela istnieje')
        else:
            self.__table_structure.append(table)
            self.__table_names.append(table.get_table_name())

    def remove_table(self, table_name: str):
        """
        Remove table method
        this method removes table instance from model's table structure

        :param tableName: table name (str)
        """
        help_index = 0

        for table in self.__table_structure:

            if table.get_table_name() == table_name:
                self.__table_structure.remove(table)
                self.__table_names.remove(table.get_table_name())

            help_index = help_index + 1

    def add_row(self, table_name: str, row_list: list):
        """
        Add row method
        this method inserts new row into existing table

        :param tableName: table name (str)
        :param rowList: list of row content (list)
        """
        for table in self.__table_structure:

            if table.get_table_name() == table_name:

                # columnTypes = [types for types in x.getColumnDict().values()] #List comprehession expression which fill new list with column types (int, float, str)
                try:

                    table.add_row(row_list)

                except Exception as exception:
                    print(exception)

    def edit_row(self, table_name: str, content: list, new_content: list):
        for table in self.__table_structure:
            if table.get_table_name() == table_name:
                table.update_row(content, new_content)

    def remove_row(self, table_name: str, row_list: list):
        """
        Remove row method
        this method removes selected row from selected table

        :param table_name: table name (str)
        :param row_list: list of row content (list)
        """
        for table in self.__table_structure:

            if table.get_table_name() == table_name:
                table.removeRow(row_list)
                table.numberOfRowsDeincrement()

    def get_row_index(self, table_name: str, row: str):
        index = 0
        for rows in self.get_table(table_name).get_content():
            if str(rows) == row:
                return index
            else:
                index = index + 1

    def lambda_browse(self, table_name: str, lambda_expression: str):
        """
        Lambda browse method
        this method searches for tables components which meet described conditions

        :param table_name: table name (str)

        :return: Boolean
        """
        try:
            new_table = []

            column_name = lambda_expression.split(':')[0][7:]

            for table in self.__table_structure:

                if table.get_table_name() == table_name:

                    column_names = [colName for colName in table.get_column_dict().keys()]

                    for row in table.get_content():

                        help_index = 0
                        for component in row:  # Iterating by table components

                            if column_names[help_index] == column_name and eval(lambda_expression)(
                                    eval(self.__type_dict[self.get_table(table_name).get_column_types_listp()[help_index]])(
                                            component)):
                                new_table.append(row)
                            help_index = help_index + 1

            return new_table
        except Exception as exception:
            print(exception)

    def generate_lambda_expression(self, table_name: str):
        """
        generate lambda expression
        this method generates random lambda-expression
        :param tableName: str
        :return: str
        """
        column_names = []
        content = self.get_table(table_name).get_content()
        column_types = self.get_table(table_name).get_column_types_list()
        operators = ['==', '!=', '>', '<']
        for name in self.get_table(table_name).get_column_dict():
            column_names.append(name)

        index = random.randint(0, len(column_names) - 1)
        if column_types[index] == 'str':
            lambda_expression = 'lambda ' + str(column_names[index]) + ':' + str(column_names[index]) + operators[
                random.randint(0, 1)] + '\'' + str(content[random.randint(0, len(content) - 1)][index] + '\'')
        else:
            lambda_expression = 'lambda ' + str(column_names[index]) + ':' + str(column_names[index]) + operators[
                random.randint(0, len(operators) - 1)] + str(content[random.randint(0, len(content) - 1)][index])

        return lambda_expression

    def write_to_file(self, file_name: str):
        """
        Write to file method
        this method writes tables structure to file with extension ".txt"

        :param fileName: file name (str)
        """
        with open(file_name, 'w') as f:
            for table in self.__table_structure:
                f.write(str(table) + '\n')
        f.close()

    def read_from_file(self, file_name: str):
        """
        Read from file method
        this method loads tables structure from file with extension ".txt"

        :param fileName: file name (str)
        :return list
        """
        l = []
        new_tables = []
        i = 0
        with open(file_name, 'r') as f:
            for lines in f:
                if i % 5 == 0:
                    l.append(lines.strip())
                    new_tables.append(lines.strip())
                    if lines.strip() in self.__table_names:
                        self.remove_table(lines.strip())
                else:
                    l.append(eval(lines.strip()))
                if i % 5 == 4:
                    self.add_table(Table(*l))
                    l = []
                i = i + 1
        return new_tables

    def return_table_index(self, table_list, table_name: str):
        """
        Return Table Index Function
        this function returns table index in model table structure using table name

        :param tableList: list of tables (list)
        :param tableName: table name (str)
        :return: index: table index (int)
        """
        index = 0

        for table in table_list:
            if table.get_table_name() == table_name:
                return index
            else:
                index = index + 1
        raise Exception('nie ma takiej tabeli')

    def get_table_row(self, table_name: str, index: int):

        for table in self.__table_structure:

            if table.get_table_name() == table_name:
                return table.get_row(index)

    def get_table_number_of_rows(self, table_name: str):

        for table in self.__table_structure:

            if table.get_table_name() == table_name:
                return table.get_number_of_rows()

    def get_table(self, table_name: str) -> Table:

        for table in self.__table_structure:

            if table.get_table_name() == table_name:
                return table
