
from django.db import migrations, models

def set_default_country(apps, schema_editor):
    Record = apps.get_model('webapp', 'Record')
    for record in Record.objects.all():
        record.country = 'Default Country'
        record.save()

class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_record_country'),
        # Add your migration dependencies here
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='country',
            field=models.CharField(max_length=100, default='Default Country'),
        ),
        migrations.RunPython(set_default_country),
    ]
