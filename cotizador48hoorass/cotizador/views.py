from django.shortcuts import render, redirect
from .models import Cotizador
from .forms import CotizadorForm
import arrow

# Create your views here.


def viewsssCotizador(request):

    dates = Cotizador.objects.all()[3]
    split = str(dates.dates).split('-')

    one = split[0]
    two = split[1]

    # arrow.format('MM/DD/YYYY')
    a = arrow.get(one, 'MM/DD/YYYY')
    b = arrow.get(two, 'MM/DD/YYYY')

    delta = (b-a)
    total = delta.days

    # dates = Cotizador.objects.all().only("dates")
    # split = str(dates).split()
    # splits = self.dates.split("-")
    #     one = ""
    #     two = ""

    #     print(one, two)

    #     one = splits[0]
    #     two = splits[1]

    #     # arrow.format('MM/DD/YYYY')
    #     a = arrow.get(one, 'MM/DD/YYYY')
    #     b = arrow.get(two, 'MM/DD/YYYY')

    #     delta = (b-a)
    #     print(delta.days)
    context = {
        'fechas': dates,
        'separador': split,
        'total': total,

    }
    return render(request, 'precompra.html', context)


def Cotizadors(request):
    data = {
        'form': CotizadorForm()
    }

    if request.method == 'POST':
        formulario = CotizadorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = 'Cotizador Guardado'
            return redirect('viewCotizador')
        else:
            data['form'] = formulario
    return render(request, 'fechas.html', data)

    # def agregar_producto(request):
    # data = {
    #     'form': ProductoForm()
    # }

    # if request.method == 'POST':
    #     formulario = ProductoForm(data=request.POST, files=request.FILES)
    #     if formulario.is_valid():
    #         formulario.save()
    #         messages.success(request, 'Producto Registrado')
    #         return redirect('listarProducto')
    #     else:
    #         data['form'] = formulario
    # return render(request, 'app/producto/agregar.html', data)
