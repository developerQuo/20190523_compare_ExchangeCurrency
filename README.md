# compare_ExchangeCurrency
## 환율정보 크롤링을 통한 비교 
<span style="color:red">
## 무단크롤링이므로 서비스는 완전히 구현하지 않았습니다.
</span>

### 개요
* 구분: 웹서비스
* 제작인원: 1명 (본인)
* 제작기간: 2019.05.13 ~ 2019.05.23 (약 2주)
* 주제: 주요 은행별 환율고시 페이지들을 크롤링해서 화폐별로 환율을 비교하여 고시하는 웹페이지.
* 용도: 은행별 우대금리, 환율 등을 한눈에 비교하여 개인들의 환전에 도움을 주기위함.
* 특이사항
	+ 개발환경: python 3.7
	+ 라이브러리: BeautifulSoup

### 환율고시 예시
***
<p align="center">
<img src="/img/exCurrTable.JPG" width="100%" height="80%" title="테이블"></img>
</p>   
   
* 주요 은행별로 위안화 환율을 크롤링하였다.