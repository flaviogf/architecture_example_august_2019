from marshmallow import EXCLUDE, Schema, fields, validate


class StoreBudgetItem(Schema):
    name = fields.Str(required=True, validate=[validate.Length(min=3)])
    quantity = fields.Integer(required=True)
    price = fields.Float(required=True)


store_budget_item = StoreBudgetItem(unknown=EXCLUDE)


class StoreBudget(Schema):

    name = fields.Str(required=True, validate=[validate.Length(min=3)])
    email = fields.Email(required=True)
    items = fields.List(fields.Nested(store_budget_item), required=True)
    delivery_type = fields.Str(required=True,
                               validate=[validate.OneOf(choices=['normal', 'fast', 'withdrawal'])])


store_budget = StoreBudget(unknown=EXCLUDE)
