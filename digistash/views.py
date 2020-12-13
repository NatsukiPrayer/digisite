
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from registration.models import Profile
from digistash.models import Digimon
from django.urls import reverse

from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-id')[:5]
    template = loader.get_template('digistash/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'digistash/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'digistash/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        print(request.user)
        digi = Digimon.objects.get(name=selected_choice)
        print(digi)
        prof = Profile.objects.get(user=request.user)
        prof.digimons.add(digi)
        if digi.name == 'Tsunomon':
            prof.haveT = True
        if digi.name == 'Gigimon':
            prof.haveG = True
        if digi.name == 'DemiVeemon':
            prof.haveV = True
        prof.save()
        print(prof.digimons.all())
        print(prof.check_digi())
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return redirect('/digistash/all_digi', request)
def all_digi(request):
    return render(request, 'digistash/all_digi.html', {'digimons':Digimon.objects.all()})
def acq_digi(request):
    try:
        selected_choice = request.POST['choice']
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'digistash/acq_digi.html', {'usersDigi':Profile.objects.get(user=request.user).digi_list(),
                                                        'quest':['DemiVeemon', 'Gigimon', 'Tsunomon'],
                                                           'haveT':Profile.objects.get(user=request.user).haveT,
                                                           'haveG':Profile.objects.get(user=request.user).haveG,
                                                           'haveV':Profile.objects.get(user=request.user).haveV,})
    else:
        print(request.user)
        print(selected_choice)
        print(selected_choice)
        print(selected_choice)
        digi = Digimon.objects.get(name=selected_choice)
        print(digi)
        prof = Profile.objects.get(user=request.user)
        if prof.money>=digi.money_to_evolve and prof.meat>=digi.meat_to_evolve:
            prof.money-=5
            prof.money -= 5
            prof.digimons.add(digi)
            if digi.name == 'Tsunomon':
                prof.haveT = True
            if digi.name == 'Gigimon':
                prof.haveG = True
            if digi.name == 'DemiVeemon':
                prof.haveV = True
            prof.save()
            return render(request, 'digistash/acq_digi.html',
                          {'usersDigi': Profile.objects.get(user=request.user).digi_list(),
                           'quest': ['DemiVeemon', 'Gigimon', 'Tsunomon'],
                           'sc_msg': "Succsess!", 'haveT':Profile.objects.get(user=request.user).haveT,
                                                           'haveG':Profile.objects.get(user=request.user).haveG,
                                                           'haveV':Profile.objects.get(user=request.user).haveV,})
        else:
            return render(request, 'digistash/acq_digi.html',
                          {'usersDigi': Profile.objects.get(user=request.user).digi_list(),
                           'quest': ['DemiVeemon', 'Gigimon', 'Tsunomon'],
                           'er_msg': "You don't have enough money or meat!", 'haveT':Profile.objects.get(user=request.user).haveT,
                                                           'haveG':Profile.objects.get(user=request.user).haveG,
                                                           'haveV':Profile.objects.get(user=request.user).haveV,})
        print(prof.digimons.all())
        print(prof.check_digi())
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'digistash/acq_digi.html',
                      {'usersDigi': Profile.objects.get(user=request.user).digi_list(),
                       'quest': ['DemiVeemon', 'Gigimon', 'Tsunomon'], 'haveT':Profile.objects.get(user=request.user).haveT,
                                                           'haveG':Profile.objects.get(user=request.user).haveG,
                                                           'haveV':Profile.objects.get(user=request.user).haveV,})
def my_digi(request):
    if request.method == 'POST':
        loggedUser = Profile.objects.get(user=request.user)
        for digimon in loggedUser.digi_list():
            if request.POST.get(digimon):
                evolving = request.POST[digimon]
                af_evolving = evolving.replace('Evolve to ', '')
                bf_evolving = digimon
        dg = Digimon.objects.get(name=bf_evolving)
        if loggedUser.meat>=dg.meat_to_evolve and loggedUser.money>=dg.money_to_evolve:
            loggedUser.money-=dg.money_to_evolve
            loggedUser.meat -= dg.meat_to_evolve
            loggedUser.digimons.remove(Digimon.objects.get(name=bf_evolving))
            loggedUser.digimons.add(Digimon.objects.get(name=af_evolving))
            loggedUser.save()
            return render(request, 'digistash/my_digi.html',
                          {'digimons': Profile.objects.get(user=request.user).digimons.all(),
                           'sc_msg':'Successfully evolved!'})
        else:
            return render(request, 'digistash/my_digi.html',
                          {'digimons': Profile.objects.get(user=request.user).digimons.all(),
                           'er_msg':"You don't have enough money or meat to evolve!" })
    return render(request, 'digistash/my_digi.html',
                  {'digimons': Profile.objects.get(user=request.user).digimons.all(),})

