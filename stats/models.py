from django.db import models


class Catalogs(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    IsDeleted = models.BooleanField()
    ModifiedDate = models.DateTimeField()
    Name = models.CharField(max_length=500)
    PZCrmId = models.BigIntegerField(primary_key=False)
    UpdatedAt = models.DateTimeField()


class CatalogFolders(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CatalogId = models.ForeignKey(Catalogs, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    IsDeleted = models.BooleanField()
    ModifiedDate = models.DateTimeField()
    Name = models.CharField(max_length=500)
    PZCrmId = models.BigIntegerField(primary_key=False)
    ParentFoldersId = models.ForeignKey('self', on_delete=models.CASCADE)
    UpdatedAt = models.DateTimeField()
    IsActive = models.BooleanField()


class Countries(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CountryName = models.CharField(max_length=50)
    CreatedAt = models.DateTimeField()
    UpdatedAt = models.DateTimeField()


class CrmSystems(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    Guid = models.UUIDField()
    IsDeleted = models.BooleanField()
    ModifiedDate = models.DateTimeField()
    Name = models.CharField(max_length=80)
    PZCrmId = models.BigIntegerField(primary_key=False)
    UpdatedAt = models.DateTimeField()
    Token = models.CharField(max_length=80)


class Companies(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    CrmSystemId = models.ForeignKey(CrmSystems, on_delete=models.CASCADE)
    IsDeleted = models.BooleanField()
    ModifiedDate = models.DateTimeField()
    Name = models.CharField(max_length=200)
    PZCrmId = models.BigIntegerField(primary_key=False)
    UpdatedAt = models.DateTimeField()
    CatalogId = models.ForeignKey(Catalogs, on_delete=models.CASCADE)


class CustomerAccountTypes(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    CrmSystemId = models.ForeignKey(CrmSystems, on_delete=models.CASCADE)
    InitialBalance = models.DecimalField(decimal_places=10, max_digits=12)
    IsDeleted = models.BooleanField()
    Name = models.CharField(max_length=80)
    PZCrmId = models.BigIntegerField(primary_key=False)
    UpdatedAt = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    Guid = models.UUIDField()
    ModifiedDate = models.DateTimeField()
    SystemType = models.IntegerField()
    CreatedBy = models.CharField(max_length=80)
    ModifiedBy = models.CharField(max_length=80)


class CustomerAccountLevels(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    AccountTypeId = models.ForeignKey(CustomerAccountTypes, on_delete=models.CASCADE)
    CanDowngrade = models.BooleanField()
    Condition = models.DecimalField(decimal_places=10, max_digits=12)
    CreatedAt = models.DateTimeField()
    CreatedBy = models.CharField(max_length=80)
    CreatedDate = models.DateTimeField()
    Guid = models.UUIDField()
    IsDeleted = models.BooleanField()
    LevelType = models.IntegerField()
    MetricType = models.IntegerField()
    ModifiedBy = models.CharField(max_length=80)
    ModifiedDate = models.DateTimeField()
    Name = models.CharField(max_length=80)
    Number = models.IntegerField()
    UpdatedAt = models.DateTimeField()
    Value = models.DecimalField(decimal_places=10, max_digits=12)


class Customers(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    BirthDate = models.DateTimeField()
    CreatedAt = models.DateTimeField()
    CrmSystemId = models.ForeignKey(CrmSystems, on_delete=models.CASCADE)
    Email = models.CharField(max_length=60)
    FirstName = models.CharField(max_length=50)
    IsDeleted = models.BooleanField(default=False)
    LastName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    PZCrmId = models.BigIntegerField(primary_key=False)
    Password = models.CharField(max_length=30)
    Phone = models.CharField(max_length=25)
    UpdatedAt = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    Guid = models.UUIDField()
    ModifiedDate = models.DateTimeField()
    Sex = models.IntegerField()
    CentralApiId = models.CharField(max_length=100)
    LastBirthdayCongratulation = models.DateTimeField()


class CustomerAccounts(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    Balance = models.DecimalField(decimal_places=10, max_digits=12)
    BlockReason = models.CharField(max_length=100)
    CreatedAt = models.DateTimeField()
    CustomerId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    IsDeleted = models.BooleanField()
    PZCrmId = models.BigIntegerField()
    TypeId = models.ForeignKey(CustomerAccountTypes, on_delete=models.CASCADE)
    UpdatedAt = models.DateTimeField()
    Blocked = models.BooleanField()
    CreatedDate = models.DateTimeField()
    Guid = models.UUIDField()
    LevelId = models.ForeignKey(CustomerAccountLevels, on_delete=models.CASCADE)
    ModifiedDate = models.DateTimeField()


# Карты
class CustomerCards(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    AccountId = models.ForeignKey(CustomerAccounts, on_delete=models.CASCADE)
    BarCode = models.BigIntegerField()
    BlockReason = models.CharField(max_length=80)
    CreatedAt = models.DateTimeField()
    CustomerId = models.ForeignKey(Customers, on_delete=models.CASCADE)
    ExpirationDate = models.DateTimeField()
    IsDeleted = models.BooleanField(default=False)
    Number = models.BigIntegerField(primary_key=False)
    OfferedDate = models.DateTimeField()
    PZCrmId = models.BigIntegerField(primary_key=False)
    PinCode = models.IntegerField()
    Status = models.IntegerField()
    UpdatedAt = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    Guid = models.UUIDField()
    ModifiedDate = models.DateTimeField()
    ActivateDate = models.DateTimeField()
    GiftEvent = models.CharField(max_length=80)
    IsActivate = models.BooleanField()


class Genres(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    GenreName = models.CharField(max_length=100)
    UpdatedAt = models.DateTimeField()


class Halls(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CompanyId = models.ForeignKey(Companies, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    Description = models.CharField(max_length=50)
    IsDefault = models.BooleanField(default=True)
    IsDeleted = models.BooleanField(default=False)
    ModifiedDate = models.DateTimeField()
    Name = models.CharField(max_length=50)
    PZCrmId = models.BigIntegerField(default=0, primary_key=False)
    UpdatedAt = models.DateTimeField()


class Cinemas(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    Address = models.CharField(max_length=100)
    Alias = models.CharField(max_length=100)
    ApiIp = models.CharField(max_length=100)
    ApiPort = models.CharField(max_length=100)
    CityName = models.CharField(max_length=100)
    CreatedAt = models.DateTimeField()
    HallId = models.ForeignKey(Halls, on_delete=models.CASCADE)
    IsActive = models.BooleanField()
    Name = models.CharField(max_length=100)
    Site = models.CharField(max_length=200)
    TimeZone = models.IntegerField()
    UpdatedAt = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    IsDeleted = models.BooleanField()


class CashStations(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CompanyId = models.ForeignKey(Companies, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    IsDeleted = models.BooleanField()
    ModifiedDate = models.DateTimeField()
    Name = models.CharField(max_length=500)
    PZCrmId = models.BigIntegerField(primary_key=False)
    UpdatedAt = models.DateTimeField()
    HallId = models.ForeignKey(Halls, on_delete=models.CASCADE)


class HrPeoples(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CompanyId = models.ForeignKey(Companies, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    FirstName = models.CharField(max_length=50)
    IsDelete = models.BooleanField(default=False)
    LastName = models.CharField(max_length=50)
    MiddleName = models.CharField(max_length=50)
    ModifiedDate = models.DateTimeField()
    Name = models.CharField(max_length=50)
    PositionId = models.BigIntegerField()
    UpdatedAt = models.DateTimeField()


class MovieFormats(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    FormatName = models.CharField(max_length=20)
    CreatedAt = models.DateTimeField()
    UpdatedAt = models.DateTimeField()


class MovieHrPeoples(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    DisplayName = models.CharField(max_length=100)
    FullName = models.CharField(max_length=100)
    HallId = models.ForeignKey(Halls, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50)
    OriginalId = models.IntegerField()
    UpdatedAt = models.DateTimeField()


class MovieOrders(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    CustomerCardId = models.ForeignKey(CustomerCards, on_delete=models.CASCADE)
    Guid = models.CharField(max_length=100)
    OrderSourceId = models.BigIntegerField(primary_key=False)
    UpdatedAt = models.DateTimeField()
    HallId = models.ForeignKey(Halls, on_delete=models.CASCADE)
    MovieHrPeopleId = models.ForeignKey(MovieHrPeoples, on_delete=models.CASCADE)


class Movies(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    Duration = models.FloatField()
    Name = models.CharField(max_length=120)
    Rate = models.CharField(max_length=3)
    Story = models.TextField(max_length=500)
    UpdatedAt = models.DateTimeField()
    PZCrmId = models.BigIntegerField(primary_key=False)
    GenreId = models.ForeignKey(Genres, on_delete=models.CASCADE)


class MovieCountries(models.Model):
    MovieId = models.ForeignKey(Movies, on_delete=models.CASCADE)
    CountryId = models.ForeignKey(Countries, on_delete=models.CASCADE)


class Orders(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CashStationId = models.ForeignKey(CashStations, on_delete=models.CASCADE)
    CloseTimeStamp = models.DateTimeField()
    Closed = models.BooleanField(default=True)
    CreatedAt = models.DateTimeField()
    CustomerCardId = models.ForeignKey(CustomerCards, on_delete=models.CASCADE)
    Guid = models.UUIDField()
    IsDeleted = models.BooleanField(default=False)
    OpenTimeStamp = models.DateTimeField()
    PZCrmId = models.BigIntegerField(primary_key=False)
    UpdatedAt = models.DateTimeField()
    AccountId = models.ForeignKey(HrPeoples, on_delete=models.CASCADE)


class FiscalChecks(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    FiscalShiftId = models.IntegerField()
    IsReversal = models.BooleanField(default=False)
    Number = models.IntegerField()
    OperationType = models.IntegerField()
    OrderId = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ReversalAccountId = models.IntegerField()
    ReversalTimeStamp = models.DateTimeField()
    TimeStamp = models.DateTimeField()
    UpdatedAt = models.DateTimeField()


class PaymentTypes(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    PaymentTypeName = models.CharField(max_length=30)
    UpdatedAt = models.DateTimeField()


class BarPayments(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    Amount = models.FloatField()
    Change = models.FloatField()
    CreatedAt = models.DateTimeField()
    Deleted = models.BooleanField()
    OrderId = models.ForeignKey(Orders, on_delete=models.CASCADE)
    PaymentTypeId = models.ForeignKey(PaymentTypes, on_delete=models.CASCADE)
    UpdatedAt = models.DateTimeField()


class Products(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    Name = models.CharField(max_length=100)
    ParentFolderId = models.ForeignKey(CatalogFolders, on_delete=models.CASCADE)
    UpdatedAt = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    IsDeleted = models.BooleanField()
    ModifiedDate = models.DateTimeField()
    PZCrmId = models.BigIntegerField(primary_key=False)
    CatalogId = models.ForeignKey(Catalogs, on_delete=models.CASCADE)
    IsActive = models.BooleanField(default=True)
    IsSaleDisable = models.BooleanField(default=False)


class OrderItems(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    IsDeleted = models.BooleanField(default=False)
    OrderId = models.ForeignKey(Orders, on_delete=models.CASCADE)
    PZCrmId = models.BigIntegerField(primary_key=False)
    Payment = models.DecimalField(decimal_places=10, max_digits=12)
    ProductId = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.DecimalField(default=1, decimal_places=10, max_digits=12)
    UpdatedAt = models.DateTimeField()


class Rentals(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    HallId = models.ForeignKey(Halls, on_delete=models.CASCADE)
    FromDate = models.DateTimeField()
    MovieId = models.ForeignKey(Movies, on_delete=models.CASCADE)
    PuNumber = models.IntegerField()
    SessionCount = models.IntegerField()
    ToDate = models.DateTimeField()
    UpdatedAt = models.DateTimeField()
    MoviePZId = models.BigIntegerField(primary_key=False)


class Sessions(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    CreatedAt = models.DateTimeField()
    Deleted = models.BooleanField(default=False)
    Locked = models.BooleanField(default=False)
    MovieId = models.ForeignKey(Movies, on_delete=models.CASCADE)
    SessionTime = models.DateTimeField()
    TextCode = models.CharField(max_length=10)
    UpdatedAt = models.DateTimeField()
    HallId = models.ForeignKey(Halls, on_delete=models.CASCADE)
    PZCrmId = models.BigIntegerField(primary_key=False)
    MovieFormatId = models.ForeignKey(MovieFormats, on_delete=models.CASCADE)


class MovieOrderItems(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    BonusPayment = models.FloatField()
    CreatedAt = models.DateTimeField()
    IsRefund = models.BooleanField(default=False)
    MovieOrderId = models.ForeignKey(MovieOrders, on_delete=models.CASCADE)
    Payment = models.FloatField()
    Price = models.FloatField()
    RefundTimeStamp = models.DateTimeField()
    SeatId = models.BigIntegerField(primary_key=False)
    SessionId = models.ForeignKey(Sessions, on_delete=models.CASCADE)
    TicketId = models.BigIntegerField(primary_key=False)
    TimeStamp = models.DateTimeField()
    UpdatedAt = models.DateTimeField()
    PZCrmId = models.BigIntegerField(primary_key=False)
    HallId = models.ForeignKey(Halls, on_delete=models.CASCADE)


class Transactions(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    AccountId = models.ForeignKey(CustomerAccounts, on_delete=models.CASCADE)
    CardId = models.ForeignKey(CustomerCards, on_delete=models.CASCADE)
    CreatedAt = models.DateTimeField()
    IsChecked = models.BooleanField(default=False)
    OrderId = models.UUIDField()
    System = models.IntegerField()
    Type = models.IntegerField()
    UpdatedAt = models.DateTimeField()
    Value = models.DecimalField(decimal_places=10, max_digits=12)
    Checked = models.BooleanField(default=False)
    Guid = models.UUIDField()
    SourceId = models.BigIntegerField(primary_key=False)
    TimeStamp = models.DateTimeField()
    UserId = models.ForeignKey(HrPeoples, on_delete=models.CASCADE)
