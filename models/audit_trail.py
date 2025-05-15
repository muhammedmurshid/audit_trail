from odoo import models, fields, api


class AuditTrail(models.Model):
    _name = 'audit.trail'
    _description = 'Audit Trail'

    name = fields.Char(string='Name')
    model = fields.Char(string='Model')
    record_id = fields.Integer(string='Record ID')
    user_id = fields.Many2one('res.users', string='User')
    action = fields.Selection([
        ('create', 'Create'),
        ('write', 'Write'),
        ('unlink', 'Delete')
    ], string='Action')
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    changes = fields.Text(string='Changes')
    record_name = fields.Char(string="Record Name")
    old_value = fields.Char(string="Old Value")
    changed_value = fields.Char(string="Changed Value")
    description = fields.Char(string="Description")
    changes_short = fields.Char(string='Changes (short)', compute='_compute_changes_short')
    changes_old = fields.Char(string='Old Value', compute='_compute_changes_short')
    changes_new = fields.Char(string='Changed Value', compute='_compute_changes_short')

    @api.depends('old_value','changed_value')
    def _compute_changes_short(self):
        for rec in self:
            if rec.changes:
                rec.changes_short = rec.changes[:70] + '...' if len(rec.changes) > 70 else rec.changes
            else:
                rec.changes_short = ''
            if rec.old_value:
                rec.changes_old = rec.old_value[:70] + '...' if len(rec.old_value) > 70 else rec.old_value
            else:
                rec.changes_old = ''
            if rec.changed_value:
                rec.changes_new = rec.changed_value[:70] + '...' if len(rec.changed_value) > 70 else rec.changed_value
            else:
                rec.changes_new = ''