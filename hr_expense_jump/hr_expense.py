# -*- coding: utf-8 -*-

from openerp import models, api
from openerp.osv import fields, osv

class HrExpenseExpenseInherit(models.Model):
    _inherit = 'hr.expense.expense'

    _columns = {
        'state': fields.selection([
            ('draft', 'New'),
            ('confirm', 'Confirm'),
            ('accepted', 'Accepted'),
            ('done', 'Done'),
            ],
            'Status', readonly=True, track_visibility='onchange', copy=False,
            help='When the expense request is created the status is \'Draft\'.\nThen the accounting entries are made for the expense request, the status is \'Waiting Payment\'.'),
    }

    @api.model
    def action_move_create(self):
    	res = super(HrExpenseExpenseInherit, self).action_move_create()
    	# get current expenese
    	for expense in self:
    		# get current account_move object from expense
    		account_move = expense.account_move_id
    		# checking state (unposted) of the move (in case of, lol)
    		if account_move.state == "draft":
    			# unposted -> posted account_move
				account_move.post()
		return res