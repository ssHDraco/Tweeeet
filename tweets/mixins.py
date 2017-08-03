from django import forms
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

class FormUserNeededMixin(object):
	def form_valid(self, form):
		if self.request.user.is_authenticated():
			form.instance.user = self.request.user
			return super(FormUserNeededMixin, self).form_valid(form)
		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue."])
			return self.form_invalid(form)

class UserOwnerMixin(object):
	def form_valid(self, form):
		if form.instance.user == self.request.user:
			print("does work")
			return super(UserOwnerMixin, self).form_valid(form)
		else:
			form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["This user is not allowed to change the data."])
			return self.form_invalid(form)

	def delete(self, request, *args, **kwargs):
		if self.get_object().user == self.request.user:
			return super(UserOwnerMixin, self).delete(request, *args, **kwargs)
		else:
			raise ValidationError("Can't delete other user's tweet!")
