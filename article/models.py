from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")#auth.user tablosundan bir foreign key belirlemiş oluyorum
    #yazarlar buradaki kullanıcılar olacak aslında o yüzden
    #yazar silindiğinde ona ait olanların da silinmesi için Cascade yaptık
    title = models.CharField(max_length = 50, verbose_name="Başlık")
    content = RichTextField()
    article_image = models.FileField(blank=True,null=True,verbose_name="Makaleye Fotoğraf Ekleyin") # boşta olabilir
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")#o anki tarihi veri tabanına otomatik olarak atayacak

#bu oluşturduğum modeli kaydetmek için admin.py de kayıt edşcez
    def __str__(self):
        return self.title #article altında listelenirken başlıkta yazan yazacak
        #eğer yazarın gözükmesini isteseydik author yazardık gibi

    class Meta:
        ordering = ['-created_date']#en son eklenen makalemiz ilk gösterilir.


class Comment(models.Model):
    article  = models.ForeignKey(Article,on_delete=models.CASCADE, verbose_name="Makale" , related_name="comments")

    comment_author = models.CharField(max_length= 50, verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    #model oluşturduk admin.pyye eklicez

    def __str__(self):
        return self.comment_content
    
    class Meta:
        ordering = ['-comment_date']
