from errors import EmptyTableNameException
from errors import NoTableChosenException
from errors import NoRowChosenException
from errors import EmptyColumnNameException
from errors import NoColumnTypeChosenException
from errors import NoColumnTableException
from errors import BadEnteredTypeException


class ProjectController:
    """
    Project Controller class
    """

    def check_table_name(self, table_name: str):
        """
        Check table name method
        this method checks if table name is not empty

        :param tableName: table name (str)
        """
        if table_name.isspace() or table_name == '':
            raise EmptyTableNameException()
        else:
            pass

    def check_removed_table_name(self, table_name: str):
        """
        Check removed table name method
        this method checks if removed table name is correct
        :param tableName: table name (str)
        """
        if table_name == 'Wybierz tabele':
            raise NoTableChosenException()
        else:
            pass

    def check_removed_row(self, row: str):
        if row == 'Wybierz rekord':
            raise NoRowChosenException()
        else:
            pass

    def check_column_name(self, column_name: str):
        """
        Check column name method
        this method checks if column name is not empty
        :param columnName: column name (str)
        """
        if column_name.isspace() or column_name == '':
            raise EmptyColumnNameException()
        else:
            pass

    def check_column_type(self, column_type):
        """
        Check column type method
        this method checks if added column type is correct

        :param columnType: column data type (str)
        """
        if column_type == 'Wybierz Typ':
            raise NoColumnTypeChosenException()
        else:
            pass

    def check_number_of_columns(self, number_of_columns):
        """
        Check number of columns method
        this method checks if number of columns in created table is not equal 0

        :param numberOfColumns: number of columns (int)
        """
        if number_of_columns == 0:
            raise NoColumnTableException()
        else:
            pass

    def check_entered_type(self, value: str, column_type: str):
        """
        Check entered type method
        this method checks if entered value (type str) can be projected to it's column type

        :param value: value (str)
        :param columnType: column type (str)
        """
        if column_type == 'int_auto_increment':
            pass
        else:
            if value.isspace() or value == "":
                raise BadEnteredTypeException(expression=value, message="Kolumna nie może być pusta!")
            if column_type == 'str':
                pass
            else:
                try:
                    value = eval(column_type)(value)
                except:
                    raise BadEnteredTypeException(expression=value)
