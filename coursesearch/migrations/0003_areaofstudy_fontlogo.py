# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursesearch', '0002_auto_20151119_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='areaofstudy',
            name='fontlogo',
            field=models.CharField(max_length=30, default=1),
            preserve_default=False,
        ),
    ]
