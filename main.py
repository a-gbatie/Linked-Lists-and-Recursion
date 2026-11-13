from linked_list import LinkedList

if __name__ == "__main__":
  """
  Use this file to create a LinkedList instance and perform operations 
  like insertion, recursion-based sum, search, and reverse.
  """

  # TODO: 1) Create a LinkedList instance
  list = LinkedList()
  print("Linked list created!")
  print("Head:", list.head)

  # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
  empty_list = LinkedList()
  
  list.insert_at_front(30)
  list.insert_at_front(20)
  list.insert_at_front(10)
  
  print("First node:", list.head.data)
  print("Second node:", list.head.next.data)
  print("Third node:", list.head.next.next.data)
  
  # TODO: 3) Display the list to verify insertion 
  print("Linked List:")
  list.display()
  empty_list.display()
  
  # TODO: 4) Call recursive_sum and print the result
  total = list.recursive_sum()
  print("Sum of all nodes:", total)
  print("Empty list sum:", empty_list.recursive_sum())
  

  # TODO: 5) Call recursive_search with a target and print result
  print("Search for 20:", list.recursive_search(20))
  print("Search for 99:", list.recursive_search(99))
  print("Search empty list:", empty_list.recursive_search(10))
  

  # TODO: 6) Call recursive_reverse, then display the reversed list
    