from odoo import _, fields, api, models


class VehicleModel(models.Model):
    _name = "vehicle.model"
    _description = "Vehicle data structure"
    _rec_name = "reg_number"

    def _valid_field_parameter(self, name, param):
        if param == 'unique':
            return True
        return super()._valid_field_parameter(name, param)

    model = fields.Text(string="Truck Model", required=True)
    yom = fields.Text(string="Y.O.M", required=True,)
    reg_number = fields.Text(string="Reg Number", required=True, unique=True)