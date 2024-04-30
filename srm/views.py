from django.db.models import Sum
from django.shortcuts import render, redirect
from .models import Lead
from django.contrib.auth.decorators import user_passes_test
from app.models import Storage, House

@user_passes_test(lambda u: u.status == 2 or u.is_admin, login_url='/index/')
def lead_list_view(request):

    lead = Lead.objects.all().order_by('-id')

    return render(request, 'srm/lead_list.html', {'lead': lead})


@user_passes_test(lambda u: u.status == 2 or u.is_admin, login_url='/index/')
def lead_delete_view(request, pk):

    leads = Lead.objects.filter(id=pk).first()
    leads.delete()

    return redirect('lead_list')


def storage_list_view(request):
    orders = Storage.objects.filter(status=3)
    total_price = orders.aggregate(total=Sum('house__price'))['total']

    return render(request, 'srm/order_list.html',{'orders': orders, 'total_price': total_price})