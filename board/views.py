from django.shortcuts import render, get_object_or_404, redirect
from .forms import BoardForm
from comment.forms import CommentForm
from .models import Board
from django.utils import timezone

def post(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.update_date=timezone.now()
            board.save()
            return redirect('show')
    else:
        form = BoardForm()
        return render(request, 'post.html', {'form' : form})

def show(request):
    boards = Board.objects
    return render(request, 'show.html', {'boards' : boards})

def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    form = CommentForm()
    return render(request, 'detail.html', {'board' : board_detail, 'form': form})

def edit(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.update_date=timezone.now()
            board.save()
            return redirect('show')
    else:
        form = BoardForm(instance=board)
        return render(request, 'edit.html', {'form' : form})

def delete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('show')

def home(request):
    return render(request, 'home.html')
