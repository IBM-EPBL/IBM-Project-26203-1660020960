from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addmoney_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_money', models.CharField(choices=[('Expense', 'Expense'), ('Income', 'Income')], max_length=10)),
                ('quantity', models.BigIntegerField()),
                ('Date', models.DateField(default=django.utils.timezone.now)),
                ('Category', models.CharField(choices=[('Food', 'Food'), ('Travel', 'Travel'), ('Shopping', 'Shopping'), ('Necessities', 'Necessities'), ('Entertainment', 'Entertainment'), ('Saving', 'Saving'), ('Miscellaneous', 'Miscellaneous'), ('Other', 'Other')], default='Food', max_length=20)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
