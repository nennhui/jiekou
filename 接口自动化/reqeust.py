#__author__ = 'chaoneng'
import  requests
import xlrd
import  time
import post_email
cookie=1


def user_request(get_adr):
    data=xlrd.open_workbook(get_adr)
    #打开xls的表
    table=data.sheet_by_index(0)
    #获取表的行数
    nrows= table.nrows-1

    result_all=[]
    #循环执行excel表格的接口
    for i in range(nrows):
        i=i+1
        #拼接host路径
        name=table.row(i)[0].value #获取用例名
        host=table.row(i)[1].value #获取域名
        can=table.row(i)[2].value  #获取地址
        urla=str(host+can)                 #拼接host路径
        method=table.row(i)[3].value   #判断传值方法
        parm=table.row(i)[4].value  #获取参数
        data=table.row(i)[6].value  #获取预期结果

        if method=='get':
            response=requests.get(urla,params=parm)
        else:
            response=requests.post(urla,data=parm)
        date=eval(data)
        if date["status_code"]==response.status_code:
            if date["url"]==response.url:
                if date["content"]==response.text:
                    result="接口正常"
                else :
                    result="请求返回内容有异常"
            else:
                result="未正常重定向，转向%s" %response.url

        else :
            result="访问异常，出现%s" %response.status_code
        if result=="接口正常":
            break
        else:
            code=response.status_code
            url=response.url
            result_list=[name,urla,result]
            result_all.append(result_list)
    return  result_all



def wanwa(post_adr,get_adr):
    start_time=time.ctime()

    # err_list=[[1,1,1],[2,2,2],[3,3,3]]
    err_list=user_request(get_adr)
    end_time=time.ctime()
    if err_list==[]:
        content="<div>接口正常<div>"
    else:
        content="""            <div class="container-fluid">
                <div class="row-fluid">
                    <div class="span4">
                    测试用例
                    </div>
                    <div class="span4">
                    接口地址
                    </div>
                    <div class="span4">
                    异常结果
                    </div>
                </div>
            </div>"""


    ##############################################################################
    #拼接展示的内容
    ##############################################################################
        for i in err_list:
            txt="""
            <div class="container-fluid">
                <div class="row-fluid">
                    <div class="span4">
                        %s
                    </div>
                    <div class="span4">
                        %s
                    </div>
                    <div class="span4">
                        %s
                    </div>
                </div>
            </div>
                """ %(i[0],i[1],i[2])
            content=content+txt


#-------------------------------------------------------------------------------------------------------

    html_base="""<html>

        <head>
        <title>测试结果
        </title>
            <style type="text/css" >
        td{
        width:300px;


        }
        </style>
        <link href="http://libs.baidu.com/bootstrap/2.3.2/css/bootstrap.min.css" rel="stylesheet">
        <script src="http://libs.baidu.com/jquery/2.0.0/jquery.js"></script>
        </head>

        <body>
        <div id="title">
            <h1>接口测试</h1>
            <P>开始时间:<strong>%s</strong></P>
            <p>结束时间:<strong>%s</strong></p>

        </div>
        <div id=content">

            <P>测试结果</P>
            <div id="result">


            </div>

        </div>

         %s
        </body>

        </html>"""   %(start_time,end_time,content)
#---------------------------------------------------------------------------
    with open(post_adr,"w") as f:
        f.write(html_base)


if __name__=="__main__":


    post_adr="d://1.html"  #存结果地址
    get_adr="d://post.xls"  #测试用例的xls地址
    type="html"
    wanwa(post_adr,get_adr)
    post_email.duqu(post_adr)
