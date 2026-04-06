# [ADP 실기 가이드] Python 3.7 & R 4.1 가상환경 완벽 세팅법 (Miniconda)

ADP 실기 시험장 환경(보통 Python 3.7, R 4.1)과 동일한 환경을 내 컴퓨터에 구축하는 가장 확실한 방법입니다.

---

## 1. 전제 조건
- **Miniconda**가 설치되어 있어야 합니다. (없다면 [Miniconda 홈페이지](https://docs.conda.io/en/latest/miniconda.html)에서 Windows 64-bit용 설치)
- **VS Code**와 **Quarto**가 설치되어 있으면 좋습니다.

---

## 2. 가상환경 구축 단계

### Step 1: 아나콘다 이용 약관 동의
최근 Conda 정책 변경으로 인해 이용 약관 동의가 필요합니다. 터미널(PowerShell)에서 아래 세 줄을 각각 실행하세요.

```powershell
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/msys2
```

### Step 2: ADP 전용 가상환경 생성
Python 3.7과 R 4.1을 동시에 포함하는 독립된 환경을 만듭니다. (약 5~10분 소요)

```powershell
conda create -n adp_env python=3.7 r-base=4.1 r-essentials -c conda-forge -y
```

### Step 3: 가상환경 활성화 및 필수 패키지 설치
활성화 후 시험에 자주 나오는 핵심 패키지들을 미리 설치합니다.

```powershell
# 가상환경 활성화
conda activate adp_env

# Python 핵심 패키지 (버전 명시)
pip install xgboost==0.90 lightgbm==2.2.3 catboost==0.14.0 statsmodels==0.13.2 imbalanced-learn==0.5.0

# R 핵심 패키지
conda install r-tidyverse r-tidymodels r-caret r-randomforest r-xgboost r-desctools r-pmcmrplus r-proc -c conda-forge -y
```

---

## 3. 버전 확인 (신뢰도 체크)
터미널에서 아래 명령어로 버전이 맞는지 최종 확인합니다.

- **Python**: `python --version` -> `Python 3.7.12` 확인
- **R**: `R.exe --version` -> `R version 4.1.3` 확인

---

## 4. Quarto(.qmd)에서 사용하기

새로운 `.qmd` 파일을 만들 때 상단에 아래 설정을 붙여넣으면, 자동으로 우리가 만든 가상환경을 사용하여 R과 Python 코드를 실행합니다.

```yaml
---
title: "분석 주제 입력"
format: html
---

```{r setup, include=FALSE}
library(reticulate)
# adp_env 가상환경 연결
use_condaenv("adp_env", required = TRUE)

# 출력 옵션 (네이버 블로그 복사 최적화)
knitr::opts_chunk$set(
  echo = TRUE,          # 코드 표시
  collapse = FALSE,     # 코드와 결과창 분리
  comment = ""          # 결과창 앞의 ## 기호 제거
)
```


---

## 5. 자주 묻는 질문 (FAQ)

- **가상환경 삭제는 어떻게 하나요?**
  `conda env remove -n adp_env` 명렁어로 깔끔하게 지울 수 있습니다.
- **VS Code를 다시 키면 어떻게 하나요?**
  터미널에 `conda activate adp_env`를 입력하거나, VS Code 하단에서 인터프리터를 `adp_env`로 선택하면 됩니다.

---
> **Tip**: 네이버 블로그에 올리실 때는 Quarto HTML 미리보기 화면을 그대로 드래그하여 복사-붙여넣기 하시면 형식이 가장 잘 유지됩니다!

---
*Created on: 2026-03-18*
