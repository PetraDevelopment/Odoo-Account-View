from odoo import fields, models, api


class CustomAccountAccount(models.Model):
    _inherit='account.account'

    special_view = fields.Boolean(string="Special View" )
    done=fields.Boolean("Done")




  

class CustomAccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    special_account_name = fields.Char(string='Special Account Name', related='account_id.name', readonly=True)
    special_account_code = fields.Char(string='Special Account Code', related='account_id.code', readonly=True)
    account_id = fields.Many2one(
        comodel_name='account.account',
        string='Account',
        compute='_compute_account_id',
        store=True, 
        readonly=False, precompute=True,
        inverse='_inverse_account_id',
        index=True,
        auto_join=True,
        ondelete="cascade",
        check_company=True,
        domain=lambda self: self._compute_account_domain(),
        
        tracking=True,
    )


    


    @api.onchange('account_id')
    def _compute_account_domain(self):
        
        products_with_quantity = self.env['account.account'].search([('special_view', '=', False)])
        product_ids = products_with_quantity.ids

        return {'domain': {'account_id': [('id', 'in', product_ids)]}}
        

    
    
    

    
