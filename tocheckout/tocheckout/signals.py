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

"""
Note that sometimes you will get duplicate signals emitted, depending on configuration of your systems. 
If you do encounter this, you will need to add the "dispatch_uid" to your connect handlers:
http://code.djangoproject.com/wiki/Signals#Helppost_saveseemstobeemittedtwiceforeachsave
"""

# Not available IPN from 2checkout

from django.dispatch import Signal

# Sent when a payment is successfully processed.
payment_was_successful = Signal()

# Sent when a payment is error.
payment_was_error = Signal()

# Sent when a signature is not valid
signature_error = Signal()
