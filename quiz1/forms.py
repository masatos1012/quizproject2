from django import forms


class QuizForm(forms.Form):
    question_text = forms.CharField(label='問題文', max_length=200)
    choice1 = forms.CharField(label='選択肢1', max_length=200)
    choice2 = forms.CharField(label='選択肢2', max_length=200)
    choice3 = forms.CharField(label='選択肢3', max_length=200)
    choice4 = forms.CharField(label='選択肢4', max_length=200)
    correct_choice = forms.ChoiceField(label='正解の選択肢',
                                       choices=[('1', '選択肢1'), ('2', '選択肢2'), ('3', '選択肢3'), ('4', '選択肢4')])
