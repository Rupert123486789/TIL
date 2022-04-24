## ![펭귄](template_view_routing.assets/펭귄.png)

<br>

## Swagger / Fixtures / Query

<br>

## REST API - M:N

<br>

### 1. REST API 문서화

<br>

* **drf-yasg 라이브러리**
  * "Yet another Swagger generator"
  * API를 설계하고 문서화 하는데 도움을 주는 라이브러리
  * Swagger & OpenAPI 2.0 문서를 제공
  * 설치 및 등록
  * swagger 관련 url 설정
  * 접속 후 확인

<br>

---

<br>

## Fixtures 

<br>

* **How to provied initial data for models**
  * 앱을 처음 설정할 때 미리 준비된 데이터로 데이터베이스를 미리 채우는 것이 필요한 상황이 있음
  * 마이그레이션 또는 fixtures와 함께 초기 데이터를 제공

<br>

* **fixtures**
  * 데이터베이스의 serialized 된 내용을 포함하는 파일 모음
  * django가 fixtures 파일을 찾는 경로
    * app/fixtures/

<br>

* **dumpdata**
  * 응용 프로그램과 관련된 데이터베이스의 모든 데이터를 표준 출력으로 출력

<br>

* **loaddata**
  * fixture의 내용을 검색하여 데이터베이스로 로드

<br>

* **fixtures 실습**
  * 프로젝트 준비
  * 가상환경 생성 및 활성화
  * 패키지 설치 및 migrate
  * fixtures 데이터 추출을 위해 django-seed 라이브러리를 사용해 데이터 생성
  * 각 모델별 dumpdata 실행
  * 실행 결과
  * articles/fixtures/articles, accounts/fixtures/accounts 경로에 추출한 파일 배치하기
  * lodadata 실행
    * 단, loaddata 전에 데이터베이스 삭제
    * **✨[주의] fixtures는 직접 생성하는 것이 아닌 dumpdata를 통해 생성하는 것이니 직접 작성하려 하지 말 것**

<br>

---

<br>

## Improve query

<br>

### 1. 쿼리셋 이해하기

<br>

* **QuerySets are lazy**
  * "쿼리셋은 게으르다."
  * 쿼리셋을 만드는 작업에는 데이터베이스 작업이 포함되지 않음
  * 하루 종일 필터를 함께 쌓을 수 있으며(stack filters), Django는 쿼리셋이 '평가(evaluated)' 될 때까지 실제로 쿼리를 실행하지 않음
  * DB에 쿼리를 전달하는 일이 웹 애플리케이션을 느려지게 하는 주범 중 하나이기 때문
  * 다음 구문에서 몇 개의 쿼리가 DB에 전달될까?
    * print(articles)에서 단 **✨한 번** 전달되

<br>

* **평가 (evaluated)**
  * 쿼리셋에 해당하는 DB의 레코드들을 실제로 가져오는 것
    * == hit, access, Queries database
  * 평가된 모델들은 쿼리셋의 내장 캐시(cache)에 저장되며, 덕분에 우리가 쿼리셋을 다시 순회하더라도 똑같은 쿼리를 DB에 다시 전달하지 않음

<br>

* **[참고] 캐시 (cache)**
  * 데이터나 값을 미리 복사해 놓는 임시 장소
  * 캐시의 접근 시간에 비해 "원래 데이터를 접근하는 시간이 오래 걸리는 경우" 또는 "값을 다시 계산하는 시간을 절약하고 싶은 경우"에 사용
  * 캐시에 데이터를 미리 복사해 놓으면 계산이나 접근 시간 없이
  * 더 빠른 속도로 데이터에 접근할 수 있음
  * 시스템의 효율성을 위해 여러 분야에서 두루 사용됨

<br>

