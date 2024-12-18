# Generated by Django 5.1.3 on 2024-11-11 06:42

from django.db import migrations

def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    admin_group, _ = Group.objects.get_or_create(name='Admin')
    manager_group, _ = Group.objects.get_or_create(name='Manager')
    customer_group, _ = Group.objects.get_or_create(name='Customer')

    admin_permissions = Permission.objects.all()
    admin_group.permissions.set(admin_permissions)

    manager_permissions = Permission.objects.filter(
        codename__in=[]
    )
    manager_group.permissions.set(manager_permissions)

    customer_permissions = Permission.objects.filter(
        codename__in=[] 
    )
    customer_group.permissions.set(customer_permissions)

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]
