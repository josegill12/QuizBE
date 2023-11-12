# Generated by Django 4.2.7 on 2023-11-09 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_quizanswer_savedquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedquestion',
            name='saved_options',
            field=models.ManyToManyField(related_name='included_in_saved_questions', to='quizapp.option'),
        ),
    ]