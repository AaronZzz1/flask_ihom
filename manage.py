#coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session

app = Flask(__name__)



#做好配置的类
class Config(object):


    # 配置私密钥匙，因为csrf需要用到session,要配置在配置行中
    SECRET_KEY = 'ishdfjflk'
    DEBUG=True
    #mysql的配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # redis的配置,没有默认的配置，我们只是仿照写的
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    #配置session
    SESSION_TYPE = 'redis'  #制定session保存到redis数据库
    SESSION_USE_SIGNER = True #让cookie中的session_id别加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT) #使用redis实例
    PERMANENT_SESSION_LIFETIME = 60*60*72 #设置session的过期时间



app.config.from_object(Config)

#连接数据库
db = SQLAlchemy(app)

#创建redis储存对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)

#配置csrf防护对象
csrf = CSRFProtect(app)

#配置session对象
Session(app)






#管理脚本，命令管理app

@app.route('/index',methods=["GET","POST"])
def index():

    return 'index'
if __name__ == '__main__':
    app.run()