* **쿼리셋이 평가되는 시점 (When QuerySets are evaluated**
  1. Iteration
     * QuerySet은 반복 가능하며 처음 반복 할 때 데이터베이스 쿼리를 실행
  2. bool()
     * bool() 또는 if문 사용과 같은 bool 컨텍스르에서 QuerySet을 테스트하면 쿼리가 실행
     * ✨결과가 하나 이상 존재하는지 확인하기만 한다면 exist()를 사용하는 것이 더 효율적
  3. 이외 Pickling/Caching, Slicing, repr(), len(), list() 에서 평가됨

<br>

* **캐시와 쿼리셋**
  * 각 쿼리셋에는 데이터베이스 엑세스를 최소화하는 '캐시'가 포함 되어있음
    1. 새로운 쿼리셋이 만들어지면 캐시는 비어있음
    2. 쿼리셋이 처음으로 평가되면 데이터베이스 쿼리가 발생
       * Django는 쿼리 결과를 쿼리셋의 캐시에 저장하고 명시적으로 요청된 결과를 반환
       * 이후 쿼리셋 평가는 캐시된 결과를 재사용

<br>

* **쿼리셋이 캐시되지 않는 경우**
  * 쿼리셋 객체에서 특정 인덱스를 반복적으로 가져오면 매번 데이터베이스를 쿼리
  * 그러나 쿼리셋 전체가 이미 평가된 경우 캐시에서 확인

<br>

* **쿼리셋 캐시 관련**
  1. with 템플릿 태그 사용하기
     * 쿼리셋의 캐싱 동작을 사용하여 더 간단한 이름으로 복잡한 변수를 캐시
  2. iterator() 사용하기
     * 객체가 많을 때 쿼리셋의 캐싱 동작으로 인해 많은 양의 메모리가 사용될 때 사용
     * 다음 챕터 like(좋아요) 코드 예시에서 확인할 예정

<br>

---

<br>

### 2. 필요하지 않은 것을 검색하지 않기

<br>

* **Don't retrieve things you don't need**
  * .count()
    * 카운트만 원하는 경우
    * len(queryset) 대신 QureySet.count() 사용하기
  * .exists()
    * 최소한 하나의 결과가 존재하는지 확인하려는 경우
    * if queryset 대신 QuerySet.exists() 사용하기

<br>

* **좋아요 코드 예시**
  * if문 때문에 쿼리셋이 '평가'되고, 이에 따라 쿼리셋 캐시에도 전체 레코드가 저장
  * exists()는 쿼리셋 캐시를 만들지 않으면서 특정 레코드가 존재하는지 검사
    * 결과 전체가 필요하지 않은 경우 유용
  * if문 안에서 반복문이 있다면, 순회할 때는 if문에서 캐시된 쿼리셋이 사용됨
    * 그런데 쿼리셋이 엄청나게 크다면..? 쿼리셋 캐시 자체가 문제가 될 수 있음
  * iterator()는 객체가 많을 때 쿼리셋의 캐싱 동작으로 인해 많은 양의 메모리가 사용될 때 사용
  * 몇 천개 단위의 레코드를 다뤄야 할 경우, 이 데이터를 한번에 가져와 메모리에 올리는 행위는 매우 비효율적이기 때문
  * 데이터를 작은 덩어리로 쪼개어 가져오고, 이미 사용한 레코드는 메모리에서 지움
  * 그런데 쿼리셋이 엄청 큰 경우 평가되는 if문도 문제가 될 수 있음

<br>

* **"안일한 최적화 주의"**
  * exists()와 iterator() 메서드를 사용하면 메모리 사용을 최적화할 수 있지만, 쿼리셋 캐시는 생성되지 않기 때문에, DB 쿼리가 중복될 수 있음

<br>

---

<br>

### 3. Annotate

<br>

* **실습 준비**
  * 프로젝트 준비
  * 가상환경 생성 및 활성화
  * 패키지 설치
  * migrate 및 fixtuer 데이터 load

<br>

* **[참고] Django Debug Toolbar**
  * 현재 요청/응답에 대한 다양한 디버그 정보를 표시하고, 다양한 패널에서 자세한 정보를 표시

<br>

* **annotate**
  * 단순히 SQL로 계산해 하나의 테이블의 필드로 추가하여 붙여 올 수 있는 경우
  * "게시글 별로 댓글 수를 출력 해보기"
  * 개선 전 - 11 queries including 10 similar
  * 개선 후 - 1query

<br>

* **[참고] JOIN 개요**
  * 두 개 이상의 테이블들을 연결 또는 결합하여 데이터를 출력하는 것을 JOIN이라고 함
  * 관계형 데이터베이스의 가장 큰 장점이자 핵심적인 기능
  * 일반적으로 PK나 FK 값의 연관에 의해 JOIN이 성립
  * SQL JOIN에 대해서는 다양한 Visualization 사이트 참고하기
    * https://sql-joins.leopard.in.ua/
    * https://joins.spathon.com/

<br>

* **이제부터 시작**
  * 여기까지는 중복을 제거하지 않고 단순히 쿼리 개수만 날린 것
  * 이것보다 더 큰 문제는 **✨반복문을 도는 상황에서의 1:N, M:N 호출 상황임**

<br>

---

<br>

### 4. 한번에 모든 것을 검색하기

<br>

* **Retrieve everything at once if you know you will need it**
  1. select_related()
     * 1:1 또는 1:N 참조 관계에서 사용
     * DB에서 INNER JOIN을 활용
  2. prefetch_related()
     * M:N 또는 1:N 역참조 관계에서 사용
     * DB가 아닌 Python을 통한 JOIN

<br>

* **select_related()**
  * SQL의 INNER JOIN을 실행하여 테이블의 일부를 가져오고, SELECT FROM에서 관련된 필드들을 가져옴
  * 단, single-valued relationships 관계(foreign key and one-to-one)에서만 사용 가능
  * "게시글의 사용자 이름까지 출력을 해보기"
  * 개선 전 - 11 queries including 10 similar and 10 duplicates
  * 개선 후 - 1 query

<br>

* **prefetch_related()**
  * selected_related와 달리 SQL의 JOIN을 실행하지 않고, python에서 joining을 실행
  * selecte_related가 지원하는 single-valued relationships 관계에 더해, select_related를 사용하여 수행 할 수 없는 M:N and 1:N 역참조 관계에서 사용 가능
  * "댓글 목록을 모두 출력을 해보기"
  * 개선 전 - 11 queries including 10 similar
  * 개선 후 - 2 queries

<br>

* **복합 활용**
  * "댓글에 더해서 해당 댓글을 작성한 사용자 이름까지 출력 해보기"
  * 개선 전 - 111 queries including 110 similar and 100 duplicates
  * 1개 + 10개 + 10개에 대한 10개 = 111개
  * 개선 후 1단계 - 102 queries including 100 similar and 100 duplicates
  * 개선 후 2단계 - 2 queries

<br>

* **섣부른 최적화**
  * "작은 효율성(small efficiency)에 대해서는, 말하자면 97% 정도에 대해서는 잊어버려라. 섣부는 최적화(premature optimization)는 모든 악의 근원이다."
  * ![image-20220424215446675](swagger_fixtures_query.assets/image-20220424215446675.png)





​	

