# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TargetScore'
        db.create_table(u'mathapp_targetscore', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('difficulty', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mathapp.Difficulty'])),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=230)),
        ))
        db.send_create_signal(u'mathapp', ['TargetScore'])

        # Deleting field 'User.target_score'
        db.delete_column(u'mathapp_user', 'target_score')

        # Adding M2M table for field target_scores on 'User'
        m2m_table_name = db.shorten_name(u'mathapp_user_target_scores')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'mathapp.user'], null=False)),
            ('targetscore', models.ForeignKey(orm[u'mathapp.targetscore'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'targetscore_id'])


    def backwards(self, orm):
        # Deleting model 'TargetScore'
        db.delete_table(u'mathapp_targetscore')

        # Adding field 'User.target_score'
        db.add_column(u'mathapp_user', 'target_score',
                      self.gf('django.db.models.fields.IntegerField')(default=230),
                      keep_default=False)

        # Removing M2M table for field target_scores on 'User'
        db.delete_table(db.shorten_name(u'mathapp_user_target_scores'))


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
            'correct_answer': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.ProblemGenerator']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'time': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.User']"}),
            'user_answer': ('django.db.models.fields.CharField', [], {'max_length': '256'})
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
        u'mathapp.targetscore': {
            'Meta': {'object_name': 'TargetScore'},
            'difficulty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.Difficulty']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '230'})
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
            'reset_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'target_scores': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mathapp.TargetScore']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['mathapp']