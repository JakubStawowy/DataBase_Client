from abc import ABCMeta
import abc

class ModelBase(metaclass=ABCMeta):
    @abc.abstractmethod
    def addTable(self, table):
        pass
    @abc.abstractmethod
    def removeTable(self, tableName):
        pass
    @abc.abstractmethod
    def addRow(self, tableName, rowList):
        pass
    @abc.abstractmethod
    def editRow(self, tableName, content, newContent):
        pass
    @abc.abstractmethod
    def removeRow(self,tableName,rowList):
        pass
    @abc.abstractmethod
    def getRowIndex(self, tableName, row):
        pass
    @abc.abstractmethod
    def lambdaBrowse(self, tableName, lambdaExpression):
        pass
    @abc.abstractmethod
    def writeToFile(self, fileName):
        pass
    @abc.abstractmethod
    def readFromFile(self, fileName):
        pass
    @abc.abstractmethod
    def returnTableIndex(self, tableList, tableName):
        pass
    @abc.abstractmethod
    def getTableRow(self, tableName, index):
        pass
    @abc.abstractmethod
    def getTableNumberOfRows(self, tableName):
        pass
    @abc.abstractmethod
    def getTable(self, tableName):
        pass


