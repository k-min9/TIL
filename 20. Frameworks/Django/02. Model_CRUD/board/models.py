from django.db import models
from django.db.models.fields import TextField

# 질문 게시판
class Question(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updatedd_at = models.DateTimeField(auto_now=True)

    # 게시판 내 표시 내용을 object(1)에서 제목으로 변경
    def __str__(self):
        return self.title