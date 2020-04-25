from Table import Table

class ProjectModel:
    """
    Model Class constructor
    TableStructure list is used to storage tables
    """
    def __init__(self):

        self.__tableStructure = []

    """
    Adding table method
    This method adds new table classes to model's table structure
    """
    def addTable(self, newTableStructure:Table):

        self.__tableStructure.append(newTableStructure)

    """
    Create table method 
    This method creates new table class instance and adds it to model's table structure
    """
    def createTable(self,tableName:str, numberOfColumns:int, numberOfRows:int,columnDict:dict, content:list):

        newTable = Table(tableName,numberOfColumns,numberOfRows,columnDict,content)

        self.addTable(newTable)

    """
    Remove table method 
    this method removes table instance from model's table structure
    """
    def removeTable(self,tableName:str):

        helpIndex = 0

        for x in self.__tableStructure: #Iterating by tables

            if x.getTableName() == tableName:

                self.__tableStructure.remove(x)

            helpIndex = helpIndex+1
    """
    Add row method
    this method inserts new row into existing table
    """
    def addRow(self, tableName:str, rowList:list):

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

    """
    Remove row method
    this method removes selected row from selected table
    """
    def removeRow(self,tableName:str,rowList:list):

        for x in self.__tableStructure:

            if x.getTableName()==tableName:

                x.removeRow(rowList)

    def showStructure(self):

        for x in self.__tableStructure:

            print(x)

    """
    Lambda browse method
    this method searches for tables components which meet described conditions
    """
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

                            if columnNames[helpIndex] == columnName and eval(lmbd)(z) == True:
                                    print(z) #if component meet's conditions, it is printed

                            helpIndex = helpIndex+1

        except Exception as e:
            print(e)

    """
    Write to file method
    this method writes tables structure to file with extension ".txt" 
    """
    def writeToFile(self,fileName:str):

        with open(fileName,'w') as f:
            for x in self.__tableStructure:
                f.write(str(x)+'\n')

        f.close()

    """
    Read from file method
    this method loads tables structure from file with extension ".txt"
    """
    def readFromFile(self, fileName:str):

        l = []
        i = 0
        with open(fileName) as f:
            for lines in f:
                if i%5 == 0:
                    l.append(lines.strip())
                else:
                    l.append(eval(lines.strip()))
                if i%5 == 4:
                    self.createTable(*l)
                    l=[]
                i = i + 1

model = ProjectModel()
model.createTable('tabela1',2,2,{'kol1':'int','kol2':'str'},[[1,'w1'],[2,'w2']])
model.createTable('tabela2',2,2,{'kol1':'int','kol2':'str'},[[3,'w3'],[4,'w4']])
model.lambdaBrowse('tabela1')