# Generated by Django 4.1.4 on 2023-01-02 11:49

from django.db import migrations, models
import main_page_cafe.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page_cafe', '0007_alter_book_table_f_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=300)),
                ('position', models.PositiveIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to=main_page_cafe.models.Hero.get_file_name)),
            ],
            bases=(models.Model, main_page_cafe.models.Import_file),
        ),
    ]