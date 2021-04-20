from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from accounts.decorators import user_required
from core.clean_up import clean_up_files
from pets.forms.comment_form import CommentForm
from pets.forms.pet_form import PetForm
from pets.models import Pet, Like, Comment


def list_pets(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, 'pets/list.html', context)

@login_required
def show_pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
            'form': CommentForm(),
            'can_delete': request.user == pet.user,
            'can_edit': request.user == pet.user,
            'can_like': request.user != pet.user,
            'has_liked': pet.like_set.filter(user=request.user).exists(),
            'can_comment': request.user != pet.user,
        }
        return render(request, 'pets/details.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.pet = pet
            comment.user = request.user
            comment.save()
            return redirect('pet details', pk)
        context = {
            'pet': pet,
            'form': form,
        }
        return render(request, 'pets/details.html', context)

@login_required
def like_pet(request, pk):
    like = Like.objects.filter(user=request.user, pet_id=pk).first()
    if like:
        like.delete()
    else:
        pet = Pet.objects.get(pk=pk)
        like = Like(user=request.user)
        like.pet = pet
        like.save()
    return redirect('pet details', pk)


def persist(request, pet, template_name):
    if request.method == 'GET':
        form = PetForm(instance=pet)
        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'pets/{template_name}.html', context)
    else:
        old_image = pet.image
        form = PetForm(request.POST, request.FILES, instance=pet)

        if form.is_valid():
            if old_image:
                clean_up_files(old_image.path)
            form.save()
            return redirect('pet details', pet.pk)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'pets/{template_name}.html', context)

@login_required
def create_pet(request):
    return persist(request, Pet(), 'create')

@user_required(Pet)
def edit_pet(request, pk):
    return persist(request, Pet.objects.get(pk=pk), 'edit')

@login_required
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
        }

        return render(request, 'pets/delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')