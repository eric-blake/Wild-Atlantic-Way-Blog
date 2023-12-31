# Generated by Django 3.2.22 on 2023-11-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waw_blog', '0003_remove_post_view_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='waw_blog.Category'),
        ),
    ]
