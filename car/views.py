from django.shortcuts import render,redirect
from django.views.generic import DetailView
from car.models import Car_Model,Order
from car.forms import CommentForm


class CarDetailsView(DetailView):
    model = Car_Model
    template_name = 'car_details.html'
    pk_url_kwarg = 'id'
    
    def get(self, request, *args, **kwargs):
        car_model_objects = Car_Model.objects.all()
        print(car_model_objects)
        return super().get(request, *args, **kwargs,)
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        car_model = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car_model = car_model
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car_model = self.get_object()
        comments = car_model.comments.all()
        data = Car_Model.objects.all()
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        context['car'] = car_model
        context['data'] = data
        return context

