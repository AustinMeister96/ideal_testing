from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import ParticipantForm, QuestionForm, Breath_Collection_Form, Blood_Collection_Form, Lab_Processing_Form, Exposure_Form, Exposure_Form2, Exposure_Form3, Indirect_costs_form, Mandatory_questionaire_form, SearchForm, CT_Scan_Form, CancerHistoryForm, Mandatory_questionaire_form_c, Mandatory_questionaire_form_de, Mandatory_questionaire_form_fg, inclusion_form, testParticipantForm, MyForm, CT_Scan_Nodule_Form_1, CT_Scan_Nodule_Form_2, annual_study_update_part_a_form, annual_study_update_part_b_form, annual_study_update_medications_form
from .models import Participant, Question, Breath_Collection, Blood_Collection, lab_processing, Indirect_costs, Mandatory_questionaire, ct_scan, ct_scan_nodule_1, ct_scan_nodule_2, ct_scan_nodule_3, ct_scan_nodule_4, ct_scan_nodule_5, Exposure, Exposure2, Exposure3, Mandatory_questionaire_c, Mandatory_questionaire_de, Mandatory_questionaire_fg, inclusion,  testParticipant, UserAccounts, Exposure, Exposure2, Exposure3, Mandatory_questionaire, Mandatory_questionaire_c, Mandatory_questionaire_de, Mandatory_questionaire_fg, inclusion,  testParticipant, UserAccounts,PLCO_score, annual_study_update_part_a, annual_study_update_part_b, annual_study_update_medications, annual_study_update, last_mandatory_questionnaire
from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory
from .forms import biological_relatives_with_cancer_form, plco_score_form, ParticipantSearchForm, CT_Scan_Nodule_Form_3, CT_Scan_Nodule_Form_4, CT_Scan_Nodule_Form_5, annual_study_update_part_b_form, annual_study_update_part_a_form, annual_study_update_form, last_mandatory_questionnaire_form
##from django.core.exceptions import ObjectDoesNotExist
import csv
from django.http import HttpResponseRedirect as redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.sessions.models import Session
import re
from django.http import FileResponse
from pdfrw import PdfReader, PdfWriter, IndirectPdfDict
import json
from django.db.models import Q
from django.db import IntegrityError
from django.contrib import messages
from .models import History, biological_relatives_with_cancer
from django.views.generic.edit import CreateView, UpdateView
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.template.loader import get_template
from django.views.generic import View
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
import json
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib import styles
from django.contrib.staticfiles import finders
from django.http import JsonResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.contrib import messages


def download_pdf(request):
    pdf_path = finders.find('your_file.pdf')
    print('Working here 1')
    if pdf_path:
        with open(pdf_path, 'rb') as pdf_file:
            print('working here')
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="your_file.pdf"'
            return response
    else:
        return HttpResponse("PDF file not found.", status=404)


class GeneratePDF2(View):
    def get(self, request, *args, **kwargs):
        form_data = get_form_data(request)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="data.pdf"'

        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        
        elements = []
        elements.append(Paragraph("Form Data PDF", styles['Title']))
        elements.append(Paragraph("Below is the data submitted in the form:", styles['Normal']))
        
        for field, value in form_data.items():
            field_line = f"<strong>{field}:</strong> {value}<br/>"
            elements.append(Paragraph(field_line, styles['Normal']))

        doc.build(elements)
        pdf = buffer.getvalue()
        buffer.close()

        response.write(pdf)
        return response


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        form_data_json = request.session.get('form_data')
        if form_data_json:
            form_data = json.loads(form_data_json)
            form_data_string = "\n".join([f"{key}: {value}" for key, value in form_data.items()])

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="data.pdf"'

            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            styles = getSampleStyleSheet()

            elements = []
            elements.append(Paragraph("Form Data PDF", styles['Title']))
            elements.append(Paragraph("Below is the data submitted in the form:", styles['Normal']))
            elements.append(Paragraph(form_data_string, styles['Normal'])) 

            doc.build(elements)
            pdf = buffer.getvalue()
            buffer.close()

            response.write(pdf)
            return response
        else:
            return HttpResponse("Form data not available.")


def generate_pdf_oldNotWorking(data):
    print('working here')
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    for field_name, value in data.items():
        if field_name != 'csrfmiddlewaretoken':
            field_label = field_name.replace('_', ' ').title()
            elements.append(f'{field_label}: {value}')

    doc.build(elements)
    buffer.seek(0)
    return buffer

def generate_pdf(data):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []
    paragraph_style = styles.getSampleStyleSheet()['Normal']
    for field_name, value in data.items():
        if field_name != 'csrfmiddlewaretoken':
            field_label = field_name.replace('_', ' ').title()
            paragraph_text = f'<b>{field_label}:</b> {value}'
            paragraph = Paragraph(paragraph_text, style=paragraph_style)
            elements.append(paragraph)

    doc.build(elements)
    buffer.seek(0)
    print('working pdf here')
    return buffer

def get_form_data(request):
    form_data = {
        'Visit Date': request.POST.get('{form.visit_date}', ''),
        'Postal Code': request.POST.get('postal_code', ''),
        'Date of Birth': request.POST.get('date_of_birth', ''),
        'Current Age': request.POST.get('current_age', ''),
        'Current Height': request.POST.get('current_height', ''),
        'Current Height Unit': request.POST.get('current_height_unit', ''),
        'Current Weight': request.POST.get('current_weight', ''),
        'Current Weight Unit': request.POST.get('current_weight_unit', ''),
        'Sex at Birth': request.POST.get('sex_birth', ''),
        'Gender Identity': request.POST.get('gender_identity', ''),
        'Ethnicity': request.POST.get('ethnicity', ''),
        'Ethnicity (Other)': request.POST.get('ethnicity_other', ''),
        'Born in Canada': request.POST.get('born_in_canada', ''),
        'Year Moved to Canada': request.POST.get('year_moved_to_canada', ''),
        'Birthplace': request.POST.get('birthplace', ''),
        'Highest Education Level': request.POST.get('highest_education_lvl', ''),
        'Highest Education Level (Other)': request.POST.get('highest_education_lvl_other', ''),
    }
    return form_data

