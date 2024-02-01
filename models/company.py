# -*- coding: utf-8 -*-
from datetime import timedelta, datetime, date
from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = "res.company"

    def _get_user_fiscal_lock_date(self):
        """The original method is overridden to obtain the fiscal closing date with a new user group"""
        """Get the fiscal lock date for this company depending on the user"""
        self.ensure_one()
        lock_date = max(self.period_lock_date or date.min, self.fiscalyear_lock_date or date.min)
        if self.user_has_groups('int_account_lock.accountant_role'):
            lock_date = self.fiscalyear_lock_date or date.min
        return lock_date
