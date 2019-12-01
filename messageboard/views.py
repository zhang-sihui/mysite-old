from django.views import generic
from django.utils import timezone
from .models import MessageBoard


# Create your views here.


class MsgBoardIndexView(generic.ListView):
    template_name = 'message/message_list.html'
    context_object_name = 'latest_message_list'

    def get_queryset(self):
        return MessageBoard.objects.filter(
            sub_date__lte=timezone.now()
        ).order_by('-sub_date')


class MsgBoardCreateView(generic.CreateView):
    model = MessageBoard
    template_name = 'message/message_create_form.html'
    fields = ['message']
    success_url = '/messageboard/message_list/'
