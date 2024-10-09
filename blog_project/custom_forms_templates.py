from django.forms.utils import ErrorList
from django.forms.renderers import TemplatesSetting

class CustomFormRenderer(TemplatesSetting):
    form_template_name = 'form_templates/custom_form.html'

class BootstrapErrorList(ErrorList):
    template_name = 'form_error/bootstrap_error.html'
    # template_name = 'form_templates/bootstrap_error.html' # doesn't work