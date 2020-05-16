from ControllerBase import ControllerBase
from Errors import *


class ProjectController(ControllerBase):
    """
    Project Controller class
    """
    def checkTableName(self,tableName:str):
        """
        Check table name method
        this method checks if table name is not empty

        :param tableName: table name (str)
        """
        if tableName.isspace() or tableName == '':
            raise EmptyTableNameException()
        else:
            pass

    def checkRemovedTableName(self,tableName:str):
        """
        Check removed table name method
        this method checks if removed table name is correct
        :param tableName: table name (str)
        """
        if tableName == 'Wybierz tabele':
            raise NoTableChosenException()
        else:
            pass
    def checkRemovedRow(self,row:str):
        if row=='Wybierz rekord':
            raise NoRowChosenException()
        else:
            pass
    def checkColumnName(self,columnName:str):
        """
        Check column name method
        this method checks if column name is not empty
        :param columnName: column name (str)
        """
        if columnName.isspace() or columnName=='':
            raise EmptyColumnNameException()
        else:
            pass
    def checkColumnType(self,columnType):
        """
        Check column type method
        this method checks if added column type is correct

        :param columnType: column data type (str)
        """
        if columnType == 'Wybierz Typ':
            raise NoColumnTypeChosenException()
        else:
            pass

    def checkNumberOfcolumns(self,numberOfColumns):
        """
        Check number of columns method
        this method checks if number of columns in created table is not equal 0

        :param numberOfColumns: number of columns (int)
        """
        if numberOfColumns == 0:
            raise NoColumnTableException()
        else:
            pass

    def checkEnteredType(self, value:str, columnType:str):
        """
        Check entered type method
        this method checks if entered value (type str) can be projected to it's column type

        :param value: value (str)
        :param columnType: column type (str)
        """
        if columnType == 'int_auto_increment':
            pass
        else:
            if value.isspace() or value=="":
                raise BadEnteredTypeException(expression=value,message="Kolumna nie może być pusta!")
            if columnType=='str':
                pass
            else:
                try:
                    value = eval(columnType)(value)
                except:
                    raise BadEnteredTypeException(expression=value)







