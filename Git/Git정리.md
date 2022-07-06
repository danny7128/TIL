# Git

## Git이란

- git==형상관리도구==프로젝트 버전 관리==분산버전관리 시스템
  포트폴리오X =>TIL(Today I Learned)을 통해 관리하는법을 알려주겠다.

마크다운 개요==문서 구조화
텍스트 기반의 가벼운 마크업 언어
ex)HTML(웹 문서)
text-to-HTML conversion tool

마크다운 활용 예 - README.md
	          - 기술 블로그=>정적사이트 생성기
	          - Jupyter notebook

typora == 마크다운 에디터(editor==편집기)
추천하는이유 : 바로바로 나옴
문서를 작성하는데 별도의 문법이 있구나 정도로 이해하기



# 마크다운 문법



## 마크다운 문법 = Heading
Heading은 문서의 제목이나 소제목으로 사용
#다음에 한칸 띄어야함
#의 개수에 따라 h1~h6까지 표현 가능하다.



## 마크다운 문법 - List
목록(list)
순서가 없는 리스트 :-(hypen), *(asterisk)
목록 활용시 단계를 tab과 shift + tab으로 조절한다.

순서가 있는 리스트: 1.

## 마크다운 문법 - Fenced Code block
`(backtick)기호 3개를 활용하여 작성한다.
특정 언어를 명시하면 Syntax highlighting기능이 적용된다.
​ctrl+엔터 하면 바로나옴

파이썬의 주석=# 주석
html의 주석=<!-- 주석 -->

## 마크다운 문법 - Inline Code block
backtick 기호 1개를 인라인에 활용하여 작성('')

## 마크다운 문법 - Link
[문자열](url)을 통해 링크를 작성 가능
타이포라에서는 ctrl +click을 하면 들어갈 수 있음

## 마크다운 문법 - 이미지
`![문자열](url)`을 통해 이미지를 사용 가능
그냥 이미지 끌어나다가 놓아도 가능(우리컴퓨터의 경로는 다르기 때문에 이미지가 깨져보임)

마크다운 문법 - Blockquotes (인용문)
>를 통해 인용문 작성

## 마크다운 문법 - Table (표)
본문>표>표 삽입(ctrl + t)


마크다운 문법 -text 강조
굵게(볼드체):**
기울림(이탤릭체):*
취소선:~~

마크다운 문법 - 수평선
3개 이상의 ***,---,___



## Git 명령어

git init
git status
git add .
git commit -m '1.txt와2.txt를 만들었음
git log

git config --global user.email "kdt-live@hphk.kr"
git config --global user.name "kdt-live"

## 기본 흐름
Staging 단계가 있는 이유 : 버전으로 기록할 파일을 모으는 '임시공간' 으로 단순하게 생각해주시면 됩니다~!

modified : 파일이 수정된 상태
staged :
committed : 커밋이 완료된 상태

git log
현재 저장소에 기록된 커밋(=버전)을 조회

git log -1(이전(=최근)커밋 1개 가져와라)
git log --online
git log -2 --oneline:최근 2개를 한줄로 보여줘

nothing to commit == 1.커밋할 것이 없다! => staging area가 비어있다~!

working tree clean == 2.지금 새로 작업한 것도 없네! =>1통도 비어있다~!




