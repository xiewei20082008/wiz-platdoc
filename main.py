import os
import sys
import webbrowser
import html2text
# https://github.com/aaronsw/html2text
import codecs


html='''
<!doctype html>
<!--

  Instructions:

  - Save this file.
  - Replace "USER" with your GitHub username.
  - Replace "REPO" with your GitHub repo name.
  - Replace "Your Project" with your project name.
  - Upload this file (or commit to GitHub Pages).

  Customize as you see fit!

-->
<html>
<head>
  <meta charset='utf-8'>
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <meta name="viewport" content="width=device-width">

  <title>Your Project</title>

  <!-- Flatdoc -->
  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
  <script src='https://cdn.rawgit.com/rstacruz/flatdoc/v0.9.0/legacy.js'></script>
  <script src='https://cdn.rawgit.com/rstacruz/flatdoc/v0.9.0/flatdoc.js'></script>

  <!-- Flatdoc theme -->
  <link  href='https://cdn.rawgit.com/rstacruz/flatdoc/v0.9.0/theme-white/style.css' rel='stylesheet'>
  <script src='https://cdn.rawgit.com/rstacruz/flatdoc/v0.9.0/theme-white/script.js'></script>

  <!-- Meta -->
  <meta content="Your Project" property="og:title">
  <meta content="Your Project description goes here." name="description">

  <!-- Initializer -->
  <script>
    Flatdoc.run({
      fetcher: Flatdoc.file('%s')
    });
  </script>
</head>
<body role='flatdoc' class='no-literate'>

  <div class='header'>
    <div class='left'>
      <h1>Your Project</h1>
      <ul>
        <li><a href='https://github.com/USER/REPO'>View on GitHub</a></li>
        <li><a href='https://github.com/USER/REPO/issues'>Issues</a></li>
      </ul>
    </div>
    <div class='right'>
      <!-- GitHub buttons: see http://ghbtns.com -->
      <iframe src="http://ghbtns.com/github-btn.html?user=USER&amp;repo=REPO&amp;type=watch&amp;count=true" allowtransparency="true" frameborder="0" scrolling="0" width="110" height="20"></iframe>
    </div>
  </div>

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

os.system('pause')