## ![펭귄](template_view_routing.assets/펭귄.png)

<br>

## Model Relationship II

<br>

## Intro

<br>

### 1. 병원 진료 기록 시스템

<br>

* **병원 진료 기록 시스템을 통한 M:N 관계 학습**
  * 환자와 의사가 사용하는 병원 진료 기록 시스템 구축
    * 병원 시스템에서 가장 핵심이 되는 객체는 무엇일까? => 환자와 의사
    * 이 둘의 관계를 어떻게 표현할 수 있을까?
* **시작하기 전**
  * 모델링은 현실 세계를 최대한 유사하게 반영하기 위한 것
  * 우리 일상에 가까운 예시를 통해 DB를 모델링하고, 그 내부에서 일어나는 데이터의 흐름을 어떻게 제어할 수 있을지 고민해보기

<br>

* **1. 1:N의 한계**

  * 1:N 모델 관계 설정

  * 의사 2명과 환자 2명 생성

  * 1번 환자가 1번 의사의 진료를 마치고, 2번 의사에게도 방문하려고 한다면, 새로운 예약을 생성해야 함.

  * 기존의 예약을 유지한 상태로 새로운 예약을 생성

  * 새로 생성한 3번 환자는 1번 환자와 다름

  * 한 번에 두 의사에게 진료를 받고자 함

  * 하나의 외래 키에 2개의 의사 데이터를 넣을 수 없음

  * 정리

    * 새로운 예약을 생성하는 것이 불가능
      * 새로운 객체를 생성해야 함
    * 여러 의사에게 진료 받은 기록을 환자 한 명에 저장할 수 없음
      * 외래 키에 '1, 2' 형식의 데이터를 사용 할 수 없음

    

<br>

* **2. 중개 모델**
  * 중개 모델(혹은 중개 테이블, Associative Table) 작성
  * 중개 모델과의 모델 관계 확인
    * ![image-20220423203618870](model_relationship2(M_N).assets/image-20220423203618870.png)
  * 의사 1명과 환자 1명 생성 및 예약 생성
  * 예약 내역 조회
  * 의사의 예약 환자 조회
  * 환자의 담당 의사 조회
  * 환자 1명 추가 생성 및 1번 의사에게 예약 생성
  * 의사의 예약 환자 조회
  * ✨중개 모델에 의해 다대다 관계가 설정되었음

<br>

* **3. ManyToManyField**
  * 다대다 (M:N, many-to-many) 관계 설정 시 사용하는 모델 필드
  * 하나의 필수 위치인자(M:N 관계로 설정할 모델 클래스)가 필요
  * ManyToManyField 작성 (중개 모델 삭제)
    * 필드 작성 위치는 Doctor 또는 Patient 모두 작성 가능(✨어디든 상관 없음)
    * 💥1:N과 의 차이점 
      * M:N 관계를 맺는 2개의 테이블에는 아무런 변화가 없음(외래키 X)
      * 2개의 테이블이 같이 사용하는 중개 테이블이 생성됨
      * 1:N에서는 외래키가 무조건 N쪽에 위치(종속관계)
      * M:N은 어느 곳에도 서로 종속되지 않음(대등한 관계)
    * 단지 참조 / 역참조의 관계만 바뀜
      * 중개 모델 일경우는 둘다 역참조임
      * ManyToManyField에서는 필드를 중심으로 참조/역참조
  * ManyToManyField로 인해 생성된 중개 테이블 확인
  * 의사 1명과 환자 2명 생성
  * 예약 생성 (참조)
    1. patient1이 doctor1에게 예약
    2. patient1이 예약한 의사 목록 확인
    3. doctor1에게 예약된 환자 목록 확인
  * 예약 생성 (역참조)
    1. doctor1이 patient2를 예약
    2. doctor1에게 예약된 환자 목록 확인
    3. patient2, patien1이 각각 예약한 의사 목록 확인
    4. add라는 queryser API가 생김
    5. ✨역참조로 진행했을뿐, 환자가 참조했을때의 데이터 결과와 동일함
  * 중개 테이블 데이터 확인
  * 예약 삭제 (역참조)
    1. doctor1이 patient1 진료 예약 취소
    2. doctor1에게 예약된 환자 목록 확인
    3. patient1이 예약한 의사 목록 확인
  * 예약 삭제 (참조)
    1. patient2가 doctor1 진료 예약 취소
    2. patient2가 예약한 의사 목록 확인
    3. doctor1에게 예약된 환자 목록 확인
  * 중계 테이블 데이터 확인

<br>

