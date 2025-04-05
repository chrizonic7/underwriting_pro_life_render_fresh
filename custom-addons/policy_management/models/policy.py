from odoo import models, fields, api
from datetime import date

class InsurancePolicy(models.Model):
    _name = 'policy.policy'
    _description = 'Insurance Policy'

    name = fields.Char("Client Name", required=True)
    policy_number = fields.Char("Policy Number", required=True)
    policy_type = fields.Selection([
        ('anticipated_endowment', 'Anticipated Endowment'),
        ('endowment', 'Endowment'),
        ('whole_life_limited', 'Whole Life Limited'),
        ('whole_life_unlimited', 'Whole Life Unlimited'),
        ('term_life', 'Term Life'),
        ('group_life', 'Group Life'),
        ('child_education', 'Child Education')
    ], required=True)
    occupation = fields.Char("Occupation")
    dob = fields.Date("Date of Birth")
    age = fields.Integer("Age Next Birthday", compute="_compute_age")
    basic_rate = fields.Float("Basic Rate")
    sum_assured = fields.Float("Sum Assured")
    duration_years = fields.Integer("Policy Duration (Yrs)")
    modal_factor = fields.Float("Modal Factor")
    hazardous_rate = fields.Float("Hazardous Rate")
    is_hazardous = fields.Boolean("Hazardous Occupation")
    currency = fields.Selection([('lrd', 'Liberian Dollars'), ('usd', 'USD')], default='lrd')
    
    policy_fee = fields.Float("Policy Fee", compute="_compute_total_premium", store=True)
    sai = fields.Float("SAI", compute="_compute_total_premium", store=True)
    premium = fields.Float("Base Premium", compute="_compute_total_premium", store=True)
    total_premium = fields.Float("Total Premium", compute="_compute_total_premium", store=True)
    documents = fields.One2many('policy.document', 'policy_id', string="Attachments")

    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            if rec.dob:
                today = date.today()
                rec.age = today.year - rec.dob.year + 1

    @api.depends('sum_assured', 'basic_rate', 'modal_factor', 'hazardous_rate', 'is_hazardous')
    def _compute_total_premium(self):
        for rec in self:
            if rec.sum_assured and rec.basic_rate and rec.modal_factor:
                rate = rec.basic_rate
                if rec.is_hazardous:
                    rate += (rate * 0.002)

                base_premium = (rec.sum_assured / 1000.0) * rate * rec.modal_factor
                sai = (rec.sum_assured / 1000.0) * rec.hazardous_rate * rec.modal_factor
                policy_fee = 720.0 * rec.modal_factor

                rec.premium = round(base_premium, 2)
                rec.sai = round(sai, 2)
                rec.policy_fee = round(policy_fee, 2)
                rec.total_premium = round(base_premium + sai + policy_fee, 2)