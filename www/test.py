import orm as orm, asyncio

from models import User, Blog, Comment

async def test(loop):
	
	await orm.create_pool(loop, user='wwwdata', password='123456', db='awesome')
	u = User(name='Test3', email='test4@example.com', passwd='1234567890', image='about:blank')
	await u.save()

	print('Success!')

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()