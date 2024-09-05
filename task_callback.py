# @Author: Noaghzil
# @Date: 2023/09/02
# @Description: 使用 add_done_callback() 方法处理协程任务的完成事件

import asyncio
import logging

# 假设这是你想要运行的协程
async def some_coroutine():
    try:
        # 协程中的代码，可能会抛出异常
        # ...
        pass
    except Exception as e:
        # 记录异常信息
        logging.error(f'Exception occurred in some_coroutine: {e}')
        # 可以选择重新抛出异常，或者处理它
        # raise

async def muti_task_done(task: asyncio.Task) -> None:
    try:
        # 等待任务完成
        await task
    except asyncio.exceptions.TaskError as e:
        # 捕获 TaskError 并获取原始异常
        original_exception = e.original
        logging.error(f'Task failed with exception: {original_exception}')
    except asyncio.CancelledError:
        logging.warning(f'Task was cancelled: {task}')
    except Exception as e:
        # 捕获其他类型的异常
        logging.error(f'An unexpected exception occurred: {e}')
    finally:
        if task in running_tasks:
            running_tasks.remove(task)

async def main():
    global running_tasks
    running_tasks = [asyncio.create_task(some_coroutine()) for _ in range(5)]

    for task in running_tasks:
        task.add_done_callback(lambda t: asyncio.create_task(muti_task_done(t)))

    await asyncio.gather(*running_tasks)

asyncio.run(main())
