# spotify-dashboard

```markdown
# 🎵 Spotify DashBoard Project

Spotify API를 활용하여 실시간으로 계정 데이터를 분석하고 시각화하는 웹 대시보드 프로젝트입니다.

## 🛠 주요 기능
- **인증(Auth)**: Spotify API 연동을 위한 OAuth 2.0 인증 처리
- **데이터 수집(Fetcher)**: 사용자의 재생 목록 및 트랙 정보 추출
- **데이터 처리(Processor)**: 수집된 데이터의 가공 및 분석
- **시각화(Visualizer)**: 분석된 데이터를 차트 등으로 시각화
- **웹 인터페이스**: `app.py`를 통한 대시보드 실행

## 📂 폴더 구조
```text
.
├── src/
│   ├── auth.py        # API 인증 관련 로직
│   ├── fetcher.py     # 데이터 크롤링 및 수집
│   ├── processor.py   # 데이터 전처리 및 분석
│   └── visualizer.py  # 결과물 시각화
├── .env               # 환경 변수 (API 키 등)
├── app.py             # 메인 실행 파일
└── README.md

```

## 🚀 시작하기

### 1. 환경 설정

프로젝트 실행을 위해 **`.env`** 파일에 Spotify API 키 정보를 반드시 입력해야 합니다. 루트 폴더에 `.env` 파일을 생성하고 아래 형식을 맞춰주세요.

```env
SPOTIPY_CLIENT_ID='사용자의_클라이언트_ID'
SPOTIPY_CLIENT_SECRET='사용자의_클라이언트_시크릿'
SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

```

### 2. 패키지 설치

```bash
pip install spotipy flask pandas  # 필요에 따라 수정

```

### 3. 실행

```bash
python app.py

```

## ⚠️ 주의사항

보안을 위해 `.env` 파일은 절대 깃허브(GitHub) 등 공용 저장소에 업로드하지 마세요. (현재 `.gitignore` 처리가 되어 있습니다.)

```

---

### 💡 작성 팁
* **파일 내용 수정**: 실제 사용 중인 라이브러리(예: Flask, Streamlit 등)에 따라 **패키지 설치** 부분을 조금씩 수정해 주세요.
* **GitHub 업로드**: 이 파일을 저장한 후 다시 한번 `git add README.md`, `git commit -m "Add README.md"`, `git push`를 실행하면 깃허브 메인 페이지에 예쁘게 출력됩니다.

```
