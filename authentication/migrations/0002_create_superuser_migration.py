from django.db import migrations, models
from django.core.management import call_command

def create_superuser(apps, schema_editor):
    call_command('create_custom_superuser')

class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
