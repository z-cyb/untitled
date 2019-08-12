from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import base64
import hashlib
import json
from json import dumps
import urllib
#计算平方
import numpy
import requests

# Create your views here.
def index(request):
    pass
    return render(request,'routine/index.html')

#base64编码
def base(request):
    # if request.method == 'GET':
    #     return render(request, 'routine/base.html')
    # elif request.method == 'POST':
    #     name = request.POST.get('name')
    #     content = name
    #     bytes_content = content.encode(encoding='utf-8')
    #     b64_content = base64.b64encode(bytes_content).decode()
    #     text = request.POST.get('text')
    #     content = text
    #     content2_paw_bytes = base64.b64decode(content)
    #     content2_base64_str = content2_paw_bytes.decode()
    #     content = {
    #         'b64_content': str(b64_content).replace("b,'",'').replace("'",''),
    #         'b64_content_js': content2_base64_str
    #     }
    #     return render(request, 'routine/base.html', content)
    content =request.GET.get('routine','')
    print(content)
    bytes_content = content.encode(encoding='utf-8')
    b64_content = base64.b64encode(bytes_content)
    b64_content_text = b64_content.decode()
    text = request.GET.get('decode', '')
    # print(text)
    content2_paw_bytes = base64.b64decode(text)
    content2_base64_str = content2_paw_bytes.decode()
    # print(content2_base64_str)
    content = {
        'b64_content': b64_content_text,
        'b64_content_js': content2_base64_str
    }
    context_json=json.dumps(content)
    return HttpResponse(context_json)

# def base2(request):
#     if request.method == 'GET':
#         return render(request, 'routine/base.html')
#     elif request.method == 'POST':
#         name = request.POST.get('name')
#         content = name
#         content2_paw_bytes = base64.b64decode(content)
#         content2_base64_str = content2_paw_bytes.decode()
#         content = {
#             'b64_content_jm':content2_base64_str
#         }
#         return render(request, 'routine/base.html', content)
#哈希编码
def haxi(request):
    if request.method=='GET':
        return render(request,'routine/haxi.html')
    elif request.method=='POST':
        name =request.POST.get('name')
        print(name)
        sha256=hashlib.sha256()
        sha256.update(name.encode('utf-8'))
        hash_name=sha256.hexdigest()
        context={
           "hash_name": hash_name
        }
        return render(request, 'routine/haxi.html',context)
def jsys(request):
    # if request.method=='GET':
    #     return render(request,'routine/jsas.html')
    # elif request.method=='POST':
    #     text=request.POST.get('text')
    #     jsjm =json.loads(text)
    #     print(json)
    #     context={
    #         "jsjm":jsjm
    #     }
    #     return render(request, 'routine/jsas.html',context)
    js =request.GET['js']
    js=js.replace(' ','')
    js1=js.replace('\n','')
    context={
        'js':js1
    }
    reap_json =json.dumps(context)
    return HttpResponse(reap_json)
def jsys2(request):
    if request.method=='GET':
        return render(request,'routine/jsas.html')
    elif request.method=='POST':
        text=request.POST.get('text')
        jsjm =json.dumps(text,indent=4)
        jsjm =jsjm.encode(encoding='utf-8').decode()
        context={
            "yszjs":jsjm
        }
        return render(request, 'routine/jsas.html',context)
def bmi(request):
    if request.method =='GET':
        return render(request,'routine/bmi.html')
    elif request.method=='POST':
        text=float(request.POST.get('text'))
        kg=float(request.POST.get('kg'))
        text=numpy.square(text)
        bmi=kg/text
        context={
            'bmi':bmi
        }
        if bmi >=32:
            context['mess']=f'您的BMI指数是{bmi},结果为严重肥胖'
        elif bmi >=28:
            context['mess'] = f'您的BMI指数是{bmi},结果为肥胖'
        elif bmi >= 24:
            context['mess'] = f'您的BMI指数是{bmi},结果为过重'
        elif bmi >=18.5:
            context['mess'] = f'您的BMI指数是{bmi},结果为正常'
        elif bmi <=18.4:
            context['mess'] = f'您的BMI指数是{bmi},结果为偏瘦'
        return render(request, 'routine/bmi.html',context)
def weather(request):
    # city_code = 101100701  # 101180101    101100105
    url = f'https://www.tianqiapi.com/api/'
    params={
        'version':"v1",
        'cityid':'101100105'
    }
    resp = requests.get(url=url,params=params)
    resp =json.loads(resp.text)
    data=resp['data']
    hours=resp['data'][0]['hours']#实时播报
    city=resp['city']
    day=resp['data'][0]['day'] #今天
    date=resp['data'][0]['date'] #今天日期
    week=resp['data'][0]['week'] #星期
    wea=resp['data'][0]['wea'] #天气状态
    air_level=resp['data'][0]['air_level'] #空气质量
    tem1=resp['data'][0]['tem1'] #温度
    win=resp['data'][0]['win'][0] #风向
    air_tips=resp['data'][0]['air_tips'] #事宜
    context={
        'hours':hours,
        "data":data,
        "city":city,
        "day":day,
        "date":date,
        "week":week,
        "wea":wea,
        "tem1":tem1,
        "win":win,
        "air_level":air_level,
        "air_tips": air_tips,

    }
    return render(request,'routine/weather.html',context)