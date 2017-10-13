# -*- coding: UTF-8 -*-

class Users:

    def __init__(self):
        self.table = []

    def getCount(self):
        return len(self.table)

    def insert(self,data):

        if hasattr(data,"id") == False:
            data["id"] = self.getCount() + 1
        
        self.table.append(data)
        print("Bilgiler kaydedildi")
    
    def select(self,id):
        if(len(self.table) == 0):
            return

        for item in self.table:
            if item["id"] and item["id"] == id:
                return item
        
        print("Kullanıcı bulunamadı")

    def update(self,id,data):
        for item in self.table:
            if(item["id"] and item["id"] == id):
                item["name"] = data["name"]
                item["lastname"] = data["lastname"]

        print("Bilgiler güncellendi")
    
    def delete(self,id):
        print("Kullanıcı bilgileri silindi")

    def getAll(self):
        print(self.table)