@login_required(login_url='login')
def index(request):
    form = ParticipantForm
    return render(request, 'DataEntry/index.html', {'form': form})

@login_required(login_url='login')
def index_participant(request, participant_id=None):
    form = ParticipantForm()
    request.session['participant_id'] = participant_id
    
    if participant_id:
        request.session['participant_id'] = participant_id
    
    context = {
        'form': form,
        'participant_number': participant_id,
    }

    return render(request, 'DataEntry/index_participant.html', context)

@login_required(login_url='login')
def search_and_add(request):
    form = ParticipantSearchForm()

    if request.method == 'POST':
        form = ParticipantSearchForm(request.POST)
        if form.is_valid():
            participant_number = form.cleaned_data['participant_number']

            try:
                participant = Participant.objects.get(participant_number=participant_number)
                request.session['participant_num'] = participant.participant_number
                return render(request, 'search_result.html', {'participant': participant})
            except Participant.DoesNotExist:
                pass

    return render(request, 'search_page.html', {'form': form})

@login_required(login_url='login')
def add_inclusion(request):
    participant_form = ParticipantForm(request.POST)
    if request.method == 'POST':
        if participant_form.is_valid():
            participant_num = participant_form.cleaned_data['participant_number']
            participant, created = Participant.objects.get_or_create(participant_number=participant_num)
            if created:
                participant_num = participant_form.cleaned_data['participant_number']
                participant_num = participant_num.replace('-', '0')
                participant, created = Participant.objects.get_or_create(participant_number=participant_num)

        else:
            participant_num = request.POST.get('participant_number')
            return HttpResponseRedirect(reverse('add_inclusion_participant', args=[participant_num]))
        
    else:
        print(participant_form.errors)
        participant_form = ParticipantForm()
    
    context = {
        'participant_form': participant_form,
    }

    return render(request, 'DataEntry/inclusion.html', context)


def generate_pdf(request, participant_id):
    print("Generating PDF for participant ID:", participant_id)
    participant = get_object_or_404(Participant, participant_number=participant_id)
    inclusion_data = inclusion.objects.filter(participant_num=participant).first()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{participant_id}_report.pdf"'

    p = canvas.Canvas(response)

    p.drawString(100, 750, "Participant Report")
    p.drawString(100, 730, f"Participant ID: {participant_id}")
    p.drawString(100, 710, "Participant Data:")

    if inclusion_data:
        p.drawString(100, 690, f"Field 1: {inclusion_data.field1}")
        p.drawString(100, 670, f"Field 2: {inclusion_data.field2}")
    p.showPage()
    p.save()
    return response


@login_required(login_url='login')
def add_inclusion_participant(request, participant_id=None):
    if participant_id:
        participant = get_object_or_404(Participant, participant_number=participant_id)
        inclusion_data = inclusion.objects.filter(participant_num=participant).first()
        print(participant)
        print('the participant number is: ')
        print(participant_id)

    if request.method == 'POST':
            form = inclusion_form(request.POST, request.FILES, instance=inclusion_data)
            form.participant_num = participant_id
            if form.is_valid():
                print('form is valid')
                print(request.FILES)
                if 'consent_form' in form.fields:
                    consent_form_url = form.cleaned_data['consent_form']
                    form.instance.consent_form_path = consent_form_url
                form.save(commit=False)
                form.participant_number = participant
                form.save()
                print('data saved')
                return HttpResponseRedirect(reverse('add_inclusion_participant', args=[participant_id]) + '?submitted=True')
            
    elif 'generate_pdf' in request.POST:
        return generate_pdf(request, participant_id)
    elif 'submit' in request.POST:
        print('something')

    else:
        form = inclusion_form(instance=inclusion_data)
        print('errors here')
        print(form.errors)

    context = {
        'form': form,
        'participant_id': participant_id,

    }
    print(form.errors)
    return render(request, 'DataEntry/inclusion_participant.html', context)


@login_required(login_url='login')
def add_inclusion_participant_old(request, participant_id=None):
    if participant_id:
        participant = get_object_or_404(Participant, participant_number=participant_id)
        inclusion_data = inclusion.objects.filter(participant_num=participant).first()
        print(participant)
        print('the participant number is: ')
        print(participant_id)

    if not participant_id:
        participant = None
        inclusion_data = None
        print('reaching here')
        print(participant_id)

    if request.method == 'POST':
        if 'generate_pdf' in request.POST:
            return generate_pdf(request, participant_id)
        elif 'submit' in request.POST:

            form = inclusion_form(request.POST, request.FILES, instance=inclusion_data)
            form.participant_num = participant_id
            if form.is_valid():
                print('form is valid')
                print(request.FILES)
                if 'consent_form' in form.fields:
                    print('reaching here')
                    consent_form_url = form.cleaned_data['consent_form']
                    form.instance.consent_form_path = consent_form_url
                form.participant_number = participant_id
                form.save()
                return HttpResponseRedirect(reverse('add_inclusion_participant', args=[participant_id]) + '?submitted=True')


    
    else:
        form = inclusion_form(instance=inclusion_data)
        print(form.fields)
        print(form.errors)

    context = {
        'form': form,
    }
    print(form.errors)
    return render(request, 'DataEntry/inclusion_participant.html', context)
    

def add_inclusion_participant_old(request, participant_num=None):
    participant = None 
    form = inclusion_form()
    if request.method == 'POST':
       
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('add_inclusion_participant', args=[participant_num]) + '?submitted=True')
            
    else:
        
        form = inclusion_form(instance=participant)  
        print(form.errors)

    context = {
        'form': form,
         
    }

    return render(request, 'DataEntry/inclusion_participant.html', context)


def add_inclusion_oldSept29(request, participant_num=None):
    participant_already_exists = False
    
    if request.method == 'POST':
        participant_form = ParticipantForm(request.POST)
        
        if participant_form.is_valid():
            participant_num = participant_form.cleaned_data['participant_number']
            cleaned_participant_num = participant_num.replace('-', '0')
            
            participant, created = Participant.objects.get_or_create(
                participant_number=cleaned_participant_num
                
            )
            if created:
                return redirect(f'/DataEntry/add_inclusion/{cleaned_participant_num}/')
            else:
                participant_already_exists = True
                print("This participant number has already been used")
        else:
            print("Participant Form Errors:", participant_form.errors)
            return JsonResponse({'error': participant_form.errors}, status=400)

    else:
        participant_form = ParticipantForm()

    context = {
        'participant_form': participant_form,
        'participant_already_exists': participant_already_exists,
    }

    return render(request, 'DataEntry/inclusion.html', context)


