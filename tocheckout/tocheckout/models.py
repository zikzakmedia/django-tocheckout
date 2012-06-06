# -*- encoding: utf-8 -*-
############################################################################################
#
#    Django 2Checkout Payments 
#    Copyright (C) 2012 Zikzakmedia S.L. (<http://www.zikzakmedia.com>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################################

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

#import hashlib TODO

RESULT_ACTIVE = 0
RESULT_INACTIVE = 2

RESULT_CHOICES = (
    (RESULT_ACTIVE, _('Correct')),
    (RESULT_INACTIVE, _('Invalid')),
)

class tocheckoutResponse(models.Model):
    
    creation_date = models.DateTimeField(auto_now_add=True)
    
    result = models.IntegerField(_('Result'), choices=RESULT_CHOICES, default=RESULT_CHOICES,) #0 -> transaccin autorizada / 2 -> Transaccion fallida
    transaction = models.CharField(_('Transaction'), max_length=12) # transaction ID
    total = models.CharField(_('Transaction'), max_length=12) # total

