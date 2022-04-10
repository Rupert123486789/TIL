## ![펭귄](template_view_routing.assets/펭귄.png)

<br>

## Django Form

<br>

* 각각 model을 하나의 데이터 베이스 테이블에 매핑

<br>

### 1.  Form Class

<br>

* **Intro**
  * 우리는 지금까지 HTML, form, input을 통해서 사용자로부터 데이터를 받음
  * 이렇게 직접 사용자의 데이터를 받으면 입력된 데이터의 유효성을 검증하고, 필요시에 입력된 데이터를 검증 결과와 함께 다시 표시해야 함
    * 사용자가 입력한 데이터는 개발자가 요구한 형식이 아닐 수 있음을 항상 생각해야 함
  * 이렇게 사용자가 입력한 데이터를 검증하는 것을 '유효성 검증'이라고 하는데, 이 과정을 코드로 모두 구현하는 것은 많은 노력이 필요한 작업임
  * Django는 이러한 과중한 작업과 반복 코드를 줄여줌으로써 이 작업을 훨씬 쉽게 만들어 줌
    * "Django Form"
  * ✨model로 레이아웃을 짜고, 그 레이아웃 기반으로 DB 생성

<br>

* **Django's forms**
  * Form은 Django의 유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단
  * Django는 Form과 관련한 유효성 검사를 단순화 하고 자동화 할 수 있는 기능을 제공하여 개발자로 하여금 직접 작성하는 코드보다 더 안전하고 빠르게 수행 하는 코드를 작성할 수 있게 함
  * Django는 form에 관련된 작업의 아래 세 부분을 처리해 줌
    	1. 렌더링을 위한 데이터 준비 및 재구성
    	1. 데이터에 대한 HTML forms 생성
    	1. 클라이언트로부터 받은 데이터 수신 및 처리

<br>

* **The Django 'Form Class'**
  * Django Form 관리 시스템의 핵심
  * Form 내 field, field 배치, 디스플레이 widget, label, 초기값, 유효하지 않는 field에 관련된 에러 메세지를 결정
  * Django는 사용자의 데이터를 받을 때 해야 할 과중한 작업(데이터 유효성 검증, 필요 시 입력된 데이터 검증 결과 재출력, 유효한 데이터에 대해 요구되는 동작 수행 등)과 반복 코드를 줄여 줌

<br>

* **Form 선언하기**
  * Model을 선언하는 것과 유사하며 같은 필드타입을 사용 (또한, 일부 매개변수도 유사함)
  * forms 라이브러리에서 파생된 Form 클래스를 상속받음

<br>

* **Form 사용하기**

<br>

* **Form rendering options**

  * `<label>` & `<input> `  쌍에 대한 3가지 출력 옵션

  1.  as_p()
     * 각 필드가 단락(`<p>` 태그)으로 감싸져서 렌더링 됨
  2. as_ul()
     * 각 필드가 목록 항목(`<li>` 태그)으로 감싸져서 렌더링 됨
     * `<ul>` 태그는 직접 작성해야 함
  3. as_table()
     * 각 플디가 테이블(`<tr>` 태그) 행으로 감싸져서 렌더링 됨
     * `<table>` 태그는 직접 작성해야 함

<br>

* **Django의 HTML input 요소 표현 방법 2가지**
  1. Form fields (✨생산성 때문에 사용)
     * input에 대한 유효성 검사 로직을 처리하며 템플릿에서 직접 사용 됨
  2. Widgets
     * 웹 페이지의 HTML input 요소 렌더링
     * GET/POST 딕셔너리에서 데이터 추출
     * widgets은 반드시 Form fields에 할당됨

<br>

* **Widgets**
  * Django의 HTML input element 표현
  * HTML 렌더링 처리
  * 주의 사항
    * Form Fields와 혼동되어서는 안됨
    * Form Fields는 input 유효성 검사를 처리
    * Widgets은 웹페이지에서 input element의 단순 raw한 렌더링 처리
  * 상속, 이미  만들어진 (Model) 사용
  *  id는 장고가 알아서 생성

<br>

---

<br>

### 2. Model Form

<br>

* **Intro**
  * Django Form을 사용하다 보면 Model에 정의한 필드를 유저로 부터 입력 받기 위해 Form에서 Model 필드를 재정의하는 행위가 중복 될 수 있음
  * 그래서 Django는 Model을 통해 Form Class를 만들 수 있는 Model Form이라는 Helper 제공

<br>

* **Model Form Class**
  * Model을 통해 Form Class를 만들 수 있는 Helper
  * 일반 Form Class와 완전히 같은 방식(객체 생성)으로 view에서 사용 가능

