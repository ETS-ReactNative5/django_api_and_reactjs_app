# Generated by Django 2.0.5 on 2019-02-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_note', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usernote',
            options={'managed': True, 'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='usernote',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='usernote',
            name='note_type',
            field=models.CharField(choices=[('Profile', 'Profile'), ('CastingRequest', 'CastingRequest'), ('Search', 'Search'), ('View', 'View'), ('Favorite', 'Favorite'), ('Share', 'Share'), ('Block', 'Block'), ('MedicalCondition', 'MedicalCondition'), ('Medical', 'Medical'), ('Login', 'Login'), ('Logout', 'Logout'), ('TID', 'TID'), ('ChangePassword', 'ChangePassword'), ('Rating', 'Rating'), ('PersonalInfo', 'PersonalInfo'), ('Immigration', 'Immigration'), ('Language', 'Language')], default='Profile', max_length=30),
        ),
    ]
