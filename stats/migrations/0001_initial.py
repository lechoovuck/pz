# Generated by Django 3.1.5 on 2021-01-11 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CashStations',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField()),
                ('IsDeleted', models.BooleanField()),
                ('ModifiedDate', models.DateTimeField()),
                ('Name', models.CharField(max_length=500)),
                ('PZCrmId', models.BigIntegerField()),
                ('UpdatedAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CatalogFolders',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField()),
                ('IsDeleted', models.BooleanField()),
                ('ModifiedDate', models.DateTimeField()),
                ('Name', models.CharField(max_length=500)),
                ('PZCrmId', models.BigIntegerField()),
                ('UpdatedAt', models.DateTimeField()),
                ('IsActive', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Catalogs',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField()),
                ('IsDeleted', models.BooleanField()),
                ('ModifiedDate', models.DateTimeField()),
                ('Name', models.CharField(max_length=500)),
                ('PZCrmId', models.BigIntegerField()),
                ('UpdatedAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField()),
                ('IsDeleted', models.BooleanField()),
                ('ModifiedDate', models.DateTimeField()),
                ('Name', models.CharField(max_length=200)),
                ('PZCrmId', models.BigIntegerField()),
                ('UpdatedAt', models.DateTimeField()),
                ('CatalogId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.catalogs')),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CountryName', models.CharField(max_length=50)),
                ('CreatedAt', models.DateTimeField()),
                ('UpdatedAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CrmSystems',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField()),
                ('Guid', models.UUIDField()),
                ('IsDeleted', models.BooleanField()),
                ('ModifiedDate', models.DateTimeField()),
                ('Name', models.CharField(max_length=80)),
                ('PZCrmId', models.BigIntegerField()),
                ('UpdatedAt', models.DateTimeField()),
                ('Token', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAccountLevels',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CanDowngrade', models.BooleanField()),
                ('Condition', models.DecimalField(decimal_places=10, max_digits=12)),
                ('CreatedAt', models.DateTimeField()),
                ('CreatedBy', models.CharField(max_length=80)),
                ('CreatedDate', models.DateTimeField()),
                ('Guid', models.UUIDField()),
                ('IsDeleted', models.BooleanField()),
                ('LevelType', models.IntegerField()),
                ('MetricType', models.IntegerField()),
                ('ModifiedBy', models.CharField(max_length=80)),
                ('ModifiedDate', models.DateTimeField()),
                ('Name', models.CharField(max_length=80)),
                ('Number', models.IntegerField()),
                ('UpdatedAt', models.DateTimeField()),
                ('Value', models.DecimalField(decimal_places=10, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAccounts',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Balance', models.DecimalField(decimal_places=10, max_digits=12)),
                ('BlockReason', models.CharField(max_length=100)),
                ('CreatedAt', models.DateTimeField()),
                ('IsDeleted', models.BooleanField()),
                ('PZCrmId', models.BigIntegerField()),
                ('UpdatedAt', models.DateTimeField()),
                ('Blocked', models.BooleanField()),
                ('CreatedDate', models.DateTimeField()),
                ('Guid', models.UUIDField()),
                ('ModifiedDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerCards',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('BarCode', models.BigIntegerField()),
                ('BlockReason', models.CharField(max_length=80)),
                ('CreatedAt', models.DateTimeField()),
                ('ExpirationDate', models.DateTimeField()),
                ('IsDeleted', models.BooleanField(default=False)),
                ('Number', models.BigIntegerField()),
                ('OfferedDate', models.DateTimeField()),
                ('PZCrmId', models.BigIntegerField()),
                ('PinCode', models.IntegerField()),
                ('Status', models.IntegerField()),
                ('UpdatedAt', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField()),
                ('Guid', models.UUIDField()),
                ('ModifiedDate', models.DateTimeField()),
                ('ActivateDate', models.DateTimeField()),
                ('GiftEvent', models.CharField(max_length=80)),
                ('IsActivate', models.BooleanField()),
                ('AccountId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.customeraccounts')),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('GenreName', models.CharField(max_length=100)),
                ('UpdatedAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Halls',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField()),
                ('Description', models.CharField(max_length=50)),
                ('IsDefault', models.BooleanField(default=True)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('ModifiedDate', models.DateTimeField()),
                ('Name', models.CharField(max_length=50)),
                ('PZCrmId', models.BigIntegerField(default=0)),
                ('UpdatedAt', models.DateTimeField()),
                ('CompanyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.companies')),
            ],
        ),
        migrations.CreateModel(
            name='HrPeoples',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField()),
                ('FirstName', models.CharField(max_length=50)),
                ('IsDelete', models.BooleanField(default=False)),
                ('LastName', models.CharField(max_length=50)),
                ('MiddleName', models.CharField(max_length=50)),
                ('ModifiedDate', models.DateTimeField()),
                ('Name', models.CharField(max_length=50)),
                ('PositionId', models.BigIntegerField()),
                ('UpdatedAt', models.DateTimeField()),
                ('CompanyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.companies')),
            ],
        ),
        migrations.CreateModel(
            name='MovieFormats',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('FormatName', models.CharField(max_length=20)),
                ('CreatedAt', models.DateTimeField()),
                ('UpdatedAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieHrPeoples',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('DisplayName', models.CharField(max_length=100)),
                ('FullName', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=50)),
                ('OriginalId', models.IntegerField()),
                ('UpdatedAt', models.DateTimeField()),
                ('HallId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.halls')),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('Duration', models.FloatField()),
                ('Name', models.CharField(max_length=120)),
                ('Rate', models.CharField(max_length=3)),
                ('Story', models.TextField(max_length=500)),
                ('UpdatedAt', models.DateTimeField()),
                ('PZCrmId', models.BigIntegerField()),
                ('GenreId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.genres')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTypes',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('PaymentTypeName', models.CharField(max_length=30)),
                ('UpdatedAt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('IsChecked', models.BooleanField(default=False)),
                ('OrderId', models.UUIDField()),
                ('System', models.IntegerField()),
                ('Type', models.IntegerField()),
                ('UpdatedAt', models.DateTimeField()),
                ('Value', models.DecimalField(decimal_places=10, max_digits=12)),
                ('Checked', models.BooleanField(default=False)),
                ('Guid', models.UUIDField()),
                ('SourceId', models.BigIntegerField()),
                ('TimeStamp', models.DateTimeField()),
                ('AccountId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.customeraccounts')),
                ('CardId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.customercards')),
                ('UserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.hrpeoples')),
            ],
        ),
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('Deleted', models.BooleanField(default=False)),
                ('Locked', models.BooleanField(default=False)),
                ('SessionTime', models.DateTimeField()),
                ('TextCode', models.CharField(max_length=10)),
                ('UpdatedAt', models.DateTimeField()),
                ('PZCrmId', models.BigIntegerField()),
                ('HallId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.halls')),
                ('MovieFormatId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.movieformats')),
                ('MovieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.movies')),
            ],
        ),
        migrations.CreateModel(
            name='Rentals',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('FromDate', models.DateTimeField()),
                ('PuNumber', models.IntegerField()),
                ('SessionCount', models.IntegerField()),
                ('ToDate', models.DateTimeField()),
                ('UpdatedAt', models.DateTimeField()),
                ('MoviePZId', models.BigIntegerField()),
                ('HallId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.halls')),
                ('MovieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.movies')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('Name', models.CharField(max_length=100)),
                ('UpdatedAt', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField()),
                ('IsDeleted', models.BooleanField()),
                ('ModifiedDate', models.DateTimeField()),
                ('PZCrmId', models.BigIntegerField()),
                ('IsActive', models.BooleanField(default=True)),
                ('IsSaleDisable', models.BooleanField(default=False)),
                ('CatalogId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.catalogs')),
                ('ParentFolderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.catalogfolders')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CloseTimeStamp', models.DateTimeField()),
                ('Closed', models.BooleanField(default=True)),
                ('CreatedAt', models.DateTimeField()),
                ('Guid', models.UUIDField()),
                ('IsDeleted', models.BooleanField(default=False)),
                ('OpenTimeStamp', models.DateTimeField()),
                ('PZCrmId', models.BigIntegerField()),
                ('UpdatedAt', models.DateTimeField()),
                ('AccountId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.hrpeoples')),
                ('CashStationId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.cashstations')),
                ('CustomerCardId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.customercards')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('IsDeleted', models.BooleanField(default=False)),
                ('PZCrmId', models.BigIntegerField()),
                ('Payment', models.DecimalField(decimal_places=10, max_digits=12)),
                ('Quantity', models.DecimalField(decimal_places=10, default=1, max_digits=12)),
                ('UpdatedAt', models.DateTimeField()),
                ('OrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.orders')),
                ('ProductId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.products')),
            ],
        ),
        migrations.CreateModel(
            name='MovieOrders',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('Guid', models.CharField(max_length=100)),
                ('OrderSourceId', models.BigIntegerField()),
                ('UpdatedAt', models.DateTimeField()),
                ('CustomerCardId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.customercards')),
                ('HallId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.halls')),
                ('MovieHrPeopleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.moviehrpeoples')),
            ],
        ),
        migrations.CreateModel(
            name='MovieOrderItems',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('BonusPayment', models.FloatField()),
                ('CreatedAt', models.DateTimeField()),
                ('IsRefund', models.BooleanField(default=False)),
                ('Payment', models.FloatField()),
                ('Price', models.FloatField()),
                ('RefundTimeStamp', models.DateTimeField()),
                ('SeatId', models.BigIntegerField()),
                ('TicketId', models.BigIntegerField()),
                ('TimeStamp', models.DateTimeField()),
                ('UpdatedAt', models.DateTimeField()),
                ('PZCrmId', models.BigIntegerField()),
                ('HallId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.halls')),
                ('MovieOrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.movieorders')),
                ('SessionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.sessions')),
            ],
        ),
        migrations.CreateModel(
            name='MovieCountries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CountryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.countries')),
                ('MovieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.movies')),
            ],
        ),
        migrations.CreateModel(
            name='FiscalChecks',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('FiscalShiftId', models.IntegerField()),
                ('IsReversal', models.BooleanField(default=False)),
                ('Number', models.IntegerField()),
                ('OperationType', models.IntegerField()),
                ('ReversalAccountId', models.IntegerField()),
                ('ReversalTimeStamp', models.DateTimeField()),
                ('TimeStamp', models.DateTimeField()),
                ('UpdatedAt', models.DateTimeField()),
                ('OrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('BirthDate', models.DateTimeField()),
                ('CreatedAt', models.DateTimeField()),
                ('Email', models.CharField(max_length=60)),
                ('FirstName', models.CharField(max_length=50)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('LastName', models.CharField(max_length=50)),
                ('MiddleName', models.CharField(max_length=50)),
                ('PZCrmId', models.BigIntegerField()),
                ('Password', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=25)),
                ('UpdatedAt', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField()),
                ('Guid', models.UUIDField()),
                ('ModifiedDate', models.DateTimeField()),
                ('Sex', models.IntegerField()),
                ('CentralApiId', models.CharField(max_length=100)),
                ('LastBirthdayCongratulation', models.DateTimeField()),
                ('CrmSystemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.crmsystems')),
            ],
        ),
        migrations.AddField(
            model_name='customercards',
            name='CustomerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.customers'),
        ),
        migrations.CreateModel(
            name='CustomerAccountTypes',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateTimeField()),
                ('InitialBalance', models.DecimalField(decimal_places=10, max_digits=12)),
                ('IsDeleted', models.BooleanField()),
                ('Name', models.CharField(max_length=80)),
                ('PZCrmId', models.BigIntegerField()),
                ('UpdatedAt', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField()),
                ('Guid', models.UUIDField()),
                ('ModifiedDate', models.DateTimeField()),
                ('SystemType', models.IntegerField()),
                ('CreatedBy', models.CharField(max_length=80)),
                ('ModifiedBy', models.CharField(max_length=80)),
                ('CrmSystemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.crmsystems')),
            ],
        ),
        migrations.AddField(
            model_name='customeraccounts',
            name='CustomerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.customers'),
        ),
        migrations.AddField(
            model_name='customeraccounts',
            name='LevelId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.customeraccountlevels'),
        ),
        migrations.AddField(
            model_name='customeraccounts',
            name='TypeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.customeraccounttypes'),
        ),
        migrations.AddField(
            model_name='customeraccountlevels',
            name='AccountTypeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.customeraccounttypes'),
        ),
        migrations.AddField(
            model_name='companies',
            name='CrmSystemId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.crmsystems'),
        ),
        migrations.CreateModel(
            name='Cinemas',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=100)),
                ('Alias', models.CharField(max_length=100)),
                ('ApiIp', models.CharField(max_length=100)),
                ('ApiPort', models.CharField(max_length=100)),
                ('CityName', models.CharField(max_length=100)),
                ('CreatedAt', models.DateTimeField()),
                ('IsActive', models.BooleanField()),
                ('Name', models.CharField(max_length=100)),
                ('Site', models.CharField(max_length=200)),
                ('TimeZone', models.IntegerField()),
                ('UpdatedAt', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField()),
                ('IsDeleted', models.BooleanField()),
                ('HallId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.halls')),
            ],
        ),
        migrations.AddField(
            model_name='catalogfolders',
            name='CatalogId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.catalogs'),
        ),
        migrations.AddField(
            model_name='catalogfolders',
            name='ParentFoldersId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.catalogfolders'),
        ),
        migrations.AddField(
            model_name='cashstations',
            name='CompanyId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.companies'),
        ),
        migrations.AddField(
            model_name='cashstations',
            name='HallId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.halls'),
        ),
        migrations.CreateModel(
            name='BarPayments',
            fields=[
                ('Id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Amount', models.FloatField()),
                ('Change', models.FloatField()),
                ('CreatedAt', models.DateTimeField()),
                ('Deleted', models.BooleanField()),
                ('UpdatedAt', models.DateTimeField()),
                ('OrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.orders')),
                ('PaymentTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stats.paymenttypes')),
            ],
        ),
    ]
