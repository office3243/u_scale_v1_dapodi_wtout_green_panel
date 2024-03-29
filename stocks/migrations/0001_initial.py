# Generated by Django 2.2.6 on 2019-11-05 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_created=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('opening_weight', models.FloatField(default=0.0)),
                ('in_weight', models.FloatField(default=0.0)),
                ('merge_in_weight', models.FloatField(default=0.0)),
                ('out_weight', models.FloatField(default=0.0)),
                ('closing_weight', models.FloatField(default=0.0)),
                ('status', models.CharField(choices=[('PN', 'Pending'), ('DN', 'Done')], default='PN', max_length=2)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='materials.Material')),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
