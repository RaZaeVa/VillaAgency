from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from .models import House, Storage
from django.views.generic import ListView
from .filters import HouseFilters
from .forms import HouseUpdateForm, HouseCreateForm
from django.contrib.auth.decorators import user_passes_test
from srm.models import Lead

def index_view(request):
    houses = House.objects.filter(is_active=True)[:6]

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        lead = Lead(
            full_name=name,
            email=email,
            subject_line=subject,
            message=message
        )
        lead.save()
        return redirect('index')

    return render(request, 'app/index.html', {'houses': houses})


class HouseListView(ListView):
    model = House
    template_name = 'add/house_list.html'
    context_object_name = 'houses'
    filterset_class = HouseFilters
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()

        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super(). get_context_data(**kwargs)

        context['filter'] = self.filterset

        houses = context['houses']
        paginator = Paginator(houses, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            houses = paginator.page(page)
        except PageNotAnInteger:
            houses = paginator.page(1)
        except EmptyPage:
            houses = paginator.page(paginator.num_pages)
        context['houses'] = houses

        return context


def house_detail_view(request, pk):
    house = House.objects.filter(id=pk).first()
    if request.method == 'POST' and 'buy' in request.POST:
        storage = Storage(
            user=request.user,
            house=house,
        )
        storage.save()
        return redirect('index')

    return render(request, 'app/house_detail.html', {'house': house})


@user_passes_test(lambda u: u.status == 2 or u.is_admin, login_url='/index/')
def house_update_view(request, pk):
    house = House.objects.filter(id=pk).first()

    if request.method == 'POST':
        form = HouseUpdateForm(request.POST, instance=house)

        if form.is_valid():
            form.save()
            return redirect('house_detail', house.id)

    form = HouseUpdateForm(instance=house)

    return render(request, 'app/house_update.html', {'house':house, 'form': form})


@user_passes_test(lambda u: u.status == 2 or u.is_admin, login_url='/index/')
def house_delete_view(request, pk):
    house = House.objects.filter(id=pk).first()
    house.delete()

    return redirect('index')


@user_passes_test(lambda u: u.status == 2 or u.is_admin, login_url='/index/')
def house_create_view(request):
    if request.method == 'POST':
        form = HouseCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('index')

    form = HouseCreateForm()

    return render( request, 'app/house_create.html', {'form': form})