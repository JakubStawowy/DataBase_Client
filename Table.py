class Table:
    """
    Table class
    this class stores table parameters (table name, number of columns, number of rows, column names with types, table content)
    """
    def __init__(self, tableName='', numberOfColumns=0, numberOfRows=0, columnDict={}, content=[]):
        """
        Table class constructor

        :param tableName: table name (str)
        :param numberOfColumns:  number of table columns (int)
        :param numberOfRows: number of table rows (int)
        :param columnDict: Column Dictionary (dict)
            (this dictionary stores column names with column types)
        :param content: table content (list)
        """
        self.__tableName = tableName
        self.__numberOfColumns = numberOfColumns
        self.__numberOfRows = numberOfRows
        self.__columnDict = columnDict
        self.__content = content

        self.getTableName=lambda :self.__tableName
        self.getColumnDict=lambda :self.__columnDict
        self.getContent=lambda :self.__content
        self.getNumberOfColumns = lambda :self.__numberOfColumns
        self.getNumberOfRows = lambda : self.__numberOfRows
        self.getRow = lambda index: self.__content[index]


    def numberOfRowsIncrement(self):
        """
        Number of rows increment function
        this function adds value 1 to table number of rows (this function is called after inserting new row into table)
        """
        self.__numberOfRows = self.__numberOfRows + 1

    def removeRow(self, rowList):
        """
        Remove row function
        this function removes row from table content

        :param rowList: list of row content (list)
        """
        self.__content.remove(rowList)

    def addRow(self, content: list):
        """
        Add Row function
        this function inserts new row into table content

        :param content: row content (list)
        """
        self.__content.append(content)
        self.__numberOfRows=self.__numberOfRows+1

    def addColumn(self,columnName:str, columnType:str):
        """
        Add column method
        this method increases number of columns in table and adds column name and type to column dictionary

        :param columnName: column name (str)
        :param columnType: columnt data type (str)
        """
        self.__columnDict[columnName]=columnType
        self.__numberOfColumns=self.__numberOfColumns+1

    def setTableName(self,tableName:str):
        """
        Set table name method
        this method sets table name

        :param tableName: table name (str)
        """
        self.__tableName=tableName

    def setContent(self, content:list):

        self.__content=content


    def __str__(self):
        return self.__tableName + "\n" + str(self.__numberOfColumns) + '\n' + str(self.__numberOfRows) + '\n' + str(
            self.__columnDict) + '\n' + str(self.__content)

