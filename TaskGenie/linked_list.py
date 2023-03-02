class Node():
    def __init__(self, data, next_node, previous_node):
        self.data = data
        self.next_node = next_node
        self.previous_node = previous_node
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def print_list(self):
        #Adds existing nodes to a string for visualization
        string = ""
        node = self.head
        while node:
            string += str(node.data) + " --> "
            node = node.next_node
        string += "None"
        print(string)
        
    def add_beginning(self, data):
        node = Node(data, self.head, None)
        #If the list is empty the first node is tail and head
        if self.head == None:
            self.tail = node
            self.head = node
            return
            
        self.head.previous_node = node
        self.head = node
        
    def add_end(self, data):
        #If the list is empty uses .add_beginning instead
        if self.head == None:
            self.add_beginning(data)
            return
        
        #Adds node and sets it to tail
        node = Node(data, None, self.tail)
        self.tail.next_node = node
        self.tail = node
        
    def delete(self, data):
        node = self.head
        
        #Finds node to be deleted and changes previous and next nodes of surroundings
        while node:
            if node.data == data:
                if node is self.head and node is self.tail:
                    #Resets list
                    self.head = None
                    self.tail = None
                    return
                    
                if node is self.head:
                    node.next_node.previous_node = node.previous_node
                    self.head = node.next_node
                    return
                
                if node is self.tail:
                    node.previous_node.next_node = node.next_node
                    self.tail = node.previous_node
                    return
                
                node.previous_node.next_node = node.next_node
                node.next_node.previous_node = node.previous_node 
                return
            node = node.next_node
            
    def search(self, data):
        node = self.head
        
        # Searches for node based on data
        # This still needs to be adapted based on what we are looking for.
        while node:
            if node.data == data:
                return node
    
from task import Task    
    
    
ll = LinkedList()

# milena_present = Task("Milena Present", "Saturday", "Medium", "Going to Marienplatz to buy the present at the langerie shop")
# waqar_call = Task("Calling Waqar", "Today", "High", "Calling Waqar to wish happy birthday")        
# taranta_call = Task("Calling Duarte", "Sunday", "Low", "Calling Duarte to ask about the moving")
# bede_call = Task("Calling Bede", "Sunday", "Low", "Calling Bede to aks how he is going")
# interview = Task("Interview with Pixeda", "Today", "High", "Having phone interview today")     
# shower = Task("Take a Shower", "Today", "High", None)     

# ll.add_beginning(milena_present)
# ll.add_beginning(waqar_call)
# ll.add_beginning(taranta_call)
# ll.add_beginning(bede_call)
# ll.add_beginning(interview)
# ll.add_beginning(shower)
# ll.print_list()

# print(ll.head.data.title)
