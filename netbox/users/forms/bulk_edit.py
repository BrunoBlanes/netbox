from django import forms
from django.utils.translation import gettext as _

from netbox.forms import NetBoxModelBulkEditForm
from users.models import *
from utilities.forms import add_blank_choice
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField
from utilities.forms import BootstrapMixin
from utilities.forms.widgets import DatePicker, NumberWithOptions

__all__ = (
    'ObjectPermissionBulkEditForm',
    'UserBulkEditForm',
)


class UserBulkEditForm(BootstrapMixin, forms.Form):
    pk = forms.ModelMultipleChoiceField(
        queryset=None,  # Set from self.model on init
        widget=forms.MultipleHiddenInput
    )
    first_name = forms.CharField(
        max_length=150,
        required=False
    )
    last_name = forms.CharField(
        max_length=150,
        required=False
    )
    is_active = forms.BooleanField(
        required=False,
        label=_('Active')
    )
    is_staff = forms.BooleanField(
        required=False,
        label=_('Staff status')
    )
    is_superuser = forms.BooleanField(
        required=False,
        label=_('Superuser status')
    )

    model = NetBoxUser
    fieldsets = (
        (None, ('first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')),
    )
    nullable_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pk'].queryset = self.model.objects.all()


class ObjectPermissionBulkEditForm(BootstrapMixin, forms.Form):
    pk = forms.ModelMultipleChoiceField(
        queryset=None,  # Set from self.model on init
        widget=forms.MultipleHiddenInput
    )
    description = forms.CharField(
        max_length=200,
        required=False
    )
    enabled = forms.BooleanField(
        required=False,
    )

    model = ObjectPermission
    fieldsets = (
        (None, ('description', 'enabled')),
    )
    nullable_fields = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pk'].queryset = self.model.objects.all()
