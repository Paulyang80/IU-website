from ytTimes import watch_times

def dataSearch(search):
    if(search=="藝名"):
        return "IU / 아이유"
    elif(search=="姓名"):
        return "李知恩/이지은/Lee Ji Eun"
    elif(search=="生日"):
        return "1993年5月16日"
    elif(search=="身高"):
        return "162cm"
    elif(search=="體重"):
        return "45kg"
    elif(search=="血型"):
        return "A型"
    elif(search=="星座"):
        return "金牛座"
    elif(search=="出生地"):
        return "韓國首爾市"
    elif(search=="學歷"):
        return "同德女子高等學校"
    elif(search=="興趣"):
        return "讀書、唱歌、跳舞"
    elif(search=="特長"):
        return "吉他、唱歌、機器人舞"
    elif(search=="出道日期"):
        return "2008年9月18日"
    elif(search=="經紀公司"):
        return "LOEN Entertainment"
    elif(search=="粉絲名稱"):
        return "U-ana (Uaena)"
    else:
        return watch_times(search)