from odoo import _, fields, api, models


class DriverModel(models.Model):
    _name = "driver.model"
    _description = "Driver data structure"

    name =  fields.Text(string="Name", required=True)
    email = fields.Text(string="Email", required=True)
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string="Gender", required=True)
    id_number = fields.Integer(string="Id Number", required=True)
    phone_number = fields.Text(string="Phone Number", required=True)