* **4. related_name**
  * target model(관계 필드를 가지지 않은 모델-의사)이 source model(관계 필드를 가진 모델-환자)을 참조할 때(역참조) 사용할 manager의 이름을 설정
  * ✨역참조 : 타겟 모델이 소스모델을 참조한다
  * 즉, 역참조 시에 사용하는 manager의 이름을 설정
  * ForeignKey의 related_name과 동일
    * ![image-20220423204956792](model_relationship2(M_N).assets/image-20220423204956792.png)
    * patient_ser => patients (복수형, M:N임을 나타내기 위해)
  * doctor1의 예약 호나자 목록 확인 해보기 (역참조)
  * ✨related_name 설정 후 기존의 _set manager는 더 이상 사용할 수 없음

<br>

* **중개 모델(테이블) in Django**
  * django는 ManyToManyField를 통해 중개 테이블을 자동으로 생성
  * 그렇다면 중개 테이블을 직접 작성하는 경우는 없을까?
    * 중개 테이블을 수동으로 지정하려는 경우 through 옵션을 사용하여, 중개 테이블을 나타내는 Django 모델을 지정할 수 있음 (다음 챕터에서 확인)
    * ✨가장 일반적인 용도는 중개 테이블에 추가 데이터를 사용해 다대다 관계로 연결하려는 경우에 사용
      * ex. 예약시간 / 병명 등 추가 데이터를 넣을 수가 없음 (ManyToManyField 만으로는)
      * 직접 작성해야함

<br>

* **요약**
  * 실제 Doctor와 Patient 테이블이 변하는 것은 없음
  * 1:N 관계는 완전한 종속의 관계이지만, M:N 관계는 **💥의사에게 진찰받는 환자, 환자를 진찰하는 의사의 두가지 형태로 모두 표현이 가능한 것**

<br>

----

<br>

## ManyToManyField

<br>

* **ManyToManyField's 개념 및 특징**
  * 다대다 (M:N, many-to-many) 관계 설정 시 사용하는 모델 필드
  * 하나의 필수 위치인자 (M:N 관계로 설정할 모델 클래스)가 필요
  * 모델 필드의 RelatedManager를 사용하여 관련 개체를 추가, 제거 또는 만들 수 있음
    * add(), remove(), create(), clear() ...
  * [참고] RelatedManager
    * 일대다 또는 다대다 관련 컨텍스트에서 사용되는 manager

<br>

* **ManyToManyField's Arguments**
  1. related_name
     * target model(관계 필드를 가지지 않은 모델)이 source model(관계 필드를 가진 모델)을 참조할 때(역참조 시) 사용할 manager의 이름을 설정
     * ForeignKey의 realted_name과 동일
  2. through
     * 중개 테이블을 직접 작성하는 겨우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정할 수 잇음
     * 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우 (extra data with a many-to-many relationship)에 주로 사용됨
  3. symmetrical
     * ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용
     * symmetrical=True(기본값)일 경우 Django는 person_set 매니저를 추가하지 않음
     * source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면, target 모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 함
       * 즉, 내가 당신의 친구라면 당신도 내 친구 되는 것
       * 대칭을 원하지 않는 경우 False로 설정
       * Follow 기능 구현에서 다시 확인 할 것
       * ![image-20220423210402396](model_relationship2(M_N).assets/image-20220423210402396.png)

​	

<br>

* **Related Manager**
  * 1:N 또는 M:N 관련 컨텍스트에서 사용되는 매니저
  * 같은 이름의 메서드여도 각 관계(1:N, M:N)에 따라 다르게 사용 및 동작
    * 1:N에서는 target 모델 인스턴스만 사용 가능
    * M:N 관계에서는 관련된 두 객체에서 모두 사용 가능
  * 메서드 종류
    * add(), remove(), create(), clear(), set() 등

<br>

* **add()**
  * "지정된 객체를 관련 객체 집합에 추가"
  * 이미 존재하는 관계에 사용하면 관계가 복제되지 않음
  * 모델 인스턴스, 필드 값(PK)을 인자로 허용
    * ![image-20220423210704180](model_relationship2(M_N).assets/image-20220423210704180.png)

<br>

* **remove()**
  * "관련 객체 집합에서 지정된 모델 객체를 제거"
  * 내부적으로 QuerySet.delete()를 사용하여 관계가 삭제됨
  * 모델 인스턴스, 필드 값(PK)을 인자로 허용
    * ![image-20220423210751814](model_relationship2(M_N).assets/image-20220423210751814.png)

<br>

