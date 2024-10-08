async def davomat(name):
    user = {
        'John': 'yuq',
        "E'zoza":'bor'
    }
    try:
        return str(user[name])
    except KeyError:
        return "Bunday o'quvchi yuq"