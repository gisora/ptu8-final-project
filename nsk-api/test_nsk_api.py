import unittest
import requests
import json

# API url adresas
REQUEST_URL = "https://nsk-api-2plmfoaoua-lz.a.run.app/api/predict"

# perduodamas request body, dict žodynas
REQUEST_BODY = {"abstract": "The Attempted Suicide Short Intervention Program (ASSIP) was adapted for hospital delivery and to address substance use problems as well as evaluated for feasibility, acceptability, and therapist fidelity in a series of preparatory steps (n = 28) and in a pilot randomized controlled trial, RCT (n = 34). In the RCT, patients with suicide attempts and substance use problem(s) with sufficient lengths of stay to deliver three ASSIP therapy sessions in hospital were randomized to adapted ASSIP or treatment as usual control. A blinded assessor identified suicide reattempts over 6-month follow-up with the Columbia-Suicide Severity Rating Scale (C-SSRS) and a comprehensive multi-source method. Treatment process measures and the Scale for Suicidal Ideation (SSI) were also administered.Median hospital stay was 13 days. ASSIP subjects reported high satisfaction with the treatment and high therapeutic alliance. Study therapists showed high fidelity to the modified ASSIP intervention. Repetition of suicide attempt was common in both study groups including a combined 9 (26%) subjects with reattempt based on C-SSRS and 13 (38%) subjects with reattempt based on multiple sources. Adult suicide attempt patients with substance use problems who require lengthy hospitalizations are at exceptionally high risk and may require additional strategies to lower risk."}

# tikimas gauti response teksas
RESPONSE_TEXT = '[{"line_number":0,"class":"OBJECTIVE","text":"The Attempted Suicide Short Intervention Program (ASSIP) was adapted for hospital delivery and to address substance use problems as well as evaluated for feasibility, acceptability, and therapist fidelity in a series of preparatory steps (n = 28) and in a pilot randomized controlled trial, RCT (n = 34)."},{"line_number":1,"class":"METHODS","text":"In the RCT, patients with suicide attempts and substance use problem(s) with sufficient lengths of stay to deliver three ASSIP therapy sessions in hospital were randomized to adapted ASSIP or treatment as usual control."},{"line_number":2,"class":"METHODS","text":"A blinded assessor identified suicide reattempts over 6-month follow-up with the Columbia-Suicide Severity Rating Scale (C-SSRS) and a comprehensive multi-source method."},{"line_number":3,"class":"METHODS","text":"Treatment process measures and the Scale for Suicidal Ideation (SSI) were also administered.Median hospital stay was 13 days."},{"line_number":4,"class":"RESULTS","text":"ASSIP subjects reported high satisfaction with the treatment and high therapeutic alliance."},{"line_number":5,"class":"RESULTS","text":"Study therapists showed high fidelity to the modified ASSIP intervention."},{"line_number":6,"class":"RESULTS","text":"Repetition of suicide attempt was common in both study groups including a combined 9 (26%) subjects with reattempt based on C-SSRS and 13 (38%) subjects with reattempt based on multiple sources."},{"line_number":7,"class":"CONCLUSIONS","text":"Adult suicide attempt patients with substance use problems who require lengthy hospitalizations are at exceptionally high risk and may require additional strategies to lower risk."}]'

# tikimas gauti response sąrašo dydis, 8 - sakiniai
RESPONSE_LIST_LEN = 8

# kiekvieno sakinio žodyno raktai
RESPONSE_DICT_KEYS = ['line_number', 'class', 'text']

# galimos sakinių klasės
NSK_CLASSES = ["BACKGROUND", "CONCLUSIONS", "METHODS", "OBJECTIVE", "RESULTS"]

# užklausa ir atsakas iš API
response = requests.post(REQUEST_URL, json=REQUEST_BODY)

# užklausos rezultato json į python žodynų sąrašą
response_list = json.loads(response.text)


class TestNskApi(unittest.TestCase):

    # ar gaunamas rezultatas iš api
    def test_response_status_200(self):
        self.assertEqual(response.status_code, 200)

    # ar gauto rezultato tekstas teisingas
    def test_response_text(self):
        self.assertEqual(response.text, RESPONSE_TEXT)

    # ar gautas teisingas skaičius sakinių
    def test_response_list_len(self):
        self.assertEqual(len(response_list), 8)

    # ar kiekvienas saraso žodynas sudarytas iš nurodytų raktų
    def test_response_dict_keys(self):
        for sentence in response_list:
            self.assertEqual(list(sentence.keys()), RESPONSE_DICT_KEYS)

    # ar kiekviena grąžinta klasė iš nurodyto sąrašo
    def test_response_class_names(self):
        for sentence in response_list:
            self.assertIn(sentence['class'], NSK_CLASSES)

    # ar kiekvienas eilutės numeris sveikas skaičius
    def test_response_line_numbers_type(self):
        for sentence in response_list:
            self.assertIsInstance(sentence['line_number'], int)


if __name__ == '__main__':
    unittest.main(verbosity=2)