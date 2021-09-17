1. 프로젝트 생성 (https://console.cloud.google.com/apis/dashboard)
2. API 및 서비스 사용 설정을 선택
3. Cloud Speech-to-Text API를 검색하여 선택 및 사용
4. 사용자 인증 정보 (서비스 계정)
5. 서비스 계정 선택 및 서비스 계정 만들기 
6. 계정 이름 적당히 부여 후 만들기 (역할 : 소유자)
7. 키 만들기(json)
8. json 파일 적당한 위치에 놓고 환경 변수 등록 (변수이름 : GOOGLE_APPLICATION_CREDENTIALS,  변수값 : json 파일 경로 + 파일이름까지)

9. cloud sdk 설치 (https://cloud.google.com/sdk/docs/downloads-versioned-archives)
10. C:\에 압축 풀기  (풀면 C:\google-cloud-sdk 가 됨)
11. 클라우드 도구 경로 추가 (C:\google-cloud-sdk\install.bat)
12. C:\google-cloud-sdk\bin\gcloud init   (기존 설정 지우려면 C:\Users\사용자명\AppData\Roaming\gcloud 날림)
13. 명령 프롬프트에서 Cloud Speech API를 위해 만든 프로젝트 번호 선택

14. 파이썬 설치 (https://www.python.org/downloads/windows/)
15. virtualenv 설치 (pip install virtualenv) (pip install virutalenvwrapper-win)
16. 가상환경 디렉토리 생성 후 이동 (mkdir speech / cd speech)
17. 가상환경 만듬 (virtualenv env)
18. 활성화 (.\env\Scripts\activate)  -> 빠져나오려면 deactivate 타이핑
19. 가상환경 내에서 cloud client library for python 설치  (pip install --upgrade google-cloud-storage)
20. (옵션) visual studio 설치 (http://landinghub.visualstudio.com/visual-cpp-build-tools)
21. Cloud speech API Client Library 설치 (pip install google-cloud-speech)
22. 서비스 계정 활성화 ( c:\google-cloud-sdk\bin\gcloud auth activate-service-account --key-file="json경로및파일명")
23. 마이크 사용 위한 패키지 설치 (https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio  에서 파이썬 버전에 맞게)
24. 받은 패키지 설치 (pip install 파일명)

25. (옵션) https://github.com/googleapis/python-speech/blob/master/samples/microphone/transcribe_streaming_mic.py 실행하여 음성 테스트
    -> 코드 내 , en-US 를 ko-KR 로 변경 가능.

26. (옵션) https://gist.github.com/mabdrabo/8678538  실행하여 녹음을 하면 file.wav 생성됨

27. (옵션) quickstart.py (내 github - repo:google에 업로드)실행하여 file.wav를 텍스트로 추출해 봄. 

28. (옵션) 추가 예제 : https://github.com/googleapis/python-speech/tree/master/samples

29. https://console.cloud.google.com/ 에서 버킷 생성 및 파일 업로드

30. wav 변환 시,  mono 에 8000 으로 함  

31. 내 github - repo:google 에서 speech.py 다운로드 받고 적절하게 수정 및 실행.
