from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# PATH = "https://dena.snar.jp/index.aspx"
# PATH = "https://safie-recruit.snar.jp/"
# PATH = "https://moneyforward-recruit.snar.jp/index.aspx"
# PATH = "https://linecorp.snar.jp/"
# PATH = "https://gree-recruit.snar.jp/"
# PATH = "https://job.axol.jp/jn/s/kddi_24/entry/agreement"
PATH = "https://mypage.3050.i-webs.jp/sumika2024/applicant/entry/index/entrycd/"

driver.get(PATH)

JOB_TYPE_SNAR_JP = "rpt_GroupItem_lkb_Apply_0"

INFO = {
    "NAME": "高橋 はな",
    "FURIGANA": "タカハシ ハナ",
    "GENDER": "female",
    "EMAIL": "example.japan@gmail.com",
    "SUB_EMAIL": "example.japan2@gmail.com",
    "MOBILE": "010-1234-5678",
    "BIRTH_DAY": "2000/01/15",
    "GRADUATION_DAY": "2024/09",
    "GRADUATED": False,
    "LAB": "国際経済学ゼミ",
    "CLUB": "オリエンテーリング",
    "ZIP": "100-0001",
    "PREFECTURE": "東京都",
    "ADDRESS": "千代田区千代田1-1",
    "APARTMENT": "日本アパート201号",
    "SAME_ADDRESS": True,
}


def snar_jp(job_id: str) -> None:
    driver.find_element(By.ID, job_id).click()
    driver.find_element(By.ID, "lkb_Agree").click()
    driver.implicitly_wait(0.5)

    driver.find_element(By.ID, "tbx_name1").send_keys(INFO["NAME"].split(' ')[0])
    driver.find_element(By.ID, "tbx_name2").send_keys(INFO["NAME"].split(' ')[1])
    driver.find_element(By.ID, "tbx_kana1").send_keys(INFO["FURIGANA"].split(' ')[0])
    driver.find_element(By.ID, "tbx_kana2").send_keys(INFO["FURIGANA"].split(' ')[1])
    driver.find_element(By.ID, "tbx_mail").send_keys(INFO["EMAIL"])
    driver.find_element(By.ID, "tbx_mail_R").send_keys(INFO["EMAIL"])

    try:
        driver.find_element(By.ID, "tbx_smail").send_keys(INFO["SUB_EMAIL"])
        driver.find_element(By.ID, "tbx_smail_R").send_keys(INFO["SUB_EMAIL"])
    except NoSuchElementException:
        pass

    yyyy = driver.find_element(By.ID, "ddl_birthY")
    Select(yyyy).select_by_visible_text(INFO["BIRTH_DAY"].split('/')[0])
    mm = driver.find_element(By.ID, "ddl_birthM")
    try:
        Select(mm).select_by_visible_text(INFO["BIRTH_DAY"].split('/')[1])
    except NoSuchElementException:
        Select(mm).select_by_visible_text(INFO["BIRTH_DAY"].split('/')[1][1])
    dd = driver.find_element(By.ID, "ddl_birthD")
    try:
        Select(dd).select_by_visible_text(INFO["BIRTH_DAY"].split('/')[2])
    except NoSuchElementException:
        Select(dd).select_by_visible_text(INFO["BIRTH_DAY"].split('/')[2][1])

    yyyy_university = driver.find_element(By.ID, "ddl_sotsuyY")
    Select(yyyy_university).select_by_visible_text(INFO["GRADUATION_DAY"].split('/')[0])

    mm_university = driver.find_element(By.ID, "ddl_sotsuyM")
    try:
        Select(mm_university).select_by_visible_text(INFO["GRADUATION_DAY"].split('/')[1])
    except NoSuchElementException:
        Select(mm_university).select_by_visible_text(INFO["GRADUATION_DAY"].split('/')[1][1])

    graduation_status = driver.find_element(By.ID, "ddl_sotsuk")
    if INFO["GRADUATED"]:
        Select(graduation_status).select_by_visible_text("既卒")
    else:
        Select(graduation_status).select_by_visible_text("卒業予定")

    try:
        driver.find_element(By.ID, "tbx_keitai1").send_keys(INFO["MOBILE"].split('-')[0])
        driver.find_element(By.ID, "tbx_keitai2").send_keys(INFO["MOBILE"].split('-')[1])
        driver.find_element(By.ID, "tbx_keitai3").send_keys(INFO["MOBILE"].split('-')[2])
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, "tbx_tel11").send_keys(INFO["MOBILE"].split('-')[0])
        driver.find_element(By.ID, "tbx_tel12").send_keys(INFO["MOBILE"].split('-')[1])
        driver.find_element(By.ID, "tbx_tel13").send_keys(INFO["MOBILE"].split('-')[2])
    except NoSuchElementException:
        pass

    try:
        if INFO["GENDER"] == "male":
            gender = driver.find_element(By.ID, "rbt_sex1")
            driver.execute_script("arguments[0].click();", gender)
        elif INFO["GENDER"] == "female":
            gender = driver.find_element(By.ID, "rbt_sex2")
            driver.execute_script("arguments[0].click();", gender)
        else:
            gender = driver.find_element(By.ID, "rbt_sex3")
            driver.execute_script("arguments[0].click();", gender)
    except NoSuchElementException:
        pass

    try:
        driver.find_element(By.ID, "tbx_zip1").send_keys(INFO["ZIP"].split('-')[0])
        driver.find_element(By.ID, "tbx_zip2").send_keys(INFO["ZIP"].split('-')[1])
        prefecture = driver.find_element(By.ID, "ddl_ken")
        Select(prefecture).select_by_visible_text(INFO["PREFECTURE"])
        driver.find_element(By.ID, "tbx_addr1").send_keys(INFO["ADDRESS"])
        driver.find_element(By.ID, "tbx_addr2").send_keys(INFO["APARTMENT"])

        if INFO["SAME_ADDRESS"]:
            try:
                same_address = driver.find_element(By.ID, "cbx_kflg")
                driver.execute_script("arguments[0].click();", same_address)
            except NoSuchElementException:
                pass
    except NoSuchElementException:
        pass


