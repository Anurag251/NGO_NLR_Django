# Generated by Django 4.0.4 on 2022-08-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_article_alter_news_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=225)),
                ('image', models.FileField(upload_to='teams/')),
                ('designation', models.CharField(max_length=225)),
                ('position', models.CharField(choices=[('team', 'Team Member'), ('board', 'Board Member'), ('both', 'both')], max_length=225)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
    ]
