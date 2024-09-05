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

import unittest
import logging
from tortoise import Tortoise, run_async
from encrypt_case.tortoise_case.module import Patient
import asyncio

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TestPatientOperations(unittest.IsolatedAsyncioTestCase):
    db_url = 'mysql://root:123456@127.0.0.1:3306/llm_demo?echo=true&pool_recycle=120'

    @classmethod
    async def asyncSetUp(cls):
        logger.info("Setting up the database connection")
        await Tortoise.init(
            db_url=cls.db_url,
            modules={"models": ["encrypt_case.tortoise_case.module"]},
            timezone="Asia/Shanghai"
        )
        await Tortoise.generate_schemas()
        logger.info("Database setup complete")

    @classmethod
    async def asyncTearDown(cls):
        logger.info("Closing database connections")
        await Tortoise.close_connections()
        logger.info("Database connections closed")

    async def test_create_patient(self):
        logger.info("Testing patient creation")
        patient = await Patient.create(
            id_number='123456789012345678',
            name='张三',
            gender='男',
            birthday='1990-01-01'
        )
        logger.info(f"Created patient with ID: {patient.id}")
        self.assertIsNotNone(patient.id)
        self.assertEqual(patient.name, '张三')
        logger.info("Patient creation test passed")

    async def test_update_patient(self):
        logger.info("Testing patient update")
        patient = await Patient.create(
            id_number='987654321098765432',
            name='李四',
            gender='女',
            birthday='1995-05-05'
        )
        logger.info(f"Created patient with ID: {patient.id}")
        await Patient.filter(id=patient.id).update(name='王五')
        logger.info(f"Updated patient {patient.id} name to '王五'")
        updated_patient = await Patient.get(id=patient.id)
        self.assertEqual(updated_patient.name, '王五')
        logger.info("Patient update test passed")

    async def test_search_patient(self):
        logger.info("Testing patient search")
        await Patient.create(
            id_number='111222333444555666',
            name='赵六',
            gender='男',
            birthday='1985-10-10'
        )
        logger.info("Created test patient for search")
        query = Patient.filter(name__icontains='六')
        result = await query.all()
        logger.info(f"Found {len(result)} patients matching search criteria")
        self.assertGreaterEqual(len(result), 1, "At least one patient should be found")
        found_match = any(patient.name == '赵六' for patient in result)
        self.assertTrue(found_match, "Expected to find a patient named '赵六'")
        logger.info("Patient search test passed")

    async def test_delete_patient(self):
        logger.info("Testing patient deletion")
        patient = await Patient.create(
            id_number='777888999000111222',
            name='钱七',
            gender='女',
            birthday='2000-12-31'
        )
        logger.info(f"Created patient with ID: {patient.id}")
        await Patient.filter(id=patient.id).delete()
        logger.info(f"Deleted patient with ID: {patient.id}")
        deleted_patient = await Patient.filter(id=patient.id).first()
        self.assertIsNone(deleted_patient)
        logger.info("Patient deletion test passed")

if __name__ == '__main__':
    logger.info("Starting test suite")
    asyncio.run(unittest.main())
    logger.info("Test suite completed")