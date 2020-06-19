from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404

from boards.models import Board, Topic, Post
from boards.forms import TopicForm


def index_page_view(request):
    boards = Board.objects.all()
    return render(request, 'index.html', {'boards_list': boards})


def board_details_view(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'board_details.html', {'board': board})


@login_required
def new_topic_view(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.user = request.user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                authored_by=request.user
            )
        return redirect('board-details', pk=board.pk)
    form = TopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


def topic_posts(request, board_pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=board_pk, pk=topic_pk)
    return render(request, 'topic_posts.html', {'topic': topic})
