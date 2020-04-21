from Table import Table


class ProjectModel:

    def __init__(self):

        self.__tableStructure = []

    def addTable(self, newTableStructure):

        self.__tableStructure.append(newTableStructure)

    def createTable(self,tableName:str, numberOfColumns:int, numberOfRows:int,columnDict:dict, content:list):

        newTable = Table(tableName,numberOfColumns,numberOfRows,columnDict,content)
        self.addTable(newTable)

    def deleteTable(self,tableName):

        index = 0
        for x in self.__tableStructure:
            if x.getTableName() == tableName:
                self.__tableStructure.remove(x)
            index = index+1

    def addRow(self, tableName, rowList):
        index = 0

        for x in self.__tableStructure:
            if x.getTableName() == tableName:
                columnTypes = [types for types in x.getColumnDict().values()]
                try:
                    index1=0
                    for y in rowList:
                        if str(type(y)) != '<class \''+columnTypes[index1]+'\'>':

                            print("zly typ: ",type(y),' dla typu:''<class \''+columnTypes[index1]+'\'>')
                            raise Exception('Zly typ')

                        else:
                            index1=index1+1

                    x.addRow(rowList)

                except Exception as exc:
                    print(exc)
                index = index+1

    def showStructure(self):
        for x in self.__tableStructure:
            print(x)





