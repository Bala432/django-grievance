# Generated by Django 2.1.5 on 2019-03-01 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190228_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(default=' ', max_length=50)),
                ('details', models.TextField(max_length=512)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('superpost', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='publish', to='app.UserInfo')),
            ],
        ),
    ]
