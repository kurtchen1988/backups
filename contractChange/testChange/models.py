# -*- coding: utf-8 -*
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class TMesgRoutExchO2I(models.Model):
    mesg_id = models.CharField(max_length=15)
    mesg_type = models.CharField(max_length=255)
    mesg_code = models.CharField(max_length=255, blank=True, null=True)
    mesg_incode = models.CharField(max_length=255, blank=True, null=True)
    ent_code = models.CharField(max_length=255, blank=True, null=True)
    ent_name = models.CharField(max_length=255, blank=True, null=True)
    vertify_code = models.CharField(max_length=255, blank=True, null=True)
    mesg_data = models.BinaryField(blank=True, null=True)
    segment_status = models.FloatField(blank=True, null=True)
    mesg_status = models.CharField(max_length=1)
    update_time = models.DateField(blank=True, null=True)
    operate_time = models.DateField(blank=True, null=True)
    district_code = models.CharField(max_length=255, blank=True, null=True)
    clued = models.NullBooleanField()
    uuid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mesg_rout_exch_o2i'


class TMesgRoutExchO2ISx(models.Model):
    mesg_id = models.FloatField()
    mesg_type = models.CharField(max_length=255)
    mesg_code = models.CharField(max_length=255, blank=True, null=True)
    mesg_incode = models.CharField(max_length=255, blank=True, null=True)
    ent_code = models.CharField(max_length=255, blank=True, null=True)
    ent_name = models.CharField(max_length=255, blank=True, null=True)
    vertify_code = models.CharField(max_length=255)
    segment_status = models.FloatField(blank=True, null=True)
    mesg_status = models.CharField(max_length=1)
    update_time = models.DateField()
    operate_time = models.DateField(blank=True, null=True)
    district_code = models.CharField(max_length=255)
    sync_time = models.DateField(blank=True, null=True)
    mesg_data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mesg_rout_exch_o2i_sx'

