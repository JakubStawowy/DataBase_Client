class Table:
    def __init__(self,tableName:str, numberOfColumns:int, numberOfRows:int,columnDict:dict, content:list):
        self.__tableName = tableName
        self.__numberOfColumns = numberOfColumns
        self.__numberOfRows = numberOfRows
        self.__columnDict = columnDict
        self.__content = content

    def getTableName(self):

        return self.__tableName

    def getColumnDict(self):

        return self.__columnDict

    def addRow(self,content:list):

        self.__content.append(content)

    def __str__(self):

        return self.__tableName+", "+str(self.__numberOfColumns)+', '+str(self.__numberOfRows)+', '+str(self.__columnDict)+','+str(self.__content)
