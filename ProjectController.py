class ProjectController:
    """
    Project Controller class
    """
    def checkTableName(self,tableName:str):
        """
        Check table name method
        this method checks if table name is not empty

        :param tableName: table name (str)
        """
        if tableName == '':
            raise Exception('Zla nazwa tabeli')
        else:
            pass

    def checkRemovedTableName(self,tableName:str):
        """
        Check removed table name method
        this method checks if removed table name is correct
        :param tableName: table name (str)
        """
        if tableName == 'Wybierz tabele':
            raise Exception('Tabela nie zostala wybrana!')
        else:
            pass

    def checkColumnName(self,columnName:str):
        """
        Check column name method
        this method checks if column name is not empty
        :param columnName: column name (str)
        """
        if columnName=='':
            raise Exception('Zla nazwa kolumny')
        else:
            pass
    def checkColumnType(self,columnType):
        """
        Check column type method
        this method checks if added column type is correct

        :param columnType: column data type (str)
        """
        if columnType == 'Wybierz Typ':
            raise Exception('Zly typ kolumny')
        else:
            pass

    def checkNumberOfcolumns(self,numberOfColumns):
        """
        Check number of columns method
        this method checks if number of columns in created table is not equal 0

        :param numberOfColumns: number of columns (int)
        """
        if numberOfColumns == 0:
            raise Exception('Za mała ilość kolumn!')
        else:
            pass

    def cancel(self):
        raise Exception('')
