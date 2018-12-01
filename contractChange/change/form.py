# -*- coding: utf-8 -*
from django import forms
from django.core.exceptions import ValidationError
from .models import TMesgRoutExchI2O, TMesgRoutExchI2OSxBuf

class LookUp(forms.Form):

	mesg_incode = forms.CharField(label='mesg_incode')
	sx_or_not = forms.ChoiceField(label='请选择市县', choices=(('sx','市县'),('sbj','省本级')))
	

	def clean(self):
		self.cleaned_data['mesg_incode'] = self.cleaned_data['mesg_incode'].strip()
		if self.cleaned_data['sx_or_not'] == 'sx':
			if TMesgRoutExchO2ISx.objects.filter(mesg_incode__contains=self.cleaned_data['mesg_incode']).exists():
				return self.cleaned_data
			else:
				raise forms.ValidationError('输入的mesg_incode无法在数据库搜索到，请重新输入！')

		elif self.cleaned_data['sx_or_not'] == 'sbj':
			if TMesgRoutExchO2I.objects.filter(mesg_incode__contains=self.cleaned_data['mesg_incode']).exists():
				return self.cleaned_data
			else:
				raise forms.ValidationError('输入的mesg_incode无法在数据库搜索到，请重新输入！')

		else:
			raise forms.ValidationError('未知错误')
	#print(mesg_incode)
	#print(sx_or_not)

class ChangeForm(forms.Form):
	file = forms.FileField(label='修改证明文件')
	supplier_name = forms.CharField(label='供应商名称')
	bank = forms.CharField(label='供应商开户行')
	account = forms.CharField(label='供应商银行账户')

	def clean(self):
		self.cleaned_data['supplier_name'] = self.cleaned_data['supplier_name'].strip()
		self.cleaned_data['bank'] = self.cleaned_data['bank'].strip()
		self.cleaned_data['account'] = self.cleaned_data['account'].strip()
		return self.cleaned_data