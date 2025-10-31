from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

# Create your views here.
from .models import Product, ProductImage
from django.views.generic import (CreateView, ListView, 
                                  DetailView, UpdateView, DeleteView)


# Importing custom forms
from .forms import ProductImageForm

# -----------Product CRUD-----------------
class AddProduct(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'products/add_product.html'
    # success_url = reverse_lazy("view_products")

class ViewProducts(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/products.html'

class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_details.html'

    # DetailsView doesn't carry an inbuilt form object.
    # We'll create our own form and pass it as an extra context into the template.

    # Let's create a form object from the custom built ProductImageForm and send it
    # as extra context data . 
    # Django CBV utilizes a method called `get_context_data` to collect context data for 
    # template rendering. Let's override that method.

    def get_context_data(self, **kwargs):
        # collecting the context created by the original method
        context =  super().get_context_data(**kwargs)
        # adding new data to the context dictionary
        context['form'] = ProductImageForm() # creating a new empty form object
                                             # and adding it into context
        return context # returning the altered context.
    
    # DetailView, doesn't handle post requests, as it is not its purpose.
    # Let's define a post method for this CBV.
    # In urls.py, the `.as_view()` will help route any post request in this view, to this
    # post method.
    def post(self, request, pk):
        # filter the particular Product object for which the image is getting added.
        this_product = Product.objects.get(id = pk) # filtering product by id
        # We create a new form object using the same form class and passing the request data
        form = ProductImageForm(request.POST, request.FILES)
        # now, this form is an object, containing all the data submitted by user.

        # form.save()  -> gives us an object of ProductImage model now, with full details
        # collected from user. But, it lacks reference to the particular product.
        # to add this, first, we need to retrieve an object out of this form.
        # form.save() will also write into the DB. We'll do that after altering the object
        # and adding the product reference.
        # We'll use form.save(commit=False) => creates ProductImage object, but doesn't
        # commit(or save) into DB. This gives us time to add product reference.
        this_product_image = form.save(commit=False)
        this_product_image.product = this_product
        # But the object is not saved in DB.
        # Let's save the completed object.
        this_product_image.save()
        return redirect('prod_detail', pk=pk)
    

class EditProduct(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'products/edit_product.html'
    # success_url = reverse_lazy('view_products')

class RemoveProduct(DeleteView):
    model = Product
    template_name = 'products/del_product.html'
    success_url = reverse_lazy('view_products')


# -----ProductImages--------

class EditProductImage(UpdateView):
    model = ProductImage
    # to utilize custom form object in CBV, we have to provide attribute, `form_class`
    # form_class = ProductImageForm
    template_name = 'products/edit_product_image.html'
    

class DelProductImage(DeleteView):
    model = ProductImage
    # to utilize custom form object in CBV, we have to provide attribute, `form_class`
    # form_class = ProductImageForm
    template_name = 'products/del_product_image.html'

    # defining get_success_url as DeleteView will not use the get_absolute_url method
    def get_success_url(self):
        product_pk = self.object.product.pk
        return reverse_lazy('prod_detail', kwargs={'pk': product_pk})
    


