#!/bin/bash
#get
curl -u admin:administrador https://django-rest-mariopayan.c9users.io/comments/
#get
curl -u admin:administrador https://django-rest-mariopayan.c9users.io/comments/1/
#post
curl -u admin:administrador -d "owner=1&body=BBB&marker=CCC" https://django-rest-mariopayan.c9users.io/comments/
#patch
curl -u admin:administrador -d "karma=200" https://django-rest-mariopayan.c9users.io/comments/1/ -X PATCH
#del
curl -u admin:administrador https://django-rest-mariopayan.c9users.io/comments/1/ -X DELETE
