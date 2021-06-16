#!/usr/bin/env python
# -*- coding:utf-8 -*-


import re
from skill_sheet import skill_sheet

skill_sheet = skill_sheet()
skill_sheet_key = list(skill_sheet.keys())
skill_sheet_key.sort()


def matching(pattern):
    if pattern == '':
        match_key = skill_sheet_key
        return match_dict(match_key)
    match_key = []
    for i in skill_sheet_key:
        if re.match(pattern, i, re.I):
            match_key.append(i)
    return match_dict(match_key)


def match_dict(match_key):
    match_value = []
    for i in match_key:
        match_value.append(skill_sheet[i])
    match_dict = dict(zip(match_key, match_value))
    return match_dict


matching = matching(input('无输入返回总表 输入关键字头：'))
for key in matching:
    print(key + ' : ' + matching[key])
