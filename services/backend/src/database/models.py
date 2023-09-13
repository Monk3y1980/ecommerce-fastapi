from tortoise import fields, models
from enum import Enum, IntEnum


class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    full_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Orders(models.Model):
    class Status(IntEnum):
        PENDING = 1
        PAID = 2

    class SERVICES(str, Enum):
        BUSINESS_SUPPORT = "Консультации по сопровождению бизнеса"
        BOOKKEEPING = "Ведение бухгалтерии и консультация с привлечением аудита"
        REPORTING = "Сдача отчетности по данным клиента"
        CIVIL_LAW = "Консультация и помощь по гражданскому праву"
        ADMINISTRATIVE_LAW = "Консультация и помощь по гражданскому праву"
        SOLE_PROPRIETORSHIP = "Открытие ИП"
        LCC_OPENING = "Открытие ООО"
        EDM = "Консультация и подключение к ЭДО"
        CASH_REGISTERS = "Консультация и помощь в подключении ККТ"

    id = fields.IntField(pk=True)
    status = fields.IntEnumField(Status)
    services = fields.CharEnumField(SERVICES, default=SERVICES.BUSINESS_SUPPORT)
    user = fields.ForeignKeyField("models.Users", related_name="order")
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}, {self.services}, {self.status} on {self.created_at}"
