from django.shortcuts import render
from .forms import PincodeForm
from .models import School, Pincode

def school_list(request):
    form = PincodeForm(request.POST or None)

    if form.is_valid():
        pincode = form.cleaned_data['pincode']
        try:
            pincode_obj = Pincode.objects.get(code=pincode)
            schools = School.objects.filter(pincode=pincode_obj)
        except Pincode.DoesNotExist:
            schools = []

    else:
        schools = []

    context = {
        'form': form,
        'schools': schools,
    }
    return render(request, 'schoolapp/school_list.html', context)


