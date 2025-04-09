# Generated by Django 5.1.6 on 2025-03-26 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('borrowed_books', models.ManyToManyField(blank=True, to='library.book')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
