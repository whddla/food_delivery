from django.db import models

class Admin(models.Model):
    no = models.AutoField(primary_key=True)
    id = models.CharField(max_length=10)
    pw = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'admin'


class AdminContent(models.Model):
    no = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    upload_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    view_cnt = models.IntegerField(blank=True, null=True)
    admin_no = models.ForeignKey(Admin, models.DO_NOTHING, db_column='admin_no')

    class Meta:
        managed = False
        db_table = 'admin_content'


class CeoOrder(models.Model):
    no = models.AutoField(primary_key=True)
    status = models.IntegerField()
    order_no = models.ForeignKey('UserOrder', models.DO_NOTHING, db_column='order_no')

    class Meta:
        managed = False
        db_table = 'ceo_order'



class Menu(models.Model):
    no = models.AutoField(primary_key=True)
    menu_cate = models.IntegerField()
    food_name = models.CharField(max_length=20)
    price = models.IntegerField()
    ceo_no = models.ForeignKey('User', models.DO_NOTHING, db_column='ceo_no')

    class Meta:
        managed = False
        db_table = 'menu'


class Store(models.Model):
    no = models.AutoField(primary_key=True)
    account = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    review = models.CharField(max_length=100, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    menu_no = models.IntegerField()
    ceo_no = models.ForeignKey('User', models.DO_NOTHING, db_column='ceo_no')

    class Meta:
        managed = False
        db_table = 'store'


class User(models.Model):
    no = models.AutoField(primary_key=True)
    id = models.CharField(unique=True, max_length=50)
    pw = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    addr = models.CharField(max_length=50)
    phone = models.CharField(unique=True, max_length=20)
    ceo = models.IntegerField(blank=True, null=True)
    order_num = models.IntegerField(blank=True, null=True)
    order_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserContent(models.Model):
    no = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    upload_date = models.DateField(blank=True, null=True)
    update_date = models.DateField(blank=True, null=True)
    view_cnt = models.IntegerField(blank=True, null=True)
    user_no = models.ForeignKey(User, models.DO_NOTHING, db_column='user_no')

    class Meta:
        managed = False
        db_table = 'user_content'


class UserOrder(models.Model):
    no = models.AutoField(primary_key=True)
    user_no = models.ForeignKey(User, models.DO_NOTHING, db_column='user_no')
    status = models.IntegerField()
    food_name = models.CharField(max_length=20)
    store_name = models.CharField(max_length=20)
    order_date = models.DateField()
    number = models.IntegerField()
    price = models.IntegerField()
    tip = models.IntegerField(blank=True, null=True)
    payment = models.CharField(max_length=20)
    for_ceo = models.CharField(max_length=100, blank=True, null=True)
    for_rider = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_order'