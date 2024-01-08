# Практическое задание 3


###### Форма комментария
```
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["type", "rating", "message"]

```
###### Модель комментария
```

class Comment(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, default="collaboration",
                            choices=(('collaboration', 'collaboration'),
                                     ('racing', 'racing'),
                                     ('other', 'other')))
    message = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    
    class Meta:
        verbose_name ='Комментарий'
        verbose_name_plural='Комментарии'
```

###### Детали заезда, добавление комментариев
```
def race_detail(request, race_id):
    race = get_object_or_404(Race, pk=race_id)

    if request.method == "POST":
        if "rating" in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():

                comment = comment_form.save(commit=False)
                comment.race = race
                comment.writer = request.user
                comment.save()
        else:
            Register.objects.create(racer=request.user, race=race)

        return redirect("race_detail", race_id)

    else:
        has_reg = Register.objects.filter(
           racer__id=request.user.id, race__id=race_id
        ).exists()

        regs = Register.objects.filter(race=race_id).order_by('result')

        comment_form = CommentForm()
        comments = Comment.objects.filter(race=race_id)

        return render(
           request,
           "race_detail.html",
           {
               "race": race,
               "has_no_reg": not has_reg,
               "user": request.user,
               "regs": regs,
               "comments": comments,
               'comment_form': comment_form,
           },
       )


```
