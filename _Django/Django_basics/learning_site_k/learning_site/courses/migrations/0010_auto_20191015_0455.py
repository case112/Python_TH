# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_truefalsequestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='promt',
            new_name='prompt',
        ),
    ]
