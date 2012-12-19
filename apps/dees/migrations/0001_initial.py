# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table('dees_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('project_manager', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='project_mgr_of_project', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('account_manager', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='account_mgr_of_project', null=True, on_delete=models.SET_NULL, to=orm['auth.User'])),
            ('project_id', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('dees', ['Project'])

        # Adding model 'Skill'
        db.create_table('dees_skill', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('dees', ['Skill'])

        # Adding model 'Task'
        db.create_table('dees_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dees.Project'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('prework', self.gf('django.db.models.fields.TextField')()),
            ('scope', self.gf('django.db.models.fields.TextField')()),
            ('duration', self.gf('django.db.models.fields.FloatField')()),
            ('window', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('dees', ['Task'])

        # Adding M2M table for field skills on 'Task'
        db.create_table('dees_task_skills', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('task', models.ForeignKey(orm['dees.task'], null=False)),
            ('skill', models.ForeignKey(orm['dees.skill'], null=False))
        ))
        db.create_unique('dees_task_skills', ['task_id', 'skill_id'])

        # Adding model 'ResourceRequest'
        db.create_table('dees_resourcerequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requester', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, on_delete=models.SET_NULL, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dees.Project'])),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dees.Task'])),
            ('request_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('dees', ['ResourceRequest'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table('dees_project')

        # Deleting model 'Skill'
        db.delete_table('dees_skill')

        # Deleting model 'Task'
        db.delete_table('dees_task')

        # Removing M2M table for field skills on 'Task'
        db.delete_table('dees_task_skills')

        # Deleting model 'ResourceRequest'
        db.delete_table('dees_resourcerequest')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dees.project': {
            'Meta': {'object_name': 'Project'},
            'account_manager': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'account_mgr_of_project'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'project_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'project_manager': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'project_mgr_of_project'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['auth.User']"}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'dees.resourcerequest': {
            'Meta': {'object_name': 'ResourceRequest'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dees.Project']"}),
            'request_date': ('django.db.models.fields.DateTimeField', [], {}),
            'requester': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dees.Task']"})
        },
        'dees.skill': {
            'Meta': {'object_name': 'Skill'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'dees.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'duration': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prework': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dees.Project']"}),
            'scope': ('django.db.models.fields.TextField', [], {}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dees.Skill']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'window': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['dees']