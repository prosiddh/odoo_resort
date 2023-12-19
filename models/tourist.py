from odoo import models, fields, api


class Address(models.Model):
    _name="address"
    _rec_name = "street"

    street = fields.Char(string="Street 1")
    street2 = fields.Char(string="Street 2")
    city = fields.Char(string="City")
    district = fields.Char(string="District")
    state = fields.Char(string="State")
    country = fields.Char(string="Country")


class Tourist(models.Model):
    _name = "tourist.tourist"
    _inherit = "address"
    _description = "Tourist"

    tourist_name = fields.Char(string="Name")
    tourist_age = fields.Integer('Age')
    notes = fields.Char(string="Notes")
    image = fields.Binary(string="Image")
    capital_name = fields.Char(string="Capital Name", store=True, compute="_compute")

    def button_add_info(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'add.wizard',
            'name': 'Info Add',
            'view_mode': 'form',
            'target':'new'
        }

    def button_save_info(self):
        pass


    @api.depends('tourist_name')
    def _compute(self):
        for record in self:
            if record.tourist_name:
                record.capital_name = record.tourist_name.upper()
            else:
                record.capital_name = ''
