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

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

from models import tocheckoutResponse
from settings_var import *

class tocheckoutPaymentForm(forms.Form):

    sid = forms.CharField(widget=forms.HiddenInput())
    total = forms.CharField(widget=forms.HiddenInput())
    cart_order_id = forms.CharField(widget=forms.HiddenInput())
    first_name = forms.CharField(widget=forms.HiddenInput())
    last_name = forms.CharField(widget=forms.HiddenInput())
    phone = forms.CharField(widget=forms.HiddenInput())
    street_address = forms.CharField(widget=forms.HiddenInput())
    city = forms.CharField(widget=forms.HiddenInput())
    zip = forms.CharField(widget=forms.HiddenInput())
    country = forms.CharField(widget=forms.HiddenInput())
    state = forms.CharField(widget=forms.HiddenInput())
    email = forms.CharField(widget=forms.HiddenInput())
    lang = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(tocheckoutPaymentForm, self).__init__(*args, **kwargs)

    def render(self):
        return mark_safe(u"""<form action="https://www.2checkout.com/checkout/%s" method="post" id="tocheckout_checkout">
            %s
            <input type="image" src="%s" border="0" name="submit" alt="%s" />
        </form>""" % (TOCHECKOUT_CHEKCOUT, self.as_p(), TOCHECKOUT_BUTTON_IMG, TOCHECKOUT_BUTTON_TEXT))
        
    def sandbox(self):
        return mark_safe(u"""<form action="https://www.2checkout.com/checkout/%s" method="post" id="tocheckout_checkout">
            %s
            <input type="image" src="%s" border="0" name="submit" alt="%s" />
            <input type="hidden" name="demo" value="Y" />
        </form>""" % (TOCHECKOUT_CHEKCOUT, self.as_p(), TOCHECKOUT_BUTTON_IMG, TOCHECKOUT_BUTTON_TEXT))
        
class tocheckoutResponseForm(forms.ModelForm):
    Ds_Date = forms.DateField(required=False, input_formats=('%d/%m/%Y',))
    Ds_Hour = forms.TimeField(required=False, input_formats=('%H:%M',))

    class Meta:
        model = tocheckoutResponse
    
