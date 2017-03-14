# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0004_auto_20150330_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='nome_empresa',
            new_name='classe',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='telefone',
        ),
    ]
