# Generated by Django 2.1.7 on 2019-05-23 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("common", "0013_auto_20190508_1540"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "invoice_title",
                    models.CharField(max_length=50, verbose_name="Invoice Title"),
                ),
                (
                    "invoice_number",
                    models.CharField(max_length=50, verbose_name="Invoice Number"),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("quantity", models.PositiveIntegerField(default=0)),
                (
                    "rate",
                    models.DecimalField(decimal_places=2, default=0, max_digits=12),
                ),
                (
                    "total_amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=12, null=True
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AED", "AED, Dirham"),
                            ("AFN", "AFN, Afghani"),
                            ("ALL", "ALL, Lek"),
                            ("AMD", "AMD, Dram"),
                            ("ANG", "ANG, Guilder"),
                            ("AOA", "AOA, Kwanza"),
                            ("ARS", "ARS, Peso"),
                            ("AUD", "AUD, Dollar"),
                            ("AWG", "AWG, Guilder"),
                            ("AZN", "AZN, Manat"),
                            ("BAM", "BAM, Marka"),
                            ("BBD", "BBD, Dollar"),
                            ("BDT", "BDT, Taka"),
                            ("BGN", "BGN, Lev"),
                            ("BHD", "BHD, Dinar"),
                            ("BIF", "BIF, Franc"),
                            ("BMD", "BMD, Dollar"),
                            ("BND", "BND, Dollar"),
                            ("BOB", "BOB, Boliviano"),
                            ("BRL", "BRL, Real"),
                            ("BSD", "BSD, Dollar"),
                            ("BTN", "BTN, Ngultrum"),
                            ("BWP", "BWP, Pula"),
                            ("BYR", "BYR, Ruble"),
                            ("BZD", "BZD, Dollar"),
                            ("CAD", "CAD, Dollar"),
                            ("CDF", "CDF, Franc"),
                            ("CHF", "CHF, Franc"),
                            ("CLP", "CLP, Peso"),
                            ("CNY", "CNY, Yuan Renminbi"),
                            ("COP", "COP, Peso"),
                            ("CRC", "CRC, Colon"),
                            ("CUP", "CUP, Peso"),
                            ("CVE", "CVE, Escudo"),
                            ("CZK", "CZK, Koruna"),
                            ("DJF", "DJF, Franc"),
                            ("DKK", "DKK, Krone"),
                            ("DOP", "DOP, Peso"),
                            ("DZD", "DZD, Dinar"),
                            ("EGP", "EGP, Pound"),
                            ("ERN", "ERN, Nakfa"),
                            ("ETB", "ETB, Birr"),
                            ("EUR", "EUR, Euro"),
                            ("FJD", "FJD, Dollar"),
                            ("FKP", "FKP, Pound"),
                            ("GBP", "GBP, Pound"),
                            ("GEL", "GEL, Lari"),
                            ("GHS", "GHS, Cedi"),
                            ("GIP", "GIP, Pound"),
                            ("GMD", "GMD, Dalasi"),
                            ("GNF", "GNF, Franc"),
                            ("GTQ", "GTQ, Quetzal"),
                            ("GYD", "GYD, Dollar"),
                            ("HKD", "HKD, Dollar"),
                            ("HNL", "HNL, Lempira"),
                            ("HRK", "HRK, Kuna"),
                            ("HTG", "HTG, Gourde"),
                            ("HUF", "HUF, Forint"),
                            ("IDR", "IDR, Rupiah"),
                            ("ILS", "ILS, Shekel"),
                            ("INR", "INR, Rupee"),
                            ("IQD", "IQD, Dinar"),
                            ("IRR", "IRR, Rial"),
                            ("ISK", "ISK, Krona"),
                            ("JMD", "JMD, Dollar"),
                            ("JOD", "JOD, Dinar"),
                            ("JPY", "JPY, Yen"),
                            ("KES", "KES, Shilling"),
                            ("KGS", "KGS, Som"),
                            ("KHR", "KHR, Riels"),
                            ("KMF", "KMF, Franc"),
                            ("KPW", "KPW, Won"),
                            ("KRW", "KRW, Won"),
                            ("KWD", "KWD, Dinar"),
                            ("KYD", "KYD, Dollar"),
                            ("KZT", "KZT, Tenge"),
                            ("LAK", "LAK, Kip"),
                            ("LBP", "LBP, Pound"),
                            ("LKR", "LKR, Rupee"),
                            ("LRD", "LRD, Dollar"),
                            ("LSL", "LSL, Loti"),
                            ("LTL", "LTL, Litas"),
                            ("LVL", "LVL, Lat"),
                            ("LYD", "LYD, Dinar"),
                            ("MAD", "MAD, Dirham"),
                            ("MDL", "MDL, Leu"),
                            ("MGA", "MGA, Ariary"),
                            ("MKD", "MKD, Denar"),
                            ("MMK", "MMK, Kyat"),
                            ("MNT", "MNT, Tugrik"),
                            ("MOP", "MOP, Pataca"),
                            ("MRO", "MRO, Ouguiya"),
                            ("MUR", "MUR, Rupee"),
                            ("MVR", "MVR, Rufiyaa"),
                            ("MWK", "MWK, Kwacha"),
                            ("MXN", "MXN, Peso"),
                            ("MYR", "MYR, Ringgit"),
                            ("MZN", "MZN, Metical"),
                            ("NAD", "NAD, Dollar"),
                            ("NGN", "NGN, Naira"),
                            ("NIO", "NIO, Cordoba"),
                            ("NOK", "NOK, Krone"),
                            ("NPR", "NPR, Rupee"),
                            ("NZD", "NZD, Dollar"),
                            ("OMR", "OMR, Rial"),
                            ("PAB", "PAB, Balboa"),
                            ("PEN", "PEN, Sol"),
                            ("PGK", "PGK, Kina"),
                            ("PHP", "PHP, Peso"),
                            ("PKR", "PKR, Rupee"),
                            ("PLN", "PLN, Zloty"),
                            ("PYG", "PYG, Guarani"),
                            ("QAR", "QAR, Rial"),
                            ("RON", "RON, Leu"),
                            ("RSD", "RSD, Dinar"),
                            ("RUB", "RUB, Ruble"),
                            ("RWF", "RWF, Franc"),
                            ("SAR", "SAR, Rial"),
                            ("SBD", "SBD, Dollar"),
                            ("SCR", "SCR, Rupee"),
                            ("SDG", "SDG, Pound"),
                            ("SEK", "SEK, Krona"),
                            ("SGD", "SGD, Dollar"),
                            ("SHP", "SHP, Pound"),
                            ("SLL", "SLL, Leone"),
                            ("SOS", "SOS, Shilling"),
                            ("SRD", "SRD, Dollar"),
                            ("SSP", "SSP, Pound"),
                            ("STD", "STD, Dobra"),
                            ("SYP", "SYP, Pound"),
                            ("SZL", "SZL, Lilangeni"),
                            ("THB", "THB, Baht"),
                            ("TJS", "TJS, Somoni"),
                            ("TMT", "TMT, Manat"),
                            ("TND", "TND, Dinar"),
                            ("TOP", "TOP, Paanga"),
                            ("TRY", "TRY, Lira"),
                            ("TTD", "TTD, Dollar"),
                            ("TWD", "TWD, Dollar"),
                            ("TZS", "TZS, Shilling"),
                            ("UAH", "UAH, Hryvnia"),
                            ("UGX", "UGX, Shilling"),
                            ("USD", "$, Dollar"),
                            ("UYU", "UYU, Peso"),
                            ("UZS", "UZS, Som"),
                            ("VEF", "VEF, Bolivar"),
                            ("VND", "VND, Dong"),
                            ("VUV", "VUV, Vatu"),
                            ("WST", "WST, Tala"),
                            ("XAF", "XAF, Franc"),
                            ("XCD", "XCD, Dollar"),
                            ("XOF", "XOF, Franc"),
                            ("XPF", "XPF, Franc"),
                            ("YER", "YER, Rial"),
                            ("ZAR", "ZAR, Rand"),
                            ("ZMK", "ZMK, Kwacha"),
                            ("ZWL", "ZWL, Dollar"),
                        ],
                        max_length=3,
                        null=True,
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "amount_due",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=12, null=True
                    ),
                ),
                (
                    "amount_paid",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=12, null=True
                    ),
                ),
                ("is_email_sent", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Draft", "Draft"),
                            ("Sent", "Sent"),
                            ("Paid", "Paid"),
                            ("Cancel", "Cancel"),
                            ("Pending", "Pending"),
                        ],
                        default="Draft",
                        max_length=15,
                    ),
                ),
                (
                    "assigned_to",
                    models.ManyToManyField(
                        related_name="invoice_assigned_to", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="invoice_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "from_address",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="invoice_from_address",
                        to="common.Address",
                    ),
                ),
                (
                    "to_address",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="invoice_to_address",
                        to="common.Address",
                    ),
                ),
            ],
            options={"verbose_name": "Invoice", "verbose_name_plural": "Invoices",},
        ),
    ]
