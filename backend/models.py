from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(80), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    orders = relationship("Order", back_populates="user")

    def __str__(self):
        return f"User {self.username}"


class Order(Base):
    ORDER_STATUSES = (
        ("PENDING", "pending"),
        ("PAID", "paid"),
    )

    SERVICES = (
        ("BUSINESS-SUPPORT", "Консультации по сопровождению бизнеса"),
        ("BOOKKEEPING", "Ведение бухгалтерии и консультация с привлечением аудита"),
        ("REPORTING", "Сдача отчетности по данным клиента"),
        ("CIVIL-LAW", "Консультация и помощь по гражданскому праву"),
        ("ADMINISTRATIVE-LAW", "Консультация и помощь по гражданскому праву"),
        ("SOLE-PROPRIETORSHIP", "Открытие ИП"),
        ("LCC-OPENING", "Открытие ООО"),
        ("EDM", "Консультация и подключение к ЭДО"),
        ("CASH-REGISTERS", "Консультация и помощь в подключении ККТ"),
    )

    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default="PENDING")
    service = Column(ChoiceType(choices=SERVICES), default="BUSINESS-SUPPORT")
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="orders")

    def __repr__(self):
        return f"<Order {self.id}>"
