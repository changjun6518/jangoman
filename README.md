# jangoman

This is changjun's home. welcome!
===

the real always stand still
----

### 2020/4/21/ 화요일
### django model relationships and ORM

관계형 데이터베이스 시스템에서 데이터들의 관계가 중요한데 주로 다음 3가지로 이루워져 있다.
* 1:1 
* 1:다
* 다:다

#### 일대일 관계
OneToOneField
일대일 관계는 주로 기존에 있던 테이블을 구조적으로 확장할 경우 쓰인다.        
하나의 테이블이 있을 때 그 곳에 레코드를 추가하고 싶을 때 추가하려면 기존에 있던 레코드를 전부 입력해야하지만      
테이블을 따로 만들어 주어 추가하면 기존 레코드를 입력할 필요가 없어져서 유용하다.      

#### 1대다 관계
ForeignKey
한 테이블의 2개 이상의 레코드가 다른 테이블에 있는 하나의 레코드를 참조할 때 쓰인다.       
부모와 자식관계라고 생각하는 것도 나쁘지 않다.      

#### 다대다 관계
ManyToManyField
한 테이블의 2개 이상의 레코드가 다른 테이블의 2개 이상 레코드를 참조할 때 쓰인다.        
이 경우 두 테이블의 참조 상황을 나타내기 위한 새로운 테이블이 생성된다. (중개 모델)       

### 코드

<pre>
<code>

class Library(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    library = models.ForeignKey(
        Library,
        on_delete = models.CASCADE,
    )
    author = models.ForeignKey(
        Author,
        on_delete = models.CASCADE,
    )
    language = models.ForeignKey(
        Language,
        on_delete = models.CASCADE,
    )

    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title


class Page(models.Model):
    book = models.OneToOneField(
        Book,
        on_delete = models.CASCADE,
    )

    page_length = models.IntegerField()

    def __str__(self):
        return self.page_length

</pre>
</code>

### ORM 사용하여 데이터 만들기

> import 모델 클래스 하기
<img scr = /1.JPG></img>

> Library 데이터 생성 및 객체 생성 (방법1)
<img scr = /2.JPG></img>

> Language 데이터 생성
<img scr = /3.JPG></img>

> Author 데이터 생성 (방법2)
<img scr = /4.JPG></img>

> Author, Language 객체 생성
<img scr = /5.JPG></img>

> Book 데이터 생성
<img scr = /6.JPG></img>

> all(), filter() 사용
<img scr = /7.JPG></img>

***

# 2020/4/10 금요일
#   1. django
##  2. html, css, javascript

<pre>
<code>
Holly shit!!!!
</code>
</pre>

안녕하세요

    tab으로도 된단말야?
  

![Alt text](/명언.jpg)


git hub과 vs code branch (push pull)

README.md (github때매 뜸)   

markdown 언어 사용법 링크   
(https://gist.github.com/ihoneymon/652be052a0727ad59601#file-gistfile1-md)   
끝
***