def add_inclusion_workingParticipantOnly(request):
    if request.method == 'POST':
        participant_form = ParticipantForm(request.POST)

        if participant_form.is_valid():
            participant_num = participant_form.cleaned_data['participant_number']
            print(participant_num)
            cleaned_participant_num = participant_num.replace('-', '0')
            print(cleaned_participant_num)
            participant, created = Participant.objects.get_or_create(
                participant_number=cleaned_participant_num
            )

        else:
            print("Participant Form Errors:", participant_form.errors)
            return JsonResponse({'error': participant_form.errors}, status=400)

    else:
        participant_form = ParticipantForm()

    context = {
        'participant_form': participant_form,
    }
    return render(request, 'DataEntry/inclusion.html', context)




def generate_word_document(data):
    doc = Document()
    doc.add_heading('Mandatory Questionnaire', level=1)
    return doc

@login_required(login_url='login')
def add_mandatory_questionaire(request, participant_id=None):
    print("View accessed!")
    if participant_id: 
        participant = get_object_or_404(Participant, participant_number=participant_id)
        mandatory_questionaire_data = Mandatory_questionaire.objects.filter(participant_num=participant).first()
        print('the participant number is: ', participant_id)
    
    #RelativeCancerFormSet = modelformset_factory(biological_relatives_with_cancer, form=biological_relatives_with_cancer_form, extra=1)
    
    if request.method == 'POST':
        form = Mandatory_questionaire_form(request.POST, instance=mandatory_questionaire_data)
        #formset = RelativeCancerFormSet(request.POST, prefix='relatives')

        if form.is_valid(): 
            print('form is valid')
            if not participant:
                participant = Participant.objects.create(participant_number=participant_id)
            
            mandatory_questionaire = form.save(commit=False)
            mandatory_questionaire.participant_num = participant
            mandatory_questionaire.save()
            

            # instances = formset.save(commit=False)
            # for instance in instances:
            #     instance.mandatory_questionaire = mandatory_questionaire
            #     instance.save()

            word_doc = generate_word_document(form.cleaned_data)
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = f'attachment; filename=mandatory_questionnaire.docx'
            word_doc.save(response)
            messages.success(request, 'Data saved successfully.')
            return HttpResponseRedirect(reverse('add_mandatory_questionaire', args=[participant_id]) + '?submitted=True')
        else:
            print(form.errors)
            #print(formset.errors)

    elif 'generate_pdf' in request.GET:  
        print('button pressed')
        form = Mandatory_questionaire_form(instance=mandatory_questionaire_data) 
        if mandatory_questionaire_data:
            print('yes')
            #formset = RelativeCancerFormSet(queryset=biological_relatives_with_cancer.objects.filter(mandatory_questionaire=mandatory_questionaire_data), prefix='relatives')
        else:
            print('no')
            #formset = RelativeCancerFormSet(queryset=biological_relatives_with_cancer.objects.none(), prefix='relatives')
         # Validate the form
        pdf_data = form.instance 
        pdf_buffer = generate_mandatory_questionnaire_pdf(pdf_data, request)
        print(pdf_buffer)
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        print(response)
        mandatory_questionaire_obj = Mandatory_questionaire.objects.get(participant_num=participant_id)
        participant_num = mandatory_questionaire_obj.participant_num  
        response['Content-Disposition'] = f'attachment; filename={participant_num}_mandatory_questionnaire.pdf'
        print('should be wokring here')
        return response
    
    elif 'generate_csv' in request.GET:
        form = Mandatory_questionaire_form(instance=mandatory_questionaire_data)
        mandatory_questionaire_obj = Mandatory_questionaire.objects.get(participant_num=participant_id)
        participant_num = mandatory_questionaire_obj.participant_num    
        
        csv_buffer = generate_mandatory_questionnaire_csv(form, request)
        response = HttpResponse(csv_buffer.getvalue(), content_type='application/csv')
        response['Content-Disposition'] = f'attachment; filename={participant_num}_mandatory_questionnaire.csv'
        return response
    
    elif 'save_continue' in request.GET:
        form = Mandatory_questionaire_form(request.POST, instance=mandatory_questionaire_data)
        #formset = RelativeCancerFormSet(request.POST, prefix='relatives')
        if form.is_valid():
            mandatory_questionaire = form.save(commit=False)
            mandatory_questionaire.participant_num = participant
            mandatory_questionaire.save()


        return HttpResponseRedirect(reverse('add_mandatory_questionaire_c', args=[participant_id]))

    else:
        print("Getting Data")
        print("Mandatory Questionnaire Data:", mandatory_questionaire_data)
        print("Biological Relatives with Cancer:", biological_relatives_with_cancer.objects.filter(mandatory_questionaire=mandatory_questionaire_data))

        form = Mandatory_questionaire_form(instance=mandatory_questionaire_data)
        if mandatory_questionaire_data:
            print('yes')
            #formset = RelativeCancerFormSet(queryset=biological_relatives_with_cancer.objects.filter(mandatory_questionaire=mandatory_questionaire_data), prefix='relatives')
        else:
            print('no')
            #formset = RelativeCancerFormSet(queryset=biological_relatives_with_cancer.objects.none(), prefix='relatives')

    context = {
        'form': form,
        #'formset': formset,
        'participant_id': participant_id,
        'mandatory_questionaire_data' : mandatory_questionaire_data,

    }
    print(form.errors)
    #print(formset.errors)
    #print(request.POST)
    return render(request, 'DataEntry/mandatory_questionaire.html', context)