* **through 예시**
  * 모델 관계 설정
    * ![image-20220423210835021](model_relationship2(M_N).assets/image-20220423210835021.png)
  * 중개 테이블 확인
    * ![image-20220423210904728](model_relationship2(M_N).assets/image-20220423210904728.png)
  * 의사 1명과 환자 2명 생성
  * 예약 생성 1 / 중개 테이블 확인
  * 예약 생성 2 / 중개 테이블 확인
    * through_defaults를 사용해 add(), create() 또는 set()을 사용하여 관계를 생성
  * 예약 삭제

<br>

* **데이터베이스에서의 표현**
  * Django는 다대다 관계를 나타내는 중개 테이블을 만듦
  * 테이블 이름은 다대다 필드의 이름과 이를 포함하는 모델의 테이블 이름을 조합하여 생성됨

<br>

* **중개 테이블의 필드 생성 규칙**
  1. source model 및 target model 모델이 다른 경우
     * id
     * `<containing_modle>_id` => patient_id
     * `<other_model>_id` => doctor_id
  2. ManyToManyField가 동일한 모델을 가리키는 경우
     * id
     * `from_<model>_id`
     * `to_<model>_id`

<br>

---

<br>

### 1. 좋아요 기능 (Like)

<br>

* **Like 구현**
  * ManyToManyField 작성 후 마이그레이션
  * 에러 발생 원인
    * like_users 필드 생성 시 자동으로 역참조는 .article_set 매니저를 생성
    * 그러나 이전 1:N(User:Article) 관계에서 이미 해당 매니저 이름을 사용 중이기 때문
    * User와 관계된 ForeignKey 또는 ManyToManyField 중 하나에 related_name 추가 필요
  * related_name 설정 후 마이그레이션 다시 진행
    * ![image-20220423211811981](model_relationship2(M_N).assets/image-20220423211811981.png)
  * 생성된 중개 테이블 확인

<br>

* **현재 User - Article 간 사용 가능한 DB API **
  * article.user
    * 게시글을 작성한 유저 - 1:N
  * article.like_users
    * 게시글을 좋아요한 유저 - M:N
  * user.article_set
    * 유저가 작성한 게시글(역참조) - 1:N
  * user.like_articles
    * 유저가 좋아요한 게시글(역참조) - M:N

<br>

* **Like 구현**
  * url 작성
  * like view 함수 작성

<br>

* **QuerySet API - 'exists()'**
  * QuerySet에 결과가 포함되어 있으면 True를 변환하고 그렇지 않으면 False를 반환
  * 특히 규모가 큰 QuerySet의 컨텍스트에서 특정 개체 존재 여부와 관련된 검색에 유용
  * 고유한 필드(예: primary key)가 있는 모델이 QuerySet의 구성원 인지 여부를 찾는 가장 효율적인 방법

<br>

* **Like 구현**
  * index 페이지에 like 출력 부분 작성
  * 좋아요 버튼 클릭 후 테이블 확인

<br>

---

<br>

### 2. Profile Page

<br>

* **Profile Page 작성**
  * 자연스러운 follow 흐름을 위한 회원 프로필 페이지 작성하기
  * url 작성
    * `<str>`이 맨 위에 있으면 아래 주소들은 `<int>`가 나올 때까지 다 먹힘
    * 문자열로 되어있으면 맨 아래로 놔줘야함
  * profile view 함수 작성
    * ✨get_user_model() : 현재 프로젝트에서 활정화된 유저 객체를 리턴해주는 함수
    * username도 유니크한 값 => 중복 아이디 가입 X
  * profile 페이지 작성
  * base 페이지에 프로필 링크 작성
  * index 페이지에 프로필 링크 작성

<br>

---

<br>

### 3. 팔로우 기능 (Follow)

<br>

* **Follow 구현**
  * ManyToManyField 작성 후 마이그레이션
    * symmentrical=False
      * self를 사용할 때만 사용 / True면 자동으로 추가
  * 생성된 중개 테이블 확인
    * ✨자기 자신을 참조하면 from과 to를 붙여서 만들어 줌
  * url 작성
  *  follow view 함수 작성
  * profile 페이지에 팔로우와 언팔로우 버튼 작성
    1. 팔로잉 수 / 팔로워 수 출력
    2. 자기 자신을 팔로우 할 수 없음
  * with 태그로 자주 쓰는 것을 변수로 표기 할 수 있음 => 최적화랑은 관계 없음
    * as : 이전 표기법
    * = : 최근 표기법
  * 팔로우 버튼 클릭 후 테이블 확인

<br>

---

<br>

* **마무리**
  * view 함수에 배웠던 모든 것이 있음
    * ![image-20220423213249131](model_relationship2(M_N).assets/image-20220423213249131.png)

* **추가사항**
  * cdn font awesome / Graveta 등을 이용해 아이콘이나 이미지 등을 넣을 수 있음