<br>

* **Model Form 선언하기**
  * 기존의 Form을 Model Form으로 변경해보기
  * forms 라이브러리에서 파생된 Model Form 클래스를 상속 받음
  * 정의한 클래스 안에 Meta 클래스를 선언하고, 어떤 모델을 기반으로 Form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정
    * [주의] 클래스 변수 fields와 exclude는 동시에 사용할 수 없음

<br>

* **Meta class**
  * Model의 정보를 작성하는 곳
  * Model Form을 사용할 경우 사용할 모델이 있어야 하는데 Meta Class가 이를 구성함
    * 해당 Model에 정의한 field 정보를 Form에 적용하기 위함
  * [참고] inner Class(Nested Class)
    * 클래스 내에 선언된 다른 클래스
    * 관련 클래스를 함께 그룹화 하여 가독성 및 프로그램 유지 관리를 지원 (논리적으로 묶어서 표현)
    * 외부에서 내부 클래스에 접근할 수 없으므로 코드의 복잡성을 줄일 수 있음
  * [참고] Meta 데이터
    * "데이터에 대한 데이터"
    * ex. 사진 촬영 - 사진 데이터 - 사진의 메타 데이터 (촬영 시각, 렌즈, 조리개 값 등)

<br>

* **💥Model Form이 쉽게 해주는 것**
  * 모델 필드 속성에 맞는 HTML element를 만들어 줌
  * 이를 통해 받은 데이터를 view 함수에서 유효성 검사를 할 수 있도록 함

<br>

* **create view 수정**
  * 이미 처음부터 존재하는 앱들

<br>

* is_valid() method
  * 유효성 검사를 실행하고, 데이터가 유효한지 여부를 boolean으로 반환
  * 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 is_valid()를 제공
  * [참고] 유효성 검사
    * 요청한 데이터가 특정 조건에 충족하는지 확인하는 작업
    * 데이터 베이스 각 필드 조건에 올바르지 않은 데이터가 서버로 전송되거나 저장되지 않도록 하는 것

<br>

* **The save() method**
  * Form에 바인딩 된 데이터에서 데이터 베이스 객체를 만들고 저장
  * Model Form의 하위(sub) 클래스는 기존 모델 인스턴스를 키워드 인자 **✨instance**로 받아 들일 수 있음
    * 이것이 제공되면 save()는 해당 인스턴스를 수정 (UPDATE)
    * 제공되지 않은 경우 save()는 지정된 모델의 새 인스턴스를 만듦 (CREATE)
  * Form의 유효성이 확인되지 않은 경우(hasn't been validated) save()를 호출하면 form.errors를 확인하여 에러 확인 가능

<br>

* **create view 함수 구조 변경**
  * new view 함수, url path 삭제
    * 출력 표현을 바꾸는 것 뿐이라 DB에 영향을 주지는 않음 (makemigrations 해도 변경 없음)
    * 변경 사항에 따라 다름 헷갈리면 그냥 makemigrations 하자
  * new.html => create.html 이름 변경 / 이제는 action 값이 없어도 동작
  * create 페이지 링크 작성
  * input 태그에 공백 데이터를 넣어보고 글 작성 => 에러 메시지 출력 확인
    * objects는 고정

<br>

* **DELETE**
  * DELETE 로직 작성

<br>

* **UPDATE**
  * update view 함수 작성(edit path & edit view 함수 삭제)
  * edit.html => update.html 파일명 변경
  * update 로직 완성

<br>

* **forms.py 파일 위치**
  * Form class는 forms.py 뿐만 아니라 다른 어느 위치에 두어도 상관 없음
  * 하지만 되도록 **💥app폴더/forms.py**에 작성하는 것이 일반적인 구조

<br>

* **Form & Model Form 비교**
  * Form (유일한 값 조회)
    * 어떤 Model에 저장해야 하는지 알 수 없으므로 유효성 검사 이후 cleaned_data 딕셔너리를 생성
    * cleaned_data 딕셔너리에서 데이터를 가져온 후 .save() 호출해야 함
    * Model에 연관되지 않은 데이터를 받을 때 사용
  * Model Form
    * Django가 해당 model에서 양식에 필요한 대부분의 정보를 이미 정의
    * 어떤 레코드를 만들어야 할 지 알고 있으므로 바로 .save() 호출 가능

<br>

* **Widgets 활용하기**
  * Django의 HTML input element 표현
  * HTML 렌더링을 처리
  * 2가지 작성 방식을 가짐
    * 두번째 방식 권장

<br>

----

<br>

### 3. Rendering fields manually

<br><br><br><br><br><br><br>