@login_required(login_url='login')
def add_indirect_costs(request, participant_id=None):
    print("Indirect Costs View accessed!")
    if participant_id: 
        participant = get_object_or_404(Participant, participant_number=participant_id)
        indirect_costs_data = Indirect_costs.objects.filter(participant_num=participant).first()
        print('the participant number is: ', participant_id)
    
    #RelativeCancerFormSet = modelformset_factory(biological_relatives_with_cancer, form=biological_relatives_with_cancer_form, extra=1)
    
    if request.method == 'POST':
        form = Indirect_costs_form(request.POST, instance=indirect_costs_data)
        #formset = RelativeCancerFormSet(request.POST, prefix='relatives')

        if form.is_valid(): 
            print('form is valid')

            if not participant:
                participant = Participant.objects.create(participant_number=participant_id)
            
            indirect_costs = form.save(commit=False)
            indirect_costs.participant_num = participant
            indirect_costs.save()
            

            # instances = formset.save(commit=False)
            # for instance in instances:
            #     instance.indirect_costs = indirect_costs
            #     instance.save()

            #word_doc = generate_word_document(form.cleaned_data)
            #response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            #response['Content-Disposition'] = f'attachment; filename=indirect_costs.docx'
            #word_doc.save(response)
            messages.success(request, 'Data saved successfully.')
            return HttpResponseRedirect(reverse('add_indirect_costs', args=[participant_id]) + '?submitted=True')
        else:
            print(form.errors)
            #print(formset.errors)
    elif 'save_continue' in request.GET:
        form = Indirect_costs_form(request.POST, instance=indirect_costs_data)
        #formset = RelativeCancerFormSet(request.POST, prefix='relatives')
        if form.is_valid():
            indirect_costs = form.save(commit=False)
            indirect_costs.participant_num = participant
            indirect_costs.save()


        return HttpResponseRedirect(reverse('add_stai_form_y', args=[participant_id]))
    else:
        print("Getting Data")
        print("Indirect Costs Data:", indirect_costs_data)

        form = Indirect_costs_form(instance=indirect_costs_data)
        
        if indirect_costs_data:
            print('yes')
            #formset = RelativeCancerFormSet(queryset=biological_relatives_with_cancer.objects.filter(indirect_costs=indirect_costs_data), prefix='relatives')
        else:
            print('no')
            #formset = RelativeCancerFormSet(queryset=biological_relatives_with_cancer.objects.none(), prefix='relatives')

    context = {
        'form': form,
        'participant_id': participant_id,
        'indirect_costs_data' : indirect_costs_data,
    }
    print(form.errors)
    #print(formset.errors)
    #print(request.POST)
    return render(request, 'DataEntry/indirect_costs.html', context)


@login_required(login_url='login')
def add_mandatory_questionaire_noParticipant(request):

    print(request.GET) 

    return render(request, 'DataEntry/participant_search.html')



def generate_mandatory_questionnaire_csv(form, request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mandatory_questionnaire_d.csv'

    writer = csv.writer(response)
    header = [field.label for field in form]
    writer.writerow(header)

    data = [form[field_name].value() for field_name in form.fields]
    writer.writerow(data)

    return response



def generate_mandatory_questionnaire_pdf(pdf_data, request):
    template_path = 'DataEntry/pdf_template.html' 
    template = get_template(template_path)
    context = {'form': pdf_data} 
    html = template.render(context)
    pdf_buffer = BytesIO()

    pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)
    if pisa_status.err:
        return HttpResponse('PDF generation error', content_type='text/plain')
    response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=mandatory_questionnaire.pdf'
    pdf_buffer.close()
    return response


@login_required(login_url='login')

def add_mandatory_questionaire_c(request, participant_id=None):
    print(request.GET) 
    
    participant = None
    mandatory_questionaire_c_data = None
    print("View accessed!")
    if participant_id:
        participant = get_object_or_404(Participant, participant_number=participant_id)
        mandatory_questionaire_c_data = Mandatory_questionaire_c.objects.filter(participant_num=participant).first()
        print(participant)
    
    if request.method == 'POST':
        form = Mandatory_questionaire_form_c(request.POST, instance=mandatory_questionaire_c_data)
        if not participant:
            participant = Participant.objects.create(participant_number=participant_id)
            print('created participant')

        if form.is_valid():
            print('form is valid')
            if not participant:
                participant = Participant.objects.create(participant_number=participant_id)
            
            mandatory_questionaire_c = form.save(commit=False)
            mandatory_questionaire_c.participant_num = participant
            mandatory_questionaire_c.save()
            messages.success(request, 'Data saved successfully.')
            return HttpResponseRedirect(reverse('add_mandatory_questionaire_c', args=[participant_id]) + '?submitted=True')
        else:
            print(form.errors)
            
    elif 'generate_pdf' in request.GET:
        print('button pressed')
        form = Mandatory_questionaire_form_c(instance=mandatory_questionaire_c_data)
        mandatory_questionaire_c_obj = Mandatory_questionaire_c.objects.get(participant_num=participant_id)
        participant_num = mandatory_questionaire_c_obj.participant_num 
        pdf_data = form.instance
        pdf_buffer = generate_mandatory_questionnaire_c_pdf(pdf_data, request)
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={participant_num}_mandatory_questionnaire_c.pdf'
        return response
    
    elif 'generate_csv' in request.GET:
        form = Mandatory_questionaire_form_c(instance=mandatory_questionaire_c_data) 
        csv_buffer = generate_mandatory_questionnaire_c_csv(form, request)
        mandatory_questionaire_c_obj = Mandatory_questionaire_c.objects.get(participant_num=participant_id)
        participant_num = mandatory_questionaire_c_obj.participant_num 
        response = HttpResponse(csv_buffer.getvalue(), content_type='application/csv')
        response['Content-Disposition'] = f'attachment; filename={participant_num}_mandatory_questionnaire_c.csv'
        return response

    else:
        print("Form is NOT valid!")
        form = Mandatory_questionaire_form_c(instance=mandatory_questionaire_c_data)

    context = {
        'form': form,
        'participant_id': participant_id,
    }

    return render(request, 'DataEntry/mandatory_questionaire_c.html', context)

def add_mandatory_questionaire_c_noParticipant(request):

    print(request.GET)

    return render(request, 'DataEntry/participant_search.html')

def add_mandatory_questionaire_c_with_id(request, participant_id):
    return add_mandatory_questionaire_c(request, participant_id)


def generate_mandatory_questionnaire_c_pdf(pdf_data, request):
    template_path = 'DataEntry/mandatory_questionaire_c_pdf.html'
    template = get_template(template_path)
    context = {'form': pdf_data} 
    html = template.render(context)
    pdf_buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)
    if pisa_status.err:
        return HttpResponse('PDF generation error', content_type='text/plain')
    response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=mandatory_questionnaire.pdf'
    pdf_buffer.close()
    return response

