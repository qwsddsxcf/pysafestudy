import paramiko
'''
定义函数实现连接远程，上传下载文件，可进行密钥验证，步骤如下
实例化通道,配置密钥文件，ssh远程连接，执行命令，返回元组（含有三个参数）
分别是输入，输出结果，产生错误的信息
'''
def sshconnect(ip,username,password,cmd,miyao=None,file=False):
    '''

    :param ip: 要连接的主机地址
    :param username: 要登陆的用户名
    :param password: 要登陆的用户名的密码
    :param cmd: 要执行的命令
    :param miyao: 如果有密钥验证，就传入密钥，默认为空
    :param file:如果要读取远程文件，则传入该参数
    :return:
    '''
    try:
        if miyao:
            miyao = paramiko.Ed25519Key.from_private_key_file(miyao)  # 如果密钥路径不为空就获取密钥文件信息
        transport = paramiko.Transport((ip,22))#直接建立一个通道，用于ssh,sftp
        transport.connect(username=username,password=password,pkey=miyao)#开始连接
        ceil=paramiko.SSHClient()#实例化一个ssh协议
        ceil._transport = transport#让ssh使用这个通道
        ceil.set_missing_host_key_policy(paramiko.AutoAddPolicy())#添加自动进行远程主机验证
        '''
        上面是配置连接信息以及建立连接
        下面是处理上下传文件和执行命令
        '''
        if file:
            while True:
                if cmd == "exit":
                    break
                sftp=paramiko.SFTPClient.from_transport(transport)#使用通道
                print("1：上传文件，2，下载文件")
                choice=input("请输入你的选择：")
                if choice=="1":
                    path1=input("请输入要上传的文件路径：")
                    path2=input("请输入要上传的文件位置：")
                    sftp.put(path1,path2)
                elif choice=="2":
                    path1 = input("请输入要下载的文件路径：")
                    path2 = input("请输入要下载的文件位置：")
                    sftp.get(path1,path2)
                else:
                    print("选项错误")
                cmd = input("是否继续上传文件，输入exit退出：")
        else:
            while True:
                if cmd=="exit":
                    break
                stdin, stdout, stderr=ceil.exec_command(cmd)#返回命令执行结果
                if stdout:
                    print(stdout.read().decode('utf-8'))#如果有结果，则读取后以utf8的编码解析
                if stderr:
                    print(stderr.read().decode('utf-8'))#如果有报错，则读取后以utf8的编码解析
                print("命令执行完成")
                cmd = input("请输入要继续执行的命令，输入exit退出：")
    except Exception as e:
        print(e)

if __name__ == '__main__':
        '''
        如果输入的是file，就执行文件上下传，其他就直接当作命令执行
        如果是exit，就直接退出
        '''
        cmd = input("输入file为文件读取选项，exit为退出，其他默认为命令执行，请输入选项：")
        if cmd=="exit":
           exit(0)
        if cmd=="file":
            sshconnect('ip', 'root', 'password', "None", miyao="miyaolujing",file=True)
        else:
            sshconnect('ip', 'root', 'password', cmd, miyao="miyaolujing")

