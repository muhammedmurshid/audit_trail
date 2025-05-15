from odoo import fields,api,models,_

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
            'description': self._description,
            'record_name': self.name,
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(ResPartner, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'user_id': self.env.user.id,
                'action': 'write',
                'description': self._description,
                'record_name': record.name,
                'old_value': old_vals,
                'changed_value': new_vals,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
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
                    'description': self._description,
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
            'description': self._description,
            'user_id': self.env.user.id,
            'action': 'create',
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(LeadsLogic, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'user_id': self.env.user.id,
                'old_value': old_vals,
                'changed_value': new_vals,
                'action': 'write',
                'description': self._description,
                'record_name': record.name,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
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
                    'description': self._description,
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
            'description': self._description,
            'user_id': self.env.user.id,
            'action': 'create',
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(PaymentRequest, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'user_id': self.env.user.id,
                'action': 'write',
                'old_value': old_vals,
                'changed_value': new_vals,
                'description': self._description,
                'record_name': record.name,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
            })

        return result

    def unlink(self):
        self.env['audit.trail'].create({
            'name': 'Delete Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'unlink',
            'description': self._description,
            'record_name': self.source_type + '' + self.seminar_executive,
            'changes': 'Record deleted',
        })
        return super(PaymentRequest, self).unlink()

class StudentsRefund(models.Model):
    _inherit = 'student.refund'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(StudentsRefund, self).create(vals)
        record_name = vals.get('student_name', '')
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'record_id': record.id,
            'record_name': record_name,
            'user_id': self.env.user.id,
            'action': 'create',
            'description': self._description,
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(StudentsRefund, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'user_id': self.env.user.id,
                'action': 'write',
                'old_value': old_vals,
                'changed_value': new_vals,
                'description': self._description,
                'record_name': record.name,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
            })

        return result

    def unlink(self):
        self.env['audit.trail'].create({
            'name': 'Delete Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'unlink',
            'description': self._description,
            'record_name': self.student_name,
            'changes': 'Record deleted',
        })
        return super(StudentsRefund, self).unlink()

class FeeQuickPay(models.Model):
    _inherit = 'fee.quick.pay'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(FeeQuickPay, self).create(vals)
        record_name = vals.get('name', '')
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'record_id': record.id,
            'record_name': record_name,
            'description': self._description,
            'user_id': self.env.user.id,
            'action': 'create',
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(FeeQuickPay, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'user_id': self.env.user.id,
                'action': 'write',
                'description': self._description,
                'record_name': record.name,
                'old_value': old_vals,
                'changed_value': new_vals,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
            })

        return result

    def unlink(self):
        self.env['audit.trail'].create({
            'name': 'Delete Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'unlink',
            'record_name': self.name,
            'description': self._description,
            'changes': 'Record deleted',
        })
        return super(FeeQuickPay, self).unlink()

class BaseBatches(models.Model):
    _inherit = 'op.batch'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(BaseBatches, self).create(vals)
        record_name = vals.get('name', '')
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'record_id': record.id,
            'record_name': record_name,
            'user_id': self.env.user.id,
            'description': self._description,
            'action': 'create',
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(BaseBatches, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'user_id': self.env.user.id,
                'action': 'write',
                'record_name': record.name,
                'old_value': old_vals,
                'changed_value': new_vals,
                'description': self._description,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
            })

        return result

    def unlink(self):
        self.env['audit.trail'].create({
            'name': 'Delete Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'unlink',
            'record_name': self.name,
            'description': self._description,
            'changes': 'Record deleted',
        })
        return super(BaseBatches, self).unlink()

class OpCourse(models.Model):
    _inherit = 'op.course'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(OpCourse, self).create(vals)
        record_name = vals.get('name', '')
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'record_id': record.id,
            'record_name': record_name,
            'user_id': self.env.user.id,
            'description': self._description,
            'action': 'create',
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(OpCourse, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'user_id': self.env.user.id,
                'action': 'write',
                'old_value': old_vals,
                'changed_value': new_vals,
                'record_name': record.name,
                'description': self._description,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
            })

        return result

    def unlink(self):
        self.env['audit.trail'].create({
            'name': 'Delete Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'unlink',
            'record_name': self.name,
            'changes': 'Record deleted',
            'description': self._description,
        })
        return super(OpCourse, self).unlink()

class OpDepartment(models.Model):
    _inherit = 'op.department'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(OpDepartment, self).create(vals)
        record_name = vals.get('name', '')
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'description': self._description,
            'record_id': record.id,
            'record_name': record_name,
            'user_id': self.env.user.id,
            'action': 'create',

            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(OpDepartment, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'user_id': self.env.user.id,
                'action': 'write',
                'description': self._description,
                'record_name': record.name,
                'old_value': old_vals,
                'changed_value': new_vals,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
            })

        return result

    def unlink(self):
        self.env['audit.trail'].create({
            'name': 'Delete Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'unlink',
            'description': self._description,
            'record_name': self.name,
            'changes': 'Record deleted',
        })
        return super(OpDepartment, self).unlink()

