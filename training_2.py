import copy

class singly_linked_list:
    class node :
     def __init__(self,value,next=None):
        self.value=value
        self._next=next
    
    def __init__(self):
        self.tail=self.node(None)
        self.head=self.node(None,self.tail)
        self.size=0
        self.last=self.head

    def add_first(self,data):
        new_node=self.node(data,self.head._next)
        self.size+=1
        self.head._next=new_node
        if self.last==self.head:
            self.last=new_node

    def add_last(self,data):
        new_node=self.node(data,self.tail)
        self.last._next=new_node
        self.last=new_node
        self.size+=1
            
    def __repr__(self) -> str:
       if self.size==0:
           return "head-->tail"
       else:
           new_string="head"
           curser=self.head._next
           flag=True
           while flag:
               if curser.value!=None:
                   
                   new_string=new_string+"-->"+str(curser.value)
                   
                   curser=curser._next
                   
                
               else:
                   
                       new_string=new_string+"-->"+"tail"
                       flag=False
                       
                  
           return new_string
    def find_index_from_first(self,index):
        if isinstance(index,int) and index<=self.size and index>0:
            pointer=self.head
            for i in range(index):
                pointer=pointer._next
            return f"{pointer.value}"
        else:
            return"there is something wrong in the inputs"

    def find_index_from_last(self,index):
        if isinstance(index,int) and index<=self.size and index>0:
            pointer=self.head
            for i in range((self.size-index)+1):
                pointer=pointer._next
            return f"{pointer.value}"
        else:
            return"there is something wrong in the inputs"
        
    def __add__(self,second):

        #adding with changing the first operand 
        if isinstance(second,singly_linked_list):
          sec=copy.deepcopy(second)
          self.last._next=sec.head._next
          
          self.size=self.size+sec.size
          
          self.last=sec.last
    

          self.last._next=self.tail
          
          return self
        else:
            return "both operands should be singly_linked_list"
    def add(self,second):
        #add with preserve both operands 
        
        
       first=copy.deepcopy(self)
       second=copy.deepcopy(second)
       return first+second

    def total_node(self,start):
        if self.head._next==self.tail:
            return 0
        if start._next._next==self.tail:
            return 1
        else :
            return 1+(self.total_node(start._next))
    def count_nodes(self, current):
     if current._next == self.tail:
        return 0  # Empty list or single node
     else:
        return 1 + self.count_nodes(current._next)


    def swap_index(self,first_index,second_index):
        '''
        objective:making swapping between the nodes positions in the singly linked list ...getting the positions of the nodes by virtual indices 
        where we don't have real ones 
        '''
        if isinstance(first_index,int) and isinstance(second_index,int) and 0<first_index<=self.size and 0<second_index<=self.size:
          if first_index!=second_index or self.size>1:
            smaller=min(first_index,second_index)
            larger=max(first_index,second_index)
            curser=self.head
            pre_smaller,smaller_node,smaller_node_after,pre_larger_node,larger_node,larger_node_after=0,0,0,0,0,0
            
            for i in range(0,larger+2):
                 if i==smaller-1:
                  if pre_smaller==0:
                   pre_smaller=curser
                   #print(pre_smaller.value)
                 if i==smaller:
                     if smaller_node==0:
                      smaller_node=curser
                      #print(smaller_node.value)
                 if i==smaller+1:
                     if smaller_node_after==0:
                       smaller_node_after=curser
                       #print(smaller_node_after.value)
                 if i==larger-1:
                     if pre_larger_node==0:
                       pre_larger_node=curser 
                       #print(pre_larger_node.value)
                 if i==larger:
                     if larger_node==0:
                      larger_node=curser
                      #print(larger_node.value)
                 if i==larger+1:
                     if larger==self.size:
                        larger_node_after=self.tail
                        #print("tail")
                     elif larger_node_after ==0:
                      larger_node_after=curser
                      #print(larger_node_after.value)
                 curser=curser._next
            if larger_node==self.last:
               self.last=smaller_node
            if larger-smaller==1:
              pre_smaller._next=larger_node
              larger_node._next=smaller_node
              smaller_node._next=larger_node_after

            else:
             
              smaller_node._next=larger_node_after
              pre_smaller._next=larger_node
            
              pre_larger_node._next=smaller_node
              larger_node._next=smaller_node_after



          else:
              return "no need to swap because both indices are the same or we just have one value in the list "
        else:
            return "there something wrong in the inputs"

