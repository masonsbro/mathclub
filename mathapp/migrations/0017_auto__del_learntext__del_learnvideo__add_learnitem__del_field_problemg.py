# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'LearnText'
        db.delete_table(u'mathapp_learntext')

        # Deleting model 'LearnVideo'
        db.delete_table(u'mathapp_learnvideo')

        # Adding model 'LearnItem'
        db.create_table(u'mathapp_learnitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mathapp.User'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mathapp.Skill'])),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'mathapp', ['LearnItem'])

        # Deleting field 'ProblemGenerator.learnVideo'
        db.delete_column(u'mathapp_problemgenerator', 'learnVideo_id')

        # Deleting field 'ProblemGenerator.learnText'
        db.delete_column(u'mathapp_problemgenerator', 'learnText_id')

        # Adding field 'ProblemGenerator.learnItem'
        db.add_column(u'mathapp_problemgenerator', 'learnItem',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mathapp.LearnItem'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'LearnText'
        db.create_table(u'mathapp_learntext', (
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mathapp.User'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mathapp.Skill'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'mathapp', ['LearnText'])

        # Adding model 'LearnVideo'
        db.create_table(u'mathapp_learnvideo', (
            ('code', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mathapp.User'])),
            ('skill', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mathapp.Skill'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'mathapp', ['LearnVideo'])

        # Deleting model 'LearnItem'
        db.delete_table(u'mathapp_learnitem')

        # Adding field 'ProblemGenerator.learnVideo'
        db.add_column(u'mathapp_problemgenerator', 'learnVideo',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mathapp.LearnVideo'], null=True),
                      keep_default=False)

        # Adding field 'ProblemGenerator.learnText'
        db.add_column(u'mathapp_problemgenerator', 'learnText',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mathapp.LearnText'], null=True),
                      keep_default=False)

        # Deleting field 'ProblemGenerator.learnItem'
        db.delete_column(u'mathapp_problemgenerator', 'learnItem_id')


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
            'Meta': {'object_name': 'LearnItem'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.User']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.Skill']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'mathapp.practice': {
            'Meta': {'object_name': 'Practice'},
            'correct': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.ProblemGenerator']"}),
            'time': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.User']"})
        },
        u'mathapp.problemgenerator': {
            'Meta': {'object_name': 'ProblemGenerator'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'answer_prefix': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'answer_suffix': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'learnItem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mathapp.LearnItem']", 'null': 'True'}),
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