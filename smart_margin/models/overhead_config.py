from odoo import api, fields, models
#
# Configurable Overhead
# System Parameter to set overhead:
#
# Percentage of cost OR Fixed per unit
#
# Based on product category/analytical account  i will chose based on product category for this demo

class ResConfigSettings(models.TransientModel):
    _inherit='res.config.settings'

    overhead_mode = fields.Selection([('percentage','Percentage'),('fixed','Fixed per unit')],string='Overhead Mode',
                                     config_parameter='smart_margin.overhead_mode')

class ProductCategory(models.Model):
    _inherit='product.category'

    overhead_value= fields.Float(string = 'Overhead Value')
