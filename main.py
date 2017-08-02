import os
import sys
import webbrowser
import html2text
# https://github.com/aaronsw/html2text
import codecs


html='''
<!doctype html>
<html>
<head>
  <meta charset='utf-8'>
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <meta name="viewport" content="width=device-width">
  <title></title>
  <!-- Flatdoc -->
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
  <script src='https://cdn.rawgit.com/rstacruz/flatdoc/v0.9.0/legacy.js'></script>
  <script src='https://cdn.rawgit.com/rstacruz/flatdoc/v0.9.0/flatdoc.js'></script>
  <!-- Flatdoc theme -->
  <link  href='https://cdn.rawgit.com/rstacruz/flatdoc/v0.9.0/theme-white/style.css' rel='stylesheet'>
  <script src='https://cdn.rawgit.com/rstacruz/flatdoc/v0.9.0/theme-white/script.js'></script>
  <!-- Initializer -->
  <script>
       Flatdoc.run({
          fetcher: Flatdoc.file('%s')
       });
  </script>
  <style>
    .content h1 {font-size: 2em;padding-top:60px;}
    .content h2 {font-size: 1.5em;padding-top:50px;}
    .content h3 {font-size: 1.4em;padding-top:50px !important;}
    .content p {font-size: 16px;font-family: Georgia;}
    .content li {font-size:16px;font-family: Georgia;}
    .content ul > li:before {top:9.5px;left:-23px;width:7px;height:7px;}
    .content ul {margin-left:25px;}
    .content blockquote {border-left: 4px solid #dddddd;  padding: 0 15px; color: #777777; }
  </style>
</head>
<body role='flatdoc' class='big-h3 no-literate large-brief'>
  <div class='content-root'>
    <div class='menubar'>
      <div class='menu section' role='flatdoc-menu'></div>
    </div>
    <div role='flatdoc-content' class='content'></div>
  </div>
</body>
</html>
'''

tmpHtml = 'tmp_wx.html'
tmpMarkdown = 'tmp_wx.md'
markdownFile = sys.argv[1]
print markdownFile
fileDir = os.path.dirname(markdownFile)
basename = os.path.basename(markdownFile)
htmltxt = codecs.open(markdownFile,'r','utf-8').read()
h = html2text.HTML2Text()
h.ignore_images = True
txt = h.handle(htmltxt)
rawMarkdown = codecs.open(os.path.join(fileDir,tmpMarkdown),'w','utf-8')
rawMarkdown.write(txt)
rawMarkdown.close()

html = html % tmpMarkdown

remoteFile = os.path.join(fileDir,tmpHtml)

f = open(remoteFile,'w')
f.write(html)
f.close()

webbrowser.open(remoteFile)
