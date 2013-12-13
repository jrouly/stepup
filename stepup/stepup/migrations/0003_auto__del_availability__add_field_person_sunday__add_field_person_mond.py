# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Availability'
        db.delete_table(u'stepup_availability')

        # Adding field 'Person.sunday'
        db.add_column(u'stepup_person', 'sunday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Person.monday'
        db.add_column(u'stepup_person', 'monday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Person.tuesday'
        db.add_column(u'stepup_person', 'tuesday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Person.wednesday'
        db.add_column(u'stepup_person', 'wednesday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Person.thursday'
        db.add_column(u'stepup_person', 'thursday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Person.friday'
        db.add_column(u'stepup_person', 'friday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Person.saturday'
        db.add_column(u'stepup_person', 'saturday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Removing M2M table for field sunday on 'Person'
        db.delete_table(db.shorten_name(u'stepup_person_sunday'))

        # Adding field 'Opportunity.sunday'
        db.add_column(u'stepup_opportunity', 'sunday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Opportunity.monday'
        db.add_column(u'stepup_opportunity', 'monday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Opportunity.tuesday'
        db.add_column(u'stepup_opportunity', 'tuesday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Opportunity.wednesday'
        db.add_column(u'stepup_opportunity', 'wednesday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Opportunity.thursday'
        db.add_column(u'stepup_opportunity', 'thursday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Opportunity.friday'
        db.add_column(u'stepup_opportunity', 'friday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Opportunity.saturday'
        db.add_column(u'stepup_opportunity', 'saturday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Availability'
        db.create_table(u'stepup_availability', (
            ('evening', self.gf('django.db.models.fields.BooleanField')()),
            ('morning', self.gf('django.db.models.fields.BooleanField')()),
            ('afternoon', self.gf('django.db.models.fields.BooleanField')()),
            ('night', self.gf('django.db.models.fields.BooleanField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'stepup', ['Availability'])

        # Deleting field 'Person.sunday'
        db.delete_column(u'stepup_person', 'sunday')

        # Deleting field 'Person.monday'
        db.delete_column(u'stepup_person', 'monday')

        # Deleting field 'Person.tuesday'
        db.delete_column(u'stepup_person', 'tuesday')

        # Deleting field 'Person.wednesday'
        db.delete_column(u'stepup_person', 'wednesday')

        # Deleting field 'Person.thursday'
        db.delete_column(u'stepup_person', 'thursday')

        # Deleting field 'Person.friday'
        db.delete_column(u'stepup_person', 'friday')

        # Deleting field 'Person.saturday'
        db.delete_column(u'stepup_person', 'saturday')

        # Adding M2M table for field sunday on 'Person'
        m2m_table_name = db.shorten_name(u'stepup_person_sunday')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'stepup.person'], null=False)),
            ('availability', models.ForeignKey(orm[u'stepup.availability'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'availability_id'])

        # Deleting field 'Opportunity.sunday'
        db.delete_column(u'stepup_opportunity', 'sunday')

        # Deleting field 'Opportunity.monday'
        db.delete_column(u'stepup_opportunity', 'monday')

        # Deleting field 'Opportunity.tuesday'
        db.delete_column(u'stepup_opportunity', 'tuesday')

        # Deleting field 'Opportunity.wednesday'
        db.delete_column(u'stepup_opportunity', 'wednesday')

        # Deleting field 'Opportunity.thursday'
        db.delete_column(u'stepup_opportunity', 'thursday')

        # Deleting field 'Opportunity.friday'
        db.delete_column(u'stepup_opportunity', 'friday')

        # Deleting field 'Opportunity.saturday'
        db.delete_column(u'stepup_opportunity', 'saturday')


    models = {
        u'stepup.opportunity': {
            'Meta': {'object_name': 'Opportunity'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'friday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Organization']", 'symmetrical': 'False', 'blank': 'True'}),
            'saturday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sunday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'thursday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tuesday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'wednesday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
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
            'friday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'monday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Organization']", 'symmetrical': 'False', 'blank': 'True'}),
            'saturday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sunday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'thursday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tuesday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'wednesday': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
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