from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(max_length=255)
    waktu_posting = models.DateTimeField(auto_now_add=True)
    # pembahasan
    # Post.objects.create(id="value")
    # Post.objects.all()
    # Post.objects.all()[1].delete()

    # a = Post.objects.all()[0]
    ## a.title = "judul baru"
    ## a.save()

    # looping sederhana
    # repr(semuaPost)
    # len(semuaPost)

    # email = models.EmailField(default='nama@mail.com') # default adalah options untuk memasukan nilai default email, karena field email tidak boleh kosong
    # alamat = models.CharField(max_length=200, blank=True)
    # date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.title)