def generate_mandatory_questionnaire_c_csv(form, request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mandatory_questionnaire_d.csv'

    writer = csv.writer(response)

    header = [field.label for field in form]
    writer.writerow(header)

    data = [form[field_name].value() for field_name in form.fields]
    # writer.writerow(data)
    transformed_data = []
    for value in data:
        if value is True:
            transformed_data.append('Yes')
        elif value is False:
            transformed_data.append('No')
        elif value == '':
            transformed_data.append('N/A')
        else:
            transformed_data.append(value)
    writer.writerow(transformed_data)
    return response



@login_required(login_url='login')
def add_mandatory_questionaire_de(request, participant_id=None):
    print(request.POST)
    print(f"URL Parameter - participant_id: {participant_id}")
    print(f"Participant ID: {participant_id}")
    print(f"Request method: {request.method}")
    print("View accessed!")

    if participant_id:
        participant = get_object_or_404(Participant, participant_number=participant_id)
        mandatory_questionaire_data = last_mandatory_questionnaire.objects.filter(participant_num=participant).first()
        
        print(participant)

    if request.method == 'POST':
        form = last_mandatory_questionnaire_form(request.POST, instance=mandatory_questionaire_data, initial={'participant_num': participant})
        try:
            form.save()
            if participant_id:
                return HttpResponseRedirect(reverse('add_mandatory_questionaire_de', args=[participant_id]) + '?submitted=True')
            else:
                return HttpResponseRedirect(reverse('add_mandatory_questionaire_de') + '?submitted=True')
            print('saved')
        except Exception as e:
            print(f"Error saving forms: {e}")
            print("Form errors:", form.errors)

        messages.success(request, 'Data saved successfully.')
        return HttpResponseRedirect(reverse('add_mandatory_questionaire_de', args=[participant_id]) + '?submitted=True')
    
    elif 'generate_pdf' in request.GET:
        form = last_mandatory_questionnaire_form(instance=mandatory_questionaire_data)

        pdf_buffer = generate_mandatory_questionnaire_d_pdf(form, request)
        mandatory_questionaire_de_obj = Mandatory_questionaire_de.objects.get(participant_num=participant_id)
        participant_num = mandatory_questionaire_de_obj.participant_num 
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={participant_num}_mandatory_questionnaire_de.pdf'
        return response
    
    elif 'generate_csv' in request.GET:
        form = last_mandatory_questionnaire_form(instance=mandatory_questionaire_data)
        mandatory_questionaire_de_obj = Mandatory_questionaire_de.objects.get(participant_num=participant_id)
        participant_num = mandatory_questionaire_de_obj.participant_num 
        csv_buffer = generate_mandatory_questionnaire_d_csv(form, request)
        response = HttpResponse(csv_buffer.getvalue(), content_type='application/csv')
        response['Content-Disposition'] = f'attachment; filename={participant_num}_mandatory_questionnaire_de.csv'
        return response
    else:
        form = last_mandatory_questionnaire_form(instance=mandatory_questionaire_data)


    context = {
        'form': form,
        'participant_id': participant_id,
    }
    print(form.errors)

    return render(request, 'DataEntry/mandatory_questionaire_de_new.html', context)


@login_required(login_url='login')
def add_mandatory_questionaire_de_noParticipant(request):

    print(request.GET) 

    return render(request, 'DataEntry/participant_search.html')


@login_required(login_url='login')
def generate_mandatory_questionnaire_d_pdf(form, fg_form, request):
    template_path = 'DataEntry/mandatory_questionaire_d_pdf.html'  
    template = get_template(template_path)
    context = {
        'form': form,
        'fg_form': fg_form,
    } 
    html = template.render(context)
    pdf_buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)
    if pisa_status.err:
        return HttpResponse('PDF generation error', content_type='text/plain')
    response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=mandatory_questionnaire_d.pdf'
    pdf_buffer.close()
    return response

