# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Barpayments(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    change = models.FloatField(db_column='Change')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    deleted = models.BooleanField(db_column='Deleted')  # Field name made lowercase.
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='OrderId')  # Field name made lowercase.
    paymenttypeid = models.ForeignKey('Paymenttypes', models.DO_NOTHING,
                                      db_column='PaymentTypeId')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BarPayments'


class Cashstations(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey('Companies', models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    hallid = models.ForeignKey('Halls', models.DO_NOTHING, db_column='HallId', blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CashStations'


class Catalogfolders(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    catalogid = models.ForeignKey('Catalogs', models.DO_NOTHING, db_column='CatalogId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    parentfoldersid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentFoldersId', blank=True,
                                        null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CatalogFolders'


class Catalogs(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Catalogs'


class Cinemas(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    alias = models.TextField(db_column='Alias')  # Field name made lowercase.
    apiip = models.TextField(db_column='ApiIp', blank=True, null=True)  # Field name made lowercase.
    apiport = models.IntegerField(db_column='ApiPort', blank=True, null=True)  # Field name made lowercase.
    cityname = models.TextField(db_column='CityName', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    hallid = models.ForeignKey('Halls', models.DO_NOTHING, db_column='HallId', blank=True,
                               null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    site = models.TextField(db_column='Site', blank=True, null=True)  # Field name made lowercase.
    timezone = models.IntegerField(db_column='TimeZone', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='UpdatedDate')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    serviceid = models.TextField(db_column='ServiceId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cinemas'


class Companies(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    crmsystemid = models.ForeignKey('Crmsystems', models.DO_NOTHING, db_column='CrmSystemId', blank=True,
                                    null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    timezone = models.TextField(db_column='TimeZone', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    catalogid = models.ForeignKey(Catalogs, models.DO_NOTHING, db_column='CatalogId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Companies'


class Countries(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    counryname = models.TextField(db_column='CounryName', unique=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Countries'


class Crmsystems(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    guid = models.UUIDField(db_column='Guid')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    token = models.TextField(db_column='Token', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CrmSystems'


class Customeraccountlevels(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accounttypeid = models.ForeignKey('Customeraccounttypes', models.DO_NOTHING,
                                      db_column='AccountTypeId')  # Field name made lowercase.
    candowngrade = models.BooleanField(db_column='CanDowngrade')  # Field name made lowercase.
    condition = models.DecimalField(db_column='Condition', max_digits=65535,
                                    decimal_places=65535)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    guid = models.UUIDField(db_column='Guid')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    leveltype = models.IntegerField(db_column='LevelType')  # Field name made lowercase.
    metrictype = models.IntegerField(db_column='MetricType', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=65535, decimal_places=65535)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerAccountLevels'


class Customeraccounttypes(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    crmsystemid = models.ForeignKey(Crmsystems, models.DO_NOTHING,
                                    db_column='CrmSystemId')  # Field name made lowercase.
    initialbalance = models.DecimalField(db_column='InitialBalance', max_digits=65535,
                                         decimal_places=65535)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    guid = models.UUIDField(db_column='Guid')  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    systemtype = models.IntegerField(db_column='SystemType')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    modifiedby = models.TextField(db_column='ModifiedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerAccountTypes'


class Customeraccounts(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=65535,
                                  decimal_places=65535)  # Field name made lowercase.
    blockreason = models.TextField(db_column='BlockReason', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    typeid = models.ForeignKey(Customeraccounttypes, models.DO_NOTHING,
                               db_column='TypeId')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    blocked = models.BooleanField(db_column='Blocked')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    guid = models.UUIDField(db_column='Guid')  # Field name made lowercase.
    levelid = models.ForeignKey(Customeraccountlevels, models.DO_NOTHING, db_column='LevelId', blank=True,
                                null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerAccounts'


class Customercards(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accountid = models.ForeignKey(Customeraccounts, models.DO_NOTHING, db_column='AccountId', blank=True,
                                  null=True)  # Field name made lowercase.
    barcode = models.BigIntegerField(db_column='BarCode', blank=True, null=True)  # Field name made lowercase.
    blockreason = models.TextField(db_column='BlockReason', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    customerid = models.ForeignKey('Customers', models.DO_NOTHING, db_column='CustomerId')  # Field name made lowercase.
    expirationdate = models.DateTimeField(db_column='ExpirationDate', blank=True,
                                          null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    number = models.BigIntegerField(db_column='Number')  # Field name made lowercase.
    offereddate = models.DateTimeField(db_column='OfferedDate', blank=True, null=True)  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    pincode = models.IntegerField(db_column='PinCode', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    guid = models.UUIDField(db_column='Guid')  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    activatedate = models.DateTimeField(db_column='ActivateDate', blank=True, null=True)  # Field name made lowercase.
    giftevent = models.TextField(db_column='GiftEvent', blank=True, null=True)  # Field name made lowercase.
    isactivate = models.BooleanField(db_column='IsActivate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerCards'


class Customers(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    crmsystemid = models.ForeignKey(Crmsystems, models.DO_NOTHING,
                                    db_column='CrmSystemId')  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    middlename = models.TextField(db_column='MiddleName', blank=True, null=True)  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    guid = models.UUIDField(db_column='Guid')  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(db_column='Sex')  # Field name made lowercase.
    centralapiid = models.TextField(db_column='CentralApiId', blank=True, null=True)  # Field name made lowercase.
    lastbirthdaycongratulation = models.DateTimeField(db_column='LastBirthdayCongratulation', blank=True,
                                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customers'


class Fiscalchecks(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    fiscalshiftid = models.IntegerField(db_column='FiscalShiftId')  # Field name made lowercase.
    isreversal = models.BooleanField(db_column='IsReversal')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.
    operationtype = models.IntegerField(db_column='OperationType')  # Field name made lowercase.
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='OrderId', blank=True,
                                null=True)  # Field name made lowercase.
    reversalaccountid = models.IntegerField(db_column='ReversalAccountId', blank=True,
                                            null=True)  # Field name made lowercase.
    reversaltimestamp = models.DateTimeField(db_column='ReversalTimeStamp', blank=True,
                                             null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FiscalChecks'


class Genres(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    genrename = models.TextField(db_column='GenreName', unique=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Genres'


class Halls(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Halls'


class Hrpeoples(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    companyid = models.ForeignKey(Companies, models.DO_NOTHING, db_column='CompanyId')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', blank=True, null=True)  # Field name made lowercase.
    isdelete = models.BooleanField(db_column='IsDelete')  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    middlename = models.TextField(db_column='MiddleName', blank=True, null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    positionid = models.BigIntegerField(db_column='PositionId')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HrPeoples'


class Moviecountries(models.Model):
    movieid = models.OneToOneField('Movies', models.DO_NOTHING, db_column='MovieId',
                                   primary_key=True)  # Field name made lowercase.
    countryid = models.ForeignKey(Countries, models.DO_NOTHING, db_column='CountryId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MovieCountries'
        unique_together = (('movieid', 'countryid'),)


class Movieformats(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    formatname = models.TextField(db_column='FormatName')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MovieFormats'


class Moviehrpeoples(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    displayname = models.TextField(db_column='DisplayName', blank=True, null=True)  # Field name made lowercase.
    fullname = models.TextField(db_column='FullName', blank=True, null=True)  # Field name made lowercase.
    hallid = models.ForeignKey(Halls, models.DO_NOTHING, db_column='HallId')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    originalid = models.IntegerField(db_column='OriginalId')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MovieHrPeoples'
        unique_together = (('originalid', 'hallid'),)


class Movieorderitems(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    bonuspayment = models.FloatField(db_column='BonusPayment')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    isrefund = models.BooleanField(db_column='IsRefund')  # Field name made lowercase.
    movieorderid = models.ForeignKey('Movieorders', models.DO_NOTHING, db_column='MovieOrderId', blank=True,
                                     null=True)  # Field name made lowercase.
    payment = models.FloatField(db_column='Payment')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    refundtimestamp = models.DateTimeField(db_column='RefundTimeStamp', blank=True,
                                           null=True)  # Field name made lowercase.
    seatid = models.BigIntegerField(db_column='SeatId')  # Field name made lowercase.
    sessionid = models.ForeignKey('Sessions', models.DO_NOTHING, db_column='SessionId', blank=True,
                                  null=True)  # Field name made lowercase.
    ticketid = models.BigIntegerField(db_column='TicketId')  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    hallid = models.ForeignKey(Halls, models.DO_NOTHING, db_column='HallId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MovieOrderItems'
        unique_together = (('pzcrmid', 'hallid'),)


class Movieorders(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    customercardid = models.ForeignKey(Customercards, models.DO_NOTHING, db_column='CustomerCardId', blank=True,
                                       null=True)  # Field name made lowercase.
    guid = models.TextField(db_column='Guid')  # Field name made lowercase.
    ordersourceid = models.BigIntegerField(db_column='OrderSourceId')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    hallid = models.ForeignKey(Halls, models.DO_NOTHING, db_column='HallId')  # Field name made lowercase.
    moviehrpeopleid = models.ForeignKey(Moviehrpeoples, models.DO_NOTHING, db_column='MovieHrPeopleId', blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MovieOrders'
        unique_together = (('guid', 'hallid'),)


class Movies(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    duration = models.FloatField(db_column='Duration')  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    rate = models.TextField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.
    story = models.TextField(db_column='Story', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    genreid = models.ForeignKey(Genres, models.DO_NOTHING, db_column='GenreId', blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Movies'


class Orderitems(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='OrderId')  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    payment = models.DecimalField(db_column='Payment', max_digits=65535,
                                  decimal_places=65535)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='ProductId')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=65535,
                                   decimal_places=65535)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderItems'


class Orders(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cashstationid = models.ForeignKey(Cashstations, models.DO_NOTHING,
                                      db_column='CashStationId')  # Field name made lowercase.
    closetimestamp = models.DateTimeField(db_column='CloseTimeStamp', blank=True,
                                          null=True)  # Field name made lowercase.
    closed = models.BooleanField(db_column='Closed')  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    customercardid = models.ForeignKey(Customercards, models.DO_NOTHING, db_column='CustomerCardId', blank=True,
                                       null=True)  # Field name made lowercase.
    guid = models.UUIDField(db_column='Guid')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    opentimestamp = models.DateTimeField(db_column='OpenTimeStamp')  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    accountid = models.ForeignKey(Hrpeoples, models.DO_NOTHING, db_column='AccountId', blank=True,
                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Orders'


class Paymenttypes(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    paymenttypename = models.TextField(db_column='PaymentTypeName', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PaymentTypes'


class Products(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    parentfolderid = models.ForeignKey(Catalogfolders, models.DO_NOTHING, db_column='ParentFolderId', blank=True,
                                       null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    isdeleted = models.BooleanField(db_column='IsDeleted')  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate', blank=True, null=True)  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    catalogid = models.ForeignKey(Catalogs, models.DO_NOTHING, db_column='CatalogId')  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive')  # Field name made lowercase.
    issaledisable = models.BooleanField(db_column='IsSaleDisable')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Products'


class Rentals(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    hallid = models.ForeignKey(Halls, models.DO_NOTHING, db_column='HallId')  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate')  # Field name made lowercase.
    movieid = models.ForeignKey(Movies, models.DO_NOTHING, db_column='MovieId')  # Field name made lowercase.
    punumber = models.IntegerField(db_column='PuNumber', blank=True, null=True)  # Field name made lowercase.
    sessioncount = models.IntegerField(db_column='SessionCount')  # Field name made lowercase.
    todate = models.DateTimeField(db_column='ToDate')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    moviepzid = models.BigIntegerField(db_column='MoviePZId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rentals'


class Sessions(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    deleted = models.BooleanField(db_column='Deleted')  # Field name made lowercase.
    locked = models.BooleanField(db_column='Locked')  # Field name made lowercase.
    movieid = models.ForeignKey(Movies, models.DO_NOTHING, db_column='MovieId')  # Field name made lowercase.
    sessiontime = models.DateTimeField(db_column='SessionTime')  # Field name made lowercase.
    textcode = models.TextField(db_column='TextCode', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    hallid = models.ForeignKey(Halls, models.DO_NOTHING, db_column='HallId')  # Field name made lowercase.
    pzcrmid = models.BigIntegerField(db_column='PZCrmId')  # Field name made lowercase.
    movieformatid = models.ForeignKey(Movieformats, models.DO_NOTHING, db_column='MovieFormatId', blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sessions'
        unique_together = (('pzcrmid', 'hallid'),)


class Transactions(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    accountid = models.ForeignKey(Customeraccounts, models.DO_NOTHING, db_column='AccountId', blank=True,
                                  null=True)  # Field name made lowercase.
    cardid = models.ForeignKey(Customercards, models.DO_NOTHING, db_column='CardId', blank=True,
                               null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt')  # Field name made lowercase.
    ischecked = models.BooleanField(db_column='IsChecked')  # Field name made lowercase.
    orderid = models.UUIDField(db_column='OrderId', blank=True, null=True)  # Field name made lowercase.
    system = models.IntegerField(db_column='System')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='UpdatedAt')  # Field name made lowercase.
    value = models.DecimalField(db_column='Value', max_digits=65535, decimal_places=65535)  # Field name made lowercase.
    checked = models.BooleanField(db_column='Checked')  # Field name made lowercase.
    guid = models.UUIDField(db_column='Guid')  # Field name made lowercase.
    sourceid = models.BigIntegerField(db_column='SourceId', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp')  # Field name made lowercase.
    userid = models.ForeignKey(Hrpeoples, models.DO_NOTHING, db_column='UserId', blank=True,
                               null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Transactions'


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True,
                                   max_length=150)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'


class BackendMovie(models.Model):
    name = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    description = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'backend_movie'
