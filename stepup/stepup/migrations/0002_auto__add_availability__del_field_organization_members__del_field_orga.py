# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Availability'
        db.create_table(u'stepup_availability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('morning', self.gf('django.db.models.fields.BooleanField')()),
            ('afternoon', self.gf('django.db.models.fields.BooleanField')()),
            ('evening', self.gf('django.db.models.fields.BooleanField')()),
            ('night', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'stepup', ['Availability'])

        # Adding M2M table for field people on 'Tag'
        m2m_table_name = db.shorten_name(u'stepup_tag_people')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'stepup.tag'], null=False)),
            ('person', models.ForeignKey(orm[u'stepup.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'person_id'])

        # Adding M2M table for field opportunities on 'Tag'
        m2m_table_name = db.shorten_name(u'stepup_tag_opportunities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'stepup.tag'], null=False)),
            ('opportunity', models.ForeignKey(orm[u'stepup.opportunity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'opportunity_id'])

        # Deleting field 'Organization.members'
        db.delete_column(u'stepup_organization', 'members_id')

        # Deleting field 'Organization.opportunities'
        db.delete_column(u'stepup_organization', 'opportunities_id')

        # Adding M2M table for field people on 'Organization'
        m2m_table_name = db.shorten_name(u'stepup_organization_people')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organization', models.ForeignKey(orm[u'stepup.organization'], null=False)),
            ('person', models.ForeignKey(orm[u'stepup.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organization_id', 'person_id'])

        # Adding M2M table for field opportunities on 'Organization'
        m2m_table_name = db.shorten_name(u'stepup_organization_opportunities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('organization', models.ForeignKey(orm[u'stepup.organization'], null=False)),
            ('opportunity', models.ForeignKey(orm[u'stepup.opportunity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['organization_id', 'opportunity_id'])

        # Adding field 'Opportunity.city'
        db.add_column(u'stepup_opportunity', 'city',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=50),
                      keep_default=False)

        # Adding field 'Opportunity.state'
        db.add_column(u'stepup_opportunity', 'state',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=50),
                      keep_default=False)

        # Adding field 'Opportunity.country'
        db.add_column(u'stepup_opportunity', 'country',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=50),
                      keep_default=False)

        # Adding field 'Opportunity.date_created'
        db.add_column(u'stepup_opportunity', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None),
                      keep_default=False)

        # Adding M2M table for field tags on 'Opportunity'
        m2m_table_name = db.shorten_name(u'stepup_opportunity_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('opportunity', models.ForeignKey(orm[u'stepup.opportunity'], null=False)),
            ('tag', models.ForeignKey(orm[u'stepup.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['opportunity_id', 'tag_id'])

        # Adding M2M table for field organizations on 'Opportunity'
        m2m_table_name = db.shorten_name(u'stepup_opportunity_organizations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('opportunity', models.ForeignKey(orm[u'stepup.opportunity'], null=False)),
            ('organization', models.ForeignKey(orm[u'stepup.organization'], null=False))
        ))
        db.create_unique(m2m_table_name, ['opportunity_id', 'organization_id'])

        # Deleting field 'Person.schedule'
        db.delete_column(u'stepup_person', 'schedule')

        # Deleting field 'Person.tags'
        db.delete_column(u'stepup_person', 'tags_id')

        # Adding M2M table for field sunday on 'Person'
        m2m_table_name = db.shorten_name(u'stepup_person_sunday')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'stepup.person'], null=False)),
            ('availability', models.ForeignKey(orm[u'stepup.availability'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'availability_id'])

        # Adding M2M table for field tags on 'Person'
        m2m_table_name = db.shorten_name(u'stepup_person_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'stepup.person'], null=False)),
            ('tag', models.ForeignKey(orm[u'stepup.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'tag_id'])

        # Adding M2M table for field organizations on 'Person'
        m2m_table_name = db.shorten_name(u'stepup_person_organizations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'stepup.person'], null=False)),
            ('organization', models.ForeignKey(orm[u'stepup.organization'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'organization_id'])


    def backwards(self, orm):
        # Deleting model 'Availability'
        db.delete_table(u'stepup_availability')

        # Removing M2M table for field people on 'Tag'
        db.delete_table(db.shorten_name(u'stepup_tag_people'))

        # Removing M2M table for field opportunities on 'Tag'
        db.delete_table(db.shorten_name(u'stepup_tag_opportunities'))

        # Adding field 'Organization.members'
        db.add_column(u'stepup_organization', 'members',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['stepup.Person']),
                      keep_default=False)

        # Adding field 'Organization.opportunities'
        db.add_column(u'stepup_organization', 'opportunities',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['stepup.Opportunity']),
                      keep_default=False)

        # Removing M2M table for field people on 'Organization'
        db.delete_table(db.shorten_name(u'stepup_organization_people'))

        # Removing M2M table for field opportunities on 'Organization'
        db.delete_table(db.shorten_name(u'stepup_organization_opportunities'))

        # Deleting field 'Opportunity.city'
        db.delete_column(u'stepup_opportunity', 'city')

        # Deleting field 'Opportunity.state'
        db.delete_column(u'stepup_opportunity', 'state')

        # Deleting field 'Opportunity.country'
        db.delete_column(u'stepup_opportunity', 'country')

        # Deleting field 'Opportunity.date_created'
        db.delete_column(u'stepup_opportunity', 'date_created')

        # Removing M2M table for field tags on 'Opportunity'
        db.delete_table(db.shorten_name(u'stepup_opportunity_tags'))

        # Removing M2M table for field organizations on 'Opportunity'
        db.delete_table(db.shorten_name(u'stepup_opportunity_organizations'))

        # Adding field 'Person.schedule'
        db.add_column(u'stepup_person', 'schedule',
                      self.gf('django.db.models.fields.DateField')(default=None),
                      keep_default=False)

        # Adding field 'Person.tags'
        db.add_column(u'stepup_person', 'tags',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['stepup.Tag']),
                      keep_default=False)

        # Removing M2M table for field sunday on 'Person'
        db.delete_table(db.shorten_name(u'stepup_person_sunday'))

        # Removing M2M table for field tags on 'Person'
        db.delete_table(db.shorten_name(u'stepup_person_tags'))

        # Removing M2M table for field organizations on 'Person'
        db.delete_table(db.shorten_name(u'stepup_person_organizations'))


    models = {
        u'stepup.availability': {
            'Meta': {'object_name': 'Availability'},
            'afternoon': ('django.db.models.fields.BooleanField', [], {}),
            'evening': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'morning': ('django.db.models.fields.BooleanField', [], {}),
            'night': ('django.db.models.fields.BooleanField', [], {})
        },
        u'stepup.opportunity': {
            'Meta': {'object_name': 'Opportunity'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Organization']", 'symmetrical': 'False', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Tag']", 'symmetrical': 'False', 'blank': 'True'})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Organization']", 'symmetrical': 'False', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sunday': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Availability']", 'symmetrical': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stepup.Tag']", 'symmetrical': 'False', 'blank': 'True'})
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