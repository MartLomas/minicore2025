from django.shortcuts import render
from .models import Vendedor, Venta, Reglas
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def listar_vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, 'vendedor.html', {'vendedores': vendedores})

def listar_ventas(request):
    ventas = Venta.objects.select_related('vendedor').all()
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if fecha_inicio and fecha_fin:
        ventas = ventas.filter(fecha__range=[fecha_inicio, fecha_fin])
    
    ventas_con_comision = []
    for venta in ventas:
        regla = Reglas.objects.filter(monto_min__lte=venta.monto, monto_max__gte=venta.monto).first()
        comision = 0
        if regla:
            comision = venta.monto * (regla.porcentaje / 100)
        ventas_con_comision.append({
            'venta' : venta,
            'comision': round(comision, 2),
        })

    context = {
        'ventas_con_comision': ventas_con_comision,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
    }
    return render(request, 'ventas.html', context)




def listar_reglas(request):
    reglas = Reglas.objects.all()
    return render(request, 'reglas.html', {'reglas': reglas})