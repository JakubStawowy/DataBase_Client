from ProjectController import ProjectController
from Table import Table

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
        self.__tableStructure = []
        self.__tableNames=[]
        self.__typeDict={'Tekst':'str','Liczba całkowita':'int','Liczba rzeczywista':'float','Liczba porządkowa':'int(Auto-Inc)'}
        self.getStructure = lambda: self.__tableStructure
        self.getTypeDict = lambda: self.__typeDict


    def addTable(self, table:Table):
        """
        Adding table method
        This method adds new table classes to model's table structure

        :param table: Table class

        """
        if table.getTableName() in self.__tableNames:
            raise Exception('Tabela istnieje')
        else:
            self.__tableStructure.append(table)
            self.__tableNames.append(table.getTableName())

    def removeTable(self,tableName:str):
        """
        Remove table method
        this method removes table instance from model's table structure

        :param tableName: table name (str)
        """
        helpIndex = 0

        for x in self.__tableStructure: #Iterating by tables

            if x.getTableName() == tableName:

                self.__tableStructure.remove(x)
                self.__tableNames.remove(x.getTableName())

            helpIndex = helpIndex+1

    def addRow(self, tableName:str, rowList:list):
        """
        Add row method
        this method inserts new row into existing table

        :param tableName: table name (str)
        :param rowList: list of row content (list)
        """
        for x in self.__tableStructure: #Iterating by tables
            if x.getTableName() == tableName:
                columnTypes = [types for types in x.getColumnDict().values()] #List comprehession expression which fill new list with column types (int, float, str)
                try:
                    """helpIndex=0
                    for y in rowList: #Iterating by row components
                        if str(type(y)) != '<class \''+columnTypes[helpIndex]+'\'>':
                            #if row component is not equal to a column type, the exception is raised
                            print("zly typ: ",type(y),' dla typu:''<class \''+columnTypes[helpIndex]+'\'>')
                            raise Exception('Zly typ')

                        else:
                            helpIndex=helpIndex+1"""

                    x.addRow(rowList) #if there was no exception raised, new row is added
                    #x.numberOfRowsIncrement()

                except Exception as exc:
                    print(exc)


    def removeRow(self,tableName:str,rowList:list):
        """
        Remove row method
        this method removes selected row from selected table

        :param tableName: table name (str)
        :param rowList: list of row content (list)
        """
        for x in self.__tableStructure:

            if x.getTableName()==tableName:

                x.removeRow(rowList)
                x.numberOfRowsDeincrement()
    def getRowIndex(self,tableName:str,row:list):
        index=0
        for x in self.getTable(tableName).getContent():
            if x==row:
                return index
            else:
                index=index+1

    def lambdaBrowse(self, tableName:str):
        """
        Lambda browse method
        this method searches for tables components which meet described conditions

        :param tableName: table name (str)

        :return z: table component (type(z))
        """
        try:
            lmbd = input('type lambda') #User should type lambda expression
            columnName = lmbd.split(':')[0][7:] #Lambda expression argument should be the column name user want to search
            for x in self.__tableStructure: #Iterating by tables

                if x.getTableName()==tableName:

                    columnNames = [colName for colName in x.getColumnDict().keys()] #List comprehession expression which fill new list with column names

                    for y in x.getContent(): #Iterating by rows

                        helpIndex = 0
                        for z in y: #Iterating by table components

                            if columnNames[helpIndex] == columnName and eval(lmbd)(z) == True:
                                return z  #if component meet's conditions, component is returned

                            helpIndex = helpIndex+1

        except Exception as e:
            print(e)


    def writeToFile(self,fileName:str):
        """
        Write to file method
        this method writes tables structure to file with extension ".txt"

        :param fileName: file name (str)
        """
        with open(fileName,'w') as f:
            for x in self.__tableStructure:
                f.write(str(x)+'\n')

        f.close()


    def readFromFile(self, fileName:str):
        """
        Read from file method
        this method loads tables structure from file with extension ".txt"

        :param fileName: file name (str)
        :return list
        """
        l = []
        newTables=[]
        i = 0
        with open(fileName,'r') as f:
            for lines in f:
                if i%5 == 0:
                    l.append(lines.strip())
                    newTables.append(lines.strip())
                else:
                    l.append(eval(lines.strip()))
                if i%5 == 4:
                    #self.createTable(*l)
                    self.addTable(Table(*l))
                    l=[]
                i = i + 1
        return newTables

    def returnTableIndex(self, tableList, tableName:str):
        """
        Return Table Index Function
        this function returns table index in model table structure using table name

        :param tableList: list of tables (list)
        :param tableName: table name (str)
        :return: index: table index (int)
        """
        index = 0

        for x in tableList:
            if x.getTableName() == tableName:
                return index
            else:
                index = index+1
        raise Exception('nie ma takiej tabeli')

    def getTableRow(self,tableName:str, index:int):

         for x in self.__tableStructure:

             if x.getTableName() == tableName:

                 return x.getRow(index)

    def getTableNumberOfRows(self, tableName:str):

        for x in self.__tableStructure:

            if x.getTableName() == tableName:

                return x.getNumberOfRows()

    def getTable(self,tableName:str)->Table:

        for x in self.__tableStructure:

            if x.getTableName()==tableName:

                return x
