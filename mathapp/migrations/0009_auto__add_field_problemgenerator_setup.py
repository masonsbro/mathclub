# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ProblemGenerator.setup'
        db.add_column(u'mathapp_problemgenerator', 'setup',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ProblemGenerator.setup'
        db.delete_column(u'mathapp_problemgenerator', 'setup')


    models = {
        u'mathapp.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['mathapp.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seen_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'posts_seen'", 'symmetrical': 'False', 'to': u"orm['mathapp.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'mathapp.difficulty': {
            'Meta': {'object_name': 'Difficulty'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'mathapp.problemgenerator': {
            'Meta': {'object_name': 'ProblemGenerator'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'setup': ('django.db.models.fields.TextField', [], {}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.Skill']"})
        },
        u'mathapp.skill': {
            'Meta': {'object_name': 'Skill'},
            'difficulty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.Difficulty']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'mathapp.user': {
            'Meta': {'object_name': 'User'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contributor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'password_hash': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'password_salt': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'reset_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mathapp']