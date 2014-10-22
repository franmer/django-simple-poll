# -*- coding: utf-8 -*-

import datetime
from django.db import models
from django.utils.translation import gettext as _
from django.db.models.manager import Manager
from django.core.exceptions import ValidationError
from django.conf import settings
from esgiso.models import Proyecto

User = settings.AUTH_USER_MODEL


class PublishedManager(Manager):
    def get_query_set(self):
        return super(PublishedManager, self).get_query_set().filter(is_published=True)

class Poll(models.Model):
    proyecto =  models.ForeignKey(Proyecto, related_name='preguntas')
    title = models.CharField(max_length=250, verbose_name=_('Pregunta'))
    date = models.DateField(verbose_name=_('Fecha'), default=datetime.date.today)
    is_published = models.BooleanField(default=True, verbose_name=_('Publicada'))

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-date']
        verbose_name = _('Pregunta')
        verbose_name_plural = _('Preguntas')

    def __unicode__(self):
        return self.title

    def get_vote_count(self):
        return Vote.objects.filter(poll=self).count()
    vote_count = property(fget=get_vote_count, verbose_name="Votos")

    def get_cookie_name(self):
        return str('poll_%s' % (self.pk))


class Item(models.Model):
    proyecto =  models.ForeignKey(Proyecto, related_name='respuestas')
    poll = models.ForeignKey(Poll)
    value = models.CharField(max_length=250, verbose_name=_('Valor'))
    pos = models.SmallIntegerField(default='0', verbose_name=_('Posición'))

    class Meta:
        verbose_name = _('Respuesta')
        verbose_name_plural = _('Respuestas')
        ordering = ['pos']

    def __unicode__(self):
        return u'%s' % (self.value,)

    def get_vote_count(self):
        return Vote.objects.filter(item=self).count()
    vote_count = property(fget=get_vote_count)


class Vote(models.Model):
    proyecto =  models.ForeignKey(Proyecto, related_name='votos')
    poll = models.ForeignKey(Poll, verbose_name=_('Encuesta'))
    item = models.ForeignKey(Item, verbose_name=_('Elemento votado'))
    ip = models.IPAddressField(verbose_name=_('user\'s IP'))
    user = models.ForeignKey(User, blank=True, null=True,
                             verbose_name=_('usuario'))
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Voto')
        verbose_name_plural = _('Votos')

    def __unicode__(self):
        if isinstance(self.user, User):
            username_field = getattr(User, 'USERNAME_FIELD', 'username')
            return getattr(User, username_field, '')
        return self.ip
