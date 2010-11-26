from django.conf.urls.defaults import *

urlpatterns = patterns('programas.views',
        (r'^$', 'lista'),
        (r'^exercicio1/$', 'exercicio1'),
        (r'^exercicio2/$', 'exercicio2'),
        (r'^exercicio3/$', 'exercicio3'),
        (r'^exercicio7/$', 'exercicio7'),
        (r'^exercicio10/$', 'exercicio10'),
    )

