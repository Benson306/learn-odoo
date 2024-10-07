from odoo import _, fields, api, models


class TripModel(models.Model):
    _name = "trip.model"
    _description = "Trip data structure"
    _rec_name = "sales_order"

    driver_id = fields.Many2one('driver.model', string = "Driver")
    vehicle_id = fields.Many2one('vehicle.model', string = "Vehicle")
    sales_order =  fields.Text(string="Sales Order", required=True)
    freight = fields.Selection([('loose', 'Loose Cargo'),('container', 'Container')], string="Freight Type", required=True)
    pickup = fields.Text(string="Pickup Location", required=True)
    destination = fields.Text(String="Destination", required=True)
    departure_time = fields.Datetime(string="Departure Time")
    arrival_time = fields.Datetime(string="Arrival Time")
    status = fields.Text(string="Trip Status", default="Active")