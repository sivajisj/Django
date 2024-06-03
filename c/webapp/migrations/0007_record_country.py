
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_remove_record_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='country',
            field=models.CharField(default='Unknown', max_length=100),
            preserve_default=False,
        ),
    ]