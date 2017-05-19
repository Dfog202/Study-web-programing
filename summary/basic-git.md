#git

## -사용이유
	빠른속도
	단순한구조
	비선형적 개발
	
## -설치방법 (Linux)
```
$ sudo apt-get install git
	
--  git-daemon-run 오류시
sudo apt-get purge runit
sudo apt-get purge git-all
sudo apt-get purge git
sudo apt-get autoremove
sudo apt update 
sudo apt-get install git-daemon-sysvinit
sudo apt-get install git-all
```
## -깃허브 연동
	$ git config --global user.name "username"
	$ git config --global user.email "github email address"
	$ git config --list

## -기본 사용법
* **git init** 
깃을 사용할 폴더 내에서 입력
폴더설정을 잘못했을때 and 삭제할때 해당 폴더에서  **rm -rf .git** 

* **git add 'file name'**
깃 안에있는 모든 변경된 파일 add
>git add --all

* **git commit -m 'massage'**
massage 에 commit에 관련된 간단한 메세지 입력
>git commit -m 'massage
변경사항
세부내용 bla bla'   < 이런 방법으로 세부내용 입력가능

* **git push origin master**
commit 내용을 github에 업로드
---
## -수정할때
* **git mv "file name" "change file name"**
파일명을 수정하고 싶을때
파일삭제 -> 새파일 생성 -> 새파일에 내용 복사
이름변경으로 인식함. 직접 하나씩 변경도 가능!

* **git commit --amend**  
이미 커밋한 내용에 추가하고 싶을때

* **git commit --amend -m "new message"**
새로운 commit 메세지로 변경

* **git log -p**  
깃 로그의 파일 보기

* **git reset HEAD "file name"** 
커밋에 잘못 추가된 파일 제거

* **git checkout "file name"** 
최근 커밋된 파일로 되돌리는 방법 - ** 주의!! 기존수정 내용은 사라짐**
---
## -리모트 관련
* **git remote -v** 주소확인
```
"프로젝트명" "깃허브주소" "받는곳-fetch, 보내는곳-push"
origin	https://github.com/Dfog202/second-project.git (fetch)
origin	https://github.com/Dfog202/second-project.git (push)
second	https://github.com/Dfog202/second-project2.git (fetch)
second	https://github.com/Dfog202/second-project2.git (push)

```

* **주소 추가**
```
git remote add "프로젝트명" "깃허브주소"
git remote add origin https://github.com/Dfog202/second-project.git
git push origin master
```
* **받아오기**
```
클론주소를 받아서
git clone "클론주소"
git clone https://github.com/Dfog202/remote-project.git
```
* **패치하기**
```
git fatch "프로젝트명"
git fatch origin
git merge origin/master
```  
```
git pull
```
---
## -태그
* **태그입력**
```
git tag -a '태그명'
git tag -a v1.0 
```
* **태그 설명보기**
```
git show '태그명'
git show v1.0
```
* **푸시하기** 일반적인 방법으론 불가능
```
git push "프로젝트명" "태그명"
git push origin v1.0
```
## -Branch
>주소 표시!!
git log --decorate (최신버전은 항시 적용)
git config log.decorate auto (자동설정 켜기)


* **브랜치 추가**
```
git branch "브랜치명"
git branch test
```
* **헤드 위치 변경**
```
git checkout "브랜치명"
git checkout test
```
>**Short Cut !! 브랜치 추가 + 헤드위치 변경**
git checkout -b hotfix

* **브랜치 분기 확인**
```
$ git log --oneline  --graph --all
```
* **브랜치명 변경**
```
git branch -m "브랜치명" "변경 브랜치명"
git branch -m master production
```
* **현재 브랜치와 내용 합치기**
```
git merge "합칠 브랜치명"
git merge develop
```
>충돌오류시 오류확인, 수정후 다시 add,commit
commit 내용에 오류메세지가 기본설정되있으니
내용입력 안해줘도 괜찮음

* **브랜치 삭제**
```
git branch -d "브랜치명"
git branch -d develop
```


---
<br>
<br>
#Shell

#### -zsh
 	bash와 비슷하게 동작하는 셸로 사용성이 좋다.
#### -설치방법
```
sudo apt-get install zsh
curl -L http://install.ohmyz.sh | sh
chsh -s `which zsh`
```
```
변경됬는지 확인방법
echo $SHELL 입력후 메세지 확인
/usr/bin/zsh
```
#### -필수 기본설정 (Linux)
```
vi ~/.zshrc 로 들어가서 추가입력

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

```
#### -Vim 사용법은 링크 참조!!
[Vim 단축키 링크](https://github.com/Fastcampus-WPS-5th/Utils/blob/master/vim.md)

#### -알면 좋을 터미널 명령어
pwd 현재 위치 경로확인
cat 'file name' - 내용확인
echo "Hello" > abc.txt < 헬로 내용을 가진 텍스트 파밀 만들기
take "name"  << name 폴더를 만들고 