# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Practice.question'
        db.add_column(u'mathapp_practice', 'question',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Practice.correct_answer'
        db.add_column(u'mathapp_practice', 'correct_answer',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Practice.user_answer'
        db.add_column(u'mathapp_practice', 'user_answer',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Practice.question'
        db.delete_column(u'mathapp_practice', 'question')

        # Deleting field 'Practice.correct_answer'
        db.delete_column(u'mathapp_practice', 'correct_answer')

        # Deleting field 'Practice.user_answer'
        db.delete_column(u'mathapp_practice', 'user_answer')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'mathapp.learnitem': {
            'Meta': {'ordering': "['pk']", 'object_name': 'LearnItem'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.Skill']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'mathapp.practice': {
            'Meta': {'object_name': 'Practice'},
            'correct': ('django.db.models.fields.BooleanField', [], {}),
            'correct_answer': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.ProblemGenerator']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.User']"}),
            'user_answer': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'mathapp.problemgenerator': {
            'Meta': {'object_name': 'ProblemGenerator'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'answer_prefix': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'answer_suffix': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learn_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.LearnItem']", 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'round': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'setup': ('django.db.models.fields.TextField', [], {}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.Skill']"})
        },
        u'mathapp.skill': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Skill'},
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