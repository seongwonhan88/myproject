from django import forms

from .models import Post


class PostCreateForm(forms.Form):
    photo = forms.ImageField()
    comment = forms.CharField(required=False)

    def save(self, **kwargs):
        if self.errors:
            raise ValueError('Post Validation Failed')

        post = Post.objects.create(photo=self.cleaned_data['photo'], **kwargs)
        comment_text = self.cleaned_data.get('comment')
        if comment_text:
            post.comment_set.create(author=post.author, content=comment_text)
        return post