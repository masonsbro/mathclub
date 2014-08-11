# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ProblemGenerator.learn_item'
        db.delete_column(u'mathapp_problemgenerator', 'learn_item_id')

        # Adding M2M table for field learn_item on 'ProblemGenerator'
        m2m_table_name = db.shorten_name(u'mathapp_problemgenerator_learn_item')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('problemgenerator', models.ForeignKey(orm[u'mathapp.problemgenerator'], null=False)),
            ('learnitem', models.ForeignKey(orm[u'mathapp.learnitem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['problemgenerator_id', 'learnitem_id'])


    def backwards(self, orm):
        # Adding field 'ProblemGenerator.learn_item'
        db.add_column(u'mathapp_problemgenerator', 'learn_item',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mathapp.LearnItem'], null=True),
                      keep_default=False)

        # Removing M2M table for field learn_item on 'ProblemGenerator'
        db.delete_table(db.shorten_name(u'mathapp_problemgenerator_learn_item'))


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
            'learn_item': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['mathapp.LearnItem']", 'symmetrical': 'False'}),
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
            'Meta': {'ordering': "['difficulty__pk']", 'object_name': 'TargetScore'},
            'difficulty': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.Difficulty']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '230'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.User']"})
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