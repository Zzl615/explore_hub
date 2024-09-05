# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2024/09/05 16:18:10
@Author  :   noaghzil
@Version :   1.0
@Contact :   noaghzil@gmail.com
@Last Modified by  :   noaghzil
@Last Modified time:   2024/09/05 16:18:10
'''

# here put the import lib

from module import Patient
from tortoise import Tortoise, run_async

db_url = 'mysql://root:123456@127.0.0.1:3306/llm_demo?echo=true&pool_recycle=120'


async def init_db():
    await Tortoise.init(
        db_url=db_url,
        modules={"models": ["__main__"]},
        timezone="Asia/Shanghai"
    )

async def search_patient(name):
    query = Patient.filter(name__icontains=name)
    print(query.sql())
    result = await query.all()
    for patient in result:
        print(f'Patient: {patient.id}, {patient.name}, {patient.id_number}')
        await patient.save()

async def create_patient(id_number, name, gender, birthday):
    patient = await Patient.create(
        id_number=id_number,
        name=name,
        gender=gender,
        birthday=birthday
    )
    print(f'Created patient with id: {patient.id}')
    return patient

async def update_patient(patient_id, new_name):
    patient = await Patient.filter(id=patient_id).update(name=new_name)
    print('Patient updated')
    return patient

async def delete_patient(patient_id):
    await Patient.filter(id=patient_id).delete()
    print('Patient deleted')

async def run():
    await init_db()

    # # # 创建新患者
    # patient = await create_patient('123456789012345678', '张三', '男', '1990-01-01')

    # # # 更新患者
    # await update_patient(patient.id, '李四')

    # # 查询患者
    result = await search_patient('四')

    # query = Patient.filter(name='李四')
    # print(query.sql())
    # patient = await query.first()
    # print(patient)
    # if patient:
    #     print(f'Patient: {patient.id}, {patient.name}, {patient.id_number}')
    #     patient.gender = '女1'
    #     await patient.save()
    #     print('Patient updated')
    
    # 删除患者
    # await delete_patient(patient.id)

if __name__ == '__main__':
    run_async(run())