# Gallery 백엔드
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
![join-ezgif com-video-to-gif-converter (1)](https://github.com/5121eun/gallery_back/assets/121006954/cfe56d57-b9da-4b9e-a003-fbe7bb1641b8)

- [UserViewSet](https://github.com/5121eun/gallery_back/blob/main/account/views.py#L11)
- [UserSerializer](https://github.com/5121eun/gallery_back/blob/main/account/serializers.py#L12) - 패스워드 암호화 후 DB에 저장

<br/>

### 로그인
![login-ezgif com-video-to-gif-converter (2)](https://github.com/5121eun/gallery_back/assets/121006954/b1f42bdd-e4c4-44a1-80e8-333377307e53)

- [UserLoginView](https://github.com/5121eun/gallery_back/blob/main/account/views.py#L17) - UserName과 Password를 통해 로그인 처리
<br/>

### 글 작성
![post-create-ezgif com-video-to-gif-converter](https://github.com/5121eun/gallery_back/assets/121006954/7496e30a-42aa-4e95-bb62-3ff482c9bc99)

- [PostViewSet.perform_create](https://github.com/5121eun/gallery_back/blob/main/post/views.py#L18) - API를 request한 유저 정보를 통해 글 작성자 설정
- [PostViewSet.get_all_tags](https://github.com/5121eun/gallery_back/blob/main/post/views.py#L29) - DB에서 태그 리스트 조회 후 리턴
<br/>

### 메인 페이지 및 글 조회
![gallery-ezgif com-video-to-gif-converter](https://github.com/5121eun/gallery_back/assets/121006954/32afafbd-9d1c-485a-a6cb-fb567740e1e0)

- [PostViewSet.get_queryset](https://github.com/5121eun/gallery_back/blob/main/post/views.py#L21) - 태그 검색 결과 및 최신 글 리턴
- [PostViewSet.get_all_tags](https://github.com/5121eun/gallery_back/blob/main/post/views.py#L29) - DB에서 태그 리스트 조회 후 리턴
- [PostSerializer](https://github.com/5121eun/gallery_back/blob/main/post/serializers.py) - 게시글 테이블의 작성자 필드를 유저 테이블의 외래키로 설정
