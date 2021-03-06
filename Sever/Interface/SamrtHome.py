#!/usr/bin/env python
# encoding: utf-8
'''
Created on 2016年3月10日

@author: xiaoqy
'''
from PymysqlHandle.PymysqlHandle import PymysqlHandle
from TOOL import LogHandle


class SamrtHome(object):
    userName = "verstor";
    '''
    接口文档相关的查询
    '''
    def samrtHomeMethodo(self, data,metho, user):
        self.userName = user;
        mname = 'do_' + metho
        if not hasattr(self, mname):
            returnDic = {"infoCode":-20001}
            print "interFaceMetho=" + mname;
            return returnDic
        method = getattr(self, mname)
        return method(data)
    '''
    2.1添加接口
    '''
    def do_addInterFace(self,data):
        pymysqlHandle = PymysqlHandle() 
        return pymysqlHandle.addInterFace(data["interFaceName"],data["interFaceNameStr"],data["interFacepath"])

    '''
    删除接口
    '''
    def do_deleteInterFace(self,data):
        pymysqiHandle = PymysqlHandle()
        return pymysqiHandle.deleteInterFace(data)
    '''
    2.2修改接口信息
    '''
    def do_replaceInteface(self, data):
       
        pymysqlHandle = PymysqlHandle() 
        return pymysqlHandle.replaceIntefaceInfo(data)
    '''
    2.3获取接口列表
    '''
    def do_getInterFaceList(self, data):
        
        pymysqlHandle = PymysqlHandle() 
        returnData = pymysqlHandle.getInterfaceList(data)
        return returnData
    
    '''
    2.4 获取接口信息
    '''
    def do_getInterFaceInfo(self, data):
       
        interFaceName = data['interFaceName']
        pymysqlHandle = PymysqlHandle() 
        returnData = pymysqlHandle.getInterFaceInfo(interFaceName)
        return returnData
    
    '''
    2.5获取接口入参数列表
    '''
    def do_getInputValueList(self, data): 
        interFaceName = data['interFaceName'].encode("utf-8")
        parameterTypeuse = "1001"
        pymysqlHandle = PymysqlHandle() 
        returnData = pymysqlHandle.getInterfaceParameterList(interFaceName, parameterTypeuse)
        return returnData 

    '''
    2.6获取接口出参数列表
    '''
    def do_getOutputValueList(self, data): 
        interFaceName = data['interFaceName'].encode("utf-8")
        parameterTypeuse = "1002"
        pymysqlHandle = PymysqlHandle() 
        returnData = pymysqlHandle.getInterfaceParameterList(interFaceName, parameterTypeuse)
        return returnData 
    
    '''
    2.7添加接口参数列表
    '''
    def do_addParametervalue(self, data):
          
        data_Dic = {
                    "parameterName":data['parameterName'],
                    "parameterDescribe":data['parameterDescribe'],
                    "parameterEndTime":"--",
                    "parameterBeginVersions":data['parameterBeginVersions'],
                    "parameterEndVersions":data['parameterEndVersions'],
                    "parameterType":data['parameterType'],
                    "parameterFatherName":data['parameterFatherName'],
                    "parameterCanNil":data['parameterCanNil'],
                    "parameterTypeuse":data['parameterTypeuse']
                }

        pymysqlHandle = PymysqlHandle() 
        return pymysqlHandle.addParametervalue(data_Dic)
    
    '''
    2.8根据参数id删除参数
    '''
    def do_deleteParameter(self,data):
        pymysqlHandle = PymysqlHandle() 
        return pymysqlHandle.deleteParameter(data)


        
