from django import forms
from django.core.exceptions import ValidationError

from flower_app.models import Flower


class FlowerForm(forms.ModelForm):
    months = [
        (1, 'January'), (2, 'Februar'), (3, 'März'),
        (4, 'April'), (5, 'Mai'), (6, 'Juni'), (7, 'Juli'),
        (8, 'August'), (9, 'September'), (10, 'Oktober'),
        (11, 'November'), (12, 'Dezember')
    ]
    start_date = forms.ChoiceField(choices=months)
    end_date = forms.ChoiceField(choices=months)

    class Meta:
        model = Flower
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # Check if both start_date and end_date are provided
        if start_date and end_date:
            start_month = int(start_date)
            end_month = int(end_date)

            # Validate that start_date is less than or equal to end_date
            if start_month > end_month:
                raise ValidationError("Start date cannot be later than end date.")

        return cleaned_data
