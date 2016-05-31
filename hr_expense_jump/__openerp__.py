# -*- coding: utf-8 -*-
{
    'name': "hr_expense_jump",
    'summary': """
        This module speed up the hr_expense workflow by simply 
        jumping from draft to 'done' state when clicking on Validate. 
        It also create the account_move and post it in journal.""",
    'author': "Business Agile",
    'website': "https://businessagile.eu/",
    'category': 'Human Resources',
    'version': '8.0.1',
    'depends': ['base', 'hr', 'hr_expense'],
    'data': [
        'hr_expense_workflow.xml',
        'hr_expense_view.xml',
    ],
  
}