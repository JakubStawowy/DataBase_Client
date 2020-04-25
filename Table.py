class Table:
    def __init__(self, tableName: str, numberOfColumns: int, numberOfRows: int, columnDict: dict, content: list):

        self.__tableName = tableName
        self.__numberOfColumns = numberOfColumns
        self.__numberOfRows = numberOfRows
        self.__columnDict = columnDict
        self.__content = content

        self.getTableName=lambda :self.__tableName
        self.getColumnDict=lambda :self.__columnDict
        self.getContent=lambda :self.__content

    def numberOfRowsIncrement(self):
        self.__numberOfRows = self.__numberOfRows + 1

    def removeRow(self, rowList):
        self.__content.remove(rowList)

    def addRow(self, content: list):
        self.__content.append(content)

    def __str__(self):
        return self.__tableName + "\n" + str(self.__numberOfColumns) + '\n' + str(self.__numberOfRows) + '\n' + str(
            self.__columnDict) + '\n' + str(self.__content)




