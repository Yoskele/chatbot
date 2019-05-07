from django.shortcuts import render, redirect


from .forms import Question
# Create your views here.




def help_bot(request):
	form = Question()
	if request.method == 'POST':
		form = Question(request.POST)
		if form.is_valid():
			print('After Validation')
			question_text = form.cleaned_data['question_text']
			print()
			if question_text == 'Yossi':
				answer=  ['Yossi is the King', 'hehter' ] 
				return render(request, 'help.html', {'answer':answer})

	context = {
		'form': form
	}
	return render(request, 'help.html', context)


