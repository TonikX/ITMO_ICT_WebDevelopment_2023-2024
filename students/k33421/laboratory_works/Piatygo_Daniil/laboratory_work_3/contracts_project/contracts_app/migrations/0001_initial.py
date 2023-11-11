# Generated by Django 4.2.5 on 2023-11-05 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Agent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=100)),
                ("passport_details", models.CharField(max_length=50)),
                ("contact_details", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Contract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "contract_type",
                    models.CharField(
                        choices=[
                            ("individual", "Индивидуальный"),
                            ("collective", "Коллективный"),
                        ],
                        max_length=20,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "insurance_cost",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contracts",
                        to="contracts_app.agent",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=50, unique=True)),
                ("full_name", models.TextField()),
                ("short_name", models.CharField(max_length=200)),
                ("address", models.TextField()),
                ("bank_account_number", models.CharField(max_length=50)),
                ("specialization", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="InsuranceCase",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("cause", models.TextField()),
                ("decision", models.BooleanField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "contract",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cases",
                        to="contracts_app.contract",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmploymentContract",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "agent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employment_contracts",
                        to="contracts_app.agent",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=100)),
                ("age", models.PositiveIntegerField()),
                (
                    "risk_category",
                    models.CharField(
                        choices=[
                            ("first", "Первая"),
                            ("second", "Вторая"),
                            ("highest", "Высшая"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employees",
                        to="contracts_app.organization",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contract",
            name="employees",
            field=models.ManyToManyField(
                blank=True, related_name="contracts", to="contracts_app.employee"
            ),
        ),
        migrations.AddField(
            model_name="contract",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contracts",
                to="contracts_app.organization",
            ),
        ),
    ]
