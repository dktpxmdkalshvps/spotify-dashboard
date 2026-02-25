# 🎵 Spotify 자아 성찰 대시보드

> **"내가 어떤 음악을 듣는지 데이터로 들여다보는 개인 분석 도구"**  
> Spotify 청취 기록을 실시간으로 수집하고, 나의 음악 취향과 감정 패턴을 시각화합니다.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Spotify](https://img.shields.io/badge/Spotify_API-Web_API-1DB954?style=flat-square&logo=spotify&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=flat-square&logo=plotly&logoColor=white)

---

## 📌 목차

1. [프로젝트 목적](#1-프로젝트-목적)
2. [기술 스택](#2-기술-스택)
3. [핵심 기능](#3-핵심-기능)
4. [프로젝트 구조](#4-프로젝트-구조)
5. [설치 및 실행 방법](#5-설치-및-실행-방법)
6. [스크린샷](#6-스크린샷)
7. [주의사항 및 API 제한](#7-주의사항-및-api-제한)
8. [향후 개선 계획](#8-향후-개선-계획)

---

## 1. 프로젝트 목적

우리는 매일 음악을 듣지만, 정작 **"내가 어떤 음악을 언제, 얼마나 듣는지"** 를 정확히 알고 있는 사람은 많지 않습니다.

이 프로젝트는 **Spotify Web API** 를 통해 사용자의 청취 데이터를 실시간으로 수집하고, 데이터 분석 라이브러리를 활용해 개인의 음악적 취향을 다각도로 분석합니다.

단순히 음악을 듣는 경험을 넘어, 자신의 청취 패턴과 선호도를 수치화된 데이터로 확인하는 **'데이터 기반의 자아 성찰'** 도구를 지향합니다.

| 지향점 | 설명 |
|--------|------|
| 🔍 **데이터 기반 자기 이해** | 청취 패턴을 통해 나의 시간대별 음악 취향 파악 |
| 📊 **직관적 시각화** | 숫자가 아닌 차트로 한눈에 확인하는 취향 분석 |
| ⚡ **실시간 반영** | 60초마다 자동 갱신되는 라이브 대시보드 |
| 🛡 **안전한 인증 관리** | `.env` 기반으로 API 키를 코드에서 완전 분리 |

---

## 2. 기술 스택

| 단계 | 기술 / 라이브러리 | 버전 | 주요 역할 |
|------|------------------|------|-----------|
| **Data Extraction** | `spotipy` | 2.x | Spotify Web API 래퍼. OAuth 인증 및 최근 재생 기록 수집 |
| **Environment** | `python-dotenv` | 1.x | `Client ID`, `Secret` 등 민감 정보를 `.env`로 분리 관리 |
| **Data Processing** | `pandas` | 2.x | JSON → DataFrame 변환, 시간대·인기도 파생 컬럼 생성 |
| **Visualization** | `plotly` | 5.x | 인터랙티브 바 차트, 도넛 차트, 히스토그램 구현 |
| **Web Service** | `streamlit` | 1.x | 별도 서버 없이 Python 코드만으로 웹 대시보드 구동 |

---

## 3. 핵심 기능

### 3-1. 실시간 데이터 수집
Spotify `recently_played` 엔드포인트를 호출하여 최근 50곡의 재생 기록을 수집합니다. `@st.cache_data(ttl=60)` 데코레이터를 통해 **60초 단위로 자동 갱신**되며, 수동 새로고침 버튼도 제공합니다.

```
사용자 Spotify 계정
    └─ recently_played API 호출 (최근 50곡)
         └─ JSON 파싱 → Pandas DataFrame
              └─ 파생 컬럼 생성 (시간대, 인기도 티어)
                   └─ Streamlit 대시보드 렌더링
```

### 3-2. KPI 요약 카드
대시보드 상단에 핵심 지표 5개를 카드 형태로 표시합니다.

| 지표 | 설명 |
|------|------|
| 🎵 총 재생 수 | 수집된 전체 트랙 수 |
| 🎤 고유 아티스트 | 중복 제거 후 아티스트 수 |
| 💿 고유 트랙 | 중복 제거 후 트랙 수 |
| ⭐ 평균 인기도 | 트랙 인기도(0~100) 평균 |
| ⏱ 평균 재생시간 | 분 단위 평균 트랙 길이 |

### 3-3. 아티스트 Top 10 바 차트
가장 많이 재생한 아티스트를 수평 바 차트로 시각화합니다. 인터랙티브 호버 기능으로 정확한 재생 횟수를 확인할 수 있습니다.

### 3-4. 인기도 티어 도넛 차트
트랙 인기도(0~100)를 3개 구간으로 분류합니다.

| 티어 | 기준 | 의미 |
|------|------|------|
| 🔥 메가히트 | 70점 이상 | 차트 상위권 인기곡 |
| 🎵 일반곡 | 40~69점 | 대중적으로 알려진 곡 |
| 💎 언더레이티드 | 39점 이하 | 숨겨진 명곡, 비주류 아티스트 |

### 3-5. 시간대별 청취 패턴 바 차트
재생 시각(0~23시)을 기준으로 언제 음악을 가장 많이 듣는지 시각화합니다. 나의 음악 청취 루틴(출퇴근, 새벽 감성 등)을 발견할 수 있습니다.

### 3-6. 트랙 인기도 히스토그램
재생한 곡들의 인기도 분포를 히스토그램으로 표시합니다. 분포가 왼쪽에 몰릴수록 비주류 취향, 오른쪽에 몰릴수록 대중적 취향입니다.

### 3-7. 시간대별 청취 비중 (오전/오후/저녁/새벽)
4개 시간대로 묶어 어느 시간대에 음악을 가장 많이 듣는지 한눈에 파악합니다.

### 3-8. 최근 재생 목록 테이블
재생 시각, 곡명, 아티스트, 인기도, 시간대, 인기도 티어를 표 형태로 제공합니다. 접기/펼치기 `expander` UI로 화면을 효율적으로 사용합니다.

---

## 4. 프로젝트 구조

```
spotify-dashboard/
│
├── .env                    # 🔐 인증 정보 (Git 제외 필수)
├── .gitignore              # .env, .cache 등 제외 설정
├── .cache                  # OAuth 토큰 캐시 (자동 생성)
├── requirements.txt        # 패키지 의존성
├── app.py                  # 🚀 Streamlit 진입점 및 UI 조합
│
└── src/
    ├── auth.py             # OAuth 인증 클라이언트 생성
    ├── fetcher.py          # Spotify API 데이터 수집
    ├── processor.py        # ETL 처리 및 파생 컬럼 생성
    └── visualizer.py       # Plotly 차트 함수 모음
```

**설계 원칙:** `app.py`는 UI 조합만 담당하고 모든 비즈니스 로직은 `src/` 하위 모듈로 분리하여, Streamlit을 다른 프레임워크로 교체해도 `src/`를 재사용할 수 있도록 설계했습니다.

---

## 5. 설치 및 실행 방법

### Step 1 — Spotify Developer 앱 등록

1. [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) 접속
2. **Create App** 클릭
3. Redirect URI를 `http://localhost:8501` 로 설정
4. 발급된 `Client ID`와 `Client Secret` 복사
5. **Settings → User Management** 에서 본인 Spotify 이메일 추가 (**필수**)

> ⚠️ Development Mode 앱은 등록된 이메일만 API 사용 가능합니다.

### Step 2 — 저장소 클론 및 환경 구성

```bash
# 저장소 클론
git clone https://github.com/your-username/spotify-dashboard.git
cd spotify-dashboard

# 가상환경 생성 (권장)
conda create -n spotify python=3.10
conda activate spotify
# 또는
python -m venv venv && source venv/bin/activate  # macOS/Linux
python -m venv venv && venv\Scripts\activate     # Windows
```

### Step 3 — 패키지 설치

```bash
pip install -r requirements.txt
```

`requirements.txt` 내용:
```
spotipy>=2.23.0
python-dotenv>=1.0.0
pandas>=2.0.0
numpy>=1.24.0
plotly>=5.0.0
streamlit>=1.30.0
```

### Step 4 — 환경 변수 설정

프로젝트 루트에 `.env` 파일 생성:

```env
SPOTIPY_CLIENT_ID=여기에_클라이언트_ID_입력
SPOTIPY_CLIENT_SECRET=여기에_클라이언트_시크릿_입력
SPOTIPY_REDIRECT_URI=http://localhost:8501
```

### Step 5 — 실행

```bash
streamlit run app.py
```

브라우저에서 `http://localhost:8501` 자동 오픈 → **Spotify 로그인 팝업 → 승인** → 대시보드 표시

> 첫 실행 시 `.cache` 파일이 생성되며 이후 자동 로그인됩니다.  
> 토큰 오류 발생 시 `.cache` 파일 삭제 후 재실행하세요.

---

## 6. 스크린샷

> 아래 스크린샷은 실제 실행 화면 예시입니다.

### 메인 대시보드 — KPI 카드 및 상단 차트

```
┌─────────────────────────────────────────────────────────────────┐
│  🎵 나의 음악 취향 분석 대시보드                                  │
│  Spotify 청취 데이터 기반 실시간 자아 성찰 도구                   │
├──────────┬──────────┬──────────┬──────────┬────────────────────┤
│🎵 총재생  │🎤 고유   │💿 고유   │⭐ 평균   │⏱ 평균             │
│   50     │ 아티스트  │  트랙    │ 인기도   │ 재생시간           │
│          │   23     │   47     │  61.4    │  3.42분            │
├──────────┴──────────┴──────────┴──────────┴────────────────────┤
│  🎤 많이 들은 아티스트 Top 10   │  💎 인기도 티어 분포           │
│  ██████████ NewJeans  18       │      🔥메가히트  45%           │
│  ████████   IU        14       │      🎵일반곡    38%           │
│  ██████     BTS        9       │      💎언더레이  17%           │
├─────────────────────────────────┴───────────────────────────────┤
│  🕐 시간대별 청취 패턴          │  📊 트랙 인기도 분포           │
│  ▄▄██████▄▄▄▃▃▄▅▅▄▄▃▂▁▁       │  ▁▂▃▅██▇▄▂▁ (분포 히스토그램) │
└─────────────────────────────────────────────────────────────────┘
```

### 시간대 비중 차트

```
⏰ 시간대별 청취 비중

  🌅 오전  ████████████  28%
  ☀️ 오후  ██████████    22%
  🌆 저녁  ████████████████  36%
  🌙 새벽  ██████  14%
```

### 최근 재생 목록 (expander)

```
📋 최근 재생 목록 전체 보기  ▼

  played_at          track_name        artist    popularity  time_slot  pop_tier
  2024-01-15 23:41   Hype Boy          NewJeans  85          🌙 새벽     🔥 메가히트
  2024-01-15 23:38   LILAC             IU        79          🌙 새벽     🔥 메가히트
  2024-01-15 22:10   Rainy Days        V          71          🌆 저녁     🔥 메가히트
  ...
```

---

## 7. 주의사항 및 API 제한

### Spotify API 정책 변경 (2024년 11월~)
Spotify는 2024년 11월부터 `audio-features`, `audio-analysis` 엔드포인트를 **Extended Quota Mode** 승인 앱에서만 허용합니다. 본 프로젝트는 이 제한을 우회하여 `recently_played` 응답 내 기본 메타데이터만 사용합니다.

| 엔드포인트 | 상태 | 비고 |
|-----------|------|------|
| `recently_played` | ✅ 사용 가능 | 핵심 데이터 소스 |
| `audio-features` | ❌ 제한됨 | Extended Quota 필요 |
| `artists` (장르 정보) | ⚠️ Development Mode 제한 | 이메일 등록 시 사용 가능 |

### `.gitignore` 필수 항목

```gitignore
.env
.cache
__pycache__/
*.pyc
.venv/
```

---

## 8. 향후 개선 계획

- [ ] **장르 TOP 5 차트** — Dashboard 이메일 등록 후 `sp.artists()` 재활성화
- [ ] **주간/월간 트렌드** — 청취 데이터 로컬 DB(SQLite) 누적 저장
- [ ] **아티스트 클러스터링** — KMeans 기반 취향 군집 분석
- [ ] **Streamlit Community Cloud 배포** — 무료 퍼블릭 URL 공유
- [ ] **Extended Quota Mode 신청** — `audio-features` 기반 Valence × Energy 감정 지도 복원
