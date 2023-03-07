from django.db import models

# 管理员类
class admin(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    name = models.CharField(max_length=45) # 姓名
    password = models.CharField(max_length=45) # 密码

    class Meta:
        managed = False
        db_table = 'admin'

# 医生类
class user_doctor(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    name = models.CharField(max_length=45) # 姓名
    id_card = models.CharField(max_length=45) # 身份证
    department_id = models.SmallIntegerField() # 科室
    password = models.CharField(max_length=45) # 密码
    status = models.SmallIntegerField(default=1) # 状态

    class Meta:
        managed = False
        db_table = 'user_doctor'

# Nurse
class user_nurse(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    name = models.CharField(max_length=45) # 姓名
    id_card = models.CharField(max_length=45) # 身份证
    department_id = models.SmallIntegerField() # 科室
    password = models.CharField(max_length=45) # 密码
    status = models.SmallIntegerField(default=1) # 状态

    class Meta:
        managed = False
        db_table = 'user_nurse'

# 科室类
class department(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    name = models.CharField(max_length=45) # 名称
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2) # 挂号费
    doctor_num = models.SmallIntegerField(default=0) # 医生数

    class Meta:
        managed = False
        db_table = 'department'

# 药品类
class medicine(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    name = models.CharField(max_length=45) # 名称
    price = models.DecimalField(max_digits=10, decimal_places=2) # 单价
    unit = models.CharField(max_length=45) # 单位

    class Meta:
        managed = False
        db_table = 'medicine'


# New medication delivery job
class user_patient(models.Model):
    id = models.AutoField(primary_key=True) 
    job_id = models.CharField(auto_created=True, max_length=30)
    order_id = models.CharField(max_length=30)
    box_number = models.SmallIntegerField()
    ward_number = models.SmallIntegerField()
    status = models.CharField(max_length=30)
    recorded_date = models.DateField(auto_now_add=True)
    recorded_time = models.TimeField(auto_now_add=True)
    slot_number = models.SmallIntegerField(auto_created=True)

    class Meta:
        managed = False
        db_table = 'user_patient'


# EMR
class patients_data(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=30)
    ward_number = models.SmallIntegerField()


    class Meta:
        managed = False
        db_table = 'patients_data'


### To record date selected
class test_date(models.Model):
    id = models.AutoField(primary_key=True)
    select_date = models.DateField(max_length=12)

    class Meta:
        managed = False
        db_table = 'test_date'

### To test nurse QR
class nurse_QR(models.Model):
    id = models.AutoField(primary_key=True)
    output = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'nurse_QR'