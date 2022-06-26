# from _typeshed import Self
import random

# from main import Lost
class Game:
    def __init__(self,question_data):
        self.data=question_data
        self.score=0
        self.question_number=0
    


    def ask(self):
        question=self.data[self.question_number]
        self.question_number+=1
        response=input(f"Q.{self.question_number}. {question['text']} True/False . ")
        self.checker(question,response)


    def checker(self,question,response):
        
        if question['answer']==response.title():
            self.score+=1
            if not self.question_number==len(self.data):
                print(f'You are right . Current score is {self.score}/{self.question_number}')
                print(f"The correct answer was {question['answer']}")
                print('\n\n')
                # return True
        else:
            print(f'You are wrong . Current score is {self.score}/{self.question_number}')
            print(f"The correct answer was {question['answer']}")
            print('\n\n')
            # return False





class KBC:


    def __init__(self,question):
    
        self.questions_easy=self.select_items([i for i in question if i["difficulty"]=='easy'],7)
        self.questions_medium=self.select_items([i for i in question if i["difficulty"]=='medium'],6)
        self.questions_hard=self.select_items([i for i in question if i["difficulty"]=='hard'],3)
        self.price_range=['₹1,000','₹2,000','₹3,000','₹5,000','₹10,000','₹20,000','₹40,000','₹80,000','₹1,60,000','₹3,20,000','₹6,40,000','₹12,50,000','₹25,00,000','₹50,00,000','₹1,00,00,000','₹7,00,00,000']
        self.price=0


    def select_items(self,arr,length):
        element=[]
        while not len(element)==length:
            question=random.choice(arr)
            if question not in element:
                element.append(question)
        return element
    def start_game(self):
        i=0
        Lost=False
        while not Lost and not len(self.questions_easy)==0:
            element=random.choice(self.questions_easy)
            response=input(f"{element['question']} : ")
            if self.checker(element,response):
                print(f'You have won {self.price_range[i]} till now')
                i+=1
                self.questions_easy.remove(element)
            
                
            elif i==0:
                    print('You have won nothing')
                    Lost=True
            else:
                    
                    print('Your answer is wrong')
                    print(f'correct answer is {element["correct_answer"]}')
                    print(f'You have finally won {self.price_range[i-1]}')
                    Lost=True
        while not Lost and not len(self.questions_medium)==0:
            element=random.choice(self.questions_medium)
            response=input(f"{element['question']} : ")
            if self.checker(element,response):
                print(f'You have won {self.price_range[i]} till now')
                i+=1
                self.questions_medium.remove(element)
            else:
                print('Your answer is wrong')
                print(f'correct answer is {element["correct_answer"]}')
                print(f'You have finally won {self.price_range[i-1]}')
                Lost=True
        while not Lost and not len(self.questions_hard)==0:
            element=random.choice(self.questions_hard)
            response=input(f"{element['question']} : ")
            if self.checker(element,response):
                print(f'You have won {self.price_range[i]} till now')
                i+=1
                self.questions_hard.remove(element)
            else:
                
                print('Your answer is wrong')
                print(f'correct answer is {element["correct_answer"]}')
                print(f'You have finally won {self.price_range[i-1]}')
                Lost=True
        
    def checker(self,question,response):
         return question["correct_answer"]==response
         
             
class GymRegister:
    
    def __init__(self,gym_name,gym_address,place,gym_products,gym_owner,gym_type):
        self.GymName=gym_name
        self.Place=place
        self.Address=gym_address
        self.Products=gym_products
        self.Owner=gym_owner
        self.Type=gym_type

    





        
    

        


    