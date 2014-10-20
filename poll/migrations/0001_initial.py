# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poll'
        db.create_table(u'poll_poll', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='encuestas', to=orm['esgiso.Proyecto'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'poll', ['Poll'])

        # Adding model 'Item'
        db.create_table(u'poll_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='respuestas', to=orm['esgiso.Proyecto'])),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Poll'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('pos', self.gf('django.db.models.fields.SmallIntegerField')(default='0')),
        ))
        db.send_create_signal(u'poll', ['Item'])

        # Adding model 'Vote'
        db.create_table(u'poll_vote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proyecto', self.gf('django.db.models.fields.related.ForeignKey')(related_name='votos', to=orm['esgiso.Proyecto'])),
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Poll'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Item'])),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.User'], null=True, blank=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'poll', ['Vote'])


    def backwards(self, orm):
        # Deleting model 'Poll'
        db.delete_table(u'poll_poll')

        # Deleting model 'Item'
        db.delete_table(u'poll_item')

        # Deleting model 'Vote'
        db.delete_table(u'poll_vote')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'erp.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'accion_comercial': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'blank': 'True'}),
            'comercial': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.PerfilEmpleado']"}),
            'coordenadas': ('geoposition.fields.GeopositionField', [], {'max_length': '42'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'email2_contacto': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'email_contacto': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'prospect'", 'max_length': '32'}),
            'fecha_entrada': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'localidad': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nif': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'observaciones': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'origen': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'razon_social': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'rubro_texto': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'telefono2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'erp.perfilempleado': {
            'Meta': {'object_name': 'PerfilEmpleado'},
            'email2_contacto': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'email_contacto': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'string_empleado': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'telefono2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'empleado'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['users.User']"})
        },
        u'esgiso.empleadoproyecto': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'EmpleadoProyecto'},
            'acceso': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'empleado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.PerfilEmpleado']"}),
            'es_comercial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'es_consultor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['esgiso.Proyecto']"}),
            'seleccionado': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'esgiso.proyecto': {
            'Meta': {'ordering': "['-nombre']", 'object_name': 'Proyecto'},
            'acceso_esgiso': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'empleados_asignados': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'proyectos'", 'symmetrical': 'False', 'through': u"orm['esgiso.EmpleadoProyecto']", 'to': u"orm['erp.PerfilEmpleado']"}),
            'empresa_erp': ('annoying.fields.AutoOneToOneField', [], {'related_name': "'empresa_erp'", 'unique': 'True', 'primary_key': 'True', 'to': u"orm['erp.Empresa']"}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'poll.item': {
            'Meta': {'ordering': "['pos']", 'object_name': 'Item'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Poll']"}),
            'pos': ('django.db.models.fields.SmallIntegerField', [], {'default': "'0'"}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'respuestas'", 'to': u"orm['esgiso.Proyecto']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'poll.poll': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Poll'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'encuestas'", 'to': u"orm['esgiso.Proyecto']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'poll.vote': {
            'Meta': {'object_name': 'Vote'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Item']"}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Poll']"}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'votos'", 'to': u"orm['esgiso.Proyecto']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.User']", 'null': 'True', 'blank': 'True'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['poll']
