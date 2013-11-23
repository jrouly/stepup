# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Opportunity.monday'
        db.alter_column(u'stepup_opportunity', 'monday', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Opportunity.tuesday'
        db.alter_column(u'stepup_opportunity', 'tuesday', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Opportunity.friday'
        db.alter_column(u'stepup_opportunity', 'friday', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Opportunity.wednesday'
        db.alter_column(u'stepup_opportunity', 'wednesday', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Opportunity.thursday'
        db.alter_column(u'stepup_opportunity', 'thursday', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Opportunity.sunday'
        db.alter_column(u'stepup_opportunity', 'sunday', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Opportunity.saturday'
        db.alter_column(u'stepup_opportunity', 'saturday', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Person.monday'
        db.alter_column(u'stepup_person', 'monday', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Person.tuesday'
        db.alter_column(u'stepup_person', 'tuesday', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Person.friday'
        db.alter_column(u'stepup_person', 'friday', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Person.wednesday'
        db.alter_column(u'stepup_person', 'wednesday', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Person.thursday'
        db.alter_column(u'stepup_person', 'thursday', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Person.sunday'
        db.alter_column(u'stepup_person', 'sunday', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Person.saturday'
        db.alter_column(u'stepup_person', 'saturday', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'Opportunity.monday'
        db.alter_column(u'stepup_opportunity', 'monday', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Opportunity.tuesday'
        db.alter_column(u'stepup_opportunity', 'tuesday', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Opportunity.friday'
        db.alter_column(u'stepup_opportunity', 'friday', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Opportunity.wednesday'
        db.alter_column(u'stepup_opportunity', 'wednesday', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Opportunity.thursday'
        db.alter_column(u'stepup_opportunity', 'thursday', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Opportunity.sunday'
        db.alter_column(u'stepup_opportunity', 'sunday', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Opportunity.saturday'
        db.alter_column(u'stepup_opportunity', 'saturday', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Person.monday'
        db.alter_column(u'stepup_person', 'monday', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Person.tuesday'
        db.alter_column(u'stepup_person', 'tuesday', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Person.friday'
        db.alter_column(u'stepup_person', 'friday', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Person.wednesday'
        db.alter_column(u'stepup_person', 'wednesday', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Person.thursday'
        db.alter_column(u'stepup_person', 'thursday', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Person.sunday'
        db.alter_column(u'stepup_person', 'sunday', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Person.saturday'
        db.alter_column(u'stepup_person', 'saturday', self.gf('django.db.models.fields.CharField')(max_length=100))

    models = {
        u'stepup.opportunity': {
            'Meta': {'object_name': 'Opportunity'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'friday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Organization']", 'symmetrical': 'False', 'blank': 'True'}),
            'saturday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sunday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'thursday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tuesday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'wednesday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'stepup.organization': {
            'Meta': {'object_name': 'Organization'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opportunities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Opportunity']", 'symmetrical': 'False', 'blank': 'True'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Person']", 'symmetrical': 'False', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'stepup.person': {
            'Meta': {'object_name': 'Person'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'friday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'monday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Organization']", 'symmetrical': 'False', 'blank': 'True'}),
            'saturday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sunday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'thursday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tuesday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'wednesday': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'stepup.tag': {
            'Meta': {'object_name': 'Tag'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opportunities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Opportunity']", 'symmetrical': 'False', 'blank': 'True'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Person']", 'symmetrical': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['stepup']