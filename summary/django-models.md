# models
>모델은 데이터에 대한 단일 정보 소스
>일반적으로 각 모델은 단일 데이터베이스 테이블에 매핑

### 기본구조

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```
### 모델의 사용법

* settings.py 안의 INSTALLED_APPS에 정의한 models.py을 포함하는 모듈 이름을 추가하는 것으로 가능

```python
INSTALLED APP = [
'app이름',
]
```
> migrate 를 해줘야 적용된다!!!

### 필드

>모델을 정의하는 데이터베이스 필드의 목록-
>**모델에서 가장 중요한 부분!**

* 예제

```python
from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```

### 필드의 형태

* The column type - 데이터베이스가 가지고있는 데이터가 어떤 형태인지(**INTEGER, VARCHAR, TEXT**)

* form 필드를 랜더링하는 기본 HTML형식 `(<input type="text">, <select>)`

* 최소한의 유효성 확인 - 장고에서 자동생성되는 form

### 필드 옵션

* null - 없는 값
* blank - 빈 값
* choices - 주어지는 옵션으로 선택을 제한

```python
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
```
* default - 기본값
* help_text - 보조..글
* primary_key - 키! 읽기전용 필드. 기존개체의 키값을 변경후 저장하면 새 개체 생성
* unique - 유니크한 테이블! 고유한?

### Automatic primary_key fields
* 장고에서는 각 모델에 자동으로 id필드 생성

```python
id  =  models . AutoField ( primary_key = True )
```
>장고에서 모델은 반드시 하나의 primary_key를 가져야 함

### Verbose field names
* 첫번째 인수를 사용한다. 없는경우 변수명의 `언더바_`를 스페이스바로 변환하여 자동생성 한다.

```python
# person's first name
first_name = models.CharField( "person's first name",  max_length = 30 )
# first name
first_name = models.CharField( max_length = 30 )
# 첫번째 인수로 다른값을 받아야 하는경우 지정해서 변경할수 있다.
# (ForeignKey, ManyToManyField, OneToOneField)
sites = models.ManyToManyField( Site, verbose_name = "list of sites" )
```

### 관계 (Relationships)

* 다대일 관계
> django-db.models.ForeignKey 를 사용해야 한다. 인수로 모델의 클래스를 받아오면 된다.

```python
from django.db import models

class Manufacturer(models.Model):
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
```

* 다대다 관계
> ManyToManyField를 사용하면 된다. 하지만 사용하는 모델중 하나에만 입력해야한다.

```python
class Topping(models.Model):
	pass

class Pizza(models.Model):
  toppings = models.ManyToManyField(Topping)
```
피자(Pizza)는 여러가지의 토핑(Topping)을 가질 수 있다.
그러므로, 토핑 역시 여러가지 피자에 포함 될 수 있다.

* 복잡한 다대다 관계
> through 인자를 사용해 연결해주면 된다. 더 공부하자..... 정리가 안된다 ㅠ

```python
class Person(models.Model):
    name = models.CharField(max_length=128)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
```

* 일대일 관계
>OneToOneField 를 사용한다. 상속을 사용해도 된다. 상속과 차이점....? 더 공부 필요

### 다른 앱에서 가져오기
> 해당 파일을 임포트해서 사용한다.
```python
from django.db import models
from geography.models import ZipCode

class Restaurant(models.Model):
    zip_code = models.ForeignKey(
        ZipCode,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
```

### 필드 이름 제한
* 필드명으로 파이썬 예약어는 사용이 불가능하다
* `더블 언더바__`는 사용 불가능하다

### Meta 옵션
> 메타데이터 속성을 주기 위해 내부 클래스로 Meta를 정의

```python
class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"
```
메타 데이터는 필드가 아닌 모든 것들이 들어간다

### 모델 속성
>Manager가 정의되지 않은경우 기본값은 objects

* 데이터베이스에서 인스턴스를 검색하는데 사용

### 모델 메소드
>행 단위의 기능을추가하기 위해서 custom method 사용
```python
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property    /// 이부분이 커스텀 메소드
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
```

* `__str__()` 파이썬 매직매서드로 모델 인스턴스를 문자열로 표시해야할때 사용.
* get_absolute_url() 객체의 url을 계산할 수 있도록 해준다.

### Overriding predefined model methods
> save() 및 delete()를 사용하는 작업 방식을 변경하고 싶은 경우

```python
# 다른방식으로 저장하고 싶을때
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        do_something()
        super(Blog, self).save(*args, **kwargs) # super를 사용해 진짜 save()를 불러온다
        do_something_else()
...
# 저장을 원하지 않을때
    def save(self, *args, **kwargs):
        if self.name == "Yoko Ono's blog":
            return # Yoko shall never have her own blog!
        else:
            super(Blog, self).save(*args, **kwargs) # Call the "real" save() method.
```
만약 superclass 메서드를 추가하지 않는다면, 원래 save() 메서드의 동작이 작동되지 않아 DB에 데이터를 저장하지 않게된다.

### 모델 상속
* Abstract base classes
공통된 정보를 다른 여러 모델에 넣을때 유용한 방법.
abstract = True 를 사용하면 데이터베이스를 생성하지 않는다.
```python
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta):   //이 방법으로 메타상속도 가능하다.
    db_table = 'student_info'  
```

* Multi-table inheritance
```python
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
```
데이터는 다른 테이블에 존재하지만 Place 필드는 Restaurant에서도 사용할수 있다.

* Proxy models
>  프록시를 이용한 경우에 생기는 차이는 원래 모델을 변경하지 않고 기본 모델의 정렬 순서와 관리자의 설정을 프록시에서 변경할 수 있다

```python
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MyPerson(Person):
    class Meta:
        proxy = True     // 프록시 모델에 메타값으로 proxy = True 입력해준다

    def do_something(self):
        pass
```
MyPerson은 Person을 상속받지만, table이 별도로 생성되지 않는다.
이때, Person과 MyPerson은 같은 데이터를 가진다.(같은 Person 테이블을 사용한다)

### 다중상속
> 여러 부모모델에게 상속받는것도 가능하다.. 특정이름이 같이 상속되는경우 첫번째 부모것을 받는다.
```python
class  Article ( models . Model ) :
    article_id  =  models . AutoField ( primary_key = True )
    ...

class  Book ( models . Model ) :
    book_id  =  models . AutoField ( primary_key = True )
    ...

class  BookReview ( Book ,  Article ) :
    pass
```

자세하게.. 정리필요!! 이해못해서 나도 알아보기 힘들게 적었음 ㅠ
