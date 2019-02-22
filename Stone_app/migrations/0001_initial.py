# Generated by Django 2.1.7 on 2019-02-22 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessUser',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=18)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('business_address', models.CharField(max_length=200)),
                ('office_number', models.CharField(blank=True, max_length=50, null=True)),
                ('user_image', models.ImageField(blank=True, default='Stone_app/Image/Stone_app/User_Image/no-img.jpg', null=True, upload_to='Stone_app/Media/Image/Stone_app/User_Image')),
                ('pub_date', models.DateField(auto_now=True)),
                ('kind_of_work', models.CharField(blank=True, choices=[('SC', 'سنگبری'), ('SG', 'سنگ قیچی'), ('CNC', 'CNC')], default='SC', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower_user', models.CharField(max_length=12)),
                ('followed_user', models.CharField(max_length=12)),
                ('date_of_add', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostUser',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_text', models.TextField(max_length=500)),
                ('post_picture', models.ImageField(blank=True, default='Stone_app/Media/Image/Stone_app/Posts_Images/no-img.jpg', null=True, upload_to='Stone_app/Media/Image/Stone_app/Posts_Images')),
                ('post_video', models.FileField(blank=True, default='Stone_app/Media/Video/Stone_app/Post_Video', null=True, upload_to='Stone_app/Media/Video/Stone_app/Post_Video')),
                ('post_sharp', models.CharField(blank=True, max_length=30, null=True)),
                ('date_of_add', models.DateTimeField(auto_now_add=True)),
                ('business_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Stone_app.BusinessUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=200)),
                ('username', models.CharField(max_length=12)),
                ('date_of_add', models.DateTimeField(auto_now=True)),
                ('display', models.CharField(blank=True, choices=[('show', 'نمایش نظر'), ('hide', 'حذف نظر')], default='show', max_length=4)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Stone_app.BusinessUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_page', models.IntegerField(default=0)),
                ('like_post', models.IntegerField(default=0)),
                ('post_id', models.IntegerField(blank=True, null=True)),
                ('like_comment', models.IntegerField(default=0)),
                ('comment_id', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=12)),
                ('liker_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Stone_app.BusinessUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserPageProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=0)),
                ('bio', models.TextField(blank=True, max_length=300, null=True)),
                ('Profile_Image', models.ImageField(blank=True, default='Stone_app/Media/Image/Stone_app/Profile_Image/no-img.jpg', null=True, upload_to='Stone_app/Media/Image/Stone_app/Profile_Image')),
                ('notifics', models.TextField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, choices=[('other', 'سایر'), ('Esfahan', 'اصفهان'), ('NajafAbad', 'نجف آباد'), ('Tiran', 'تیران'), ('RezvanCity', 'رضوانشهر')], default='other', max_length=30)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Stone_app.BusinessUser')),
            ],
        ),
    ]
