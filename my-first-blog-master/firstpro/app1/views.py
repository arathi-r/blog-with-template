# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . models import Post
from django.shortcuts import render
from django.contrib.auth.models import User


def post_list(request):
    me=User.objects.get(username='amma')
    posts = Post.objects.filter(author=me).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})