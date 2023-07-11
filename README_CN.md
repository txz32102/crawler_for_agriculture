# 首先下载源代码，github上的源代码会持续更新

如何下载？

<p align="center">
  <img src="static\download.png" alt="download">
</p>



下完了源码，后面跑代码的时候建议用cmd去跑，最好还是别用ide，首先我对各大ide不太熟悉，而且代码的测试都是针对于cmd终端的，没有对ide进行过测试

打开来的文件结构大概是这样的


<p align="center">
  <img src="static\structure.png" alt="structure">
</p>


然后打开cmd，输入命令，如下图

<p align="center">
  <img src="static\open_cmd.png" alt="opencmd">
</p>



这会创建python的虚拟环境，在根目录下多一个叫myenv的文件夹
python -m venv myenv
<p align="center">
  <img src="static\create_env.png" alt="create_env">
</p>



接着安装python里面设计到的库，相关的版本在requirements.txt中，激活python的虚拟环境
.\myenv\Scripts\activate

<p align="center">
  <img src="static\activate_pyEnv.png" alt="activate_pyEnv">
</p>


随后安装requirements.txt里面的python库，使用pip安装
pip install -r requirements

<p align="center">
  <img src="static\install_packages.png" alt="install_packages">
</p>

我这里安装好了，所以内容会有点不太一样

接着，跑后端的python脚本,注意目录位置
cd backend && python manage.py runserver
<p align="center">
  <img src="static\run_backend.png" alt="run_backend">
</p>

注意backend要一直开着不能关掉，不然前端网页获取不到后端信息

随后再打开一个cmd窗口，跑前端

cd frontend && npm install && npm start
这里npm install可能比较慢，这是在装node的相关库

<p align="center">
  <img src="static\run_frontend.png" alt="run_frontend">
</p>

