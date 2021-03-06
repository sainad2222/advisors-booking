# Generated by Django 3.2.2 on 2021-05-07 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminRole', '0001_initial'),
        ('userRole', '0003_user_advisors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminRole.advisor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userRole.user')),
            ],
        ),
    ]
