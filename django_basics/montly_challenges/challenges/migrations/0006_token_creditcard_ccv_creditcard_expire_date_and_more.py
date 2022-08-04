# Generated by Django 4.0.5 on 2022-07-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0005_creditcard_alter_user_address_user_credit_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='creditcard',
            name='ccv',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='creditcard',
            name='expire_date',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='credit_card_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.ManyToManyField(to='challenges.token'),
        ),
    ]
