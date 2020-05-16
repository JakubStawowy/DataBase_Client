from abc import ABCMeta
import abc

class ControllerBase(metaclass=ABCMeta):
    @abc.abstractmethod
    def checkTableName(self,tableName):
        pass
    @abc.abstractmethod
    def checkRemovedTableName(self,tableName):
        pass
    @abc.abstractmethod
    def checkRemovedRow(self,row):
        pass
    @abc.abstractmethod
    def checkColumnName(self,columnName):
        pass
    @abc.abstractmethod
    def checkColumnType(self,columnType):
        pass
    @abc.abstractmethod
    def checkNumberOfcolumns(self,numberOfColumns):
        pass
    @abc.abstractmethod
    def checkEnteredType(self, value:str, columnType):
        pass