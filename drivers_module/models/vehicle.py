from odoo import _, fields, api, models


class VehicleModel(models.Model):
    _name = "vehicle.model"
    _description = "Vehicle data structure"

    model =  fields.Text(string="Name", required=True)
    yom = fields.Integer(string="Yom", required=True)
    reg_number = fields.Text(string="Reg Number", required=True)