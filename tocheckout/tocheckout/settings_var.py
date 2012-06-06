# -*- encoding: utf-8 -*-
############################################################################################
#
#    Django 2 Checkout
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

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

TOCHECKOUT_SID = getattr(settings, "TOCHECKOUT_SID", "532001") # seller identification number
TOCHECKOUT_SECRET_WORD = getattr(settings, "TOCHECKOUT_SECRET_WORD", "12345") # secret word
TOCHECKOUT_CHEKCOUT = getattr(settings, "TOCHECKOUT_CHEKCOUT", "spurchase") #spurchase or purchase
TOCHECKOUT_BUTTON_IMG = getattr(settings, "TOCHECKOUT_BUTTON_IMG", "/static/images/icons/tocheckout.png")
TOCHECKOUT_BUTTON_TEXT = getattr(settings, "TOCHECKOUT_BUTTON_TEXT", _("Buy now"))
