from django.views import generic
from .models import Products


class ProductsListView(generic.ListView):
    """
    Generic ListView:
    model: name of the model to be used
     --> this is enough for the view to work if template product_list.html exists
      and context will be by default product_list

    template_name: user defined template_name will override the default template by default modelname_list.html
    context_object_name: used to override default modelname_list name
    ordering: used for ordering will be overridden by get_queryset()

    get_queryset(): function to get the queryset
    get_context_data(): function to add additional context
    """

    model = Products
    template_name = 'products_list.html'
    context_object_name = 'products'  # by default will be products_list
    # template_name_suffix = '_list' # used to add a suffix to template
    # ordering = ['name']  # this will be overridden by get_queryset

    def get_queryset(self):
        """
        used to get the query set if we dont need all the data
        """
        return Products.objects.all().order_by('name')

    def get_context_data(self, *args, **kwargs):
        """
        used to add additional data to the context object to be used in templates
        """
        context = super().get_context_data(*args, **kwargs)
        context['heading'] = {'headname': 'heading_name'}
        return context

    def get_template_names(self):
        """
        used to add templates dynamically based on some conditions
        if superuser:
            return 'super_user.html'
        else:
            return self.template_name.html
        """
        return self.template_name


class ProductDetailView(generic.DetailView):
    model = Products
    template_name = 'products_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.model.objects.all().order_by('name')
        return context