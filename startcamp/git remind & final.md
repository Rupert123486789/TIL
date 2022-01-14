## Git

> git은 분산버전관리시스템(DVCS) Distributed Version Control System
>
> 소스코드의 버전을 관리하고 이력도 관리할 수 있다.



### 준비하기

1. 윈도우에 git을 설치한다.(git bash 설치)
2. 초기 설치 완료 후 로컬 컴퓨터에 **Author** 정보를 설정해야한다.

```bash
$ git config --global user.email 유저이메일
$ git config --global user.name 유저네임

$ git config --global -l   // 설정 값을 확인하는 명령어
```



---



## 로컬 저장소



### 1. 저장소 초기화

```bash
$ git init

~/ ssafy(master)    // master명 확인 git 관리여부 확인
```

| Working directory                                            | Staging Area                                                 | local Repository(commit)                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------- |
| 실제 작업되는 공간<br /> 변경점이 나타나면 이곳에 파일이 등록 | commit 되기 전 임시로 파일들이 보여지는 곳 <br />이곳에서 commit 되어도 되는지 파일을 확인 | git으로 관리되는 파일들의 버전들이 저장되는 곳 |

git commit -a : add와 commit을 동시에 해주지만, 중간에 확인 불가



---



### 2. 상태를 확인

```bash
$ git status   // WD, SA 의 상태를 확인하기 위한 명령어
```

* Untracked
  * git으로 관리되지 않았던 파일이 등록된 경우
  * WD에서 해당 단어를 확인할 수 있음

* Tracked
  * New file : git으로 관리되지 않았던 파일이 Staging Area에 등록되었을 때 확인할 수 있음
  * Modified : git으로 관리되는데 수정된 파일이 Staging Area에 등록되었을 때



---



### 3. gitignore

> 주의 : gitignore에 먼저 등록하고 add를 하자!!!
>
> 미리 add 되어 잇으면 gitignore에 등록되어 있어도 계속 관리됨.
>
> 잘못해서 뺄 경우 
>
> ```bash
> $ git restore --staged 파일명
> ```

* 프로젝트에 관련 없는 파일을 등록하여 commit 되지 않도록 하는 것

  * 민감한 개인 파일

  * 개인 컴퓨터 설정파일(OS에서 활용되는 파일)
  * IDE 환경 설정 파일(.idea/)
  * 가상환경 폴더 및 파일(venv/)
* `.gitignore` 파일을 생성(확장자는 따로 없음)

  * 제외하고 싶은 파일을 등록
  * 파일명을 적어주면 끝
* gitignore 사용(code 환경에서)

```bash
- 일반적인 방법
# b.txt
# d.txt

- 특정 확장자만 무시
	 png 확장자를 가진 파일들은 전부 무시
*.png   

- 이 때 특정 파일 하나는 등록되어야 하는 경우
!파일이름.png

- 폴더를 무시 (뒤에 /)
폴더이름/

- 상위 폴더만 무시하고 싶을 때(temp-temp1 과 temp1이 있을 때) 
특정 폴더를 무시하고 싶을때 경로와 함께 폴더명을 적으면 된다
/temp1
```

* gitignore.io를 이용하면 편하게 gitignore 파일을 작성할 수 있음

  * 필요없는 파일 알아서 생성 해줌
  * 운영체제, 프로그램 입력하고 나오는 코드를 전부 복사해서 .gitignore 에 넣어주기
  * 단, 우리가 생성한 파일은 우리가 직접 등록해야함(ex) 단순 참고용도인 파일들)

  

---



### 4. Commit을 위한 준비

```bash
$ git add 파일명
$ git add .      // 현재 폴더 내에 있는변경/추가된 파일 모두를 등록
```

* Working Directory에서 Staging Area로 관리 파일들을 이동시키는 명령어
* Staging Area에서 관리 대상에 대한 판단을 하고 commit 여부를 결정



---



### 5. Commit 하기

```bash
$ git commit -m "커밋 메세지를 남기자! 유의미한 내용으로 작성"   // 협업하는 동료와 미래의 나에게 배려
```

* 버전 이력을 확정짓는 명령어
* 해당 시점의 파일 변경된 내용을 스냅샷으로 기록해 남긴다.



---



### 6. Commit 이력 확인하기

```bash
$ git log
$ git log --oneline  // 한 줄로 축약해서 보여줌
$ git log -p         // 파일의 변경 내용도 같이 보여줌
$ git log -숫자       // 숫자만큼만 보여줌
```



---



## 원격 저장소(remote Repository)

* github/gitlab/~~bitbucket(사용률이 낮음)~~



### 1. 원격 저장소 등록

* 사용을 하기 위해서는 로컬에 원격 저장소의 url 주소를 등록해야 함

```bash
$ git remote add 저장소별명(origin) 저장소주소
```

*  등록된 원격 저장소의 주소를 확인하는 방법

```bash
$ git remote -v
```

* 저장소 삭제

```bash
$ gir remote rm 저장소별명
```



---



### 2. 원격 저장소에 commit 내용 보내기

* 로컬에 저장된 commit 을 원격저장소로 전달하여 분산 버전 관리를 완성하는 부분

```bash
$ git push 저장소별명 브랜치명
$ git push -u origin master
```

* O  -u : --set-upsteram의 shortcut 형태이고 저장소 별명과 브랜치 명을 설정

​	

## 원격 저장소에서 내려받기

### 1. git clone

* `git init` , `git remote add` 동작이 포함된 내려받기 명령어
* 아무것도 없는 상태일 때 사용

* `git clone 리모트레포주소` 

  

---



### 2. git pull

* remote 서버의 정보를 내려받는 명령어
* git이 적용되어 있어야 한다.(.git 폴더가 존재해야함)
* remote 정보가 등록되어 있어야 한다.
* `git pull 리모트별명(origin) 브랜치명(master)`



---



## 기타)

### submodule warning 메세지를 봤다!!

1. 어떤 폴더가 submodule 인지 확인한다.

2. 해당 폴더로 찾아가서 .git 폴더를 제거한다.
3. 이미 staging Area에 올라간 상태라면

​		`git rm -rf --cached 폴더명` 으로 해당 폴더를 Staghing Area에서 Working Directory로 내린다.

4. git status 로 다시 상태를 체크하고
5. git add 로 Staging Area에 다시 올린다.
6. 그리고 다시 git status 로 Staging Area 에 올라온 상태를 파악하고
7. git commit 을 한다.

* 싸피 1학기 과정에서는 submodule 사용계획 X (쓸거면 구글링해서 알아보기)
* CLI 환경에서(master) 가 보이면 git init 을 하지 않는게 좋다.(submodule로 세팅됨)