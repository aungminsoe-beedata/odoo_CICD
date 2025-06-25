# -*- coding: utf-8 -*-

from odoo import fields, models


class SalaryPeriod(models.Model):
    """Model that holds Salary Period of Employee"""

    _name = "salary.period"
    _description = "Employee Salary Period"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", help="Name Period", required=True,tracking=True)

    month_start_date = fields.Date(string="Salary Start Date",required = True,tracking= True,help="This is salary computation of start date")
    month_end_date = fields.Date(string="Salary End Date",required = True,tracking= True,help="This is salary computation of end date")

    
    status = fields.Selection(selection=[('draft', 'Draft'),
                                        ('comfirm', 'Verify'),
                                        ('cancel', 'Cancel')], string='State',
                             help="State of the salary computation ",
                             default='draft', tracking=True)
    

    def action_verify(self):
         self.status = 'comfirm'

    def action_cancel(self):
         self.status = "cancel"

    def action_draft(self):
         self.status = 'draft'
    