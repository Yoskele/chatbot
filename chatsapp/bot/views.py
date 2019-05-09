from django.shortcuts import render, redirect, HttpResponse


from .forms import Question
# Create your views here.




def help_bot(request):
    form_help_center = Question()
    if request.method == 'POST':
        form_help_center = Question(request.POST)
        if form_help_center.is_valid():
            question_text = form_help_center.cleaned_data['question_text']

            if question_text == 'Upload':
                answer =  'At Your Profile You have an option to upload profile picture or even upload an image with your post'

            elif question_text == 'Contact':
                answer = 'You Can Always Reach Out To Us On This Email Adress Chat@Gmail.Com'

            elif question_text == 'Send message':
                answer = 'Your Friends are one button away to chat with. In Our platform you will be avaible to talk to eachover.'

            elif question_text == 'Delete message':
                answer = 'If you dont like one of your message you can always hit the delete button at the chatroom.'

            else:
                return render(request, 'help.html')

            context = {
                'form': form_help_center,
                'answer': answer
                }
            return render(request, 'help.html', context)
    context = {
        'form_help_center': form_help_center
    }
    return render(request, 'help.html', context)