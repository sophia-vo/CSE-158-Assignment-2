# NHANES 2021-2023 Dataset Documentation

## Overview

This dataset is a subset of the **National Health and Nutrition Examination Survey (NHANES) 2021-2023**. It specifically targets individuals aged **18 and older** and combines data from six distinct modules: Demographics, Sleep, Physical Activity, Mental Health, Alcohol Use, and Occupation.

**Data Source:** [CDC National Center for Health Statistics](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2021-2023)

---

## 1. Demographics (DEMO_L)

**Source File:** [`DEMO_L.xpt`]([https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.htm](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.htm))

The demographics file provides individual-level characteristics including gender, age, race/ethnicity, and socioeconomic indicators.

| Variable Name | Description | Values / Coding Key |
| :--- | :--- | :--- |
| **SEQN** | **Respondent Sequence Number** | Unique identifier used to join all tables. |
| **RIAGENDR** | **Gender** | `1` = Male<br>`2` = Female |
| **RIDAGEYR** | **Age in years at screening** | `18` to `79` = Age in years<br>`80` = 80 years or older (Top-coded) |
| **RIDRETH3** | **Race/Hispanic origin** | `1` = Mexican American<br>`2` = Other Hispanic<br>`3` = Non-Hispanic White<br>`4` = Non-Hispanic Black<br>`6` = Non-Hispanic Asian<br>`7` = Other Race - Including Multi-Racial |
| **DMDHHSIZ** | **Total number of people in the Household** | `1` to `6` = Exact count<br>`7` = 7 or more people |
| **INDFMPIR** | **Ratio of family income to poverty** | `0.00` to `4.99` = Exact ratio<br>`5.00` = Ratio is 5.00 or more<br>*(Note: A ratio < 1.00 indicates income below the poverty line)* |

---

## 2. Sleep Disorders (SLQ_L)

**Source File:** [`SLQ_L.xpt`]([https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/SLQ_L.htm](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/SLQ_L.htm))

Measures the participant's self-reported sleep habits on weekdays and weekends.

| Variable Name | Description | Values / Coding Key |
| :--- | :--- | :--- |
| **SLD012** | **Sleep hours - weekdays or workdays** | `2` to `24` = Hours of sleep<br>`77` = Refused<br>`99` = Don't know |
| **SLD013** | **Sleep hours - weekends** | `2` to `24` = Hours of sleep<br>`77` = Refused<br>`99` = Don't know |

---

## 3. Physical Activity (PAQ_L)

**Source File:** [`PAQ_L.xpt`]([https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/PAQ_L.htm](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/PAQ_L.htm))

Focuses on "Leisure Time Physical Activity" (LTPA). Moderate activity causes small increases in breathing/heart rate; vigorous causes large increases.

| Variable Name | Description | Values / Coding Key |
| :--- | :--- | :--- |
| **PAD800** | **Minutes moderate LTPA** | `10` to `9999` = Minutes per day (on days activity is done)<br>`7777` = Refused<br>`9999` = Don't know |
| **PAD820** | **Minutes vigorous LTPA** | `10` to `9999` = Minutes per day (on days activity is done)<br>`7777` = Refused<br>`9999` = Don't know |

---

## 4. Mental Health - Depression Screener (DPQ_L)

**Source File:** [`DPQ_L.xpt`]([https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DPQ_L.htm](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DPQ_L.htm))

Based on the PHQ-9 (Patient Health Questionnaire). Participants are asked how often they have been bothered by problems over the **last 2 weeks**.

| Variable Name | Description | Values / Coding Key |
| :--- | :--- | :--- |
| **DPQ020** | **Feeling down, depressed, or hopeless** | `0` = Not at all<br>`1` = Several days<br>`2` = More than half the days<br>`3` = Nearly every day |
| **DPQ050** | **Poor appetite or overeating** | `0` = Not at all<br>`1` = Several days<br>`2` = More than half the days<br>`3` = Nearly every day |

*Note: `7` (Refused) and `9` (Don't know) are possible for all DPQ questions.*

---

## 5. Alcohol Use (ALQ_L)

**Source File:** [`ALQ_L.xpt`]([https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/ALQ_L.htm](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/ALQ_L.htm))

Determines lifetime alcohol consumption status.

| Variable Name | Description | Values / Coding Key |
| :--- | :--- | :--- |
| **ALQ111** | **Ever had a drink of any kind of alcohol** | `1` = Yes<br>`2` = No<br>`7` = Refused<br>`9` = Don't know |

---

## 6. Occupation (OCQ_L)

**Source File:** [`OCQ_L.xpt`]([https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/OCQ_L.htm](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/OCQ_L.htm))

Assesses employment status during the week prior to the interview.

| Variable Name | Description | Values / Coding Key |
| :--- | :--- | :--- |
| **OCD150** | **Type of work done last week** | `1` = Working at a job or business<br>`2` = With a job or business but not at work (e.g., sick leave, vacation)<br>`3` = Looking for work<br>`4` = Not working at a job or business<br>`7` = Refused<br>`9` = Don't know |

---

## Data Cleaning Notes (Applied to Dataset)

In the provided `data.csv`, the following transformations were applied to the raw variables listed above:

1.  **Filtering:** Only respondents aged 18+ (`RIDAGEYR >= 18`) were included.
2.  **Inner Join:** Only respondents (`SEQN`) present in **all** six data files were retained.
3.  **Renaming:** Columns were renamed for readability (e.g., `RIAGENDR` $\rightarrow$ `Gender`).
4.  **Value Mapping:** Numeric codes (e.g., `1.0` for Gender) were mapped to their string descriptions (e.g., `"Male"`).
5.  **Calculated Fields:** `Avg_Sleep` is a derived metric calculated as a weighted average of weekday and weekend sleep.
