# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .form import *
from .models import *

# Create your views here.
def index(request):

	'''
	for i in TMesgRoutExchO2I.objects.raw("select exchmesgid.nextval as nextid, mesg_id from t_Mesg_Rout_Exch_O2i where mesg_incode = '1000000117611'"):
		print(i.mesg_type)
		print(i.nextid)
	'''
	if request.method == 'GET':
		index = LookUp()
		return render(request,'index.html',locals())
	else:
		lookfor = LookUp(request.POST)
		#print(lookfor.cleaned_data['mesg_incode'])
		if lookfor.is_valid():
			mesg_incode = lookfor.cleaned_data['mesg_incode']
			sx_or_not = lookfor.cleaned_data['sx_or_not']

			#print(sx_or_not)
			if sx_or_not == 'sx':
				msg = TMesgRoutExchO2ISx.objects.filter(mesg_incode__contains=mesg_incode)
			elif sx_or_not == 'sbj':
				msg = TMesgRoutExchO2I.objects.filter(mesg_incode__contains=mesg_incode)

			print(msg)
			return render(request,'contractList.html', locals())
		else:
			error_msg = lookfor.errors.as_json()
			print(error_msg)
			return render(request, 'index.html', locals())