#!/usr/bin/env python3


import json
import time
import requests


def getPage(page=0):
    params = {
        'text': 'NAME:Tester',
        'area': 16,					# https://api.rabota.by/areas
        'page': page,
        'per_page': 100
    }
    req = requests.get('https://api.rabota.by/vacancies', params)
    data = req.content.decode()
    print(req.url)
    req.close()
    return data


def getSkills(jsObj, skillData):
    for per_page in jsObj['items']:
        req = requests.get(per_page['url'])
        data = json.loads(req.content.decode())
        req.close()
        for skill in data['key_skills']:
            skillData.append(skill['name'])
        # time.sleep(0.25)
    return skillData


skills = []
for page in range(0, 20):
    print(f'Page {page}')
    jsObj = json.loads(getPage(page))
    getSkills(jsObj, skills)
    if (jsObj['pages'] - page) <= 1:
        break
    time.sleep(0.25)

uniSkills = set(skills)

for uniSkill in uniSkills:
    print(f'{uniSkill};{skills.count(uniSkill)}')
