from django.shortcuts import render, get_object_or_404, redirect
from board.models import Board
from .forms import CommentForm
from .models import Comment

def commentcreate(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = board
            comment.save()
            return redirect('detail', board_id=board.pk)
    else:
        form = CommentForm()
        return render(request, 'detail.html', {'form': form})