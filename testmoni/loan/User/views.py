# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib

from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import LoanForm
from .models import User


def loan_form(request):
    """
    This view shows the form to request a loan.
    """
    if request.method == 'POST':
        form = LoanForm(request.POST)

        if form.is_valid():
            form.save()
            url_api = 'http://scoringservice.moni.com.ar:7001/api/v1/scoring/'
            params = "?{}".format(request.POST.urlencode())
            resp = urllib.request.urlopen(url_api + params)
            data = resp.read().decode('utf-8')
            jsdata = json.loads(data)
            form = {'form': jsdata, 'initial': False}
        else:
            errors = form.errors
            return JsonResponse({'status': 'form_error', 'form_error': errors})
    else:
        form = {'form': LoanForm(), 'initial': True}
    ctx = {'form': form}
    return render(request, 'loan.html', ctx)


@staff_member_required
def loan_list(request):
    """
    Displays the loan list of a user administrator.
    """
    loan_list = User.objects.filter()
    ctx = {'loan_list': loan_list}
    return render(request, 'loan-list.html', ctx)


@staff_member_required
def loan_edit(request, id):
    """
    View to edit a loan.
    """
    loan = User.objects.get(id=id)
    if request.method == "POST":
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            loan = form.save(commit=False)
            form.save()
            return redirect('loan-list')
    else:
        form = LoanForm(instance=loan)
    ctx = {'form': form}
    return render(request, 'loan-edit.html', ctx)


@staff_member_required
def loan_remove(request, id):
    """
    view to delete a loan.
    """
    loan = User.objects.get(id=id)
    loan.delete()
    return redirect('loan-list')


@staff_member_required
def loan_details(request, id):
    """
    View to show the details a loan.
    """
    loan = User.objects.get(id=id)
    ctx = {'loan': loan}
    return render(request, 'loan-detail.html', ctx)
