# Generated by Django 3.2 on 2021-04-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_tempvolmodel_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempvolmodel',
            name='cvu_name',
            field=models.CharField(choices=[('0', 'ЦВУ 1.1'),
                                            ('1', 'ЦВУ 1.2'),
                                            ('2', 'ЦВУ 1.3'),
                                            ('3', 'ЦВУ 1.4'),
                                            ('4', 'ЦВУ 2.1'),
                                            ('5', 'ЦВУ 2.2'),
                                            ('6', 'ЦВУ 2.3'),
                                            ('7', 'ЦВУ 2.4'),
                                            ('8', 'ЦВУ 3.1'),
                                            ('9', 'ЦВУ 3.2'),
                                            ('A', 'ЦВУ 3.3'),
                                            ('B', 'ЦВУ 3.4'),
                                            ('C', 'ЦВУ 4.1'),
                                            ('D', 'ЦВУ 4.2'),
                                            ('E', 'ЦВУ 4.3'),
                                            ('F', 'ЦВУ 4.4')],
                                   default='0',
                                   max_length=1),
        ),
    ]
