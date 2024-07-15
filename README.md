# bootcamp
Ai developer in boostcourse + coding test
1. Miniconda3 설치, 이유: 아나콘다는 너무 많은 기능 사용하고 파이썬은 수학/공학 계산용 모델 없음 (인터프리터)
2. IDE 설치 하나. VScode 설치, 둘. 주피터 노트북 다운로드 (cmd 환경에서 실행) 
   * 주피터 노트북은 구글 코랩과 동일하지만, locallhost8080에서 돌아간다. 
3. 실행환경 세팅 (Cmder설치 => 환경변수 설정, >conda activate base >python : 권장)
   * Cmder는 윈도우 cmd 환경에서 리눅스 명령어, 윈도우 명령어 전부 가능함 ex: Vim, DIR, ls ..
4. VScdoe 실행 > code .
5. CLI 환경 Git hub 연동
    * git clone https://github.com/yourid/yourreopsitory.git
    * 깃허브, Develope Setting > Personal accesss tokens (classic) 발급
    * git status
    * git config --global user.name "Yourname" 등록
    * git config --global user.email "YourEmail" 등록
    * git config --global credential.helper store 등록
    * git add . (변경내용을 추가 for commit)
    * git commit -m "Your Message" (커밋)
    * git push || git pull (푸쉬 또는 풀)
6. 굳이 conda activate base를 실행하는 이유
   * CMD에서 Python 실행: 시스템 전역의 Python과 패키지를 사용. 환경 격리가 없고, 패키지 버전 충돌 가능성.
   * conda activate base 후 Python 실행: Conda 환경을 사용하여 환경 격리와 독립적인 패키지 관리를 제공. 패키지 버전 충돌 방지.