class circular_singly_queue:
   class node :
    def __init__(self,value,next=None):
        self.value=value
        self._next=next
   def __init__(self,data):
      
      new_node=self.node(data)
      self.last=new_node
      self.last._next=self.last
      self.size=1

   def add(self,data):
      

         new_node=self.node(data,self.last._next)
         self.last._next=new_node
         self.last=new_node
         self.size+=1

   def delete(self):
    if self.size==1:
        
         return "it's not acceptable to delete the last element..simply if it was deleted won't be longer linkedlist"
    else:
      element=self.last._next.value
      self.last._next=self.last._next._next
      self.size-=1
      return element
   
   def retrive(self):
      return self.last._next.value
   def total_no(self):
      return self.size
   
   def swap(self,first,second):
      '''
      objectives:swaping nodes by using the technique of just swapping the values without moving the nodes themselves
      inputs:first and second should be intgers more than zero and less than or equal the self.size
      '''
      if isinstance(first,int) and isinstance(second,int) and 0<first<=self.size and 0<second<=self.size:
         if first==second:
            return self
         else:
            curser=self.last
            for i in range(1,self.size+1):
               if i==first:
                  first_match_value=curser._next.value
                  first_node=curser._next
               elif i==second:
                  second_match_value=curser._next.value
                  second_node=curser._next
               curser=curser._next
            first_node.value=second_match_value
            second_node.value=first_match_value
         return self
      else:
         return "there is a problem in the inputs"
      

   
   def swap_nodes(self,first,second):
    if isinstance(first,int) and isinstance(second,int) and 0<first<=self.size and 0<second<=self.size:
      if self.size==1 :
         return self
      
      else:
         if first>second:
            first,second=second,first
        
         curser=self.last
         if second-first==1 :
            flag=False
            for i in range (0,self.size):
               if i==(first-1):
                  pre_first_node=curser
                  first_node=curser._next
                  second_node=curser._next._next
                  if self.last==second_node:
                     flag=True
                  after_second_node=curser._next._next._next
               curser=curser._next
            second_node._next,first_node._next,pre_first_node._next=first_node,after_second_node, second_node
            if flag:
               self.last=first_node
            return self
               

         if first+(self.size-1)==second:
             
             for i in range(0,second):
               if i==(second-1):
                  pre_second_node=curser
                  first_node=self.last._next
                  after_first_node=first_node._next
                  second_node=self.last
               curser=curser._next
          
             second_node._next,first_node._next,pre_second_node._next=after_first_node,second_node,first_node
             self.last=first_node
             
             return self 
         for i in range(0,second):
            if i==first-1:
               pre_first_node=curser
               
               first_node=curser._next
               
               after_first_node=curser._next._next
               
            if i==second-1:
               pre_second_node=curser
               
               second_node=curser._next
               
               after_second_node=curser._next._next
               
            curser=curser._next
        

         pre_first_node._next,pre_second_node._next,second_node._next,first_node._next=second_node,first_node,after_first_node,after_second_node
         return self
    else:
       return "there is something wrong in the inputs"   
    
   def __repr__(self) -> str:
    
         curser=self.last._next
         new_string="first:"
         for i in range (self.size):
           new_string=new_string+str(curser.value)+"-->"
           curser=curser._next
         new_string=new_string+"first:"+str(self.last._next.value)
         return new_string 
   
   def nodes_belonging(self,first,second):
      '''
      objectives: check if both nodes belong to the same list of the cicula_singly_queue(linkedlist) or not 
      inputs:
      first first node

      '''
      if isinstance(first,circular_singly_queue.node) and isinstance(second,circular_singly_queue.node):
         
         curser=first._next
         for i in range(self.size):
            if curser==second:
               return f" both {first} and {second} belong to the same list"
            curser=curser._next
         return f"nope {first} and {second} don't belong to the same list"

      else:
         return " there is something wrong in the inputs ,they should both circular_singly_queue.node to compare if they were part of the same list or not  "

class doubly_linked_queue:

    class _node:
      def __init__(self,data,pre,next):
         self.value=data
         self._pre=pre
         self._next=next
      def __repr__(self) -> str:
         return f"{self.value}"    


    def __init__(self):
       self.head=self._node(None,None,None)
       self.tail=self._node(None,self.head,None)
       self.head._next=self.tail
       self.size=0

    def add(self,data):
       new_node=self._node(data,self.tail._pre,self.tail)
       self.tail._pre._next=new_node
       self.tail._pre=new_node
       self.size+=1

    def __repr__(self):
        
        if self.size==0:
           return "head-->tail"
        
        elif self.size==1:
           return "head--> "+f"{self.head._next.value}"+" -->tail"
        else:
           new_string="head-->"

           flag=True 
           curser=self.head._next
           while flag:
            new_string=new_string+str(curser.value)+"-->"
            curser=curser._next
            if curser==self.tail:
               flag=False
        return new_string+"-->tail"   


    def mid_without_counter(self):

        head_pointer=self.head
        tail_pointer=self.tail
        if head_pointer._next==self.tail and tail_pointer._pre==self.head:
           return "the list is empty ... no mid in that list"
        elif head_pointer._next==tail_pointer._pre:
           return head_pointer._next
        else:
           flag=True
           while flag:
              if head_pointer._next==tail_pointer._pre or(head_pointer._next==tail_pointer and head_pointer==tail_pointer._pre):
                 flag=False
                 return tail_pointer._pre
              else:
                 head_pointer=head_pointer._next 
                 tail_pointer=tail_pointer._pre
    






x=doubly_linked_queue()
print(x.mid_without_counter())
x.add(50)
print(x.mid_without_counter())
x.add(60)
print(x.mid_without_counter())
x.add(70)
print(x.mid_without_counter())
x.add(80)
x.add(90)
x.add(100)
x.add(110)
print(x)
print(x.mid_without_counter())


