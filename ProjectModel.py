from Table import Table

class ProjectModel:
    """Model Class constructor
    TableStructure list is used to storage tables"""
    def __init__(self):

        self.__tableStructure = []

    """Adding table method
    This method adds new table classes to model's table structure"""
    def addTable(self, newTableStructure):

        self.__tableStructure.append(newTableStructure)
    """Create table method 
    This method creates new table class instance and adds it to model's table structure"""
    def createTable(self,tableName:str, numberOfColumns:int, numberOfRows:int,columnDict:dict, content:list):

        newTable = Table(tableName,numberOfColumns,numberOfRows,columnDict,content)
        self.addTable(newTable)

    """Delete table method 
    this method removes table instance from model's table structure """
    def deleteTable(self,tableName):

        helpIndex = 0
        for x in self.__tableStructure: #Iterating by tables
            if x.getTableName() == tableName:
                self.__tableStructure.remove(x)
            helpIndex = helpIndex+1
    """Add row method
    this method inserts new row into existing table"""
    def addRow(self, tableName, rowList):

        for x in self.__tableStructure: #Iterating by tables
            if x.getTableName() == tableName:
                columnTypes = [types for types in x.getColumnDict().values()] #List comprehession expression which fill new list with column types (int, float, str)
                try:
                    helpIndex=0
                    for y in rowList: #Iterating by row components
                        if str(type(y)) != '<class \''+columnTypes[helpIndex]+'\'>':
                            #if row component is not equal to a column type, the exception is raised
                            print("zly typ: ",type(y),' dla typu:''<class \''+columnTypes[helpIndex]+'\'>')
                            raise Exception('Zly typ')

                        else:
                            helpIndex=helpIndex+1

                    x.addRow(rowList) #if there was no exception raised, new row is added
                    x.numberOfRowsIncrement()

                except Exception as exc:
                    print(exc)

    def showStructure(self):
        for x in self.__tableStructure:
            print(x)
    """Lambda browse method
    this method searches for tables components which meet described conditions"""
    def lambdaBrowse(self, tableName:str):
        try:
            lmbd = input('type lambda') #User should type lambda expression
            columnName = lmbd.split(':')[0][7:] #Lambda expression argument should be the column name user want to search
            for x in self.__tableStructure: #Iterating by tables

                if x.getTableName()==tableName:

                    columnNames = [colName for colName in x.getColumnDict().keys()] #List comprehession expression which fill new list with column names

                    for y in x.getContent(): #Iterating by rows

                        helpIndex = 0
                        for z in y: #Iterating by table components

                            if columnNames[helpIndex] == columnName:

                                if eval(lmbd)(z) == True: #Parsing lambda expression and running it with table component as argument
                                    #if component meet's conditions, it is printed
                                    print(z)
                            helpIndex = helpIndex+1

        except Exception as e:
            print(e)