def generate_mandatory_questionnaire_d_csv(form, request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mandatory_questionnaire_d.csv'

    writer = csv.writer(response)

    header = [field.label for field in form]
    writer.writerow(header)

    data = [form[field_name].value() for field_name in form.fields]
    # writer.writerow(data)
    transformed_data = []
    for value in data:
        if value is True:
            transformed_data.append('Yes')
        elif value is False:
            transformed_data.append('No')
        elif value == '':
            transformed_data.append('N/A')
        else:
            transformed_data.append(value)

    writer.writerow(transformed_data)
    return response

@login_required(login_url='login')
def add_exposure_form(request, participant_id=None):
    participant = None
    exposure2_data = None
    exposure3_data = None

    if participant_id:
        participant = get_object_or_404(Participant, participant_number=participant_id)
        exposure2_data = Exposure2.objects.filter(participant_num=participant).first()
        exposure3_data = Exposure3.objects.filter(participant_num=participant).first()

    if request.method == 'POST':
        form2 = Exposure_Form2(request.POST, instance=exposure2_data, initial={'participant_num': participant})
        form3 = Exposure_Form3(request.POST, instance=exposure3_data, initial={'participant_num': participant})

        if form2.is_valid() and form3.is_valid():
            exposure2_instance = form2.save(commit=False)
            exposure2_instance.participant_num = participant
            exposure2_instance.save()

            exposure3_instance = form3.save(commit=False)
            exposure3_instance.participant_num = participant
            exposure3_instance.save()

            
            messages.success(request, 'Data saved successfully.')
            return HttpResponseRedirect(reverse('add_exposure_form', args=[participant_id]) + '?submitted=True')
        else:
            print("Form2 errors:", form2.errors)
            print("Form3 errors:", form3.errors)
    elif 'generate_pdf' in request.GET:
        print('button pressed')
        form2 = Exposure_Form2(instance=exposure2_data)
        form3 = Exposure_Form3(instance=exposure3_data)
        pdf_buffer = generate_exposure_questionnaire_pdf(form2, form3, request)
        print(pdf_buffer)
        response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
        print(response)
        response['Content-Disposition'] = f'attachment; filename=mandatory_questionnaire.pdf'
        print('should be working here')
        return response

    elif 'generate_csv' in request.GET:
        form2 = Exposure_Form2(instance=exposure2_data)
        form3 = Exposure_Form3(instance=exposure3_data) 
        csv_buffer = generate_exposure_csv(form2, form3, request)
        response = HttpResponse(csv_buffer.getvalue(), content_type='application/csv')
        response['Content-Disposition'] = f'attachment; filename=mandatory_questionnaire.csv'
        return response
    
    else:
        form2 = Exposure_Form2(instance=exposure2_data, initial={'participant_num': participant})
        form3 = Exposure_Form3(instance=exposure3_data, initial={'participant_num': participant})

    context = {
        'form2': form2,
        'form3': form3,
        'participant_id': participant_id,
    }
   
    return render(request, 'DataEntry/exposure_form.html', context)

def add_exposure_form_noParticipant(request):

    print(request.GET)  

    return render(request, 'DataEntry/participant_search.html')

def generate_exposure_questionnaire_pdf(form2, form3, request):
    template_path = 'DataEntry/exposure_questionaire_pdf.html'  
    template = get_template(template_path)
    context = {
        'form2': form2,
        'form3': form3,
    }  
    html = template.render(context)
    pdf_buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)
    if pisa_status.err:
        return HttpResponse('PDF generation error', content_type='text/plain')
    response = HttpResponse(pdf_buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=mandatory_questionnaire_d.pdf'
    pdf_buffer.close()
    return response


def generate_exposure_csv(form2, form3, request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mandatory_questionnaire_d.csv'

    writer = csv.writer(response)

    header = [field.label for field in form2]
    header2 = [field.label for field in form3]
    total_header = header + header2
    writer.writerow(total_header)

    data = [form2[field_name].value() for field_name in form2.fields]
    data2 = [form3[field_name].value() for field_name in form3.fields]
    transformed_data = []
    for value in data + data2:
        if value is True:
            transformed_data.append('Yes')
        elif value is False:
            transformed_data.append('No')
        elif value == '':
            transformed_data.append('N/A')
        else:
            transformed_data.append(value)
    writer.writerow(transformed_data)
    return response



@login_required(login_url='login')
def add_yearly_update(request, participant_id=None):
    participant = None
    annual_study_update_data = None

    if participant_id:
        print('here')
        participant = get_object_or_404(Participant, participant_number=participant_id)
        annual_study_update_data = annual_study_update.objects.filter(participant_num=participant).first()


    if request.method == 'POST':
        form = annual_study_update_form(request.POST, instance=annual_study_update_data, initial={'participant_num': participant})
        
        if form.is_valid():
            annual_study_update_form_instance = form.save(commit=False)
            annual_study_update_form_instance.participant_num = participant
            annual_study_update_form_instance.save()


            if participant_id:
                return HttpResponseRedirect(reverse('add_yearly_update', args=[participant_id]) + '?submitted=True')
            else:
                return HttpResponseRedirect(reverse('add_yearly_update') + '?submitted=True')
        else:
            print("Form errors:", form.errors)
    
    else:
        print('here now')
        form = annual_study_update_form(instance=annual_study_update_data, initial={'participant_num': participant})


    context = {
        'form': form,
        'participant_id': participant_id,
    }
   
    return render(request, 'DataEntry/add_yearly_update.html', context)

@login_required(login_url='login')
def add_yearly_update_noParticipant(request):
    print(request.GET)  

    return render(request, 'DataEntry/participant_search.html')

@login_required(login_url='login')
def add_breath_collection(request, participant_id=None):
    participant = None
    breath_collection_data = None

    if participant_id:
        participant = get_object_or_404(Participant, participant_number=participant_id)
        breath_collection_data = Breath_Collection.objects.filter(participant_num=participant).first()

    form = Breath_Collection_Form(instance=breath_collection_data, initial={'participant_num': participant})

    if request.method == 'POST':
        form = Breath_Collection_Form(request.POST, instance=breath_collection_data, initial={'participant_num': participant})

        if form.is_valid():
            form.save()

            if participant_id:
                return HttpResponseRedirect(reverse('add_breath_collection', args=[participant_id]) + '?submitted=True')
            else:
                return HttpResponseRedirect(reverse('add_breath_collection') + '?submitted=True')

    context = {
        'form': form,
        'participant_id': participant_id,
    }
    print(form.errors)
    print(participant_id)

    return render(request, 'DataEntry/breath_collection.html', context)

def add_breath_collection_noParticipant(request):
    print(request.GET)  # Print the GET parameters

    return render(request, 'DataEntry/participant_search.html')

@login_required(login_url='login')
def add_ct_scan(request, participant_id=None):
    print("participant_id received:", participant_id)
    if participant_id:
        participant = get_object_or_404(Participant, participant_number=participant_id)


        ct_scan_data = ct_scan.objects.filter(participant_num=participant).first()
        ct_nodule_data = ct_scan_nodule_1.objects.filter(participant_num=participant).first()
        ct_nodule_data2 = ct_scan_nodule_2.objects.filter(participant_num=participant).first()
        ct_nodule_data3 = ct_scan_nodule_3.objects.filter(participant_num=participant).first()
        ct_nodule_data4 = ct_scan_nodule_4.objects.filter(participant_num=participant).first()
        ct_nodule_data5 = ct_scan_nodule_5.objects.filter(participant_num=participant).first()

    if request.method == 'POST':
        ct_scan_form = CT_Scan_Form(request.POST, instance=ct_scan_data)
        ct_nodule_form = CT_Scan_Nodule_Form_1(request.POST, instance=ct_nodule_data)
        ct_nodule_form2 = CT_Scan_Nodule_Form_2(request.POST, instance=ct_nodule_data2)
        ct_nodule_form3 = CT_Scan_Nodule_Form_3(request.POST, instance=ct_nodule_data3)
        ct_nodule_form4 = CT_Scan_Nodule_Form_4(request.POST, instance=ct_nodule_data4)
        ct_nodule_form5 = CT_Scan_Nodule_Form_5(request.POST, instance=ct_nodule_data5)

        if 'save_ct_scan' in request.POST:
            if ct_scan_form.is_valid():
                ct_scan_data = ct_scan_form.save(commit=False)
                ct_scan_data.participant_num = participant
                ct_scan_data.save()
                messages.success(request, "CT Scan Form saved successfully.")
                ct_scan_form = CT_Scan_Form(instance=ct_scan_data)

        elif 'save_nodule' in request.POST:
            if ct_nodule_form.is_valid():
                ct_nodule_form.save()
                ct_nodule_form2.save()
                ct_nodule_form3.save()
                ct_nodule_form4.save()
                ct_nodule_form5.save()
                messages.success(request, "CT Nodule Form saved successfully.")
                ct_nodule_form = CT_Scan_Nodule_Form_1(instance=ct_nodule_data)
                ct_nodule_form2 = CT_Scan_Nodule_Form_2(instance=ct_nodule_data2)
                ct_nodule_form3 = CT_Scan_Nodule_Form_3(instance=ct_nodule_data3)
                ct_nodule_form4 = CT_Scan_Nodule_Form_4(instance=ct_nodule_data4)
                ct_nodule_form5 = CT_Scan_Nodule_Form_5(instance=ct_nodule_data5)

    else:
        ct_scan_form = CT_Scan_Form(instance=ct_scan_data)
        if ct_nodule_data:
            ct_nodule_form = CT_Scan_Nodule_Form_1(instance=ct_nodule_data)
        else:
            ct_nodule_form = CT_Scan_Nodule_Form_1(initial={'participant_num': participant})

        if ct_nodule_data2:
            ct_nodule_form2 = CT_Scan_Nodule_Form_2(instance=ct_nodule_data2)
        else:
            ct_nodule_form2 = CT_Scan_Nodule_Form_2(initial={'participant_num': participant})

        if ct_nodule_data3:
            ct_nodule_form3 = CT_Scan_Nodule_Form_3(instance=ct_nodule_data3)
        else:
            ct_nodule_form3 = CT_Scan_Nodule_Form_3(initial={'participant_num': participant})

        if ct_nodule_data4:
            ct_nodule_form4 = CT_Scan_Nodule_Form_4(instance=ct_nodule_data4)
        else:
            ct_nodule_form4 = CT_Scan_Nodule_Form_4(initial={'participant_num': participant})

        if ct_nodule_data5:
            ct_nodule_form5 = CT_Scan_Nodule_Form_5(instance=ct_nodule_data5)
        else:
            ct_nodule_form5 = CT_Scan_Nodule_Form_5(initial={'participant_num': participant})

    context = {
        'ct_scan_form': ct_scan_form,
        'participant_id': participant_id,
        'ct_nodule_form': ct_nodule_form,
        'ct_nodule_form2': ct_nodule_form2,
        'ct_nodule_form3': ct_nodule_form3,
        'ct_nodule_form4': ct_nodule_form4,
        'ct_nodule_form5': ct_nodule_form5,
    }
    print("participant:", participant)
    print("CT Scan Form Errors:", ct_scan_form.errors)
    print("CT Nodule Form Errors:", ct_nodule_form.errors)
    return render(request, 'DataEntry/ct_scan.html', context)

@login_required(login_url='login')
def add_ct_scan_noParticipant(request):
    print(request.GET) 

    return render(request, 'DataEntry/participant_search.html')

@login_required(login_url='login')
def add_blood_collection(request, participant_id=None):
    print(request.GET) 

    return render(request, 'DataEntry/participant_search.html')



@login_required(login_url='login')
def add_blood_collection_participant(request, participant_id=None):
    form = Blood_Collection_Form
    if request.method == 'POST':
        form_class = Blood_Collection_Form
        form = Blood_Collection_Form(request.POST)
        
        if form.is_valid():
            print('test')
            return HttpResponse('/add_blood_collection/?submitted=True')
        
    context = {
        'form': form,
        'participant_id': participant_id,
    }

    return render(request, 'DataEntry/blood_collection.html', context)




@login_required(login_url='login')
def add_plco_score(request, participant_id=None):
    participant = get_object_or_404(Participant, participant_number=participant_id)
    print(participant_id)
    if request.method == 'POST':
        form = plco_score_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page') 
    else:
        form = plco_score_form()

    return render(request, 'DataEntry/plco_score.html', {'form': form})

@login_required(login_url='login')
def add_plco_score_noParticipant(request):
    print(request.GET) 

    return render(request, 'DataEntry/participant_search.html')


@login_required(login_url='login')
def add_participant(request):
    submitted = False
    if request.method == 'POST':
        form_class = ParticipantForm
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('/add_participant/?submitted=True?id=' + str(form.instance.id))
    form = ParticipantForm
    context = {
        'form': form,
        'submitted': submitted
               }
    return render(request, 'DataEntry/index.html', {'form': form})

@login_required(login_url='login')
def add_protocol_deviation(request):
    submitted = False
    if request.method == 'POST':
        form_class = ParticipantForm
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('/add_participant/?submitted=True')
    form = ParticipantForm
    return render(request, 'DataEntry/index.html', {'form': form})


@login_required(login_url='login')
def add_protocol_deviations_noParticipant(request):
    print(request.GET) 

    return render(request, 'DataEntry/participant_search.html')




@login_required(login_url='login')
def update_participant_status(request):
    if request.method == 'POST':
        inclusion_criteria_values = [
            request.POST.get('inclusion_criteria_1'),
            request.POST.get('inclusion_criteria_2'),
        ]

        if all(value == 'yes' for value in inclusion_criteria_values[:5]) and all(value == 'no' for value in inclusion_criteria_values[5:]):
            participant_status = 'group 1'
        else:
            participant_status = 'group 2'

        inclusion_object = inclusion.objects.first() 
        inclusion_object.participant_status = participant_status
        inclusion_object.save()

        response_data = {'participant_status': participant_status}
        return JsonResponse(response_data)
    else:
        return render(request, 'form.html')


@login_required(login_url='login')
def add_lab_processing(request):
    if request.method == 'POST':
        form = Lab_Processing_Form(request.POST, request.FILES)
        if form.is_valid():
            lab_processing_obj = lab_processing()
            lab_processing_obj.lab_processing_upload = form.cleaned_data['lab_processing_upload']
            lab_processing_obj.save()
    else:
        form = Lab_Processing_Form()

    uploaded_files = lab_processing.objects.all()  

    return render(request, 'DataEntry/lab_processing.html', {'form': form, 'uploaded_files': uploaded_files})

@login_required(login_url='login')
def add_lab_processing_participant(request, participant_id=None):
    if participant_id:
        print('here')
    if request.method == 'POST':
        form = Lab_Processing_Form(request.POST, request.FILES)
        if form.is_valid():
            lab_processing_obj = lab_processing()
            lab_processing_obj.lab_processing_upload = form.cleaned_data['lab_processing_upload']
            lab_processing_obj.save()
    else:
        form = Lab_Processing_Form()

    uploaded_files = lab_processing.objects.all()  
    context = {
        'form': form,
        'uploaded_files': uploaded_files,
        'participant_id': participant_id,
    }

    return render(request, 'DataEntry/lab_processing.html', context)


@login_required(login_url='login')
def update_mandatory_questionaire(request, participant_id):
    mandatory_questionaire = Mandatory_questionaire.objects.get(pk=participant_id)
    form = Mandatory_questionaire_form(request.POST or None, instance=mandatory_questionaire)
    return render(request, 'DataEntry/update_mandatory_questionaire.html', {'Mandatory_questionaire': Mandatory_questionaire, 'participant_id': participant_id})

@login_required(login_url='login')
def add_clinical_procedures(request):
    return render(request, 'DataEntry/participant_search.html', {})


@login_required(login_url='login')
def add_clinical_procedures_participant(request, participant_id=None):
    print(request.GET) 
    context = {
        'participant_id': participant_id,
    }
    return render(request, 'DataEntry/clinical_procedures.html', context)


@login_required(login_url='login')
def add_protocol_deviations(request):
       return render(request, 'DataEntry/participant_search.html', {})


@login_required(login_url='login')
def add_protocol_deviations_participant(request, participant_id=None):
       
    context = {
        'participant_id': participant_id,
    }

    return render(request, 'DataEntry/protocol_deviations.html', context)

@login_required(login_url='login')
def add_plco_score_participant(request, participant_id=None):
    if request.method == 'POST':
        form = plco_score_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page') 
    else:
        form = plco_score_form()
    context = {
        'form': form,
        'participant_id': participant_id,
    }
    return render(request, 'DataEntry/plco_score.html', context)

@login_required
def add_plco_score(request):

    return render(request, 'DataEntry/participant_search.html', {})

@login_required(login_url='login')
def add_lab_processing_with_data(request, participant_num):
    participant = lab_processing.objects.get(participant_num=participant_num)
    form = Lab_Processing_Form(instance=participant)

    return render(request, 'lab_processing_with_data.html', {'form': form})

@login_required(login_url='login')
def add_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Participant form submitted successfully'})
        else:
            return JsonResponse({'error': form.errors}, status=400)



@login_required(login_url='login')
def search(request):
    query = request.GET.get('q')
    if query:
        participant = get_object_or_404(Participant, participant_number=query)
        return redirect('participant_detail', participant_id=participant.participant_number)
    else:
        return render(request, 'search.html')

@login_required(login_url='login')
def list_participants(request):
    participants = Participant.objects.all()
    context = {
        'participants': participants,
    }
    return render(request,'DataEntry/list_participants.html', context)


@login_required(login_url='login')
def show_participants(request, participant_id):
    participants = Participant.objects.get(pk=participant_id)
    context = {
        'participants': participants,
    }
    return render(request,'DataEntry/show_participants.html', context)

@login_required(login_url='login')
def history_page(request):
    histories = History.objects.all().order_by('-timestamp')
    return render(request, 'history.html', {'histories': histories})

@login_required(login_url='login')
def add_data_test(request):
    return render(request, 'DataEntry/add_data.html', {})






@login_required(login_url='login')
def dashboard(request):
    participants = Participant.objects.all()
    data = []

    for participant in participants:
        participant_data = {
            'participant': participant,
            'inclusion_data': inclusion.objects.filter(participant_num=participant).exists(),
            'questionnaire_data': Mandatory_questionaire.objects.filter(participant_num=participant).exists(),
            'questionnaire_c_data': Mandatory_questionaire_c.objects.filter(participant_num=participant).exists(),
            'questionnaire_d_data': Mandatory_questionaire_de.objects.filter(participant_num=participant).exists(),
            'exposure_data': Exposure.objects.filter(participant_num=participant).exists(),
            'breath_collection_data': Breath_Collection.objects.filter(participant_num=participant).exists(),
            'blood_collection_data': Blood_Collection.objects.filter(participant_num=participant).exists(),
            'ct_scan_data': ct_scan.objects.filter(participant_num=participant).exists(),
            'yearly_update_data': annual_study_update.objects.filter(participant_num=participant).exists(),

        }
        data.append(participant_data)

    context = {'data': data}
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def dashboard_participant(request, participant_id=None):
    participants = Participant.objects.all()
    data = []
    if participant_id:
        print('participant_id:', participant_id)
    for participant in participants:
        participant_data = {
            'participant': participant,
            'inclusion_data': inclusion.objects.filter(participant_num=participant).exists(),
            'questionnaire_data': Mandatory_questionaire.objects.filter(participant_num=participant).exists(),
            'questionnaire_c_data': Mandatory_questionaire_c.objects.filter(participant_num=participant).exists(),
            'questionnaire_d_data': Mandatory_questionaire_de.objects.filter(participant_num=participant).exists(),
            'exposure_data': Exposure.objects.filter(participant_num=participant).exists(),
            'breath_collection_data': Breath_Collection.objects.filter(participant_num=participant).exists(),
            'blood_collection_data': Blood_Collection.objects.filter(participant_num=participant).exists(),
            'ct_scan_data': ct_scan.objects.filter(participant_num=participant).exists(),
            'yearly_update_data': annual_study_update.objects.filter(participant_num=participant).exists(),

        }
        data.append(participant_data)

    context = {
        'data': data,
        'participant_id': participant_id,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def check_participant(request, number):
    try:
        participant = Participant.objects.get(participant_number=number)
        return JsonResponse({'exists': True})
    except Participant.DoesNotExist:
        return JsonResponse({'exists': False, 'message': 'Participant not found in the database.'})
    except Exception as e:
        return JsonResponse({'exists': False, 'message': str(e)})