from odoo import api, fields, models, _, SUPERUSER_ID


class cafe_item(models.Model):
    _name = 'cafe.item'  # This will create table in DB called cafe.item

    #    def total(self,cr,uid,ids,total,args=None,context=None):
    #        print"ids/////////",ids
    #        res={}
    #        for val in self.browse(cr,uid,ids):
    #            if val:
    #                res[val.id]=val.qty * val.unit_price
    #            else:
    #                res[val.id]=0.0
    #        print "res=============",res
    #        return res

    @api.onchange('qty', 'unit_price')
    def onchange_total_price(self):
        if self.qty and self.unit_price:
            self.total_price = self.qty * self.unit_price

    name = fields.Char(string='Name', size=128)
    description = fields.Char('Description', size=128)
    unit_price = fields.Float('Unit Price')
    type = fields.Selection([('food', 'Food'), ('drink', 'Drink')], string='Type')
    temp = fields.Selection([('hot', 'Hot'), ('cold', 'Cold'), ('any', 'Any')], 'How Served')
    qty = fields.Float('Quantity')
    total_price = fields.Float('Total Price')
    #        'total_price':fields.function(total,string='Total Price',type='float',store=True),
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'), ('done', 'Done')], 'State', default='draft')
    item = fields.Selection([('tea', 'Tea'), ('coffee', 'Coffee'), ('other', 'Other')], string='Item')
    other_item = fields.Char('Other Item')
    test = fields.One2many('cafe.item.test', 'cafe1', 'test')

    # create method returns id

    @api.model
    def create(self, create_values):
        # seq = self.env['ir.sequence'].next_by_code('sequence')
        # create_values["name"] = seq
        res = super(cafe_item, self).create(create_values)
        print
        "=========id==============", res, create_values
        return res

    # write method returns True or False

    @api.multi
    def write(self, vals):
        res = super(cafe_item, self).write(vals)
        print
        "======write====================", res
        return res

    @api.one
    def mohit(self):
        print
        "==========cr=======", self.env.cr
        print
        "==========uid=======", self._uid, self.env.uid
        print
        "==========context=======", self.env.context
        print
        "=============self=======", self
        print
        "=============id=========", self.id
        self.state = 'draft'
        self.unit_price = 10

    #         self.write({'unit_price':20})

    @api.multi
    def confirmed(self):
        for record in self:
            record.state = 'confirm'
            a = record.write({'test': [(0, 0, {'cafe2': 'test', 'cafe3': 'test'})]})
            print
            "=======write==================", a

    def Done(self):
        for val in self:
            val.state = 'done'

        #


#    def mohit(self,cr,uid,ids,context=None):
#        return self.write(cr,uid,ids,{'state':'draft'})
#
#
#    def confirmed(self,cr,uid,ids,context=None):
#        return self.write(cr,uid,ids,{'state':'confirm'})
#
#
#    def Done(self,cr,uid,ids,context=None):
#        return self.write(cr,uid,ids,{'state':'done'})

class cafe_item_test(models.Model):
    _name = 'cafe.item.test'

    cafe1 = fields.Many2one('cafe.item', 'test1')
    cafe2 = fields.Char('test2')
    cafe3 = fields.Char('test3')