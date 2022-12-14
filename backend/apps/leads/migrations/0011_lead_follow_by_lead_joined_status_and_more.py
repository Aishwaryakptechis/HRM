# Generated by Django 4.0.3 on 2022-10-15 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_employee_id'),
        ('leads', '0010_alter_lead_hr_date_of_calling_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='follow_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follow_by', to='users.user'),
        ),
        migrations.AddField(
            model_name='lead',
            name='joined_status',
            field=models.CharField(choices=[('blank', ' '), ('joined', 'Joined'), ('doj_extended', 'DOJ - Extended'), ('no_response', 'No Response'), ('yet_to_join', 'Yet to join'), ('declined', 'Declined'), ('joined_&_left', 'Joined & Left'), ('rejected_by_management', 'Rejected by Management')], max_length=50, null=True, verbose_name='Joined Status'),
        ),
        migrations.AddField(
            model_name='lead',
            name='offered_date_of_joining',
            field=models.DateField(null=True, verbose_name='Date of Joining'),
        ),
        migrations.AddField(
            model_name='lead',
            name='offered_review',
            field=models.CharField(blank=True, db_index=True, max_length=250, null=True, verbose_name='Review'),
        ),
        migrations.AddField(
            model_name='lead',
            name='offered_status',
            field=models.CharField(choices=[('blank', ' '), ('offer_letter_sent', 'Offer Letter Sent'), ('waiting_list', 'Waiting List'), ('check_on_later', 'Check on Later')], max_length=50, null=True, verbose_name='Offered Status'),
        ),
        migrations.AddField(
            model_name='lead',
            name='revised_date_of_joining',
            field=models.DateField(null=True, verbose_name='Revised Date of Joining'),
        ),
    ]
