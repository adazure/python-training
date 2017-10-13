# -*- coding: UTF-8 -*-

import UserRepository

users = UserRepository.Users()

users.insert({"name":"keremix","lastname":"yavuz"})
users.insert({"name":"ahmet","lastname":"mahmut"})
users.insert({"name":"cihan","lastname":"solmaz"})

print("********** arama ************")
print(users.select(2))


users.update(2,{"name":"monaco","lastname":"chelsea"})
print("********** arama ************")
print(users.select(2))