def i_webs_jp() -> None:
    driver.find_element(By.ID, "first_access").click()
    driver.find_element(By.CSS_SELECTOR, ".btn_right130 a").click()
    driver.find_element(By.NAME, "kname1").send_keys(INFO["NAME"].split(' ')[0])
    driver.find_element(By.NAME, "kname2").send_keys(INFO["NAME"].split(' ')[1])
    driver.find_element(By.NAME, "yname1").send_keys(INFO["FURIGANA"].split(' ')[0])
    driver.find_element(By.NAME, "yname2").send_keys(INFO["FURIGANA"].split(' ')[1])


def axol_jp() -> None:
    driver.find_element(By.ID, "submit").click()
    driver.find_element(By.NAME, "kanji_sei").send_keys(INFO["NAME"].split(' ')[0])
    driver.find_element(By.NAME, "kanji_na").send_keys(INFO["NAME"].split(' ')[1])
    driver.find_element(By.NAME, "kana_sei").send_keys(INFO["FURIGANA"].split(' ')[0])
    driver.find_element(By.NAME, "kana_na").send_keys(INFO["FURIGANA"].split(' ')[1])

    driver.find_element(By.NAME, "yubing_h").send_keys(INFO["ZIP"].split('-')[0])
    driver.find_element(By.NAME, "yubing_l").send_keys(INFO["ZIP"].split('-')[1])


if __name__ == '__main__':
    if "snar.jp" in PATH:
        snar_jp(JOB_TYPE_SNAR_JP)
    elif "i-webs.jp" in PATH:
        i_webs_jp()
    elif "axol.jp" in PATH:
        axol_jp()
    else:
        print("Website not yet supported.")

    on_hold = input("Enter anything on the console to exit.")
