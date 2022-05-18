## ![펭귄](vue.assets/펭귄.png)

<br>

## Vue Application

<br>

### 1. Vue Router

<br>

* 9: url을 계속 다 칠 수 는 없음 -> 미리 url을 만들어서 저장(drf.js)
* component -> 부품 / views -> url과 매핑

<br>

---

<br>

### 2. 404 page

<br>

* **404 Component** 
  * ![image-20220518201755944](vue_application.assets/image-20220518201755944.png)

<br>

* **404 Not Found 시나리오**
  1. Vue Router에 등록되지 않은 routes일 경우
     * ex. /no-such-routes
  2. Vue Router에는 등록되어 있지만, 서버에서 해당 리소스를 찾을 수 없는 경우
     * ex. /articles/987654321

<br>

* **Vue Router에 등록되지 않은 routes**
  * vue router는 routes 배열에서 순차적으로 URL을 검색
  * 등록되지 않은 모든(*) URL은 /404로 redirection
  * 브라우저에서 NotFound404 컴포넌트 확인
  * ![image-20220518202011461](vue_application.assets/image-20220518202011461.png)
    * 위치가 중요함 / 맨 위에 놓으면 모든 페이지가 404가 됨

<br>

* **서버에서 해당 리소스를 찾을 수 없는 경우**
  * ![image-20220518202101114](vue_application.assets/image-20220518202101114.png)

<br>

---

<br>

### 3. Navigation Guard

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
