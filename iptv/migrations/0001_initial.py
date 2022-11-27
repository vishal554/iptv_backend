# Generated by Django 4.1.3 on 2022-11-27 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('alt_name', models.CharField(max_length=100)),
                ('network', models.CharField(blank=True, max_length=100, null=True)),
                ('owners', models.CharField(max_length=1000)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('broadcast_area', models.CharField(max_length=1000)),
                ('is_nsfw', models.BooleanField()),
                ('launched', models.DateField(blank=True, null=True)),
                ('closed', models.DateField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('logo', models.URLField()),
                ('categories', models.ManyToManyField(related_name='channels', to='iptv.category')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('flag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='guides', serialize=False, to='iptv.channel')),
                ('site', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('channel', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, related_name='streams', serialize=False, to='iptv.channel')),
                ('url', models.URLField()),
                ('http_referrer', models.URLField()),
                ('user_agent', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('width', models.IntegerField(max_length=10)),
                ('height', models.IntegerField(max_length=10)),
                ('bitrate', models.IntegerField(max_length=10)),
                ('frame_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('added_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('checked_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SubDivision',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subdivisions', to='iptv.country')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('country', models.ManyToManyField(related_name='regions', to='iptv.country')),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='languages',
            field=models.ManyToManyField(related_name='countries', to='iptv.language'),
        ),
        migrations.AddField(
            model_name='channel',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='channels', to='iptv.country'),
        ),
        migrations.AddField(
            model_name='channel',
            name='languages',
            field=models.ManyToManyField(related_name='channels', to='iptv.language'),
        ),
        migrations.AddField(
            model_name='channel',
            name='replaced_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='iptv.channel'),
        ),
        migrations.AddField(
            model_name='channel',
            name='subdivision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='channels', to='iptv.subdivision'),
        ),
        migrations.CreateModel(
            name='BlockList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blocklist', to='iptv.channel')),
            ],
        ),
    ]
