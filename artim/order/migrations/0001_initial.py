# Generated by Django 3.2.3 on 2021-05-31 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=100)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_completed', models.BooleanField(default=False)),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('order_rejected', models.BooleanField(default=False)),
                ('order_accepted', models.BooleanField(default=False)),
                ('message', models.TextField(default=False)),
                ('artisanorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artisanorder', to='accounts.userprofile')),
                ('customerorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customerorder', to='accounts.userprofile')),
            ],
        ),
    ]