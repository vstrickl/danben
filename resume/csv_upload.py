import csv

from io import TextIOWrapper
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import CsvUploadForm

def handle_csv_upload(
        request: HttpRequest,
        model_class,
        success_url,
        form_class,
        field_mapping,
        template_name,
        context=None
):
    if context is None:
        context = {}

    if request.method == 'POST':
        form = CsvUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']

            csv_file_text = TextIOWrapper(csv_file, encoding='utf-8')
            reader = csv.reader(csv_file_text, delimiter=',')

            for row in reader:
                if len(row) < len(field_mapping):
                    continue
            
                model_fields = {}
                for field, i in field_mapping.items():
                    if i < len(row):
                        model_fields[field] = row[i]
                    else:
                        model_fields[field] = None

                model_class.objects.create(**model_fields)

            return redirect(success_url)
        
    else:
        form = form_class()
        context['form'] = form

    return render(request, template_name, context)