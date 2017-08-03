from django import forms

from .models import Tweet

class TweetModelForm(forms.ModelForm):
	content = forms.CharField(label="",
				widget=forms.Textarea(
					attrs={"placeholder": "Your message",
						"class": "form-control"}
						)
				)
	class Meta:
		model = Tweet
		fields = [
			#"user",
			"content"
		]
		#exclude = ["user"]

	#可在此進行篩選
	#def clean_content(self, *args, **kwargs):
	#	content = self.cleaned_data.get("content")
	#	if content == "abc":
	#		raise forms.ValidationError("Can't be abc")
	#	return content