class OpBranches(models.Model):
    _inherit = 'op.branch'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(OpBranches, self).create(vals)
        record_name = vals.get('name', '')
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'record_id': record.id,
            'record_name': record_name,
            'user_id': self.env.user.id,
            'action': 'create',
            'description': self._description,
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(OpBranches, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'description': self._description,
                'user_id': self.env.user.id,
                'action': 'write',
                'old_value': old_vals,
                'changed_value': new_vals,
                'record_name': record.name,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
            })

        return result

    def unlink(self):
        self.env['audit.trail'].create({
            'name': 'Delete Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'unlink',
            'record_name': self.name,
            'description': self._description,
            'changes': 'Record deleted',
        })
        return super(OpBranches, self).unlink()

class RefundPayment(models.Model):
    _inherit = 'refund.payment'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(RefundPayment, self).create(vals)
        record_name = vals.get('name', '')
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'record_id': record.id,
            'record_name': record_name,
            'user_id': self.env.user.id,
            'action': 'create',
            'description': self._description,
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(RefundPayment, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'user_id': self.env.user.id,
                'action': 'write',
                'old_value': old_vals,
                'changed_value': new_vals,
                'record_name': record.name,
                'description': self._description,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
            })

        return result

    def unlink(self):
        self.env['audit.trail'].create({
            'name': 'Delete Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'unlink',
            'record_name': self.name,
            'description': self._description,
            'changes': 'Record deleted',
        })
        return super(RefundPayment, self).unlink()

class InvoiceReports(models.Model):
    _inherit = 'invoice.reports'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(InvoiceReports, self).create(vals)
        record_name = vals.get('name', '')
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'record_id': record.id,
            'record_name': record_name,
            'user_id': self.env.user.id,
            'action': 'create',
            'description': self._description,
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(InvoiceReports, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'user_id': self.env.user.id,
                'action': 'write',
                'old_value': old_vals,
                'changed_value': new_vals,
                'record_name': record.name,
                'description': self._description,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
            })

        return result

    def unlink(self):
        self.env['audit.trail'].create({
            'name': 'Delete Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'unlink',
            'record_name': self.name,
            'description': self._description,
            'changes': 'Record deleted',
        })
        return super(InvoiceReports, self).unlink()

class ReceiptReports(models.Model):
    _inherit = 'receipts.report'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(ReceiptReports, self).create(vals)
        record_name = vals.get('name', '')
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'record_id': record.id,
            'record_name': record_name,
            'user_id': self.env.user.id,
            'action': 'create',
            'description': self._description,
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(ReceiptReports, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'user_id': self.env.user.id,
                'action': 'write',
                'old_value': old_vals,
                'changed_value': new_vals,
                'record_name': record.name,
                'description': self._description,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
            })

        return result

    def unlink(self):
        self.env['audit.trail'].create({
            'name': 'Delete Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'unlink',
            'record_name': self.name,
            'description': self._description,
            'changes': 'Record deleted',
        })
        return super(ReceiptReports, self).unlink()

class SeminarLeadsAudit(models.Model):
    _inherit = 'seminar.leads'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(SeminarLeadsAudit, self).create(vals)
        record_name = vals.get('institute_name', '')
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'record_id': record.id,
            'record_name': record_name,
            'user_id': self.env.user.id,
            'action': 'create',

            'description': self._description,
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(SeminarLeadsAudit, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'user_id': self.env.user.id,
                'action': 'write',
                'old_value': old_vals,
                'changed_value': new_vals,
                'record_name': record.institute_name,
                'description': self._description,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
            })

        return result

    def unlink(self):
        self.env['audit.trail'].create({
            'name': 'Delete Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'unlink',
            'record_name': self.institute_name,
            'description': self._description,
            'changes': 'Record deleted',
        })
        return super(SeminarLeadsAudit, self).unlink()

class EmployeeAudit(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def create(self, vals):
        print('create method')
        record = super(EmployeeAudit, self).create(vals)
        record_name = vals.get('name', '')
        self.env['audit.trail'].create({
            'name': 'Create Record',
            'model': self._name,
            'record_id': record.id,
            'record_name': record_name,
            'user_id': self.env.user.id,
            'action': 'create',
            'description': self._description,
            'changes': str(vals),
        })
        return record

    def write(self, vals):
        for record in self:
            # Capture old values before the write
            old_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(old_vals, 'old vals')
            result = super(EmployeeAudit, record).write(vals)

            # Capture new values after the write
            new_vals = {
                field: record[field]
                for field in vals.keys()
                if field in record._fields
            }
            print(new_vals, 'new vals')

            # Create audit trail for each record individually
            self.env['audit.trail'].create({
                'name': 'Write Record',
                'model': record._name,
                'record_id': record.id,
                'user_id': self.env.user.id,
                'action': 'write',
                'old_value': old_vals,
                'changed_value': new_vals,
                'record_name': record.name,
                'description': self._description,
                'changes': f"Old: {old_vals}\nNew: {new_vals}",
            })

        return result

    def unlink(self):
        self.env['audit.trail'].create({
            'name': 'Delete Record',
            'model': self._name,
            'record_id': self.id,
            'user_id': self.env.user.id,
            'action': 'unlink',
            'record_name': self.name,
            'description': self._description,
            'changes': 'Record deleted',
        })
        return super(EmployeeAudit, self).unlink()