from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.
def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais':chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_detail.html',{'chai':chai})

def chai_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_varity']
            stores = stores.objects.filter(chai_varieties = chai_variety)
    else:form = ChaiVarietyForm()
    return render(request,'chai/chai_stores.html', {'stores': stores, 'form': form})
#  hi my name is kedar Bhame 
# near me shivraj halande is sitting on sofa  
# hi guys
