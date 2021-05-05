# Generated by Django 3.2 on 2021-05-04 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SubscribersInventory', '__first__'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('type_charge', models.CharField(blank=True, max_length=250, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True, verbose_name='Amount')),
                ('pay_ref', models.CharField(blank=True, max_length=250, null=True, verbose_name='Payment Reference')),
                ('status', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('UnPaid', 'UnPaid')], max_length=150, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('vodaconnect_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubscribersInventory.vodaconnectnumber')),
            ],
            options={
                'verbose_name': 'Other Charges',
                'verbose_name_plural': 'Other Charges',
                'ordering': ['type_charge'],
            },
        ),
        migrations.CreateModel(
            name='MonthlyCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7, null=True, verbose_name='Total Cost')),
                ('month_covered', models.DateField(blank=True, null=True)),
                ('date_payment', models.DateField(blank=True, null=True)),
                ('reference', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(blank=True, choices=[('Paid', 'Paid'), ('UnPaid', 'UnPaid')], max_length=150, null=True)),
                ('client_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.clientcode')),
                ('client_full_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubscribersInventory.voipinformation')),
                ('plan_types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubscribersInventory.plantype')),
                ('vodaconnect_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SubscribersInventory.vodaconnectnumber')),
            ],
            options={
                'verbose_name': 'Monthly Charges',
                'verbose_name_plural': 'Monthly Charges',
                'ordering': ['reference'],
            },
        ),
    ]
