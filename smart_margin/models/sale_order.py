from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit= 'sale.order'


    margin_revenue_total = fields.Float(string='Total Revenue',compute='_compute_margin',store=True)
    margin_cogs_total = fields.Float(string='Total COGS',compute='_compute_margin',store=True)
    margin_net_total = fields.Float(string='Margin Net',compute='_compute_margin',store=True)
    margin_frozen = fields.Boolean(string ='Frozen margin',default=False)


    def action_confirm(self):
        res= super(SaleOrder,self).action_confirm()
        self.write({'margin_frozen':True})
        return res

    @api.depends('order_line.margin_line_revenue','order_line.margin_line_cogs')
    def _compute_margin(self):
        for order in self:

            if order.margin_frozen:
                continue
            order.margin_revenue_total = sum(order.order_line.mapped('margin_line_revenue'))
            order.margin_cogs_total = sum(order.order_line.mapped('margin_line_cogs'))
            order.margin_net_total=order.margin_revenue_total-order.margin_cogs_total


    def get_smart_margin(self):
        return {
            'revenue':self.margin_revenue_total,
            'cogs':self.margin_cogs_total,
            'net':self.margin_net_total,
        }

    def get_margin_breakdown(self):
        lines_data=[]
        ###| Product | Sold Qty | Unit Price | Landed Cost | Overhead | Line Margin
        for line in self.order_line:
            lines_data.append({
                'product': line.product_id.display_name,
                'qty': line.product_uom_qty,
                'price_unit': line.price_unit,
                'landed_cost': line.landed_cost,
                'overhead_cost': line.overhead_cost,
                'line_margin':line.margin_line_total,
                'cost_breakdown': line.get_cost_breakdown(),
                'overhead_breakdown': line.get_overhead_breakdown(),
            })
        return lines_data