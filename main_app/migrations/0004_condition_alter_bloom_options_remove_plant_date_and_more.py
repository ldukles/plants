# Generated by Django 4.0.5 on 2022-07-08 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_bloom_delete_conditions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sun', models.CharField(max_length=15)),
                ('moisture', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterModelOptions(
            name='bloom',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='plant',
            name='date',
        ),
        migrations.AddField(
            model_name='plant',
            name='conditions',
            field=models.ManyToManyField(to='main_app.condition'),
        ),
    ]
