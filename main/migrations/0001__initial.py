from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=100))
                ('course', models.CharField(max_length=100))
                ('year_level', models.IntegerField())
            ]
        )
    ]