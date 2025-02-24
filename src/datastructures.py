from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self.next_id= 1
        self._members = [{
            "id" : self._generateId(),
            "first_name" : "John",
            "last_name" : last_name,
            "age" : "33",
            "lucky_numbers" : [7,13,22]
        },
            {
            "id" : self._generateId(),
            "first_name" : "Jane",
            "last_name" : last_name,
            "age" : "35",
            "lucky_numbers" : [10,14,3]
        },
            {
            "id" : self._generateId(),
            "first_name" : "Jimmy",
            "last_name" : last_name,
            "age" : "5",
            "lucky_numbers" : [1]
            }]
        

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id= self.next_id
        self.next_id += 1
        return generated_id
        

    
    
    def add_member(self, member):
        if not member.get("id"):
            member["id"] = self._generateId() 
        self._members.append(member)

        

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
            return False
            


    def get_member(self, member_id):
       for member in self._members:
             if member["id"] == member_id:
                 return member
             return None
           

            

        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members