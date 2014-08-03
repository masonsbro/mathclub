# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'User.password_salt'
        db.alter_column(u'mathapp_user', 'password_salt', self.gf('django.db.models.fields.CharField')(max_length=32, null=True))

        # Changing field 'User.password_hash'
        db.alter_column(u'mathapp_user', 'password_hash', self.gf('django.db.models.fields.CharField')(max_length=128, null=True))

    def backwards(self, orm):

        # Changing field 'User.password_salt'
        db.alter_column(u'mathapp_user', 'password_salt', self.gf('django.db.models.fields.CharField')(default='', max_length=32))

        # Changing field 'User.password_hash'
        db.alter_column(u'mathapp_user', 'password_hash', self.gf('django.db.models.fields.CharField')(default='', max_length=128))

    models = {
        u'mathapp.user': {
            'Meta': {'object_name': 'User'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contributor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'password_salt': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'reset_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mathapp']