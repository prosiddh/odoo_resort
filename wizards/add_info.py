from odoo import api, fields, models

class addWizard(models.TransientModel):
    _name="add.wizard"
    _description = "Add Wizard"

    tourist_name_of = fields.Many2one('res.partner')
    tourist_age_number = fields.Integer('Age')


