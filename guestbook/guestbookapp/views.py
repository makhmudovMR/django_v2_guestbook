from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentsForm

def index(request):
    comments = Comment.objects.order_by('-date_added')
    context = {'comments': comments}
    return render(request, 'guestbookapp/index.html', context)


def sign(request):
    if request.method == 'POST':
        form = CommentsForm(request.POST)

        if form.is_valid(): # if token is valid
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return redirect('index')
    else:
        form = CommentsForm()

    context = {'form': form}
    return render(request, 'guestbookapp/sign.html', context=context)
