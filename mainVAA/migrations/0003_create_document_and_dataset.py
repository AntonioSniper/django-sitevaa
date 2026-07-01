from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainVAA', '0002_wordtemplate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'document',
            },
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familia', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('otchestvo', models.TextField(blank=True, null=True)),
                ('tip', models.TextField(blank=True, null=True)),
                ('tip_title', models.TextField(blank=True, null=True)),
                ('module', models.TextField(blank=True, null=True)),
                ('module_code', models.TextField(blank=True, null=True)),
                ('specialization', models.TextField(blank=True, null=True)),
                ('kurs', models.IntegerField(blank=True, null=True)),
                ('group', models.TextField(blank=True, null=True)),
                ('date_begin', models.TextField(blank=True, null=True)),
                ('date_finish', models.TextField(blank=True, null=True)),
                ('head1', models.TextField(blank=True, null=True)),
                ('head2', models.TextField(blank=True, null=True)),
                ('ruc_pract', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('fio_genitive', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='practice_data', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'data_set',
            },
        ),
    ]