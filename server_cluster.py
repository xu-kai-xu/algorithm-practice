"""
一个关于服务器集群的题目
有 server_num 台服务器
有 task_num 种任务需要部署在服务器上，
数组 task[task_num]表示每种任务的数量
定义服务器负载为一台服务器上的任务数，最大负载为服务器集群中任务数最多的服务器的负载
求最大负载最小时的服务器任务分配方式


不对
"""

server_num = 8
task = [1, 10, 101, 40, 1]

def get_max_load(server_num, task):
    task.sort()
    task.reverse()
    max_load = 0
    for i in range(0, len(task)):
        if task[i] > server_num:
            max_load = max(max_load, task[i] / server_num)
            if task[i] % server_num != 0:
                max_load += 1
        else:
            max_load = max(max_load, 1)
    return max_load


if __name__ == '__main__':
    print(get_max_load(server_num, task))




