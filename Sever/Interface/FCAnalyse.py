#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2016年8月18日

@author: xiaoqy
'''

import time;
import datetime

from FC3DAnalyse.FC3DProbability import FC3DProbability
from PymysqlHandle.PymysqlHandle import PymysqlHandle
from TOOL import LogHandle
from TOOL.DownLoadFile import DownLoadFile


class FCAnalyse(object):
    '''
    classdocs
    '''
    userName = "verstor";
    '''
    接口文档相关的查询
    '''
    def FCAnalyseMethodo(self, data, user):
        self.userName = user;
        interFaceMetho = data['inefaceMode']
        mname = 'do_' + interFaceMetho
        if not hasattr(self, mname):
            returnDic = {"inforCode":-20001}
            print "interFaceMetho=" + mname;
            return returnDic
        method = getattr(self, mname)
        return method(data)

    '''
    2.1获取3D数据
    '''
    def do_getFC3DData(self, data):
        LogHandle.writeLog(0, '获取3D数据', self.userName)
        pymysqlHandle = PymysqlHandle()
        return pymysqlHandle.getFC3dData(data)
    
    '''
    2.2获取最后一期福彩3D数据
    '''
    def do_getLastFCData(self, data): 
        LogHandle.writeLog(0, '获取最后一期福彩3D数据', self.userName)
        pymysqlHandle = PymysqlHandle()
        return pymysqlHandle.getLastFCData()
    
    '''
    2.3获取推荐的号码
    '''
    def do_getRecommendCode(self, data):
        
        LogHandle.writeLog(0, '获取推荐的号码', self.userName)
        fc = FC3DProbability()
        data = fc.getRecommend(data["BeginOutNO"], data["EndOutNO"], data["Probability"], data["RecommendOutON"]) 
        if len(data) <= 0:
            returnDic = {"inforCode":1004}   
            returnDic['result'] = data
        else:
            returnDic = {"inforCode":0}   
            returnDic['result'] = data
        return returnDic
    '''
    2.4获取遗漏数据
    '''  
    def do_getOmitData(self, data): 
        LogHandle.writeLog(0, '获取遗漏数据', self.userName)
        pymysqlHandle = PymysqlHandle()
        returnDic = pymysqlHandle.getOmitData(data)
        return returnDic