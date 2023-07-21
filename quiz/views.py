from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from quiz.models import Quiz, Results

def say_hello(request):
    return render(request, 'quiz/hello.html', {'name':'Chae'})

def manager_quiz_view(request):
    # pack = get_object_or_404(Quiz)
    # quiz_list = Quiz.objects.all()
    # context = { "quiz_list": pack}
    return render(request, 'manager/set_quiz.html')

def insert_single(request):
    if request.method == 'POST':
        request_quiz = request.POST.get('quiz')
        request_answer = request.POST.get('answer')
        print("insert_single >> ", request_quiz, request_answer)

        if not request_quiz:
            return JsonResponse({'message' : 'input is empty'}, status=403)
        
        if request_answer != 'true' and request_answer != 'false':
            return JsonResponse({'message' : 'answer is wrong'}, status=403)
        
        new_quiz = Quiz(content = request_quiz, answer = request_answer)
        new_quiz.save()

        return JsonResponse({'message' : 'Done'}, status=200)