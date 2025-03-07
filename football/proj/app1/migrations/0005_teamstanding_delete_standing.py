# Generated by Django 5.1.6 on 2025-03-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_club_standing_club'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamStanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100, unique=True)),
                ('matches_played', models.PositiveIntegerField(default=0)),
                ('wins', models.PositiveIntegerField(default=0)),
                ('losses', models.PositiveIntegerField(default=0)),
                ('draws', models.PositiveIntegerField(default=0)),
                ('points', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Standing',
        ),
    ]
