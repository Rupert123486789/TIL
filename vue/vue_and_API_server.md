## ![펭귄](vue.assets/펭귄.png)

<br>

## Vue & API Server

<br>

### 1. Server  & Client

<br>

* **Server**
  * 클라이언트에게 '정보', '서비스'를 제공하는 컴퓨터 시스템
  * 정보 & 서비스
    * Django를 통해 응답한 template
    * DRF를 통해 응답한 JSON

<br>

* **Server - 정보 & 서비스 제공**
  * ![image-20220516201726119](vue_and_API_server.assets/image-20220516201726119.png)
  * ![image-20220516201733669](vue_and_API_server.assets/image-20220516201733669.png)

<br>

* **Client**
  * 서버에게 그 서버가 맡는(서버가 제공하는) **✨서비스를 요청(request)**하고, 서비스 요청을 위해 필요한 인자를 ✨**서버가 요구하는 방식에 맞게 제공**하며, 서버로부터 반환되는 응답을 ✨**사용자에게 적절한 방식으로 표현(response)**하는 기능을 가진 시스템
    * 💥**request - > response**

<br>

* **Client - 서버에 올바른 요청**
  * ![image-20220516202031895](vue_and_API_server.assets/image-20220516202031895.png)
    * ✨올바른 요청 == 형식에 맞는 요청(ex. urls.py,  / articles/ ...)
  * ![image-20220516202040461](vue_and_API_server.assets/image-20220516202040461.png)

<br>

* **Client - 사용자에게 적절하게 표현**
  * ![image-20220516202156646](vue_and_API_server.assets/image-20220516202156646.png)
  * ![image-20220516202221069](vue_and_API_server.assets/image-20220516202221069.png)

<br>

* **정리**
  * Server는 ✨**"정보 제공"**
    * DB와 통신하며 데이터를 CRUD
    * 요청을 보낸 Client에게 이러한 정보를 응답
  * Client는 ✨**"정보 요청 & 표현"**
    * Server에게 정보(데이터) 요청
    * 응답 받은 정보를 잘 가공하여 화면에 보여줌
  * ✨Data -> ERD -> Modeling
  * ✨어떤 데이터를 보낼지에 대한 합의

<br>

---

<br>

### 2. Start Project Model + Serializer

<br>

---

<br>

### 3. CORS

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
