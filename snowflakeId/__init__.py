#! /usr/bin/python3
# -*- coding:UTF-8 -*-


from .generator import DefaultIdGenerator
from .options import IdGeneratorOptions


def next_id(worker_id = 1,worker_id_bit_length = 6) -> int:
    ''' 
        生成雪花算法id
        :param worker_id: 机器码, 必须由外部设定, 最大值 2^worker_id_bit_length-1
        :param worker_id_bit_length 机器码位长, 默认值6, 取值范围 [1, 15]
        :return: snowflake_id
    '''

    # 声明id生成器参数，需要自己构建一个worker_id
    opts =  IdGeneratorOptions(
        worker_id = worker_id,
        worker_id_bit_length = worker_id_bit_length,
        seq_bit_length = 6
    )
    
    # - worker_id 机器码, 必须由外部设定, 最大值 2^worker_id_bit_length-1。全局唯一id, 区分不同uuid生成器实例
    # - worker_id_bit_length 机器码位长, 默认值6, 取值范围 [1, 15]（要求：序列数位长+机器码位长不超过22）。生成的uuid中worker_id占用的位数
    # - seq_bit_length 序列数位长, 默认值6, 取值范围 [3, 21]（要求：序列数位长+机器码位长不超过22）。生成的uuid中序列号占用的位数
    #options = IdGeneratorOptions(worker_id=0, worker_id_bit_length=6, seq_bit_length=6)
    
    #opts.base_time = 12311111112 # 1970-05-23 19:45:11
    opts.base_time  = 2649600000 # 1970-02-01 00:00:00
    
    idgen = DefaultIdGenerator()
    # 保存参数 
    idgen.set_id_generator(opts)   
    # 生成id
    id = idgen.next_id()
    
    return id

def next_id_str(worker_id = 1) -> str:
    ''' 
        生成雪花算法id
        :param worker_id: 机器码, 必须由外部设定, 最大值 2^worker_id_bit_length-1
        :param worker_id_bit_length 机器码位长, 默认值6, 取值范围 [1, 15]
        :return: snowflake_id
    '''
    id_str = str(next_id(worker_id))
    return id_str


