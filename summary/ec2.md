# EC2

## 로컬부분 설정하기!
>장고 프로젝트 생성 후 secret_key 숨기기

**python**
3.6.1

**gitignore**
```
.config_secret/  깃에 올라가지 않게 내용 추가
```

### Create secret config files
```
project_folder/
  .config_secret/
    settings_common.json
    settings_debug.json
    settings_deploy.json
  .djnago_app.
  ...
  ...
```

#### settings_common.json example
```json
{
  "django": {
    "secret_key": "Your secret_key insert Here!!!"
  }
}
```

#### settings_debug & deploy.json
```json
{
  "django": {
    "allowed_hosts": [
      "*"
    ]
  }
}
```

#### settings 경로 지정
```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)

# .config_secret폴더 및 하위 파일 경로
CONFIG_SECRET_DIR = os.path.join(ROOT_DIR, '.config_secret')
CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
CONFIG_SECRET_DEBUG_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_debug.json')
CONFIG_SECRET_DEPLOY_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_deploy.json')
```


#### 주의 run server 명령어 변경됨!!
```
# local developement
python3 manage.py runserver --settings=config.settings.debug
```

## 서버부분 설정하기 !!
aws 아마존 주소
https://aws.amazon.com/
> 회원가입 후 첫화면에서 'ec2' 검색

### AWS EC2 우분투 선택
* instance -> 상단에 Launch instance 클릭
* ubuntu 선택 -> 하단에 launch 버튼 클릭

### 시크릿키 받기
* 키페어를 받고 받은 키를 ssh 폴더로 이동
(로컬 터미널)
```
# (다운받은 폴더에서) mv <key pair name>.pem ~/.ssh

➜  Downloads mv WPS-Lee.pem ~/.ssh
```


### 서버의 가상 컴퓨터 접속하기
* 홈페이지의 instance 선택

* 하단의 주소 확인
Public DNS: ec2-52-79-214-181.ap-northeast-2.compute.amazonaws.com

* 명령어에 유저명을 입력해주고 주소를 붙여넣기 후 실행 (기본 유저명 : ubuntu)
```
명령어: ssh -i ~/.ssh/WPS-Lee.pem
유저명: ubuntu + @
주 소: ec2-52-79-214-181.ap-northeast-2.compute.amazonaws.com
```

* 서버 가상컴퓨터 접속명령어
```
ssh -i ~/.ssh/WPS-Lee.pem ubuntu@ec2-52-79-214-181.ap-northeast-2.compute.amazonaws.com
```

* 권한 설정 변경
(서버 터미널)
```
 ➜  .ssh chmod 400 WPS-Lee.pem
```

* 변경확인
```
/
ls
```

* ubuntu(사용자)로 권한 변경된것 확인
```
...
drwxr-xr-x   2 root   root   4.0K  6월 19 23:52 sbin
drwxr-xr-x   2 root   root   4.0K  4월 29 08:38 snap
drwxr-xr-x   3 ubuntu ubuntu 4.0K  6월 29 06:39 srv
dr-xr-xr-x  13 root   root      0  6월 29 06:35 sys
drwxrwxrwt   8 root   root   4.0K  6월 29 10:48 tmp
drwxr-xr-x  10 root   root   4.0K  6월 19 23:49 usr
drwxr-xr-x  13 root   root   4.0K  6월 19 23:52 var
...
```
### 유저등록 & Access key 등록
* awscli 설치
pip install awscli

https://console.aws.amazon.com/iam/home?region=ap-northeast-2#/home
iam -> user -> add user
```
* 이름 EC2-User 입력후 첫번째 체크 선택
* attach existing policies directly 선택
* ec2 검색
* AmazonEC2FullAccess 체크후 next
* Access key 와 Secret Access Key 확인
```
> Secret Key는 유저 생성시에만 확인가능, 이후로는 확인불가!! 주의 !!

* 명령어 입력
(서버 터미널)
```
aws configure

AWS Access Key ID [None]:
AWS Secret Access Key [None]:
Default region name [None]: ap-northeast-2
Default output format [None]: json
```

### zshrc 단축키 설정 (안해도 무방)
(로컬 터미널) ~/.zshrc
```
# alias - fastcampus wps 5th

# 로컬에서 서버로 접속
alias con-ec2="ssh -i ~/.ssh/WPS-Lee.pem ubuntu@ec2-52-79-214-181.ap-northeast-2.compute.amazonaws.com"

# 로컬에서 서버로 전송
# scp -i <인증서위치> -r <프로젝트폴더> ubuntu@<인스턴스 Public DNS>:/srv/deploy_ec2
alias scp-ec2-ori="scp -i ~/.ssh/WPS-Lee.pem -r /home/leesh/projects/django/deploy_ec2 ubuntu@ec2-52-79-214-181.ap-northeast-2.compute.amazonaws.com:/srv/deploy_ec2"

# 삭제
alias delete-ec2="ssh -i ~/.ssh/WPS-Lee.pem ubuntu@ec2-52-79-214-181.ap-northeast-2.compute.amazonaws.com rm -rf /srv/deploy_ec2"

# 업데이트~? 삭제 재전송
alias scp-ec2="delete-ec2 && scp-ec2-ori"
```

### 서버에 필수프로그램 설치
* 언어팩 설치 (선택사항)
```
sudo apt-get install language-pack-ko
sudo locale-gen ko_KR.UTF-8
```

#### ubuntu 관련
* python-pip 설치
```
sudo apt-get install python-pip
```

* zsh 설치
```
sudo apt-get install zsh
```

* oh-my-zsh 설치
```
sudo curl -L http://install.ohmyz.sh | sh
```

* Default shell 변경
```
sudo chsh ubuntu -s /usr/bin/zsh
```

* pyenv requirements 설치
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
```

* pyenv 설치
```
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

* pyenv 설정 .zshrc 에 기록
```
vi ~/.zshrc
export PATH="/home/ubuntu/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

* pillow 라이브러리 설치
```
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
```

#### Django 관련
* pyenv로 파이썬 설치 및 virtualenv 생성
```
pyenv install 3.6.1
pyenv virtualenv 3.6.1 '가상환경 이름'
pyenv local '가상환경 이름'
```

* requirements 설치
```
pip install -r requirements.txt
```

### 서버의 runserver 외부에서 접속방법
* runserver 주소 변경
>0:8000 << 을 뒤에 적어줘서 외부에서 접근 가능하게

```
./manage.py runserver --settings=config.settings.debug 0:8000
```

* Security group 생성 (ec2) (ip가 고정이 아니라면 매번 접속시마다 바꿔줘야 함!!)
```
* instance ---> 가장 우측에 Security Group 클릭
* Create Security Group 클릭
* 이름과 설명 작성
*inbound -> add Rule
* Type = ssh, source = my ip
* Type = custom TCP, port range = 8000
```

* 새로 설정한 그룹으로 변경
```
instance -> 상단의 actions -> networking -> change Security group
```

## 접속방법
>자신의 Public DNS 주소 + :8000

```
http://ec2-52-79-214-181.ap-northeast-2.compute.amazonaws.com:8000/
```

## 서버가 껏다 켜지면..DNS주소가 변한다 바꿀거 많다

## migrate ... 변경됨 복잡하다

./manage.py makemigrations --settings=config.settings.debug

./manage.py migrate --settings=config.settings.debug

## 메번 입력해주쟈!
>위에처럼 뒤에 복잡한 명령어를 다시 안붙여놔도 된당
>근데 창을 닫으면 초기화... 저장되는 세팅이 아님

```
 export DJNAGO_SETTINGS_MODULE=config.settings.debug
```
