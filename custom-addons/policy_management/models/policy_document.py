from odoo import models, fields

class PolicyDocument(models.Model):
    _name = 'policy.document'
    _description = 'Policy Document Library'

    name = fields.Char("Document Title", required=True)
    policy_id = fields.Many2one('policy.policy', string="Linked Policy")
    file = fields.Binary("Upload Document", required=True)
    file_name = fields.Char("File Name")
    doc_type = fields.Selection([
        ('wording_life', 'Life Policy Wording'),
        ('wording_medical', 'Medical Policy Wording'),
        ('certificate', 'Employee Certificate'),
        ('endorsement', 'Endorsement'),
    ], string="Document Type", required=True)