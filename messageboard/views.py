from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import MessageBoard
from .forms import MessageBoardForm


# Create your views here.


class MsgBoardIndexView(generic.ListView):
    template_name = 'message/message_list.html'
    context_object_name = 'latest_message_list'

    def get_queryset(self):
        return MessageBoard.objects.filter(
            sub_date__lte=timezone.now()
        ).order_by('-sub_date')


def message_create(request):
    # 留言表单
    if request.method == "POST":
        msg_form = MessageBoardForm(request.POST)
        if msg_form.is_valid():
            content = msg_form.cleaned_data['content']
            cmt = MessageBoard.objects.create()
            cmt.content = content
            cmt.sub_date = timezone.now()
            cmt.reply = "暂未回复"
            cmt.reply_date = timezone.now()
            cmt.save()
            return HttpResponseRedirect(reverse('messageboard:message_list'))
    else:
        msg_form = MessageBoardForm()
    return render(request, 'message/message_create_form.html', locals())
