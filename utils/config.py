# coding: utf-8
import os.path

HOST = 'https://raw.githubusercontent.com/'
OWNER = 'mbinary' #'USTC-Courses'  #'mbinary'#
REPO = 'USTC-CS-Courses-Resource'
BRANCH = 'master'


PATH = os.path.join(HOST,OWNER,REPO,BRANCH)


WALKDIR = '/mnt/c/Users/mbinary/gitrepo/USTC-Course'


TARDIR = '/mnt/d/blogfile/blog/source/ustc-cs'



HTML = '''

<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.2.0/css/all.css" integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ" crossorigin="anonymous">
    <link href="https://mbinary0.github.io/resource/github.markdown.css" rel="stylesheet">
  </head>
  <body>
     	<div><h2>
                <a href="../index.html">&nbsp;&nbsp;<i class="fa fa-level-up"></i>&nbsp;&nbsp;</a>:
                /{cur}
            </h2>
        </div>
        
        
        <h2>Directories</h2>
        <ul>
        {dirLst}
        </ul>

        <h2>Files</h2>
        <ul>
        {fileLst}
        </ul>

        <div style="text-decration:underline;display:inline">
        <a href="https://github.com/mbinary/USTC-CS-Courses-Resource.git" target="_blank" rel="external"><i class="fa fa-github"></i>&nbsp; Github</a>
        <a href="mailto:&#122;huheqin@mail.ustc.edu.cn?subject=反馈与建议" style="float:right" target="_blank" rel="external"><i class="fa fa-envelope"></i>&nbsp; Feedback</a>
        </div>

        {readme}
    </body>  
</html>
    '''


'''
    <script>
    var len=$("#box li").length;

    function init(){
        for(i=8;i<len;i++){
            $("#box li").eq(i).addClass("hid");   
        }
    }

    $("#tog-dir").click(function(){
        var t=$(this).attr("class");
        if(t=="show"){
            $("#box .hid").addClass("show");
        }else{
            $("#box .hid").removeClass("show");
        }  
    });

    init();//初始化隐藏多余标签
    </script>



    <style>
    #box .hid{display:none;}
    #box .show{display:block;}
    </style>
'''
