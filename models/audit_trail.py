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


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(ResPartner, self).create(vals)
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'record_id': record.id,
            'user_id': self.env.user.id,
            'action': 'create',
            'record_name': self.name,
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        print('write method')
        result = super(ResPartner, self).write(vals)
        self.env['audit.trail'].create({
            'name': 'Write Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'write',
            'record_name': self.name,
            'changes': str(vals),
        })
        return result

    def unlink(self):
        for record in self:
            if self.env.user not in self.env['audit.trail'].exclude_users:
                self.env['audit.trail'].create({
                    'name': 'Delete Record',
                    'model': self._name,
                    'record_id': record.id,
                    'user_id': self.env.user.id,
                    'action': 'unlink',
                    'record_name': self.name,
                    'changes': 'Record deleted',
                })

        return super(ResPartner, self).unlink()


class LeadsLogic(models.Model):
    _inherit = 'leads.logic'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(LeadsLogic, self).create(vals)
        record_name = vals.get('name', '')
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'record_id': record.id,
            'record_name': record_name,
            'user_id': self.env.user.id,
            'action': 'create',
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        print('write method')
        result = super(LeadsLogic, self).write(vals)
        self.env['audit.trail'].create({
            'name': 'Write Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'record_name': self.name,
            'action': 'write',
            'changes': str(vals),
        })
        return result

    def unlink(self):
        for record in self:
            if self.env.user not in self.env['audit.trail'].exclude_users:
                self.env['audit.trail'].create({
                    'name': 'Delete Record',
                    'model': self._name,
                    'record_id': record.id,
                    'user_id': self.env.user.id,
                    'action': 'unlink',
                    'record_name': self.name,
                    'changes': 'Record deleted',
                })

        return super(LeadsLogic, self).unlink()


class PaymentRequest(models.Model):
    _inherit = 'payment.request'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(PaymentRequest, self).create(vals)
        record_name = vals.get('name', '')
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'record_id': record.id,
            'record_name': record_name,
            'user_id': self.env.user.id,
            'action': 'create',
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        print('write method')
        result = super(PaymentRequest, self).write(vals)
        self.env['audit.trail'].create({
            'name': 'Write Record',
            'model': self._name,
            'record_id': self.id,
            'record_name': self.source_type + ''+ self.seminar_executive,
            'user_id': self.env.user.id,
            'action': 'write',
            'changes': str(vals),
        })
        return result

    def unlink(self):

        self.env['audit.trail'].create({
            'name': 'Delete Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'unlink',
            'record_name': self.source_type + '' + self.seminar_executive,
            'changes': 'Record deleted',
        })
        return super(PaymentRequest, self).unlink()
