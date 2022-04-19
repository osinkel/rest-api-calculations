import enum

from sqlalchemy import Column, Enum, Numeric, Integer

from db.settings.base import Base

from logic.math_logic import operations

allowed_operations = enum.Enum('AllowedOperations', {el: el.lower() for el in list(operations.keys())}, type=str)


class Operation(Base):
    __tablename__ = 'operations'

    id = Column(Integer, primary_key=True)
    operator = Column(Enum(allowed_operations))
    number1 = Column(Numeric)
    number2 = Column(Numeric)
    result = Column(Numeric)

    def __init__(self, operator, number1, number2, result):
        self.operator = operator
        self.number1 = number1
        self.number2 = number2
        self.result = result
