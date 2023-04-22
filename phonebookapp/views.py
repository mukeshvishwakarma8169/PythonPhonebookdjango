from django.shortcuts import render
from phonebookapp.models import *
from django.shortcuts import render, redirect
from django.db import connection
# Create your views here.


def phonemasteraddnew(request):
    cursor = connection.cursor()
    cursor.execute("select max(id) from mstphonebook order by id desc limit 1")
    r = cursor.fetchone()
    if r[0] == '' or r[0] == None:
        r = '1'
    else:
        r = str(int(r[0])+1)
    print(r[0])
    if request.method == "POST":

        phbid = request.POST.get('phonebook_id')
        nm = request.POST.get('name')
        ctnt = request.POST.get('contact')
        if ctnt == '' or ctnt == None:
            ctnt = ''

        if phonebook.objects.filter(phonebook_id=phbid).exists():
            si = phonebook.objects.order_by(
                'phonebook_id').last().phonebook_id + 1
        phonebook(phonebook_id=phbid, name=nm, contact=ctnt).save()
        return redirect('/phone')

    return render(request, 'phonebook/index.html', {'ren': r})


def phonemasterindex(request):
    ren = phonebook.objects.all().order_by('phonebook_id').reverse()
    return render(request, "phonebook/show.html", {'ren': ren})


def phonemasteredit(request, id):
    ren = phonebook.objects.get(id=id)
    return render(request, "phonebook/edit.html", {'ren': ren})


def phonemasterupdate(request):
    if request.method == "POST":
        phbid = request.POST.get('phonebook_id')
        nm = request.POST.get('name')
        ctnt = request.POST.get('contact')

        print('this ios rm', phbid, nm, ctnt)

        phonebook.objects.filter(phonebook_id=phbid).update(
            name=nm, contact=ctnt)

    return redirect('/phone')


def phonemasterdestroy(request, id):
    ren = phonebook.objects.get(id=id)
    ren.delete()
    return redirect("/phone")
