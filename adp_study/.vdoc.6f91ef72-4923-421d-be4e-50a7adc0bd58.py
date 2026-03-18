# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import pandas as pd
import scipy.stats as stats

# 1. GitHub Raw URL에서 데이터 불러오기
# (본인의 GitHub에 파일을 올린 후 Raw 주소로 교체하세요!)
url = "https://github.com/MOON001208/ADP-data-set-and-analysis/tree/main/adp_study/data/coffee_one_sample.csv"
df = pd.read_csv(url)

# 2. 정규성 검정 (Shapiro-Wilk)
stat, p_val = stats.shapiro(df['volume'])
print(f"[정규성 검정] p-value: {p_val:.4f}") 

# 3. 단일 표본 t-검정
stat, p_val = stats.ttest_1samp(df['volume'], popmean=300)
print(f"[단일표본 t-검정] p-value: {p_val:.4f}")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import pandas as pd
import scipy.stats as stats

# 1. 데이터 불러오기
url = "https://raw.githubusercontent.com/MOON001208/ADP-data-set-and-analysis/main/data/school_scores_independent.csv"
df = pd.read_csv(url)

# 그룹별 데이터 분리
score_m = df[df['group'] == 'M']['score']
score_f = df[df['group'] == 'F']['score']

# 2. 정규성 검정
print("남학생 정규성 p: ", stats.shapiro(score_m).pvalue)
print("여학생 정규성 p: ", stats.shapiro(score_f).pvalue)

# 3. 등분산성 검정 (Levene/Bartlett) 
stat, levene_p = stats.levene(score_m, score_f)
print(f"[등분산성 검정] p-value: {levene_p:.4f}")

# 4. 독립 표본 t-검정 
t_stat, t_pval = stats.ttest_ind(score_m, score_f, equal_var=True)
print(f"[독립표본 t-검정] p-value: {t_pval:.4f}")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import pandas as pd
import scipy.stats as stats

# 1. 데이터 불러오기
url = "https://raw.githubusercontent.com/MOON001208/ADP-data-set-and-analysis/main/data/blood_pressure_paired.csv"
df = pd.read_csv(url)

# 차이값 정규성 검정 (after - before)
df['diff'] = df['after'] - df['before']
stat, p_val = stats.shapiro(df['diff'])
print(f"[차이값 정규성 검정] p-value: {p_val:.4f}")

# 2. 대응 표본 t-검정 (단측 검정: less)
t_stat, t_pval = stats.ttest_rel(df['after'], df['before'], alternative='less')
print(f"[대응표본 t-검정] p-value: {t_pval:.4f}")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
