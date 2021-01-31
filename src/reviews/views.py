from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import ReviewModelForm
from .models import Review
# BASE VIEW CLASS = View


# Create your views here.
class ReviewObjectMixin(object):
    model = Review
    lookup = 'id'

    def get_object(self):
        id_ = self.kwargs.get(self.lookup)
        obj = None
        if id_ is not None:
            obj = get_object_or_404(self.model, id=id_)
        return obj


class ReviewListView(View):
    template_name = 'reviews/review_list.html'
    querySet = Review.objects.all()

    def get_queryset(self):
        return self.querySet

    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        print(self.querySet.all())
        return render(request, self.template_name, context)


class MyListView(ReviewListView):
    querySet = Review.objects.filter(id=1)


class ReviewCreateView(View):
    template_name = 'reviews/review_create.html'

    def get(self, request, *args, **kwargs):
        # GET method
        form = ReviewModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = ReviewModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = ReviewModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)


class ReviewDeleteView(ReviewObjectMixin, View):
    template_name = 'reviews/review_delete.html'

    def get(self, request, id_=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id_=None, *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/reviews/')
        return render(request, self.template_name, context)


class ReviewUpdateView(ReviewObjectMixin, View):
    template_name = 'reviews/review_update.html'

    def get(self, request, id_=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ReviewModelForm(instance=obj)
            context = {'object': obj, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, id_=None, *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ReviewModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context = {'object': obj, 'form': form}
        return render(request, self.template_name, context)


class ReviewView(ReviewObjectMixin, View):
    template_name = 'reviews/review_detail.html'

    def get(self, request, id_=None, *args, **kwargs):
        # GET method
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)


# HTTP Methods - Function based views
def ReviewsListView_FuncBased(request, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})
