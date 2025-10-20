from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Movie
from .forms import MovieForm

# Create
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie added.")
            return redirect('movies:list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form, 'mode': 'Create'})

# Read (list)
def movie_list(request):
    movies = Movie.objects.all().order_by('MovieTitle')
    return render(request, 'movies/movie_list.html', {'movies': movies})

# Read (detail)
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

# Update
def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, "Movie updated.")
            return redirect('movies:detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form, 'mode': 'Update'})

# Delete
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        messages.success(request, "Movie deleted.")
        return redirect('movies:list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})