class cirular_singly_stack:
   class node :
    def __init__(self,value,next=None):
        self.value=value
        self._next=next
   def __init__(self,data):
      new_node=self.node(data)
      self.last=new_node
      new_node._next=self.last
      self.size=1

   def add(self,data):
      new_node=self.node(data,self.last._next)
      self.last._next=new_node
      self.last=new_node
      self.size+=1

   def delete(self):
      element=self.last.value
      if self.size==1:
         return "it's not acceptable to delete the last element..simply if it was deleted won't be longer linkedlist"
      else:
         flag=True
         pointer=self.last._next
         while flag:
          if pointer._next==self.last:
             flag=False
             pointer._next=self.last._next
             self.last=pointer
          else:
             pointer=pointer._next
         self.size-=1
         return element
   def  retrive(self):
      return self.last.value
   def total_no(self):
      return self.size
   
   def __repr__(self) -> str:
    
         curser=self.last._next
         new_string="first:"
         for i in range (self.size):
           new_string=new_string+str(curser.value)+"-->"
           curser=curser._next
         new_string=new_string+"first:"+str(self.last._next.value)
         return new_string 
   
   def swap(self,first,second):
      '''
      objectives:swaping nodes by using the technique of just swapping the values without moving the nodes themselves
      inputs:first and second should be intgers more than zero and less than or equal the self.size
      '''
      if isinstance(first,int) and isinstance(second,int) and 0<first<=self.size and 0<second<=self.size:
         if first==second:
            return self
         else:
            curser=self.last
            for i in range(1,self.size+1):
               if i==first:
                  first_match_value=curser._next.value
                  first_node=curser._next
               elif i==second:
                  second_match_value=curser._next.value
                  second_node=curser._next
               curser=curser._next
            first_node.value=second_match_value
            second_node.value=first_match_value
         return self
      else:
         return "there is a problem in the inputs"

   def swap_nodes(self,first,second):
    if isinstance(first,int) and isinstance(second,int) and 0<first<=self.size and 0<second<=self.size:
      if self.size==1 :
         return self
      
      else:
         if first>second:
            first,second=second,first
        
         curser=self.last
         if second-first==1 :
            flag=False
            for i in range (0,self.size):
               if i==(first-1):
                  pre_first_node=curser
                  first_node=curser._next
                  second_node=curser._next._next
                  if self.last==second_node:
                     flag=True
                  after_second_node=curser._next._next._next
               curser=curser._next
            second_node._next,first_node._next,pre_first_node._next=first_node,after_second_node, second_node
            if flag:
               self.last=first_node
            return self
               

         if first+(self.size-1)==second:
             
             for i in range(0,second):
               if i==(second-1):
                  pre_second_node=curser
                  first_node=self.last._next
                  after_first_node=first_node._next
                  second_node=self.last
               curser=curser._next
          
             second_node._next,first_node._next,pre_second_node._next=after_first_node,second_node,first_node
             self.last=first_node
             
             return self 
         for i in range(0,second):
            if i==first-1:
               pre_first_node=curser
               
               first_node=curser._next
               
               after_first_node=curser._next._next
               
            if i==second-1:
               pre_second_node=curser
               
               second_node=curser._next
               
               after_second_node=curser._next._next
               
            curser=curser._next
        

         pre_first_node._next,pre_second_node._next,second_node._next,first_node._next=second_node,first_node,after_first_node,after_second_node
         return self
    else:
       return "there is something wrong in the inputs"       

x=circular_singly_queue(5)
y=cirular_singly_stack(5)
a=x.last
a1=x.last
a3=5
print(x.nodes_belonging(a,a3))
print(x)
print(y)
x.add(20)
a=x.last
x1=circular_singly_queue(5)
a1=x1.last
print(x.nodes_belonging(a,a1))
y.add(20)
print(x.last._next._next._next._next.value)
print(y.last._next._next._next._next.value)
x.add(11)
y.add(11)
x.add(14)
y.add(14)
x.add(80)
y.add(80)
print(x)
print(y)
print(x.delete())
print(y.delete())
x.add(60)
x.add(70)
y.add(60)
y.add(70)
print("\n")
print(x)
print(x.swap(6,1))
print(x.swap_nodes(6,1))

print(y)
print(y.swap(1,6))
print(y.swap_nodes(1,6))


print("\n")
print(x)
print(x.swap(1,4))
print(x.swap_nodes(1,4))
print(y)
print(y.swap(1,4))
print(y.swap_nodes(1,4))

print("\n")
print(x)
print(x.swap(1,3))
print(x.swap_nodes(1,3))
print(y)
print(y.swap(1,3))
print(y.swap_nodes(1,3))


print("\n")
print(x)
print(x.swap(1,2))
print(x.swap_nodes(1,2))
print(y)
print(y.swap(1,2))
print(y.swap_nodes(1,2))



print(type(x.last),type(y.last))
x=0

for i in range(10):
    x+=0.1
print(x==1,x)


index="dssdasd"

x=2789
factor=48

for i in range(3):
   print(2789+(7*factor))
   factor+=6


print(5//2)
