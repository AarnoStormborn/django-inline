from django.shortcuts import render, redirect
from django.http.response import HttpResponse


from .forms import (
    ProductForm, VariantFormSet, ImageFormSet
)
from .models import (
    Image,
    Product,
    Variant
)

def product_list(request):

    data = Product.objects.all()
    context = {'products':data}
    return render(request, 'products/product_list.html', context)

def createProduct(request):

    form = ProductForm(request.POST or None)
    variantForm = VariantFormSet(request.POST or None, request.FILES or None, prefix='variants')
    imageForm = ImageFormSet(request.POST or None, request.FILES or None, prefix='images')
    if request.method == 'POST':
        
        if form.is_valid():
            product = form.save()
        
        if variantForm.is_valid():
            for form in variantForm:
                if form.cleaned_data:
                    variant = form.save(commit=False)
                    variant.product = product
                    variant.save()

        if imageForm.is_valid():
            for form in imageForm:
                if form.cleaned_data:
                    image = form.save(commit=False)
                    image.product = product
                    image.save()
        
        return redirect('products_list')
    else:
        named_formsets = {'variants':variantForm,'images':imageForm}
        context = {'form':form, 'named_formsets':named_formsets}
        return render(request, 'products/product_create_or_update.html', context)

def updateProduct(request, pk):

    product = Product.objects.get(id=pk)

    form = ProductForm(request.POST or None, instance=product)
    variantForm = VariantFormSet(request.POST or None, request.FILES or None, instance=product, prefix='variants')
    imageForm = ImageFormSet(request.POST or None, request.FILES or None, instance=product, prefix='images')

    if request.method == 'POST':

        if form.is_valid():
            product = form.save()
        
        if variantForm.is_valid():
            for form in variantForm:
                if form.cleaned_data:
                    variant = form.save(commit=False)
                    variant.product = product
                    variant.save()

        if imageForm.is_valid():
            for form in imageForm:
                if form.cleaned_data:
                    image = form.save(commit=False)
                    image.product = product
                    image.save()

        return redirect('products_list')

    else:
        named_formsets = {'variants':variantForm,'images':imageForm}
        context = {'form':form, 'named_formsets':named_formsets}
        return render(request, 'products/product_create_or_update.html', context)


def deleteProduct(request, pk):

    product = Product.objects.get(id=pk)
    product.delete()
    return redirect('products_list')

def deleteImage(request, pk):

    image = Image.objects.get(id=pk)
    image.delete()
    return redirect('update_product', image.product.id)

def deleteVariant(request, pk):

    variant = Variant.objects.get(id=pk)
    variant.delete()
    return redirect('update_product', variant.product.id)







