import pydantic


class User(pydantic.BaseModel):
    user_cd: str
    name: str
    age: int = 20


def main1():
    print('hello')


def main2():
    user1 = User(user_cd='u_001', name='Alice')
    user2 = User(user_cd='u_002', name='Bob', age=30)

    print(user1)
    print(user2)


def main3():
    user1_dct = {'user_cd': 'u_001', 'name': 'Alice'}
    user1 = User.parse_obj(user1_dct)
    print(user1)


def main4():
    user1_dct = {'user_cd': 'u_001', 'name': 'Alice'}
    user1 = User(**user1_dct)
    print(user1)


def main5():
    user1_data = [('user_cd', 'u_001'), ('name', 'Alice')]
    user1 = User.parse_obj(user1_data)
    print(user1)


def main6():
    user1 = User(user_cd='u_001', name='Alice')
    print(user1.user_cd)
    print(user1.name)
    print(user1.age)


def main7():
    user1 = User(user_cd='u_001', name='Alice')
    print(type(user1.dict()))
    print(user1.dict())


def main8():
    user1 = User(user_cd='u_001', name='Alice')
    print(type(user1.json()))
    print(user1.json())


if __name__ == '__main__':
    main8()
