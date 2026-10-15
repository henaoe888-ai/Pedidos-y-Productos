from django.shortcuts import render
from .models import Producto

# Create your views here.
def listar_productos(request):
    if request.method == "POST":
        productos = Producto(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            precio = request.POST["precio"],
            stock = request.POST["stock"],
            registro = request.POST["registro"]
        )

        productos.save()
    return render(request, "productos/formulario.html")


