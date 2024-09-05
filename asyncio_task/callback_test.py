# @Author: Noaghzil
# @Date: 2023/09/02
# @Description: 使用 add_done_callback() 方法处理协程任务的完成事件
import asyncio
import logging

async def some_coroutine():
    # 这里是协程的代码
    try:
        await asyncio.sleep(1)
        result = {
            "hello": "world"
        }
        # print(result['world'])
        print('Done')
    except Exception as e:
        print(f'Error: {e}')
        raise e
    return result

def task_done_one(future: asyncio.Task) -> None:
    try:
        # 等待任务完成，这里会抛出异常，如果任务已经被取消或完成
        result = future.result()
        print(f'Task completed: {result}')
    except asyncio.CancelledError:
        # 任务被取消
        logging.warning(f'Task was cancelled: {future}')
    except Exception as e:
        # 任务抛出异常
        logging.error(f'{e.__class__.__name__}: {e}')
    finally:
        print('Task done')
        # 确保任务已经从任务列表中移除
        if future in running_tasks:
            running_tasks.remove(future)


def task_done_two(future: asyncio.Task) -> None:
    running_tasks.remove(future)
    if future.exception():
        logging.error(f'Task failed with exception2: {future.exception()}')

async def task_done_three(task: asyncio.Task) -> None:
    try:
        # 等待任务完成
        result = await task
        print(f'Task completed: {result}')
    except asyncio.CancelledError:
        logging.warning(f'Task was cancelled: {task}')
    except Exception as e:
        # 捕获其他类型的异常
        logging.error(f'An unexpected exception occurred: {e}')
    finally:
        if task in running_tasks:
            running_tasks.remove(task)


async def main():
    # 假设这是您运行的任务列表
    global running_tasks
    running_tasks = [asyncio.create_task(some_coroutine()) for _ in range(5)]

    # 为每个任务添加完成时的回调
    for task in running_tasks:
        # task.add_done_callback(task_done_one)
        # task.add_done_callback(task_done_two)
        task.add_done_callback(lambda t: asyncio.create_task(task_done_three(t)))

    # 等待所有任务完成
    await asyncio.gather(*running_tasks)

# 运行事件循环直到所有任务完成
asyncio.run(main())
