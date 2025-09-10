from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit='sale.order.line'


    landed_cost = fields.Float(string='Landed Cost',compute='_compute_costs',store=True)
    overhead_cost = fields.Float(string='Overhead Cost',compute='_compute_costs',store=True)
    margin_line_revenue = fields.Float(string='Revenue',compute='_compute_costs',store=True)
    margin_line_cogs = fields.Float(string='COGS',compute='_compute_costs',store=True)
    margin_line_total = fields.Float(string='Line Margin',compute='_compute_costs',store=True)

    def _get_landed_cost(self):
        #asume landed costs sits on procuct price
        return self.product_id.standard_price

    def _get_overhead_cost(self):

        overhead_mode = self.env['ir.config_parameter'].sudo().get_param('smart_margin.overhead_mode','percentage')
        overhead_value= self.product_id.categ_id.overhead_value or 0

        if overhead_mode=='percentage':
            return self.product_id.standard_price * overhead_value /100.0
        elif overhead_mode=='fixed':
            return overhead_value
        return 0


    @api.depends('product_id','product_id.standard_price','product_uom_qty','price_unit')
    def _compute_costs(self):
        for line in self.filtered(lambda l:not l.order_id.margin_frozen):
            line.landed_cost= line._get_landed_cost()
            line.overhead_cost= line._get_overhead_cost()
            line.margin_line_revenue = line.price_unit * line.product_uom_qty
            line.margin_line_cogs = (line.landed_cost+line.overhead_cost)* line.product_uom_qty
            line.margin_line_total = line.margin_line_revenue - line.margin_line_cogs


    def get_cost_breakdown(self):

        ### since we assumed no landed cost edge cases and that landed cosrts are already applied to product price,
        # so fetching the landed costs here will not be accurate always
        # as we do no consider the removal strategy , costing method and quantity allocation
        # i will use this for demo purpose only
        landed_cost_adjustment_lines = self.env['stock.valuation.adjustment.lines'].search([('product_id','=',self.product_id.id)])
        landed_cost_list=[]
        for line in landed_cost_adjustment_lines:
            landed_cost_list.append({'label':line.cost_line_id.product_id.name ,
                                     'value':line.additional_landed_cost /line.quantity  })

        return landed_cost_list


    def get_overhead_breakdown(self):

        overhead_mode = self.env['ir.config_parameter'].sudo().get_param('smart_margin.overhead_mode', 'percentage')
        overhead_value = self.product_id.categ_id.overhead_value or 0

        if overhead_mode=='percentage':
            return {'type':'Percentage' ,'value':overhead_value}
        elif overhead_mode=='fixed':
            return {'type': 'Fixed', 'value': overhead_value}

        return {}


