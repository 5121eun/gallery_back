# Gallery
## 설명
사진 공유 사이트

<br/>

## 사용 툴
![image](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![image](https://img.shields.io/badge/next%20js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![image](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![image](	https://img.shields.io/badge/axios-671ddf?&style=for-the-badge&logo=axios&logoColor=white)

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![image](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

<br/>

## 주요기능
### 회원가입  
![join](https://github.com/5121eun/gallery_front/assets/121006954/b9315323-65c8-4f68-8d02-2fe487be7514)

- [UserViewSet](https://github.com/5121eun/gallery_back/blob/main/account/views.py#L11)
- [UserSerializer](https://github.com/5121eun/gallery_back/blob/main/account/serializers.py#L12) - 패스워드 암호화 후 DB에 저장

<br/>

### 로그인  
![login](https://github.com/5121eun/gallery_front/assets/121006954/21f27af5-94d2-437f-9153-03e6a78c332a)

- [UserLoginView](https://github.com/5121eun/gallery_back/blob/main/account/views.py#L17) - UserName과 Password를 통해 로그인 처리
<br/>

### 글 작성
![create](https://github.com/5121eun/gallery_front/assets/121006954/5f1dc5e0-fd53-41c5-a6e6-737aea684652)

- [PostViewSet.perform_create](https://github.com/5121eun/gallery_back/blob/main/post/views.py#L18) - API를 request한 유저 정보를 통해 글 작성자 설정
- [PostViewSet.get_all_tags](https://github.com/5121eun/gallery_back/blob/main/post/views.py#L29) - DB에서 태그 리스트 조회 후 리턴

### 메인 페이지 및 글 조회
![show](https://github.com/5121eun/gallery_front/assets/121006954/a85fabf4-933f-4282-84ab-165e87d22049)

- [PostViewSet.get_queryset](https://github.com/5121eun/gallery_back/blob/main/post/views.py#L21) - 태그 검색 결과 및 최신 글 리턴
- [PostViewSet.get_all_tags](https://github.com/5121eun/gallery_back/blob/main/post/views.py#L29) - DB에서 태그 리스트 조회 후 리턴
- [PostSerializer](https://github.com/5121eun/gallery_back/blob/main/post/serializers.py) - 게시글 테이블의 작성자 필드를 유저 테이블의 외래키로 설정
