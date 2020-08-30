from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import MessageBoard
from .forms import MessageBoardForm


# Create your views here.

class MsgBoardIndexView(generic.ListView):
    template_name = 'message/messages.html'
    context_object_name = 'latest_message_list'

    def get_queryset(self):
        return MessageBoard.objects.filter(sub_date__lte=timezone.now()).order_by('-sub_date')


def create_message(request):
    if request.method == 'POST':
        msg_form = MessageBoardForm(request.POST)
        if msg_form.is_valid():
            content = msg_form.cleaned_data['content']
            message_board = MessageBoard.objects.create()
            message_board.content = content
            message_board.sub_date = timezone.now()
            message_board.reply = '暂未回复'
            message_board.reply_date = timezone.now()
            message_board.save()
            return HttpResponseRedirect(reverse('messageboard:messages'))
    else:
        msg_form = MessageBoardForm()
    return render(request, 'message/create.html', locals())
