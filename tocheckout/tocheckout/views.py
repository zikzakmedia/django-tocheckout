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

from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from tocheckout.tocheckout.signals import *
from tocheckout.tocheckout.forms import tocheckoutResponseForm

# Not available IPN from 2checkout

# @csrf_exempt
# def tocheckout_ipn(request):
# 
    # form = tocheckoutResponseForm(request.GET)
    # if form.is_valid():
        # tocheckout_resp = form.save()
        # payment_was_successful.send(sender=tocheckout_resp)
# 
        # if request.GET['result'] == 0:
            # payment_was_successful.send(sender=tocheckout_resp)
        # else:
            # payment_was_error.send(sender=tocheckout_resp)
# 
    # return HttpResponse()
